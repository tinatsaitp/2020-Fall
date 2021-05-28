#1.
name = "Fred"
for i in range (100):
    print(i+1, name)



#2.
import random
import my

def wordlist(filename):
    words = []
    with open(filename) as book:
        for lines in book:
            for word in my.cleanedup(lines).split():
                if word not in words:
                    words.append(word)
    return words

def rejoin(characters):
    word = ''
    for string in characters:
        word += string
    return word

def scramble(word):
    mixed = list(word)
    random.shuffle(mixed)
    return rejoin(mixed)

words = wordlist('pap.txt')

while True:
    theword = random.choice(words)
    mixed = scramble(theword)
    print('Letters: ', mixed)
    guess = input('Guess: ')
    if guess == theword:
        print('Right')
    else:
        print('Sorry, the word is', theword)



#3.
import random
import my

def wordlists(filename):
    words = {}
    with open(filename) as book:
        for lines in book:
            for word in my.cleanedup(lines).split():
                length = len(word)
                if length in words:
                    words[length].append(word)
                else:
                    words[length] = [word]
    return words

def rejoin(characters):
    word = ''
    for string in characters:
        word += string
    return word

def scramble(word):
    mixed = list(word)
    random.shuffle(mixed)
    return rejoin(mixed)

words = wordlists('pap.txt')

level = 3

while True:
    theword = random.choice(words[level])
    mixed = scramble(theword)
    print('Letters: ', mixed)
    guess = input('Guess: ')
    if guess == theword:
        print('Right')
        level += 1
    else:
        print('Sorry, the word is', theword)
        level -= 1



#4.
import random

suits = ['clubs','diamonds','heart','spades']
facevalues = ['ace','2','3','4','5','6','7','8','9','10','jack','queen','king']

#***
deck = []
for i in range(5):
    picksuit = random.choice(suits)
    pickfacevalue = random.choice(facevalues)
    print('the', pickfacevalue, 'of', picksuit)
#***



def shuffledDeck():
    deck = []
    for facevalue in facevalues:
        for suit in suits:
            deck.append(facevalue + 'of' + suit)
    random.shuffle(deck)
    return deck

d = shuffledDeck()

for number in range(5):
    print(d[number])



#5.
import random

suits = ['clubs','diamonds','heart','spades']
facevalues = ['ace','2','3','4','5','6','7','8','9','10','jack','queen','king']

def shuffledDeck():
    deck = []
    for facevalue in facevalues:
        for suit in suits:
            deck.append(facevalue + 'of' + suit)
    random.shuffle(deck)
    return deck

def facevaluesOf(card):
    return card.split()[0]

def suitsOf(card):
    return card.split()[2]

d = shuffledDeck()

numberOfAces = 0
numberOfClubs = 0

for number in range(5):
    card = d[number]
    print(card)
    if facevaluesOf(card) == 'ace':
        numberOfAces += 1
    if suitsOf(card) == 'clubs':
        numberOfClubs += 1
        
print("Number of aces: ", numberOfAces)
print("Number of clubs: ", numberOfClubs)



#6.
import cards

d = cards.shuffledDeck()

numberOfAces = 0
numberOfClubs = 0

for number in range(5):
    card = d[number]
    print(card)
    if cards.faceValueOf(card) == 'ace':
        numberOfAces += 1
    if cards.suitOf(card) == 'clubs':
        numberOfClubs += 1
        
print("Number of aces: ", numberOfAces)
print("Number of clubs: ", numberOfClubs)
