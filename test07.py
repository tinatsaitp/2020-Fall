#Name: Yun-Ting Tsai
pat2f = '{0:8.2f}'

def makePoly (a, b, c, d):
    def poly (x):
        return a*x**3 + b*x**2 + c*x + d
    return poly

def goalSeek(function, lowLimit, highLimit, target, maxError = .01):
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

with open ('poly.txt') as data:
    for line in data:
        if line[0] != '#':
            numbers = []
            for items in line.split(' '):
                if items != '':
                    numbers.append(items)
            A = float(numbers [0])
            B = float(numbers [1])
            C = float(numbers [2])
            D = float(numbers [3])
            Lo = float(numbers [4])
            Hi = float(numbers [5])
            getpoly = makePoly(A, B, C, D)
            roots = goalSeek(getpoly, Lo, Hi, 0, .001)
            letter = A, B, C, D
            for i in letter:
                print(pat2f.format(i), end = ' ')
            print (' -> ', pat2f.format(roots))
