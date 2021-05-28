#1.
count = 0
with open ('pap.txt') as book:
    for line in book:
        for word in line:
            if word == 'e':
                count += 1
print("Number of times the lowercase letter 'e' is used:", count)

#2.
count = 0
with open ('Unit2.py') as program:
    for line in program:
        if 'for' in line:
            count += 1
print("The word 'for' was encountered", count, "time.")

#3.
mincount = 999
minword = ""
fruit = ["apple", "banana", "peach", "plum", "grapefruit"]
for word in fruit:
    count = len(word)
    if count < mincount:
        minword = word
        mincount = count
print("The shortest word:", minword)

#4.
total = 0
numbers = [3, 17, 1, 44, 239]
for number in numbers:
    total += number
average = total/len(numbers)
print(average)

#5. (How to apply 'append' function into our program)
lengths = []
students = ['Ed', 'Ted', 'Fred', 'Jennifer']
for name in students:
    lengths.append(len(name))
print(lengths)

#6.
answer = input("How are you feeling? ")
words = answer.split()

vowels = "aeiou"
maxcount = 0 

for word in words:
    num = 0
    for letter in word:
        if letter in vowels:
            num += 1
    if num > maxcount:
        maxcount = num
        maxword = word
print(maxword, maxcount)
