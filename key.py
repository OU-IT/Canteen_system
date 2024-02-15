import tkinter as tk
import sys,os

numz = ""
num=""

class NumInput:
    def __init__(self, master):
        self.master = master
        self.num_entry = tk.StringVar()
        self.num_entry.set("")


        self.key_frames = [
            [('1'), ('2'), ('3')],
            [('4'), ('5'), ('6')],
            [('7'),('8'),('9')],
            [('0'),('auto'),('yes')]
        ]


        self.buttons = []
        for row_index, row_data in enumerate(self.key_frames):
            for col_index, button_text in enumerate(row_data):
                if button_text == 'Clear':
                    button = tk.Button(self.master, text=button_text, width=10, height=3,
                                       command=lambda btn_txt=button_text: self.append_number(int(btn_txt)))
                elif button_text == 'yes':
                    button = tk.Button(self.master, text=button_text, width=10, height=3,
                                       command=lambda btn_txt=button_text: self.enter_number(btn_txt))
                else:
                    button = tk.Button(self.master, text=button_text, width=10, height=3,
                                       command=lambda btn_txt=button_text: self.append_number(btn_txt))
                button.grid(row=row_index, column=col_index)
                self.buttons.append(button)

                # 创建显示输入的数字的标签
        self.num_label = tk.Label(self.master, textvariable=self.num_entry, font=('Arial', 24))
        self.num_label.grid(row=len(self.key_frames), column=0, columnspan=3)

    def append_number(self,num):
        global numz
        numz = numz + str(num)

    def clear_entry(self):
        self.num_entry.set("")

    def enter_number(self,a):
        global numz
        if num == "yes":
            numz = numz[:-3]

def run():
    root = tk.Tk()
    root.title("数字输入")
    root.geometry("350x350")
    num_input = NumInput(root)
    root.mainloop()
