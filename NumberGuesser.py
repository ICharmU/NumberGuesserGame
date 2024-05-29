import random
import tkinter as tk
from tkinter import *

win = tk.Tk()
win.geometry("2560x1920")
win.title("Number Guesser Game")

random.seed(0)
max = 16
number_to_guess = random.randint(1,max)
player_guess = IntVar()
number_of_guesses = IntVar()
hint = StringVar()
user_input_number = IntVar()

number_of_guesses.set(0)
hint.set("Guess your first number!")

def game_startup():
    global start_button
    start_button = Button(win, text='Start Game', font=('Helvetica', 48), command = game_startup_transition, relief = GROOVE, bg = 'lightgreen')
    start_button.place(relx = 0.5, rely = 0.5, anchor = CENTER)

def ask_for_number():
    global user_input_number_entry, user_input_number_label, user_input_number_button, number_of_guesses
    number_of_guesses.set(0)
    user_input_number_entry = Entry(win, textvariable = user_input_number, width=3, font=('Helvetica', 48))
    user_input_number_entry.place(relx=0.5, rely = 0.4, anchor = CENTER)
    user_input_number_label = Label(win, text = 'Choose the largest number you would like to guess:', font = ('Helvetica', 48))
    user_input_number_label.place(relx=0.5, rely = 0.2, anchor = CENTER)
    user_input_number_button = Button(win, width = 32, text='Select Number', font=('Helvetica', 48), command = gameplay_loop, relief = GROOVE, bg='orange')
    user_input_number_button.place(relx = 0.5, rely = 0.6, anchor = CENTER)

def check_number():
    global num_guesses_label
    guess = player_guess.get()
    number_of_guesses.set(number_of_guesses.get()+1)
    num_guesses_label.config(text = f'You have guessed {number_of_guesses.get()} times!')
    num_guesses_label.place(relx = 0.5, rely = 0.85, anchor = CENTER)
    print(number_of_guesses.get())
    if guess>number_to_guess:
        hint.set(f"The number is less than {guess}")
    elif guess<number_to_guess:
        hint.set(f"The number is greater than {guess}")
    else:
        game_completion_cycle(gameplay_loop_widgets)
    win.update()

def gameplay_loop():
    hide_buttons([user_input_number_entry,user_input_number_label,user_input_number_button])
    global gameplay_loop_widgets, max, number_to_guess, player_guess_entry, number_of_guesses_entry, hint_label, description_label, num_guesses_label, check_number_button 
    gameplay_loop_widgets = []
    max = user_input_number.get()
    number_to_guess = random.randint(1,max)
    player_guess_entry = Entry(win, textvariable=player_guess, width = 3, font=('Helvetica', 48))
    player_guess_entry.place(relx = 0.5, rely = 0.3, anchor = CENTER)
    gameplay_loop_widgets.append(player_guess_entry)
    number_of_guesses_entry = Entry(win, textvariable=number_of_guesses, width = 3, font=('Helvetica', 48))
    number_of_guesses_entry.place(relx = -1, rely = -1, anchor = CENTER)
    gameplay_loop_widgets.append(number_of_guesses_entry)
    hint_label = Label(win, textvariable=hint, width = 50, font=('Helvetica',48))
    hint_label.place(relx = 0.5, rely = 0.7, anchor = CENTER)
    gameplay_loop_widgets.append(hint_label)
    description_label = Label(win, text=f"Try to guess the number, it is no larger than {max}", font=('Helvetica',48))
    description_label.place(relx=0.5, rely=0.1, anchor=CENTER)
    gameplay_loop_widgets.append(description_label)
    num_guesses_label = Label(win, text=f'You have guessed {number_of_guesses.get()} times!', font=('Helvetica',48))
    num_guesses_label.place(relx = 0.5, rely = 0.85, anchor = CENTER)
    gameplay_loop_widgets.append(num_guesses_label)
    check_number_button = Button(win, width=16, text='Check Number', font=('Helvetica', 48), command=check_number, relief = GROOVE, bg='pink')
    check_number_button.place(relx=0.5, rely=0.5, anchor = CENTER)
    gameplay_loop_widgets.append(check_number_button)

def game_completion_cycle(gameplay_loop_widgets):
    hide_buttons(gameplay_loop_widgets)
    global game_completion_cycle_widgets, completion_text, play_again_button
    game_completion_cycle_widgets = []
    completion_text = Label(win, text = f'Great job, the number was {number_to_guess}\n\nIt only took you {number_of_guesses.get()} guesses!', font=('Helvetica', 48))
    completion_text.place(relx = 0.5, rely = 0.2, anchor = CENTER)
    game_completion_cycle_widgets.append(completion_text)
    play_again_button = Button(win, width = 36, text = 'Play Again', font=('Helvetica', 48), command = restart_game, relief = GROOVE, bg = 'violet')
    play_again_button.place(relx = 0.5, rely = 0.5, anchor = CENTER)
    game_completion_cycle_widgets.append(play_again_button)

def game_startup_transition():
    hide_buttons([start_button])
    ask_for_number()

def restart_game():
    hide_buttons(game_completion_cycle_widgets)
    ask_for_number()

def hide_buttons(button_list):
    for button in button_list:
        button.place(relx = -1, rely = -1, anchor = CENTER)

game_startup()
win.mainloop()
