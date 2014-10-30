__author__ = 'Andrew Edwards'

import sys
from tkinter import *
import tkinter.messagebox
import random


def get_number():
    number = random.randrange(1, 999, 1, int)
    return number

class Application:

    def __init__(self, master):
        frame = Frame(master)
        frame.pack()
        self.setup_gui()

    def setup_gui(self):
        response_text = "Enter a number"
        top_menu = Menu(root)
        root.config(menu=top_menu)

        sub_menu = Menu(top_menu)
        top_menu.add_cascade(label="File", menu=sub_menu)
        sub_menu.add_command(label="Exit", command=self.exit_confirm)

        self.instruct = Label(root, text="""
I'm thinking of an number between
1 and 100.

Take a guess!
""")
        self.instruct.pack()

        entry_guess = IntVar()
        guess = Entry(textvariable=entry_guess, width=3)
        guess.pack()

        submit_button = Button(text="Submit", command= lambda: self.run_logic(guess.get()))
        submit_button.pack()

        response = Label(root, text=response_text, bd=1, relief=SUNKEN, anchor=S)
        response.pack(side=BOTTOM, fill=X)

    def run_logic(self, guess):
        pass

    def exit_confirm(self):
        confirm = tkinter.messagebox.askquestion("Exit", "Are you sure you want to quit?")
        if confirm == 'yes':
            sys.exit()


root = Tk()
b = Application(root)
root.mainloop()