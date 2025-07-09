import tkinter as tk
from tkinter import messagebox

class FridgeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("冷蔵庫管理アプリ")
        self.root.configure(bg="#f0f2f5")  

        self.items = {}

        # タイトル
        title = tk.Label(root, text="冷蔵庫管理アプリ", font=("Segoe UI", 18, "bold"), bg="#f0f2f5", fg="#333")
        title.grid(row=0, column=0, columnspan=5, pady=(20, 10))

        # 入力フレーム
        input_frame = tk.Frame(root, bg="white", padx=15, pady=10, bd=0, relief="flat")
        input_frame.grid(row=1, column=0, columnspan=5, padx=20, sticky="ew")
        input_frame.columnconfigure([0,1,2,3,4], weight=1)

        # ラベル
        tk.Label(input_frame, text="食品名", font=("Segoe UI", 12), bg="white", fg="#555").grid(row=0, column=0, sticky="w")
        tk.Label(input_frame, text="数量", font=("Segoe UI", 12), bg="white", fg="#555").grid(row=0, column=2, sticky="w")

        # 入力欄
        self.name_entry = tk.Entry(input_frame, font=("Segoe UI", 12), relief="solid", bd=1)
        self.name_entry.grid(row=0, column=1, sticky="ew", padx=(5, 15))

        self.qty_entry = tk.Entry(input_frame, font=("Segoe UI", 12), width=5, relief="solid", bd=1)
        self.qty_entry.grid(row=0, column=3, sticky="w")

        # 追加ボタン
        add_btn = tk.Button(input_frame, text="追加", command=self.add_item,
                            bg="#0078D7", fg="white", font=("Segoe UI", 12, "bold"),
                            relief="flat", padx=15, pady=5, cursor="hand2",
                            activebackground="#005A9E")
        add_btn.grid(row=0, column=4, padx=(15,0), sticky="e")

        
        self.msg_label = tk.Label(root, text="", font=("Segoe UI", 10), bg="#f0f2f5", fg="red")
        self.msg_label.grid(row=2, column=0, columnspan=5, pady=(5, 0))

        
        self.list_frame = tk.Frame(root, bg="white", padx=10, pady=10, bd=0)
        self.list_frame.grid(row=3, column=0, columnspan=5, sticky="nsew", padx=20, pady=20)

    
        root.columnconfigure([0,1,2,3,4], weight=1)
        root.rowconfigure(3, weight=1)

        self.update_list()

    def add_item(self):
        self.msg_label.config(text="", fg="red")  
        name = self.name_entry.get().strip()
        try:
            qty = int(self.qty_entry.get())
        except ValueError:
            self.msg_label.config(text="数量は整数で入力してください")
            return

        if not name:
            self.msg_label.config(text="食品名を入力してください")
            return

        if qty <= 0:
            self.msg_label.config(text="数量は1以上で入力してください")
            return

        if name in self.items:
            self.items[name] += qty
        else:
            self.items[name] = qty

        self.name_entry.delete(0, tk.END)
        self.qty_entry.delete(0, tk.END)

        self.msg_label.config(text=f"{name} を {qty} 個追加しました", fg="#28a745")  
        self.update_list()

    def update_list(self):
        for widget in self.list_frame.winfo_children():
            widget.destroy()

        
        header_bg = "#e8eaf6"
        tk.Label(self.list_frame, text="食品名", font=("Segoe UI", 12, "bold"), bg=header_bg, width=20).grid(row=0, column=0, sticky="w", padx=5, pady=5)
        tk.Label(self.list_frame, text="数量", font=("Segoe UI", 12, "bold"), bg=header_bg, width=8).grid(row=0, column=1, sticky="e", padx=5)
        tk.Label(self.list_frame, text="操作", font=("Segoe UI", 12, "bold"), bg=header_bg, width=12).grid(row=0, column=2, padx=5)

        for i, (name, qty) in enumerate(self.items.items(), start=1):
            
            bg_color = "#f9f9f9" if i % 2 == 0 else "white"
            if qty == 2:
                bg_color = "#fff8e1"  

            tk.Label(self.list_frame, text=name, font=("Segoe UI", 12), bg=bg_color, anchor="w").grid(row=i, column=0, sticky="w", padx=5, pady=2)
            tk.Label(self.list_frame, text=str(qty), font=("Segoe UI", 12), bg=bg_color, anchor="e").grid(row=i, column=1, sticky="e", padx=5)

            btn_frame = tk.Frame(self.list_frame, bg=bg_color)
            btn_frame.grid(row=i, column=2, sticky="center", padx=5)

            btn_dec = tk.Button(btn_frame, text="−", command=lambda n=name: self.change_qty(n, -1),
                                bg="#f44336", fg="white", font=("Segoe UI", 12, "bold"),
                                relief="flat", width=3, cursor="hand2", activebackground="#d32f2f")
            btn_dec.pack(side="left", padx=2)

            btn_inc = tk.Button(btn_frame, text="+", command=lambda n=name: self.change_qty(n, 1),
                                bg="#4CAF50", fg="white", font=("Segoe UI", 12, "bold"),
                                relief="flat", width=3, cursor="hand2", activebackground="#388E3C")
            btn_inc.pack(side="left", padx=2)

    def change_qty(self, name, delta):
        new_qty = self.items[name] + delta
        if new_qty <= 0:
            del self.items[name]
        else:
            self.items[name] = new_qty
        self.update_list()


if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("500x400")
    app = FridgeApp(root)
    root.mainloop()
