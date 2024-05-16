import tkinter as tk
import ttkbootstrap as ttk
import random

#playerNum
def PlayerNumber():
    playerNum = input

#BotNumber
def BotNumber():
    botNum = random.randint(0, 5)

#Compare
def Compare():
    if playerNum == botNumber:
        output_string = tk.StringVar()
        results = ttk.Label(master = window, text = 'You guessed right!', font = 'calibri, 12 bold')

#creates window
window = ttk.Window(themename = 'solar')
window.title('Number Guess')
window.geometry('800x150')

#top text
title_label = ttk.Label(master = window, text = 'Guess the number', font = 'calibri, 12 bold')
title_label.pack()

#input box
input_frame = ttk.Frame(master = window)
entry_int = tk.IntVar()
entry = ttk.Entry(master = input_frame, textvariable = entry_int)
question = ttk.Label(master = input_frame, text = 'Guess a number between 1 and 5.', font = 'calibri, 12 normal')
button = ttk.Button(master = input_frame, text = 'Confirm', command = Compare)
question.pack(side = 'left', padx = 10)
entry.pack(side = 'left', padx = 10)
button.pack(side = 'left')
input_frame.pack(pady = 10)

#run
PlayerNum()
BotNum()
window.mainloop()
