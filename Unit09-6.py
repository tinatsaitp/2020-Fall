from tkinter import *

class multipleEntry(Frame):
    def __init__(self, parent, promptText, actionText, action):
        Frame.__init__(self, parent)
        self.prompt = Label(self)
        self.prompt['text'] = promptText
        self.prompt.pack(anchor=W)

        self.entries = [self.makeEntryFrame()]
        self.moreButton = self.makeMoreButton()
        
        self.actionButton = Button(self)
        self.actionButton['text'] = actionText
        self.actionButton['command'] = action
        self.actionButton.pack(side=BOTTOM, anchor=W)
        
    def makeEntryFrame(self):
        self.lastFrame = Frame(self)
        self.lastFrame.pack(fill=X, anchor=W)
        entry = Entry(self.lastFrame)
        entry.pack(side=LEFT)
        return entry

    def makeMoreButton(self):
        button = Button(self.lastFrame)
        button['text'] = 'More'
        button['command'] = self.addEntry
        button.pack(side=LEFT)
        return button

    def addEntry(self):
        self.entries.append(self.makeEntryFrame())
        self.moreButton.destroy()
        self.moreButton = self.makeMoreButton()

    def get(self):
        return [entry.get() for entry in self.entries]
    




def pick():
    names = userInput.get()
    favorite['text'] = 'My favorite name is '
    for name in names:
        if len(name) >= 5:
            favorite['text'] += name
            return
    favorite['text'] += names[0]

root = Tk()

userInput = multipleEntry(root, 'Enter word:', 'Pick favorite', pick)
userInput.pack(expand=YES, fill=BOTH)

favorite = Label(root)
favorite.pack(side=BOTTOM, anchor = W)

mainloop()
