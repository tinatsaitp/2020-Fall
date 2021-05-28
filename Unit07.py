#1.
def function(x):
    return x*x

def goalSeek(function, lowLimit, highLimit, target, maxError=.01):

    error = maxError + 1

    while error > maxError:
        guess = (lowLimit+highLimit)/2
        result = function(guess)
        error = abs(result-target)
        if result > target:
            highLimit = guess
        if result < target:
            lowLimit = guess
    return guess

print(goalSeek(function, 0, 3, 2))
 


#2.
def makePower (exp):
    def power(x):
        return x**exp
    return power

def goalSeek(function, lowLimit, highLimit, target, maxError=.01):

    error = maxError + 1

    while error > maxError:
        guess = (lowLimit+highLimit)/2
        result = function(guess)
        error = abs(result-target)
        if result > target:
            highLimit = guess
        if result < target:
            lowLimit = guess
    return guess

for exp in range(2,11):
    power = makePower (exp)
    print (exp, goalSeek(power, 0, 5, 2))



#3.
# (Multiplication table)
pat4d = '{0:4d}'
pat2d = '{0:2d}'

print('    ', end ='')
for col in range (1, 11):
    print(pat4d.format(col), end= ' ')

print()
print()

for row in range (1, 11):
    print (pat2d.format(row), end ='  ')
    for col in range (1, 11):
        print(pat4d.format(row*col), end ='')
    print()



#4.
def mystery(x):
    return x*x - 10*x + 25

def goalSeek(function, limit1, limit2, target, maxError=.01):
    result1 = function(limit1)
    result2 = function(limit2)
    if result1 < target < result2:
        return goalSeeker (function, limit1, limit2, target, maxError)
    if result2 < target < result1:
        return goalSeeker (function, limit2, limit1, target, maxError)
    return None

def goalSeeker(function, lowLimit, highLimit, target, maxError=.01):

    error = maxError + 1

    while error > maxError:
        guess = (lowLimit+highLimit)/2
        result = function(guess)
        error = abs(result-target)
        if result > target:
            highLimit = guess
        if result < target:
            lowLimit = guess
    return guess

print(goalSeek(mystery, 0, 5, 10, .001))



#5.
entries = []

with open ('phoneData.txt') as data:
    for line in data:
        items = line.split('\t')
        name = items[0]+', '+items[1]
        area = items[2] [ :3]
        number = items[2] [4:-1]
        entries.append([name, area, number])

entries.sort()

for entry in entries:
    print('{0:24s}({1}){2}'.format(entry[0],entry[1],entry[2]))
