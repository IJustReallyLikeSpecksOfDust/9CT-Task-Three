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
        print("The information I gained from my data suggests that largely; console prices have risen accordingly with inflation, and, notably have never taken large profits. " \
        "Generally, most consoles lingered around $400 for quite some time, though with Nintendo's being lower than XBox and Playstation. In the data for manufacturing prices it's worth noting that margins were quite thin for most consoles, and the data doesn't even " \
        "show other associated costs like shippng and retailers' cuts. This suggests that the business model used to be more focused around distribution than profit on consoles, and I would argue that that hasn't changed (except the PS5 Pro). " \
        "The inflation data suggests that the purchasing power of a USD is around x 0.6 weaker than in 2005, and that is around how much the console prices have risen, specifically in recent years, which can likely be accredited " \
        "to the pandemic. Take Nintendo's prices, the Wii was $250 on release, which multiplied by 1.6 gets to $400. While not exactly the same as the US NS2 Price, it explains a large rise in prices, especially when you again" \
        " see the manufacturing prices on those two consoles, which is a much larger difference of $240. To illustrate, think of it as a fresh fruit stall. Their most recent plantation cost more due to increased demand,"
        " and the new trees are taller and thus need more labour to get the apples down. These two factors, among many others, naturally lead to a price increase, and it's the same for consoles with the inflation and manufacturing costs both rising. " \
        "As such, having conluded my research, I now hold the opinion that videogame consoles like the PS5, Xbox Series X, and Nintendo Switch 2 ARE fairly priced, as were consoles like the Wii and Xbox 360.")
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