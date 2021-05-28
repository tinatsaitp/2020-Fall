#Name: Yun-Ting Tsai

import urllib.request, shelve

url = 'http://nancymcohen.com/csci133/cpiai.txt'
file = urllib.request.urlopen(url)
lines = file.readlines()
file.close()

cpi = {}
for line in lines:
    items = line.decode().split()
    if len(items) > 0 and items[0].isdigit():
        cpi[int(items[0])] = [float(item) for item in items[:13]]

shelf = shelve.open('cpi')
shelf['cpi'] = cpi
shelf.close()



def average(n):
    totalnum = 0
    length = len(n)
    for i in n:
        totalnum += i
    return[totalnum/length]

while True:
    query = input("Enter query: ")
    newlist = query.split(' ')
    year = int(newlist[0])
    if len(newlist) > 1:
        months = [cpi[year][int(n)] for n in newlist[1:]]
    else:
        months = cpi[year][1:]
    print(months, average(months)[0])
    print()
