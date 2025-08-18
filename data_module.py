#here's the imports
import pandas as pd
import matplotlib.pyplot
import random
import time

#okay first time to define some variables
thedata = pd.read_csv('data/consdata.csv') #this should be reading the data but i dont know if it is. i'm not getting anything 
passwordentered = False
correctpass = 'cheeseburgertempo'

#print the full dataset
def fulldataset(): 
    print(thedata)
    movingon = input('You can type anything here, just input to move on. ')
    #I really have no idea if this is the output I need to give but it took me an embarassing amount of time to figure out that you needed to do it as a print, so I'm going to say this is fine.

#visualisation options. gonna take some time
def visualisations():
    print('Function not finished. Sorry.')

#finds and filters data
def datafindfilter():
    print("Alright, let's make a graph.")
    print('These are the types you can choose: 1. Scatter')
    graphtype = input('Type the number for your choice here: ')
    if graphtype == '1':
        print('Scatter graph, got it. Okay, for the values, what should be on the X axis? Make sure you type something from the csv. ')

#a simple password protection function. usage of global allows it to work between functions if i code this in a good way (with a loop)
def passwordprotection():
    global passwordentered
    global correctpass
    if passwordentered == False:
        guess = input('Input the password. ')
        if guess == correctpass:
            passwordentered = True
        else:
            print('(Not actually) Sorry to tell you this, but that password is wrong.')

#change values. this seems hard to code
def makemods():
    passwordprotection()
    if passwordentered == True:
        print('Function not finished. Sorry.')

#save the things changed by makemods. may just be integrated into makemods.
def updatefile():
    passwordprotection()
    if passwordentered == True:
        print('Function not finished. Sorry.')

#this'll either just be a pointless for-fun function or something that works between program uses, depending on if i can make the password write to another document.
def changepass():
    passwordprotection()
    if passwordentered == True:
        print('Function not finished. Sorry.')

#this exists because I wanted to refresh myself on python coding
def ropasc():
    userchoice = input('Please type Rock, Paper, or Scissors; ').lower()
    interfacechoice = str(random.randint(1,3))
    if userchoice == 'rock' and interfacechoice == '1':
        print('We both chose Rock, as such it is a tie. Not much of a landslide...')
    elif userchoice == 'rock' and interfacechoice == '2':
        print('Haha, I won! You chose Rock and I chose Paper. Yay, for once I get some excitement!')
    elif userchoice == 'rock' and interfacechoice == '3':
        print('Well... You chose Rock and I chose Scissors. Am I not a program? Why can I even lose, this is dumb.')
    elif userchoice == 'paper' and interfacechoice == '1':
        print("Well... You chose Paper and I chose Rock. That's kinda rude y'know?")
    elif userchoice == 'paper' and interfacechoice == '2':
        print('We both chose Paper, as such it is a tie. This is starting to remind me of an office...')
    elif userchoice == 'paper' and interfacechoice == '3':
        print("Haha, I won! You chose Paper and I chose Scissors! This is the most fun I've ever had.")
    elif userchoice == 'scissors' and interfacechoice == '1':
        print("Haha, I won! You chose Scissors and I chose Rock! Get... Rocked? Whatever, I won, ha-ha!")
    elif userchoice == 'scissors' and interfacechoice == '2':
        print("Well... You chose Scissors and I chose Paper. T'ch, you just got lucky.")
    elif userchoice == 'scissors' and interfacechoice == '3':
        print("We both chose Scissors, as such it is a tie. Maybe we should cut the tie.")
    elif userchoice == 'gun':
        print("What are you, 6? There's no 'Gun' choice in Rock Paper Scissors.")
    else:
        print("Are you stupid? That's not a valid choice, learn to spell! Wait, sorry that was rude, you probably just made a typo...")
    time.sleep(3)


#the other options will be local to main.py