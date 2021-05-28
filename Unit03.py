#1.
def cleanedup(s):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    cleantext = ''
    for character in s.lower():
        if character in alphabet:
            cleantext += character
        else:
            cleantext += ' '
    return cleantext


longtext = ''
wordlong = 0
with open('pap.txt') as book:
    for line in book:
        for word in cleanedup(line).split():
            if len(word) > wordlong:
                wordlong = len(word)
                longword = word
print(longword)



#2.
concordance = {}

while True:
    english = input("Enter English word: ")
    if english in concordance:
        print(english,'=', concordance[english])
    else:
        translation = input("Enter translation: ")
        concordance[english] = translation
    print()



#3.
def cleanedup(s):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    cleantext = ''
    for character in s.lower():
        if character in alphabet:
            cleantext += character
        else:
            cleantext += ' '
    return cleantext

occurrences = {}
with open ("pap.txt") as book:
    for lines in book:
        for word in cleanedup(lines).split():
            if word in occurrences:
                occurrences[word] += 1
            else:
                occurrences[word] = 1

while True:
    word = input("Enter a word: ")    
    if word in occurrences:
        print(word, "is used", occurrences[word], "times")
    else:
        print('Not Found')



#4.
name = "Fred"
for i in range(100):
    print(name)

num = 1
while num <= 100:
    print(num, 'Fred')
    num += 1



#5.
def average(numbers):
    total = 0
    for number in numbers:
        total += number
    return total/len(numbers)

while True:
    text = input("Enter numbers: ")
    usernumbers = []
    for word in text.split():
        usernumbers.append(int(word))
    print("Average:", average(usernumbers))



#6.
def average(numbers):
    total = 0
    for number in numbers:
        total += number
    return total/len(numbers)

def cleanedup(s):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    cleantext = ''
    for character in s.lower():
        if character in alphabet:
            cleantext += character
        else:
            cleantext += ' '
    return cleantext

def lengths(l):
    newlist=[]
    for newnum in l:
        newlist.append(len(words))
    return newlist

while True:
    line = input('Enter a sentence: ')
    words = cleanedup(line).split()
    print('Average word length:', average(lengths(words)))
