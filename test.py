import tkinter as tk
from tkinter import messagebox


def copy(arg):
    print(arg.cget("text"))



class myGui:

    def init(self):

        self.root = tk.Tk()

        #look of the GUI
        self.root.title("A GUI")
        self.root.geometry("600x300")

        # Installing widget
        self.label = tk.Label(self.root, text="Testing App")
        self.label.pack(padx=10, pady=10)

        # create and log value of check box
        self.check_state = tk.IntVar()

        self.check = tk.Checkbutton(self.root, text="hello?", variable=self.check_state)
        self.check.pack(padx=10, pady=10)

        # button
        self.btnwhat = tk.Button(self.root, text="click me!", command=self.message_box)
        self.btnwhat.pack(padx=10, pady=10)

        self.textbox = tk.Text(self.root, height=2, font=("Arial", 12))
        self.textbox.pack(padx=10, pady=10)

        # Frame setup
        # create frame
        self.btn_frame = tk.Frame(self.root)

        # duplicate column
        self.btn_frame.columnconfigure(0, weight=1)
        self.btn_frame.columnconfigure(1, weight=1)
        self.btn_frame.columnconfigure(2, weight=1)
        self.btn_frame.columnconfigure(3, weight=1)

        # create Buttons
        self.btn1 = tk.Button(self.btn_frame, text="1", command=lambda: self.paste_self(self.btn1))
        self.btn1.grid(row=0, column=0, sticky=tk.W + tk.E)

        self.btn2 = tk.Button(self.btn_frame, text="2", command=lambda: self.paste_self(self.btn2))
        self.btn2.grid(row=0, column=1, sticky=tk.W + tk.E)

        self.btn3 = tk.Button(self.btn_frame, text="3", command=lambda: self.paste_self(self.btn3))
        self.btn3.grid(row=0, column=2, sticky=tk.W + tk.E)

        self.btn4 = tk.Button(self.btn_frame, text="4", command=lambda: self.paste_self(self.btn4))
        self.btn4.grid(row=0, column=3, sticky=tk.W + tk.E)
        self.btn5 = tk.Button(self.btn_frame, text="5", command=lambda: self.paste_self(self.btn5))
        self.btn5.grid(row=1, column=0, sticky=tk.W + tk.E)

        self.btn6 = tk.Button(self.btn_frame, text="6", command=lambda: self.paste_self(self.btn6))
        self.btn6.grid(row=1, column=1, sticky=tk.W + tk.E)

        self.btn7 = tk.Button(self.btn_frame, text="7", command=lambda: self.paste_self(self.btn7))
        self.btn7.grid(row=1, column=2, sticky=tk.W + tk.E)

        self.btn8 = tk.Button(self.btn_frame, text="8")
        self.btn8.grid(row=1, column=3, sticky=tk.W + tk.E)

        self.btn_frame.pack(fill="x", padx=10, pady=10)

        # end of Gui class
        self.root.mainloop()

    def paste_self(self, btn_object):
        messagebox.showinfo(title="paste self", message=btn_object.cget("text"))

    def message_box(self):
        if self.check_state.get() == 1:
            messagebox.showinfo(title="answer", message="yes")

        elif self.check_state.get() == 0:
            messagebox.showinfo(title="answer", message="no!")

        else:
            print("error")
            exit()




obj = myGui()
obj.init()
