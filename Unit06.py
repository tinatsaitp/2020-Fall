#1.
name =  ['Ed', 'Ted', 'Fred', 'Jennifer']

lengths = []

for i in name:
    lengths.append(len(i))
print(lengths)


print("!!!!!!!!!!")
print("!!!!!!!!!!")
print("!!!!!!!!!!")


name =  ['Ed', 'Ted', 'Fred', 'Jennifer']

def lengths(strings):
    return[len(i) for i in strings]

print(lengths(name))



#2.
import shelve

with open("pap.txt") as book:
    lines = []
    for line in book:
        lines.append(line)
    
shelf = shelve.open('books')
shelf['Pride and Prejudice'] = lines
shelf.close()



#3.
import my, urllib.request, shelve

def averageWordLength(title):
    shelf = shelve.open('books')
    lines = shelf[title]
    shelf.close()

    number = 0
    totalLength = 0

    for line in lines:
        for word in my.cleanedup(line).split():
            number += 1
            totalLength += len(word)
    return(totalLength/number)

for title in ["Pride and Prejudice", 'Huckleberry Finn']:
    print(title, averageWordLength(title))



#4.
import urllib.request, shelve

url = ' http://nancymcohen.com/csci133/cpiai.txt'
file = urllib.request.urlopen(url)
lines = file.readlines()
file.close()

cpi = {}
for line in lines:
    items = line.decode().split()
    if len(items) > 0 and items[0].isdigit():
        cpi[int(items[0])] = [float(item) for item in items[:13]]

def pctIncrease(begin, end):
    return 100*(end/begin-1)

shelf = shelve.open('cpi')
shelf['cpi'] = cpi
shelf.close()

maxIncrease = 0
for year in range(1913,2009):
    increase = pctIncrease(cpi[year][5], cpi[year][9])
    if increase > maxIncrease:
        maxIncrease = increase
        maxYear = year

print(maxYear, maxIncrease)



#6.
def f(x):
    return 17.7/(4*x**2-12*x+13)

def xValues(begin, end, number):
    step = (end-begin)/(number-1)
    return [begin+n*step for n in range(number)]

begin = float(input('Enter beginning number: '))
end = float(input('Enter ending number: '))
print(max([f(x) for x in xValues(begin, end, 100)]))
