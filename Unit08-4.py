from tkinter import *
import my

dictionary = {}

with open('pap.txt') as book:
    for lines in book:
        for word in my.cleanedup(lines).split():
            if word in dictionary:
                dictionary[word] += 1
            else:
                dictionary[word] = 1
def search():
    endingWord = []
    ending = inputBox.get()
    for word in dictionary:
        if word [-(len(ending)): ] == ending:
            endingWord.append([dictionary[word], word])
            
    endingWord.sort()
    answerLabel['text'] = makeAnswer(endingWord[-5: ])

def makeAnswer(lastWords):
    if len(lastWords) == 0:
        return 'Nothing found'
    answer = ''
    for index in range(1, len(lastWords)+1):
        pattern = '{0} ({1})'
        if index > 1:
            pattern = ', {0} ({1})'
        answer += pattern.format(lastWords[-index][1], lastWords[-index][0])
    return answer

root = Tk()

inputFrame = Frame(root)
inputFrame.pack(anchor = W)

inputBoxLabel = Label(inputFrame)
inputBoxLabel['text'] = 'Enter ending:'
inputBoxLabel.pack(side=LEFT, fill=X)

inputBox = Entry(inputFrame)
inputBox.pack(side=LEFT, fill=X)

button = Button(inputFrame)
button['text'] = 'unscramble'
button['command'] = search
button.pack(side=LEFT, fill=X)

answerLabel = Label(root)
answerLabel.pack(side=BOTTOM, anchor = W)

mainloop()
