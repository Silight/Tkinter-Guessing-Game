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
        response = Label(root, text=response_text, bd=1, relief=SUNKEN, anchor=S)
        response.pack(side=BOTTOM, fill=X)
        sub_menu = Menu(top_menu)
        top_menu.add_cascade(label="File", menu=sub_menu)
        sub_menu.add_command(label="Exit", command=exit_confirm)
        self.instruct.pack()
        guess_entry = Entry(root, width=3)
        guess_entry.pack()
        guess_entry.insert(0, 0)
        player_guess = int(guess_entry.get())
        submit_button = Button(text="Submit", command=lambda: self.button_event(player_guess, get_number()))
        submit_button.pack()
        # needs to respond with the result of the guess


    def button_event(self, player_guess, get_number):
        pg = int(player_guess)
        gn = get_number
        if pg == gn:
            return 1
        elif pg < gn:
            return 2
        else:
            return 3


root = Tk()
b = Application(root)
root.mainloop()
