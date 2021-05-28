#Name: Yun-Ting Tsai

import random

faceValues = ['ace', '2', '3', '4', '5', '6',
              '7', '8', '9', '10', 'jack',
              'queen', 'king']

suits = ['clubs', 'diamonds', 'hearts',
         'spades']

def shuffledDeck():
    deck = []
    for faceValue in faceValues:
        for suit in suits:
            deck.append(faceValue + ' of ' + suit)
    random.shuffle(deck)
    return deck

def faceValueOf(card):
    return card.split()[0]




def oneGame(initial):
    countPick = 0
    bankroll = initial
    d = []
    while 0 < bankroll < 2*initial:
        aceYoN = 0
        d = shuffledDeck()
        for number in range(6):
            card = d[number]
            if faceValueOf(card) == 'ace':
                aceYoN = 1
        if aceYoN == 1:
            bankroll += 1
        else:
            bankroll -= 1
        countPick += 1
    return countPick

while True:
    initial = int(input("Enter initial amount: "))
    totaltimes = 0
    for number in range(1000):
        totaltimes += oneGame(initial)
    print('Average number of rounds:', totaltimes/1000)
    print()
