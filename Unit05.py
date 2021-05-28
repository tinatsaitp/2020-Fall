#1.
name = "Fred"
time = 100

def printFred (time):
    print (time, name)
    if time-1 > 0:
        printFred (time-1) #recursive function

printFred(100)



#2.
import os

def contain(filename, pattern):
    with open(filename) as file:
        for line in file:
            if pattern in line:
                return True
    return False

    
for filename in os.listdir('.'):
    if contain(filename, 'random'):
        print(filename, 'contains random')



#3.
import os

def counter(path):
    count = 0
    for filename in os.listdir(path):
        newpath = os.path.join(path, filename)
        if os.path.isdir(newpath):
            count += counter(newpath)
            #only count all files in the main directory but add all subdirectories in the main directory's folders. 
        else:
            count += 1
    return count

print(counter('.'))



#4.
import random
import os
import my

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

puzzle = input('Puzzle: ')
key = alphabetize(puzzle)
if key in unscramble:
    print(unscramble[key])
else:
    print('No answer found!')



#5.
import my

dictionary = {}

with open('pap.txt') as book:
    for lines in book:
        for word in my.cleanedup(lines).split():
            if word in dictionary:
                dictionary[word] += 1
            else:
                dictionary[word] = 1

ingWord = []

for word in dictionary:
    if word [-3: ] == "ing":
        ingWord.append([dictionary[word], word])

ingWord.sort()
print(ingWord[-5: ])



#6.
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

def evaluate(hand):
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
    if cards == [1,1,1,2]:
        return 'one pair'
    if cards == [1,2,2]:
        return 'two pair'
    if cards == [1,1,3]:
        return 'three of a kind'
    if cards == [2,3]:
        return 'full house'
    if cards == [1,4]:
        return 'four of a kind'
    return 'nothing'

hand = shuffledDeck()[ :5]
print(hand)
print(evaluate(hand))
