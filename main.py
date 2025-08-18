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
    ropasc,
    makemods,
    updatefile,
    changepass
)
TheSnoreVariable = True


print("Hi, I'm the U.I. for the Videogame Console Dataset.")

#long bit of print statements for information's sake. Might find a to toggle.
def UI():
    global TheSnoreVariable
    print('These are the functions you can access through me:')
    print('1. View Full Dataset')
    print('2. Visualise Data')
    print('3. Find Data via Search or Filter')
    print('4. Modify existing Data(Req. Password)')
    print('5. Save Modifications (Req. Password)')
    print('6. Change Password (Req. Password)')
    print("7. View my Creator's Conclusions")
    print('8. Play Rock Paper Scissors')
    print('9. Exit Program')
    what = input('What would you like to do? Input 1-9: ').strip() #found this cool thing to reduce typos
    if what == '1':
        fulldataset()
    elif what == '2':
        visualisations()
    elif what == '3':
        datafindfilter()
    elif what == '4':
        makemods()
    elif what == '5':
        updatefile()
    elif what == '6':
        changepass()
    elif what == '7':
        print('A wordy explanation of my person opinion after having done all this. Will be added... when I have done all this')
    elif what == '8':
        ropasc()
    elif what == '9':
        print('Bye-Bye!')
        TheSnoreVariable = False
    else:
        print("Apparently that's not a valid input... You should try again, you probably typed something wrong. Either that or there's a bug.")

while TheSnoreVariable == True:
    UI()
    time.sleep(1)