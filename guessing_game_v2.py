__author__ = 'Andrew Edwards'

from tkinter import *
import tkinter.messagebox
from random import *


def exit_program():
    confirm_exit = tkinter.messagebox.askquestion("Exit", "Are you sure you want to exit?")
    if confirm_exit == "yes":
        sys.exit()


class Application:

    def __init__(self, master):
        # Build the frame of the game
        frame = Frame(master)
        frame.pack()
        # Build the top menu
        top_menu = Menu(root)
        root.config(menu=top_menu)
        # Build the sub menu
        sub_menu = Menu(top_menu)
        top_menu.add_cascade(label="File", menu=sub_menu)
        sub_menu.add_command(label="Exit", command=exit_program)
        # Give some instructions
        self.instruct = Label(root, text="""
I'm thinking of a number
between 1 and 999.

Take a guess!
        """)
        self.instruct.pack()
        # Ask for user input
        user_guess = Entry(root, width=3)
        user_guess.pack()
        user_guess.insert(0, 0)  # Ensures that user_guess returns an integer before user enters anything
        user_number = int(user_guess.get())  # Pulls the user input from the Entry widget, assigns it to a variable.
        submit_button = Button(text="Submit", command=lambda: self.button_event(user_number))
        submit_button.pack()

    def button_event(self, user_input):
        # Variables
        random_number = randint(1, 999)
        player_guess = user_input
        number_guesses = 0
        # Main game logic loop
        while True:
            number_guesses += 1
            if player_guess == random_number:
                tkinter.messagebox.askokcancel("You Win!", "You got it in " + str(number_guesses) + " tries!")
                break
            elif player_guess > random_number:
                tkinter.messagebox.askokcancel("Nope", "You are too high!")
                break
            else:
                tkinter.messagebox.askokcancel("Nope", "You are too low!")
                break
        if number_guesses > 10:
            tkinter.messagebox.OK("You Lose!", "Sorry, the number I was thinking of was " + str(random_number))

root = Tk()
a = Application(root)
root.mainloop()
