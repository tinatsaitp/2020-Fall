#Name: Yun-Ting Tsai

#1.
total = 0
with open ("elon-musk.txt") as file:
    for lines in file:
        total += 1
    print('Number of tweets:', total)


            
#2.
maxword = 0
with open ("elon-musk.txt") as file:
    for lines in file:
        count = len(lines.split())
        if count > maxword:
            maxline = lines
            maxword = count
print('Tweet with max number of words:', maxline)            
                


#3.
def cleanedup(s):
    letters = '@abcdefghijklmnopqrstuvwxyz'
    cleantext = ''
    for character in s.lower():
        if character in letters:
            cleantext += character
        else:
            cleantext += ' '
    return cleantext

mentioned = {}
with open ("elon-musk.txt") as file:
    for lines in file:
        for usernames in cleanedup(lines).split():
            if '@' in usernames:
                if usernames in mentioned:
                    mentioned[usernames] += 1
                else:
                    mentioned[usernames] = 1

while True:
    username = input("Enter username: ")
    if username in mentioned:
        print('Mentioned', mentioned[username], 'times.')
    else:
        print("Not mentioned.")
    print()
