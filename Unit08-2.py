from tkinter import *
translations = {}
word = ''

def translate():
    global word
    word = userInput.get()
    userInput.delete(0, END)
    if word in translations:
        answerLabel['text'] = format(word) + ' = ' + format(translations[word])
    else:
        prompt['text'] = "Enter translation for " + format(word)
        button['text'] = 'save'
        button['command'] = save
        answer['text'] = ''

def save():
    translations[word] = userInput.get()
    userInput.delete(0, END)    
    prompt['text'] = 'Enter word:'
    button['text'] = 'Translate'
    button['command'] = translate

root = Tk()

topFrame = Frame(root)
topFrame.pack(fill=X)

prompt = Label(topFrame)
prompt['text'] = 'Enter word:'
prompt.pack(side=LEFT)

userInput = Entry(topFrame)
userInput.pack(side=LEFT, fill=X)

button = Button(topFrame)
button['text'] = 'Translate'
button['command'] = translate
button.pack(side=LEFT)

answerLabel = Label(root)
answerLabel.pack(side=BOTTOM, anchor = W)

mainloop()
