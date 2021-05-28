from tkinter import *
from myWidgets import *

def go():
    result.slideText(userInput.get())

root = Tk()

quitButton(root)

userInput = enhancedEntry(root, 'Enter text:', 'Go', go)
userInput.pack(fill=X)

result = SlidingLabel(root)
result.pack(side=LEFT, fill=X, anchor=W)

mainloop()
