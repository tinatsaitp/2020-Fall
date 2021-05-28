#Name: Yun-Ting Tsai

from tkinter import *
import random

class Card:
    def __init__(self, f, s):
        self.myFaceValue = f
        self.mySuit = s
    def __str__(self):
        return self.myFaceValue + ' of ' + self.mySuit
    def faceValue(self):
        return self.myFaceValue
    def suit(self):
        return self.mySuit

class Deck:
    faceValues = ['ace', '2', '3', '4', '5', '6', '7', '8',
                  '9', '10', 'jack', 'queen', 'king']
    suits = ['clubs', 'diamonds', 'hearts', 'spades']
    def __init__(self):
        self.theCards = [Card(faceValue, suit)
                         for faceValue in Deck.faceValues
                         for suit in Deck.suits]
        self.shuffle()
    def shuffle(self):
        random.shuffle(self.theCards)
    def deal(self):
        return self.theCards.pop()
    def cardsLeft(self):
        return len(self.theCards)

class enhancedEntry(Frame):
    def __init__(self, parent, prompt, actionText, action):
        Frame.__init__(self, parent)
        self.inputBoxLabel = Label(self)
        self.inputBoxLabel['text'] = prompt
        self.inputBoxLabel.pack(side=LEFT, fill=X)
        self.inputBox = Entry(self)
        self.inputBox.pack(side=LEFT, fill=X)
        self.button = Button(self)
        self.button['text'] = actionText
        self.button['command'] = action
        self.button.pack(side=LEFT, fill=X)
    def get(self):
        return self.inputBox.get()
    def setActionText(self, actionText):
        self.button['text'] = actionText
    def setPrompt(self, prompt):
        self.inputBoxLabel['text'] = prompt
    def setAction(self, cmd):
        self.button['command'] = cmd

class CardsFrame(Frame):
    def __init__(self, parent, hand, wid, textcolor):
        Frame.__init__(self, parent)
        for card in hand:
            self.buttons = Button(self, width=wid, fg=textcolor)
            self.buttons['text'] = format(str(card))
            self.buttons['command'] = ''
            self.buttons.pack(side=BOTTOM)
     
def faceValueOf(card):
    return card.split()[0]

def deal(n):
    deck = Deck()
    cards = [str(deck.deal()) for cd in range(n)]        
    return cards

def evaluate(hand):
    scores = 0
    facevaluescount = {}
    for card in hand:
        fv = faceValueOf(card)
        if fv in facevaluescount:
            facevaluescount[fv] += 1
        else:
            facevaluescount[fv] = 1
    cards = []
    for fv in facevaluescount:
        cards.append(facevaluescount[fv])
    cards.sort()
    for count in cards:
        if count == 2:
            scores += 1
        if count == 3:
            scores += 10
        if count == 4:
            scores += 100
    return scores

def dealfunction():
    global cardsoutput
    num = userInput.get()
    if num.isdigit() == True and 0 <= int(num) <= 52:
        n = int(num)
        hand = deal(n)
        scores = evaluate(hand)
        score['text'] = 'Score:', scores
        
        cardsoutput.destroy()
        cardsoutput = CardsFrame(root, hand, 15, 'black')
        cardsoutput.pack(fill=X)
    else:
        #If the user input is not in the condition,
        #the program will print out a button with the warning text.
        #And the button text will be red.
        cardsoutput.destroy()
        warntext = '!!! Wrong input, please input integer, 0 ~ 52 !!!'
        cardsoutput = CardsFrame(root, [warntext], 40, 'red')
        cardsoutput.pack(expand=YES, fill=BOTH)


                
root = Tk()

userInput = enhancedEntry(root, 'Number of cards:', 'Deal', dealfunction)
userInput.pack(expand=YES, fill=BOTH)

score = Label(root)
score['text'] = 'Score:'
score.pack(fill=X)

cardsoutput = CardsFrame(root, ['initial'], 15, 'black')

mainloop()
