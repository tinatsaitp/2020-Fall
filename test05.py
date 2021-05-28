#Name: Yun-Ting Tsai

import os

def cleanedup(s):
    letters = '@abcdefghijklmnopqrstuvwxyz_0123456789'
    cleantext = ''
    for character in s.lower():
        if character in letters:
            cleantext += character
        else:
            cleantext += ' '
    return cleantext

def findMentions(filename, indent):
    mentioned = {}
    with open (filename, encoding='utf-8') as file:
        for lines in file:
            for usernames in cleanedup(lines).split():
                if usernames in mentioned:
                    mentioned[usernames] += 1
                else:
                    mentioned[usernames] = 1
    name = []
    for usernames in mentioned:
        if usernames [0] == "@":
            name.append([mentioned[usernames], usernames])
    name.sort()
    for i in range (-3,0):
        ans = name [i]
        print(indent, ans[1], ans[0])

path = '.'
for filename in os.listdir(path):
    newpath = os.path.join(path, filename)
    if filename[-7:] == '.tweets':
        print(filename)
        findMentions(filename, ' ')
        print()
