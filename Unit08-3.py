from tkinter import *
import random

score = 0

root = Tk()

scoreFrame = Frame(root)
scoreFrame.pack(expand=YES, fill=BOTH)

scoreLabel = Label(scoreFrame)
scoreLabel.pack(expand=YES)

def showScore():
    scoreLabel['text'] = 'Score' + format(score)

clickFrame = Frame(root)
clickFrame.pack(side=BOTTOM, expand=YES, fill=BOTH)

def changeLabels():
    for button in buttons:
        button['text'] = random.choice(['click', 'clack', 'cluck'])
        button['bg'] = buttonColor
    root.after(1500, changeLabels)
    
def makeButton():
    button = Button(clickFrame)
    def cmd():
        global score
        if button['bg'] == buttonColor:
            if button['text'] == 'click':
                score += 10
                button['bg'] = 'light green'
            else:
                score -= 10
                button['bg'] = 'light yellow'
            showScore()
    button['command'] = cmd
    button.pack(side=LEFT, expand=YES, fill=BOTH)
    return button

buttons = [makeButton() for i in range(5)]
buttonColor = buttons [0] ['bg']

changeLabels()
showScore()
mainloop()
