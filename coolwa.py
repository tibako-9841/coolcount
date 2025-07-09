import tkinter as tk
from tkinter import messagebox

class FridgeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("冷蔵庫管理アプリ")

        self.items = {}  # 食品名 -> 数量

        # 入力欄
        tk.Label(root, text="食品名").grid(row=0, column=0)
        tk.Label(root, text="数量").grid(row=0, column=2)

        self.name_entry = tk.Entry(root)
        self.name_entry.grid(row=0, column=1)

        self.qty_entry = tk.Entry(root, width=5)
        self.qty_entry.grid(row=0, column=3)

        add_btn = tk.Button(root, text="追加", command=self.add_item)
        add_btn.grid(row=0, column=4)

        self.list_frame = tk.Frame(root)
        self.list_frame.grid(row=1, column=0, columnspan=5)

        self.update_list()

    def add_item(self):
        name = self.name_entry.get().strip()
        name = name.lower()
        try:
            qty = int(self.qty_entry.get())
        except ValueError:
            messagebox.showerror("エラー", "数量は整数を入力してください")
            return

        if not name:
            messagebox.showerror("エラー", "食品名を入力してください")
            return

        if qty < 0:
            messagebox.showerror("エラー", "数量は0以上で入力してください")
            return

        if name in self.items:
            self.items[name] += qty
        else:
            self.items[name] = qty

        self.name_entry.delete(0, tk.END)
        self.qty_entry.delete(0, tk.END)
        self.update_list()

    def update_list(self):
        # 既存のリストをクリア
        for widget in self.list_frame.winfo_children():
            widget.destroy()

        for i, (name, qty) in enumerate(self.items.items()):
            # ハイライト条件: 数量が2
            bg_color = "yellow" if qty == 2 else "white"

            label = tk.Label(self.list_frame, text=f"{name}: {qty}", width=20, bg=bg_color)
            label.grid(row=i, column=0)

            btn_dec = tk.Button(self.list_frame, text="-", command=lambda n=name: self.change_qty(n, -1))
            btn_dec.grid(row=i, column=1)

            btn_inc = tk.Button(self.list_frame, text="+", command=lambda n=name: self.change_qty(n, 1))
            btn_inc.grid(row=i, column=2)

    def change_qty(self, name, delta):
        new_qty = self.items[name] + delta
        if new_qty < 0:
            new_qty = 0
        self.items[name] = new_qty
        self.update_list()

if __name__ == "__main__":
    root = tk.Tk()
    app = FridgeApp(root)
    root.mainloop()
