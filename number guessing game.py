import tkinter as tk
import ttkbootstrap as ttk
import random
import time

#Compare
def Compare():
    playerNum = entry_int.get()
    botNum = random.randint(1, 5)
    if playerNum == botNum:
        results = ttk.Label(master = window, text = 'You guessed correctly!', font = 'calibri, 12 bold')
    elif playerNum >= 6:
        results = ttk.Label(master = window, text = 'Invalid input.', font = 'calibri, 12 bold')
    elif playerNum <= 0:
        results = ttk.Label(master = window, text = 'Invalid input.', font = 'calibri, 12 bold')
    else:
        results = ttk.Label(master = window, text = 'You did not guess correctly. Try again.', font = 'calibri, 12 bold')
    results.pack(pady = 10)

#creates window
window = ttk.Window(themename = 'solar')
window.title('Number Guess')
window.geometry('500x150')

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
window.mainloop()
