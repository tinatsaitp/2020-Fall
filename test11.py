#Name: Yun-Ting Tsai

#Objective: The user should move the ball
#           to the goal 10 times to win the Game.
#Rule: In each round, the user have 15 seconds to move the ball to the goal.
#      If the user's time is up in any round, they will lose the Game.
#      In other words, the user should move the ball to the goal within 15 seconds,
#      and they need to repeat this action 10 times(rounds) to win the Game. 
#Input: The user can use the arrow keys on the keyboard to move the ball to the goal.



from tkinter import *
from random import choice
import time



def clock():
    return time.perf_counter()



# field size can be changed
fieldSize = 300
# 300 is the default of the field size
defaultScreenSize = 300
# so that we can determine the percentage
# of how the new(changed) field size becomes compared to the default ones
newScreenPer = fieldSize / defaultScreenSize
# 25 is the default of the goal size
# 10 is the default of the ball size
# Therefore, if the field size is increased,
# everything (e.g. the goal and the ball size) will also increase by the same %
goalSize = 25*newScreenPer
ballSize = 10*newScreenPer

moveblock, ball, sx, sy, goalSpeed = None, None, 100, 100, 5
field = None
previousTime = 0
roundCounter = 0
keyboard = {'Up': False, 'Left': False, 'Down': False, 'Right': False}

# I will create a list of blocks below
blocks = []



# returns position of the *center* of the ball
def ballPosition():
    x1, y1, x2, y2 = list(field.coords(ball))
    return [(x1+x2)/2, (y1+y2)/2]


    
def startGame():
    global ball, moveblock, startTime, previousTime, roundCounter

    # each time clicking the 'Start' button, the 'Round' number will +1
    roundCounter += 1

    # to delete the ball from previous round of the Game
    if ball:
        field.delete(ball)

    # place the ball at random
    upperLeftX = choice(list(range(fieldSize-int(ballSize))))
    upperLeftY = choice(list(range(fieldSize-int(ballSize))))

    # create the ball 
    ball = field.create_oval(upperLeftX, upperLeftY, upperLeftX+ballSize,
                             upperLeftY+ballSize, fill='light blue')

    def key_press(event):
        if event.keysym == 'Up':
            keyboard['Up'] = True
        if event.keysym == 'Down':
            keyboard['Down'] = True
        if event.keysym == 'Left':
            keyboard['Left'] = True
        if event.keysym == 'Right':
            keyboard['Right'] = True
    def key_release(event):
        if event.keysym == 'Up':
            keyboard['Up'] = False
        if event.keysym == 'Down':
            keyboard['Down'] = False
        if event.keysym == 'Left':
            keyboard['Left'] = False
        if event.keysym == 'Right':
            keyboard['Right'] = False
    root.bind("<Key>", key_press) 
    root.bind("<KeyRelease>", key_release)

    # I do both 'startTime' & 'previousTime' because I want to separate
    # the time of 'elapsed' & 'dt' for easy looking at and writing codes
    startTime = clock()
    previousTime = clock()

    animate()



# make the goal move to the left (return a list of coordinates in 'field') 
def goalLeftX():
    return list(field.coords(goal))[0]


     
def animate():
    global sx, sy, goalSpeed, startTime, previousTime, roundCounter

    pattern = 'Round {0} - Elapsed time: {1:.2f} seconds \n'
    # elapsed time, which will be shown in the 'label' on the top of the Game
    elapsed = clock() - startTime
    timeDisplay['text'] = pattern.format(roundCounter, elapsed) + words1 + words2 + words3

    # measure the elapsed time more accurately 
    time = clock()
    # the time elapsed since the previous update
    dt = clock() - previousTime
    # ball displacement is vel*dt
    previousTime = time

    # process keyboard events 
    if keyboard['Up']:
        sy = -100
    if keyboard['Down']:
        sy = 100
    if keyboard['Left']:
        sx = -100
    if keyboard['Right']:
        sx = 100

    # update the Game state
    x, y = ballPosition()

    # collisions with walls
    if x+sx*dt>fieldSize or x+sx*dt<0:
        sx *= -1
    if y+sy*dt>fieldSize or y+sy*dt<0:
        sy *= -1

    # collisions with blocks
    x1 = x + sx*dt
    y1 = y + sy*dt
    for block in blocks:
        res = hitBlock(block, x, y, x1, y1)
        # dissipating collisions
        if res == 'left' or res == 'right':
            sx *= -1
        elif res == 'top' or res == 'bottom':
            sy *= -1

    # the goal bounces back
    if goalLeftX()+goalSpeed<0 or goalLeftX()+goalSize+goalSpeed>fieldSize:
       goalSpeed *= -1

    field.move(ball, sx*dt, sy*dt)
    field.move(goal, goalSpeed, 0)

    # the Game rule:
    # the user needs to enter the ball to the goal
    # while the elapsed time is less than 15 seconds
    if elapsed < 15.00:
        # if the user moves the ball into the goal
        if inGoal():
            # and finishs this task 10 times
            if roundCounter == 10:
                # the user will win the Game
                timeDisplay['text'] = '\n Game Over!!! \n You Win!!! \n'
                # they can click the 'Start' button to replay the Game (0 round)
                roundCounter = 0
        else:
            root.after(20, animate)
    # if the user does not complete the task
    # (entering the ball to the goal within 15 seconds)
    # then the user will lose the Game
    # they can click the 'Start' button to replay the Game (0 round) 
    else:
        timeDisplay['text'] = '\n Time Up!!! \n You Lose!!! \n'
        roundCounter = 0
        



def hitBlock(block, x0, y0, x1, y1):
    global moveblock

    # checks which side of the block was hit
    bx0, by0, bx1, by1 = field.coords(block)
    if bx0 <= x1 <= bx1 and by0 <= y1 <= by1:
        if y0 < by0:
            return 'top'
        elif y0 > by1:
            return 'bottom'
        elif x0 < bx0:
            return 'left'
        else:
            return 'right'
    else:
        return 'no-collision'

    # return True if the center of the ball is inside the block’s boundary
    if not moveblock:
        return False
    ballX, ballY = ballPosition()
    blockX1, blockY1, blockX2, blockY2 = field.coords(moveblock)
    return (blockX1 <= ballX <= blockX2 and
            blockY1 <= ballY <= blockY2)



# return True if the center of the ball is inside the goal area
def inGoal():
    ballX, ballY = ballPosition()
    return (goalLeftX() <= ballX <= goalLeftX()+goalSize and
            0 <= ballY <= goalSize)



root = Tk()

timeDisplay = Label(root)
# the note I want to show the user/player
words1 = '\n Note: \n You need to enter the goal 10 times to WIN the Game! \n'
words2 = 'However, you ONLY have 15 seconds in each Round. \n'
words3 = 'If your time is up in any Round, you will LOSE the Game! \n'
# show the note before the user starts the Game
# so that they can know the rules of the Game
timeDisplay['text'] = words1 + words2 + words3
timeDisplay.pack()


field = Canvas(root, width=fieldSize, height=fieldSize, bg='#fff585')
# create the goal (square)
goal = field.create_rectangle(0, goalSize, goalSize,
                              0, fill='#c520e6')
# I create 7 blocks in total
# because each block is separated and their coordinates are different,
# and I only know this way to creat blocks
# and therefore I make each block in each line
# I'm not sure if there are other more effective ways to make these blocks
# '*newScreenPer' is to increase the size of blocks, as increasing the field size
block1 = field.create_rectangle(50*newScreenPer, 100*newScreenPer,
                                125*newScreenPer, 75*newScreenPer, fill='#ff9326')
block2 = field.create_rectangle(175*newScreenPer, 100*newScreenPer,
                                250*newScreenPer, 75*newScreenPer, fill='#ff9326')
block3 = field.create_rectangle(0*newScreenPer, 150*newScreenPer,
                                75*newScreenPer, 175*newScreenPer, fill='#ff9326')
block4 = field.create_rectangle(125*newScreenPer, 150*newScreenPer,
                                175*newScreenPer, 175*newScreenPer, fill='#ff9326')
block5 = field.create_rectangle(300*newScreenPer, 150*newScreenPer,
                                225*newScreenPer, 175*newScreenPer, fill='#ff9326')
block6 = field.create_rectangle(75*newScreenPer, 225*newScreenPer,
                                100*newScreenPer, 300*newScreenPer, fill='#ff9326')
block7 = field.create_rectangle(200*newScreenPer, 225*newScreenPer,
                                225*newScreenPer, 300*newScreenPer, fill='#ff9326')
# after setting all blocks, I put them in the 'blocks' list 
blocks = [block1, block2, block3, block4, block5, block6, block7]
field.pack()

# add note of the input
promptbox = Label(root)
promptbox['text'] = 'Use the Arrow Keys to Move the Ball to the Goal'
promptbox.pack()

# create the 'Start' button
startButton = Button(root, command=startGame, text='Start')
startButton.pack()



mainloop()
