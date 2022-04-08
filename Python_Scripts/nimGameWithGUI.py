# the import list below
from tkinter import Tk, Canvas, Frame, Button, Label, Entry, END, SUNKEN, LEFT, RIGHT, DISABLED, NORMAL
from time import sleep
import random

# To run this code, load into Python, and execute runNim(n), where n is desired initial number
# of balls, in the Python shell
#

# This class is just like the solution to HW 6 Q2 with three small changes related to GUI.
class NimGame():

    def __init__(self, numberOfBalls):
        self.numberOfBallsRemaining = numberOfBalls
        statusLabel.config(text = "Nim game initialized with {} balls.".format(self.numberOfBallsRemaining))

    def remainingBalls(self):
        return self.numberOfBallsRemaining
    
    def take(self, numberOfBalls):
        
        self.numberOfBallsRemaining = self.numberOfBallsRemaining - numberOfBalls
        statusLabel.config(text = "You took {} ball(s). {} remain.".format(numberOfBalls, self.numberOfBallsRemaining))
        updateGraphics()
        
        #This block disables buttons as they become illegal options.
        #Also displays information in game instead of printing out information
        if self.numberOfBallsRemaining < 3:
            button3.config(state = DISABLED)
        if self.numberOfBallsRemaining < 2:
            button2.config(state = DISABLED)
        if self.numberOfBallsRemaining == 0:
            statusLabel.config(text = "")
            button1.config(state = DISABLED)
            #I made the canvas tell who won instead of the statusLabel for a better visual/user experience
            canvas.create_text(305, 100, fill = "blue", text = "You win!") 
            
        # After removing player-chosen balls, the graphics pause for 1.0 seconds
        # before removing computer-chosen balls.  This way the player can "see" the
        # intermediate status. 
        
        #If the game hasn't been won, the computer makes a move. If the computer wins, the player is forced to either close or restart the game.
        else:   
            updateGraphics()
            sleep(1.0)

            computerMaxBalls = min(3, self.numberOfBallsRemaining)
            compBallsTaken = random.randint(1,computerMaxBalls)
            self.numberOfBallsRemaining = self.numberOfBallsRemaining - compBallsTaken
    
            # After removing computer-chosen balls, the graphics update again.
            updateGraphics()
            statusLabel.config(text ="Computer took {} ball(s). {} remain.".format(compBallsTaken, self.numberOfBallsRemaining))
            if self.numberOfBallsRemaining < 3:
                button3.config(state = DISABLED)
            if self.numberOfBallsRemaining < 2:
                button2.config(state = DISABLED)
            if self.numberOfBallsRemaining == 0:
                statusLabel.config(text = "")
                button1.config(state = DISABLED)
                canvas.create_text(305, 100, fill = "red", text = "Computer wins!")
            
            
                
# global variables used for placement of balls
canvasHeight = 200
canvasWidth = 610
canvasBorderBuffer = 10
maxBallSize = 100
# the values of global variables below are computed and set in initializeNimAndGUI
# ballSize
# halfBallSize 
# spaceBetweenBalls 
# leftmostBallXPosition
# ballYPosition

# 1. clear the canvas
# 2. draw balls on canvas equal to number remaining in the Nim game
def updateGraphics():
    canvas.delete('all')   
    centerX = leftmostBallXPosition
    centerY = ballYPosition
    for i in range(nimGame.remainingBalls()):
        canvas.create_oval(centerX - halfBallSize,
                           centerY - halfBallSize,
                           centerX + halfBallSize,
                           centerY + halfBallSize,
                           fill="#00994c", activeoutline = "#0D0101")
        centerX = centerX + spaceBetweenBalls + ballSize
        canvas.update_idletasks()
     

        
# Callback functions invoked by GUI buttons
def takeBalls(numberToTake):
    nimGame.take(numberToTake)
    
    

#This function checks to see if the user has specified a number of balls he/she wants to play with for the next game.
#If the player has, the game intializes with the specified amount, else the game uses a default number of balls (five).
def initializeNewGame():
    inputVal = textEntry.get()
    if inputVal == "":
        numberOfBalls = 5 
        button1.config(state = NORMAL)
        button2.config(state = NORMAL)
        button3.config(state = NORMAL)
    else:
        numberOfBalls = int(textEntry.get()) 
        button1.config(state = NORMAL)
        button2.config(state = NORMAL)
        button3.config(state = NORMAL)
        
    initializeNimAndGUI(numberOfBalls)   

#####

# 1. create a NimGame object with specified number of balls
# 2. clear the graphics canvas
# 3. based on number of balls, compute values ball size and spacing and set
#     global variable used for drawing the balls.
# 
def initializeNimAndGUI(numberOfBalls):
    global nimGame
    global ballSize, halfBallSize, spaceBetweenBalls, leftmostBallXPosition, ballYPosition

    nimGame = NimGame(numberOfBalls)

    canvas.delete('all') 
    ballSize = min(maxBallSize, int(((canvasWidth-canvasBorderBuffer)//numberOfBalls)/1.2))
    halfBallSize = ballSize // 2
    spaceBetweenBalls = int(0.2 * ballSize)
    leftmostBallXPosition = (canvasBorderBuffer//2) + (spaceBetweenBalls//2) + halfBallSize
    ballYPosition = canvasHeight // 2

    updateGraphics()
    statusLabel.config(text ="Started new game.", fg = "black")
    
    
    
# create GUI for Nim Game, including
# 1. canvas where balls will be shown
# 2. some buttons, to the right of the canvas, for taking balls or starting a new game
# 3. a label, below the canvas and buttons, for status messages
#
def createGUI():
    global rootWindow
    global canvas
    global statusLabel
    global textEntry
    global button1
    global button2
    global button3

    rootWindow = Tk()
    rootWindow.title("Play Nim")
    canvasAndButtons = Frame(rootWindow)
    canvas = Canvas(canvasAndButtons, height=canvasHeight, width=canvasWidth, relief=SUNKEN, borderwidth=2, bg = "white")
    canvas.pack(side=LEFT)
    
    #setting buttons as specified and the textEntry widget with an appropriate size
    buttonFrame = Frame(canvasAndButtons)
    button1 = Button(buttonFrame, text='Take 1', command=lambda:takeBalls(1))
    button2 = Button(buttonFrame, text='Take 2', command=lambda:takeBalls(2))
    button3 = Button(buttonFrame, text='Take 3', command=lambda:takeBalls(3))
    button4 = Button(buttonFrame, text='New Game', command=initializeNewGame)
    textEntry = Entry(buttonFrame, width = 10)
   

    button1.pack()
    button2.pack()
    button3.pack()
    button4.pack()
    textEntry.pack()
    
    buttonFrame.pack(side = RIGHT)
    canvasAndButtons.pack()
    
    statusLabel = Label(rootWindow, width = 30) # Again size options are being use to make to give a widget an appropriate look.
    statusLabel.pack()
    
# Call 'runNim' with the desired number of initial balls
#
def runNim(numberOfBalls):
    createGUI()
    initializeNimAndGUI(numberOfBalls)   
    rootWindow.mainloop()

    
    