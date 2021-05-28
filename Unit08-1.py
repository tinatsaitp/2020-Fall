import random
import os
import my
from tkinter import *

def alphabetize(s):
    letters = list(s)
    letters.sort()
    return my.rejoin(letters)

unscramble = {}

with open('pap.txt') as book:
    for lines in book:
        for word in my.cleanedup(lines).split():
            key = alphabetize(word)
            if key in unscramble:
                if word not in unscramble[key]:
                    unscramble[key].append(word)
            else:
                unscramble [key] = [word]

def solve():
    puzzle = inputBox.get()
    key = alphabetize(puzzle)
    if key in unscramble:
        answerLabel['text'] = format(unscramble[key])
    else:
        answerLabel['text'] = 'No answer found!'

root = Tk()

inputFrame = Frame(root)
inputFrame.pack(fill=X)

inputBoxLabel = Label(inputFrame)
inputBoxLabel['text'] = 'Enter scrambled word:'
inputBoxLabel.pack(side=LEFT, fill=X)

inputBox = Entry(inputFrame)
inputBox.pack(side=LEFT, fill=X)

button = Button(inputFrame)
button['text'] = 'unscramble'
button['command'] = solve
button.pack(side=LEFT, fill=X)

answerLabel = Label(root)
answerLabel.pack(side=BOTTOM, anchor = W)

mainloop()
