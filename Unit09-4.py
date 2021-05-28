import random
import os
import my
from tkinter import *
from myWidgets import *

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
    puzzle = userInput.get()
    key = alphabetize(puzzle)
    if key in unscramble:
        answerLabel['text'] = format(unscramble[key])
    else:
        answerLabel['text'] = 'No answer found!'

root = Tk()

userInput = enhancedEntry(root, 'Enter scrambled word:', 'unscramble', solve)
userInput.pack(fill=X)

answerLabel = Label(root)
answerLabel.pack(side=BOTTOM, anchor = W)

mainloop()

