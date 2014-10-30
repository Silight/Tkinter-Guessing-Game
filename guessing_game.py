__author__ = 'Andrew Edwards'

from tkinter import *
import tkinter.messagebox
import random


def get_number():
    number = random.randrange(1, 999, 1, int)
    return number


def exit_confirm():
    confirm = tkinter.messagebox.askquestion("Exit", "Are you sure you want to quit?")
    if confirm == 'yes':
        sys.exit()


def run_logic(guess):
    guess = int(guess)
    if guess == get_number():
        return "You got it!"
    elif guess > get_number():
        return "Too High!"
    else:
        return "Too Low!"


class Application:

    def __init__(self, master):
        self.instruct = Label(root, text="""
I'm thinking of an number between
1 and 100.

Take a guess!
""")
        frame = Frame(master)
        frame.pack()
        self.setup_gui()

    def setup_gui(self):
        response_text = "Enter a number"
        top_menu = Menu(root)
        root.config(menu=top_menu)

        sub_menu = Menu(top_menu)
        top_menu.add_cascade(label="File", menu=sub_menu)
        sub_menu.add_command(label="Exit", command=exit_confirm)

        self.instruct.pack()

        entry_guess = IntVar()
        guess = Entry(textvariable=entry_guess, width=3)
        guess.pack()

        submit_button = Button(text="Submit", command=response_text)
        submit_button.pack()

        response = Label(root, text=response_text, bd=1, relief=SUNKEN, anchor=S)
        response.pack(side=BOTTOM, fill=X)


root = Tk()
b = Application(root)
root.mainloop()
