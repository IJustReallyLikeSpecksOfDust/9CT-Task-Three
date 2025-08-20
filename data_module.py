#here's the imports
import pandas as pd
import matplotlib.pyplot as plt
import random
import time
from PIL import Image

#okay first time to define some variables
thedata = pd.read_csv('data/consdata.csv')
infdata = pd.read_csv('data/infladata.csv')
correctpass = 'cheeseburgertempo'
hornets = Image.open('images/HollowKnightSilksong.png')

#print the full dataset
def fulldataset(): 
    whichset = input('Which dataset do you want to see? 1. Console Data; 2. Inflation Data. ')
    if whichset == '1':
        print(thedata)
        movingon = input('You can type anything here, just input to move on. ')
    elif whichset == '2':
        print(infdata)
        movingon = input('You can type anything here, just input to move on. ')
    else:
        print('My creator has kinda run out of ideas for these error messages. By the way that input was invalid.')

    #I really have no idea if this is the output I need to give but it took me an embarassing amount of time to figure out that you needed to do it as a print, so I'm going to say this is fine.

#visualisation options. gonna take some time. I want to make Scatter graphs, Line graphs that can compare values, and at least one chart of some kind.
#this is really annoying.
def visualisations():
    #print(infdata.dtypes)
    print("Alright, time for a visualisation.")
    print('These are the options you have. 1. Console Visualisation, 2. Inflation Visualisation, 3. Comparison Visualisation.')
    graphtype = input('Type the number for your choice here: ')
    if graphtype == '1':
        """print('Scatter graph, got it. Okay, for the values, what should be on the X axis? ')
        xinput = input('Make sure you type something from the console data or inflation data. ').lower
        if xinput == 'units sold':
            ecks = thedata['Units sold (million)']
        else:
            print("That couldn't be found on the file...")
        print('Hopefully that went smoothly. Now what should be on the Y axis? ')
        yinput = input('Again, type something from the console data or inflation data. ').lower
        if yinput == 'consumer price (usd)':
            wai = thedata['Consumer Price (USD)']
        else:
            print("That couldn't be found on the file...")
        tinput = input('And the title? ')
        print('Great! I should be able to handle the rest.')"""
        thedata.plot( #visual display of prices
                    kind='bar',
                    x='Console Name',
                    use_index=True,
                    y='Consumer Price (AUD)',
                    color='red',
                    alpha=0.3,
                    title='Major Console Prices since 2005'
        )
        plt.show()
    elif graphtype == '2': #shows specifically the inflation stats
        infdata.plot(
                    kind='line',
                    x='Year',
                    use_index=True,
                    y='USD Value v. 2005',
                    color='pink',
                    alpha=1,
                    title='US Inflation since 2005'
        )
        plt.show()
    elif graphtype == '3':
        infdata.plot(
                    kind='line',
                    x='USD Value v. 2005',
                    use_index=True,
                    y='Consumer Price of Most Recent Console (USD)',
                    color='olive',
                    alpha=1,
                    title='USD value vs. Console Prices'
        )
        plt.show()
    else:
        print('That was not among the provided options.')


            


        
#finds and filters data. basically just an interfaced-query.
def datafindfilter():
    print("Well, I can show you just the data from one big console player, the data from just one console, or we can find a specific data point.")
    itineary = input('What would you like to see (1. Console Company, 2. Console, 3. Find a specific data point). ')
    if itineary == '1':
        print('(1 = XBox, 2 = Nintendo, 3 = Playstation)')
        corpo = input("Which company's consoles would you like to see? ")
        if corpo == '1':
            print(thedata.iloc[[0,4,7,8],:])
        elif corpo == '2':
            print(thedata.iloc[[1,3,6,12],:])
        elif corpo == '3':
            print(thedata.iloc[[2,5,9,11],:])
        else:
            print("Hey, Maxi here. I am so sick of writing these error messages. Why did I decide to give this thing personality? I have to say 'Bad input' in like 93234 different ways. Pain. ")
    elif itineary == '2':
        print('1. XB360, 2. Wii, 3. PS3, 4. Wii U 5. XBOne, 6. PS4, 7. Switch, 8. XBSS, 9. XBSX, 10. PS5, 11. Steam Deck, 12. PS5Pro, 13. NS2')
        pc = input("Pick from the list above me. ")
        if pc == '1':
            print(thedata.iloc[0,:]) #it just matches your choice with the one in consdata
        elif pc == '2':
            print(thedata.iloc[1,:])
        elif pc == '3':
            print(thedata.iloc[2,:])
        elif pc == '4':
            print(thedata.iloc[3,:])
        elif pc == '5':
            print(thedata.iloc[4,:])
        elif pc == '6':
            print(thedata.iloc[5,:])
        elif pc == '7':
            print(thedata.iloc[6,:])
        elif pc == '8':
            print(thedata.iloc[7,:])
        elif pc == '9':
            print(thedata.iloc[8,:])
        elif pc == '10':
            print(thedata.iloc[9,:])
        elif pc == '11':
            print(thedata.iloc[10,:])
        elif pc == '12':
            print(thedata.iloc[11,:])
        elif pc == '13':
            print(thedata.iloc[12,:])
        else:
            print("Your choice was not among the ones listed above. Maybe you want the iconic: SEGA Dreamcast?")
            discard = input('Do you want to see Sega Dreamcast data? (Y/N) ') #trolling
            print('How interesting.')
        movingon = input('You can type anything here, just input to move on. ')
    elif itineary == '3':
        rox = int(input('Input the x number of the datapoint you want to see (0-12). '))
        coy = int(input('Input the y number of the datapoint you want to see (0-8). '))
        print(thedata.iloc[rox,coy])
        movingon = input('You can type anything here, just input to move on. ')
    else:
        print("You entered the input incorrectly... Here's a consolation graph.")
        hornets.show()
            
#a simple password protection function. usage of global allows it to work between functions if i code this in a good way (with a loop). Semi-finished, but Scrapped.
def passwordprotection():
    global passwordentered
    global correctpass
    if passwordentered == False:
        guess = input('Input the password. ')
        if guess == correctpass:
            passwordentered = True
        else:
            print('(Not actually) Sorry to tell you this, but that password is wrong.')

#change values. this seems hard to code. Scrapped
def makemods():
    passwordprotection()
    if passwordentered == True:
        print('Function not finished. Sorry.')

#save the things changed by makemods. may just be integrated into makemods. Scrapped
def updatefile():
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