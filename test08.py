#Name: Yun-Ting Tsai

from tkinter import *
import readquiz
import random

questions = readquiz.loadQuestions()
total = 0
correct = 0
q = []
index = 0



def getNewQuestion():
    global questions, index, q, total
    if total == len(questions):
        #Add this condition function to stop the program (make buttons inaccessible)
        #when the total score exceeds the number of the questions
        questionLabel['text'] = 'All Questions Are Completed!'
        yesButton['command'] = ''
        noButton['command'] = ''
    else:
        q = questions [index]
        questionLabel['text'] = q[0]
        index += 1
        if q[1] == True:
            yesButton['command'] = goodAnswer
            noButton['command'] = badAnswer
        else:
            yesButton['command'] = badAnswer
            noButton['command'] = goodAnswer   

def goodAnswer():
    global total, correct
    correct += 1
    total += 1
    statusLabel['bg'] = 'light green'
    statusLabel['text'] = 'Your answer was correct'
    scoreLabel['text'] = 'Score:', correct, '/', total
    getNewQuestion()
    
def badAnswer():
    global total, correct
    correct += 0
    total += 1
    statusLabel['bg'] = 'pink'
    statusLabel['text'] = 'Your answer was incorrect'
    scoreLabel['text'] = 'Score:', correct, '/', total
    getNewQuestion()



root = Tk()

questionFrame = Frame(root)
questionFrame.pack(expand=YES, fill=BOTH)

titleLabel = Label(questionFrame)
titleLabel['text'] = 'Question:'
titleLabel.pack()

questionLabel = Message(root, width=200)
questionLabel['text'] = ''
questionLabel.pack()

clickFrame = Frame(root)
clickFrame.pack(expand=YES, fill=BOTH)

yesButton = Button(clickFrame)
yesButton['text'] = 'Yes'
yesButton.pack(side=LEFT, expand=YES, fill=X)

noButton = Button(clickFrame)
noButton['text'] = 'No'
noButton.pack(side=RIGHT, expand=YES, fill=X)

answerFrame = Frame(root)
answerFrame.pack(side=BOTTOM, expand=YES, fill=BOTH)

statusLabel = Label(answerFrame)
statusLabel['text'] = 'Status'
statusLabel.pack(side=LEFT)

scoreLabel = Label(answerFrame)
scoreLabel['text'] = 'Score:', correct, '/', total
scoreLabel.pack(side=RIGHT)

    
random.shuffle(questions)
getNewQuestion()
mainloop()
