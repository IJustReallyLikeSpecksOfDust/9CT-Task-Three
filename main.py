#hey look there's stuff here
#setup imports and variables and stuff
import pandas as pd
import matplotlib.pyplot
import random
import time
from data_module import (
    fulldataset,
    visualisations,
    datafindfilter,
    ropasc
)
from PIL import Image
TheSnoreVariable = True
sensationofyourscreen = Image.open("images/TVTIME.jpg")

print("Hi, I'm the U.I. for the Videogame Console Dataset.")

#long bit of print statements for information's sake. Might find a to toggle.
def UI():
    global TheSnoreVariable
    print('These are the functions you can access through me:')
    print('1. View Full Dataset')
    print('2. Visualise Data')
    print('3. Find Data via Search or Filter')
#    print('4. Modify existing Data(Req. Password)')
#    print('5. Save Modifications (Req. Password)')
#    print('6. Change Password (Req. Password)')
    print("4. View my Creator's Conclusions")
    print('5. Play Rock Paper Scissors')
    print('6. Exit Program')
    what = input('What would you like to do? Input 1-6: ').strip() #found this cool thing to reduce typos
    if what == '1':
        fulldataset()
    elif what == '2':
        visualisations()
    elif what == '3':
        datafindfilter()
#    elif what == '4':
#        makemods()
#    elif what == '5':
#        updatefile()
#    elif what == '6':
#        changepass()
    elif what == '4':
        print('A wordy explanation of my person opinion after having done all this. Will be added... when I have done all this')
    elif what == '5':
        ropasc()
    elif what == '6':
        byebye = random.randint(0,16)
        if byebye == 0:
            print('Bye-Bye!')
        elif byebye == 1:
            print('Bye-Bye!')
        elif byebye == 2:
            print('バイバイ')
        elif byebye == 3:
            print('Silksong Tomorrow.')
        elif byebye == 4:
            print('The creator got a shiny Regidrago while working on this!')
        elif byebye == 5:
            print("I really hope Xbox 'Magnus' is the final name, because that is SUCH a cool word.")
        elif byebye == 6:
            print('how does the random function do it anyway? gotta be some form of Pseudo-RNG right? I could google it but ehhh')
        elif byebye == 7:
            print('Never ask Valve the number that comes after "2".')
        elif byebye == 8:
            print('Boutta watch the Nintendo Direct on Kirby Air Riders.')
        elif byebye == 9:
            print('Yawn.')
        elif byebye == 10:
            print('PS6 when?!')
        elif byebye == 11:
            print('Wii U 2 when?!')
        elif byebye == 12:
            print("Say it with him, folks!") #google taught me how to put images here sooooooo
            sensationofyourscreen.show('deltarune reference')
        elif byebye == 13:
            print('Unlucky number 13!')
        elif byebye == 14:
            print('Did you know human flesh tastes like pork? Wonder what the skin of integer 10 tastes like.')
        elif byebye == 15:
            print('I... AM STEVE')
        elif byebye == 16:
            print("Dont'ya just love these secret end messages?")
        time.sleep(1)
        TheSnoreVariable = False
    else:
        print("Apparently that's not a valid input... You should try again, you probably typed something wrong. Either that or there's a bug.")

while TheSnoreVariable == True:
    UI()
    time.sleep(1)