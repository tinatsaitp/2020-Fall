#1.1
people=["Fred","Ted","Ed"]
for student in people:
    print("Hello",student)


#1.2
meat=["ham","pastrami","roast beef","chicken"]
bread=["rye","whole wheat","roll"]
for inside in meat:
    for outside in bread:
        print(inside,"on",outside)


#1.3
vowels="aeiou"
word="pineapple"
for letter in vowels:
    if letter in word:
        print(letter,"is in",word)



#2
alphabet="abcdefghijklmnopqrstuvwxyz"
for letter in alphabet:
    print(letter)



#3
partofword=["ate","a","substantiate","state","it","tan"]
theword="substantiate"
for letter in partofword:
    if letter in theword:
        print(letter,"is a substring of",theword)



#4 (range function)
name="Fred"
for i in range(100):
    print(name)
    
# (class content)
for i in "..........":
    for x in "..........":
        print("Fred")
#It'll be 10 times X 10 times = 100 times



#5
for i in range(10,0,-1):
    print(i)



#6
#***
vowels="aeiou"
fruit=["apple","banana","peach","grapefruit"]
for food in fruit:
    for letter in vowels:    
        if letter in food:
            print("vowels in",food)
            print(letter)
#***
            
vowels="aeiou"
fruit=["apple","banana","peach","grapefruit"]
for food in fruit:
    print("vowels in",food)
    for letter in vowels:
        if letter in food:
            print(letter)
