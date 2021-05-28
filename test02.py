#Name: Yun-Ting Tsai

#1.
total = 0
with open('alice.txt') as book:
    for lines in book:
        for words in lines.split():
            total += 1
print('Total number of words:', total)


            
#2.
totallines = 0
totalwords = 0
with open('alice.txt') as book:
    for lines in book:
        totallines += 1
        for words in lines.split():
            totalwords += 1
            average = totalwords/totallines
print('Average number of words in a line:', average)


            
#3.
maxcount = 0
with open('alice.txt') as book:
    for lines in book:
        count = len(lines.split())
        if count > maxcount:
            maxline = lines
            maxcount = count
print('Longest line has', maxcount, 'words:', maxline)


            
#4.
answer = input('Enter word: ')
with open('alice.txt') as book:
    num = 0
    for lines in book:
        if answer in lines:
            num += 1
            if num <= 10:
                print(lines)
    if num == 0:
        print('Not found.')
print(num, 'lines contain', answer)



#Thank you for telling me how to fix the program. I really appreciate it.
#I will definitely try to fix errors by myself in the future. Thank you so much.
