import random
import tkinter as tk
from tkinter import *

win = tk.Tk()
win.geometry("2560x1920")
win.title("Number Guesser Game")

#random.seed(0)
max = 100
number_to_guess = random.randint(1,max)
player_guess = IntVar()
number_of_guesses = IntVar()
hint = StringVar()

number_of_guesses.set(0)
hint.set("Guess your first number!")

def play_game():
    guess = player_guess.get()
    number_of_guesses.set(number_of_guesses.get()+1)
    global num_guesses_label
    num_guesses_label.config(text = f'You have guessed {number_of_guesses.get()} times!')
    num_guesses_label.place(relx = 0.5, rely = 0.85, anchor = CENTER)
    print(number_of_guesses.get())
    if guess>number_to_guess:
        hint.set(f"The number is less than {guess}")
    elif guess<number_to_guess:
        hint.set(f"The number is greater than {guess}")
    else:
        hint.set(f"Nice job, the number was {number_to_guess}")
    win.update()
    


Entry(win, textvariable=player_guess, width = 3, font=('Helvetica', 36)).place(relx = 0.5, rely = 0.3, anchor = CENTER)
Entry(win, textvariable=number_of_guesses, width = 3, font=('Helvetica', 48)).place(relx = -1, rely = -1, anchor = CENTER)
Label(win, textvariable=hint, width = 50, font=('Helvetica',48)).place(relx = 0.5, rely = 0.7, anchor = CENTER)
Label(win, text=f"Try to guess the number, it is no larger than {max}", font=('Helvetica',48)).place(relx=0.5, rely=0.1, anchor=CENTER)
num_guesses_label = Label(win, text=f'You have guessed {number_of_guesses.get()} times!', font=('Helvetica',42))
num_guesses_label.pack()
num_guesses_label.place(relx = 0.5, rely = 0.85, anchor = CENTER)
Button(win, width=16, text='Check Number', font=('Helvetica', 48), command=play_game, relief = GROOVE, bg='pink').place(relx=0.5, rely=0.5, anchor = CENTER)

win.mainloop()