from tkinter import *
from myWidgets import *

translations = {}
word = ''

def translate():
    global word
    word = userInput.get()
    if word in translations:
        answerLabel['text'] = format(word) + ' = ' + format(translations[word])
    else:
        userInput.setPrompt("Enter translation for " + format(word))
        userInput.setActionText('save')
        userInput.setAction(save)
        answerLabel['text'] = ''

def save():
    translations[word] = userInput.get()
    userInput.setPrompt('Enter word:')
    userInput.setActionText('Translate')
    userInput.setAction(translate)

root = Tk()

userInput = enhancedEntry(root, 'Enter word:', 'Translate', translate)
userInput.pack(fill=X)

answerLabel = Label(root)
answerLabel.pack(side=BOTTOM, anchor = W)

mainloop()
