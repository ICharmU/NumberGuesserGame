import random
import tkinter as tk
from tkinter import *

class GamePlay(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self,parent)
        self.parent = parent
        #initialize variables, remove variables if only used in some functions
        self.max = IntVar()
        self.number_to_guess = IntVar()
        self.player_guess = IntVar()
        self.number_of_guesses = IntVar()
        self.number_of_guesses_str = StringVar()
        self.hint = StringVar()
        self.user_input_number = IntVar()
        self.completion_text_str = StringVar()
        self.description_text = StringVar()
        #ask_for_number widgets
        self.user_input_number_entry = Entry(win, textvariable = self.user_input_number, width=3, font=('Helvetica', 48))
        self.user_input_number_label = Label(win, text = 'Choose the largest number you would like to guess:', font = ('Helvetica', 48))
        self.user_input_number_button = Button(win, width = 32, text='Select Number', font=('Helvetica', 48), command = lambda:(self.max.set(self.user_input_number.get()),
                                                                                                                          self.number_to_guess.set(random.randint(1,self.max.get())), self.gameplay_loop()), relief = GROOVE, bg='orange')
        #gameplay_loop widgets
        self.player_guess_entry = Entry(win, textvariable=self.player_guess, width = 3, font=('Helvetica', 48))
        self.number_of_guesses_entry = Entry(win, textvariable=self.number_of_guesses, width = 3, font=('Helvetica', 48))
        self.hint_label = Label(win, textvariable=self.hint, width = 50, font=('Helvetica',48))
        self.description_label = Label(win, textvariable=self.description_text, font=('Helvetica',48))
        self.num_guesses_label = Label(win, textvariable=self.number_of_guesses_str, font=('Helvetica',48))
        self.check_number_button = Button(win, width=16, text='Check Number', font=('Helvetica', 48), command=self.check_number, relief = GROOVE, bg='pink')
        self.gameplay_loop_widgets = [self.player_guess_entry,self.number_of_guesses_entry,self.hint_label,self.description_label,self.num_guesses_label,self.check_number_button]
        #game_completion_cycle widgets
        self.completion_text = Label(win, textvariable = self.completion_text_str, font=('Helvetica', 48))
        self.play_again_button = Button(win, width = 36, text = 'Play Again', font=('Helvetica', 48), command = lambda:(self.hide_buttons(self.game_completion_cycle_widgets), self.ask_for_number()), relief = GROOVE, bg = 'violet')
        self.game_completion_cycle_widgets = [self.completion_text, self.play_again_button]
        #hide widgets by default
        #widget list
        self.all_widgets = [self.user_input_number_entry, self.user_input_number_label,
                            self.user_input_number_button, self.num_guesses_label]
    
    #displays starting option
    def game_startup(self):
        print('game_startup')
        start_button = Button(win, text='Start Game', font=('Helvetica', 48), command = lambda: (start_button.place(relx = -1, rely = -1, anchor = CENTER), self.ask_for_number()), relief = GROOVE, bg = 'lightgreen')
        start_button.place(relx = 0.5, rely = 0.5, anchor = CENTER)
    
    #uses a user inputted number for initializing values
    def ask_for_number(self):
        print('ask_for_number')
        self.number_of_guesses.set(0)
        self.number_of_guesses_str.set(f'You have guessed {self.number_of_guesses.get()} times!')
        print(self.number_of_guesses.get())
        self.user_input_number_entry.place(relx=0.5, rely = 0.4, anchor = CENTER)
        self.user_input_number_label.place(relx=0.5, rely = 0.2, anchor = CENTER)
        self.user_input_number_button.place(relx = 0.5, rely = 0.6, anchor = CENTER)

    #updates user information and changes the game state
    def check_number(self):
        print('check_number')
        guess = self.player_guess.get()
        self.number_of_guesses.set(self.number_of_guesses.get()+1)
        self.number_of_guesses_str.set(f'You have guessed {self.number_of_guesses.get()} times!')
        self.num_guesses_label.place(relx = 0.5, rely = 0.85, anchor = CENTER)
        print(self.number_of_guesses.get())
        if guess>self.number_to_guess.get():
            self.hint.set(f"The number is less than {guess}")
        elif guess<self.number_to_guess.get():
            self.hint.set(f"The number is greater than {guess}")
        else:
            self.game_completion_cycle()
        self.parent.update()    

    #initializes values and updates screen for a new game
    def gameplay_loop(self):
        print('gameplay_loop')
        self.hide_buttons([self.user_input_number_entry,self.user_input_number_label,self.user_input_number_button])
        self.max.set(self.user_input_number.get())
        self.number_to_guess.set(random.randint(1, self.max.get()))
        self.player_guess_entry.place(relx = 0.5, rely = 0.3, anchor = CENTER)
        self.number_of_guesses_entry.place(relx = -1, rely = -1, anchor = CENTER)
        self.hint_label.place(relx = 0.5, rely = 0.7, anchor = CENTER)
        self.description_text.set(f"Try to guess the number, it is no larger than {self.max.get()}")
        self.description_label.place(relx=0.5, rely=0.1, anchor=CENTER)
        self.num_guesses_label.place(relx = 0.5, rely = 0.85, anchor = CENTER) 
        self.check_number_button.place(relx=0.5, rely=0.5, anchor = CENTER)

    #updates screen to play again option
    def game_completion_cycle(self):
        self.hide_buttons(self.gameplay_loop_widgets)
        self.completion_text_str.set(f'Great job, the number was {self.number_to_guess.get()}\n\nIt only took you {self.number_of_guesses.get()} guesses!')
        self.completion_text.place(relx = 0.5, rely = 0.2, anchor = CENTER)
        self.play_again_button.place(relx = 0.5, rely = 0.5, anchor = CENTER)

    #hides all buttons
    def hide_buttons(self, button_list):
        print('hide_buttons')
        print(button_list)
        for button in button_list:
            button.place(relx = -1, rely = -1, anchor = CENTER)
        
if __name__ == '__main__':
    win = tk.Tk()
    win.geometry("2560x1920")
    win.title("Number Guesser Game")
    test = GamePlay(win)
    test.game_startup()
    win.mainloop()
