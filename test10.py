#Name: Yun-Ting Tsai

#  A-1K:  Mean or NastyMirror
#  A-8K:  Mean
#  A-32K: Mirror
#
#  B-1K:  NastyMirror
#  B-8K:  Mirror or Random or NastyMirror 
#  B-32K: Random
#
#  C-1K:  NastyMirror
#  C-8K:  Mirror or Counting or Mirror & Counting tie
#  C-32K: Mirror or Counting or Mirror & Counting tie

import random

class Player:
    idCounter = 0
    def __init__(self):
        self.score = 0
        self.memory = {}
        Player.idCounter += 1
        self.name = 'Player {0}'.format(Player.idCounter)
    def processResult(self, otherName, myResponse, otherResponse):
        result = [myResponse, otherResponse]
        if otherName in self.memory:
            self.memory[otherName].append(result)
        else:
            self.memory[otherName] = [result]
        if myResponse == 'nice' and otherResponse == 'nice':
            self.score += 30
        elif myResponse == 'nice' and otherResponse == 'nasty':
            self.score -= 70
        elif myResponse == 'nasty' and otherResponse == 'nice':
            self.score += 50
        else:
            self.score += 0

class FriendlyPlayer(Player):
    def __init__(self):
        Player.__init__(self)
        self.name += ' (friendly)'
    def respondsTo(self, otherName):
        return 'nice'

class MeanPlayer(Player):
    def __init__(self):
        Player.__init__(self)
        self.name += ' (mean)'
    def respondsTo(self, otherName):
        return 'nasty'

class MirrorPlayer(Player):
    def __init__(self):
        Player.__init__(self)
        self.name += ' (mirror)'
    def respondsTo(self, otherName):
        if otherName in self.memory:
            return self.memory[otherName][-1][1]
        else:
            return 'nice'
        
class RandomPlayer(Player):
    def __init__(self):
        Player.__init__(self)
        self.name += ' (random)'
    def respondsTo(self, otherName):
        choices = ['nice', 'nasty']
        return(random.choice(choices))
        
class NastyMirrorPlayer(Player):
    def __init__(self):
        Player.__init__(self)
        self.name += '(nastymirror)'
    def respondsTo(self, otherName):
        if otherName in self.memory:
            return self.memory[otherName][-1][1]
        else:
            return 'nasty'

class CountingPlayer(Player):
    def __init__(self):
        Player.__init__(self)
        self.name += '(counting)'
    def respondsTo(self, otherName):
        words = {}
        ni = 0
        na = 0
        for otherName in self.memory:
            words = self.memory[otherName]
            for word in words:
                if word[1] == 'nice':
                    ni += 1
                else:
                    na += 1
        if ni >= na:
            return 'nice'
        else:
            return 'nasty'


      
def encounter(player1, player2):
    name1, name2 = player1.name, player2.name
    response1 = player1.respondsTo(name2)
    response2 = player2.respondsTo(name1)
    player1.processResult(name2, response1, response2)
    player2.processResult(name1, response2, response1)

def makePopulation(specs):
    population = []
    for playerType, number in specs:
        for player in range(number):
            population.append(playerType())
    return population

def doGeneration(population, numberOfEncounters):
    for encounterNumber in range(numberOfEncounters):
        players = random.sample(population, 2)
        encounter(players[0], players[1])

def sortPopulation(population):
    scoreList = [[player.score, player.name, type(player)]
                 for player in population]
    scoreList.sort()
    return scoreList

def makeNextGeneration(scoreList):
    nextGeneration = []
    populationSize = len(scoreList)
    scoreList = scoreList[int(populationSize/2):]
    for score, name, playerType in scoreList:
        for number in range(2):
            nextGeneration.append(playerType())
    return nextGeneration

def newGeneration(allPlayers):
    pattern = '{:<4d}'
    a,b,c,d,e,f = 0,0,0,0,0,0
    for player in allPlayers:
        if type(player) == FriendlyPlayer:
            a += 1
        if type(player) == MeanPlayer:
            b += 1
        if type(player) == MirrorPlayer:
            c += 1
        if type(player) == RandomPlayer:
            d += 1
        if type(player) == NastyMirrorPlayer:
            e += 1
        if type(player) == CountingPlayer:
            f += 1
    print(pattern.format(a)+pattern.format(b)+pattern.format(c)+
          pattern.format(d)+pattern.format(e)+pattern.format(f))

def scenarios(letter):
    if letter == 'A':
        allPlayers = makePopulation([[FriendlyPlayer, 10],
                                     [MeanPlayer, 10],
                                     [MirrorPlayer, 10],
                                     [RandomPlayer, 10],
                                     [NastyMirrorPlayer, 10],
                                     [CountingPlayer, 10]
                                     ])
        return allPlayers
    
    if letter == 'B':
        allPlayers = makePopulation([[FriendlyPlayer, 10],
                                     [MeanPlayer, 0],
                                     [MirrorPlayer, 10],
                                     [RandomPlayer, 10],
                                     [NastyMirrorPlayer, 10],
                                     [CountingPlayer, 10]
                                     ])
        return allPlayers

    if letter == 'C':
        allPlayers = makePopulation([[FriendlyPlayer, 0],
                                     [MeanPlayer, 0],
                                     [MirrorPlayer, 10],
                                     [RandomPlayer, 10],
                                     [NastyMirrorPlayer, 10],
                                     [CountingPlayer, 10]
                                     ])
        return allPlayers





while True:
    pattern = 'Run# {0}'
    scenario = input('Enter scenario (A, B, or C): ')
    if scenario == 'A' or scenario == 'B' or scenario == 'C':
        encounters = int(input('Number of encounters: '))
        runs = int(input('Number of 20-generation runs: '))
        print()
        print('Scenario:', scenario, '  Number of encounters:',
              encounters, '  Number of runs:', runs)
        print()
        for generationNumber in range(runs):
            allPlayers = scenarios(scenario)
            print(pattern.format(generationNumber+1))
            print('Friend ', 'Mean ', 'Mirror ', 'Random ',
                  'NastyM ', 'Counting ')
            for i in range(20):
                doGeneration(allPlayers, encounters)
                sortedResults = sortPopulation(allPlayers)
                newGeneration(allPlayers)
                allPlayers = makeNextGeneration(sortedResults)
                print()
        allPlayers = []
    else:
        print('Please enter scenario (ONLY A, B, or C)! \n')
