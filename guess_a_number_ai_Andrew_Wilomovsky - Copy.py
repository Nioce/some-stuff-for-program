# Guess-A-Number AI
#
# Andrew, Wilomovsky(s)
# September 1, 2016


import random
import sys
import time
import os
import getpass

def start_screen():
    print("""
░░░░░░░░▄▀█▀█▄██████████▄▄░░░░░░
░░░░░░░▐██████████████████▌░░░░░ 
░░░░░░░████Welcome██To██████▌░░░░░
░░░░░░▐███████████████████▌░░░░░
░░░░░░████The████Start-Screen████▄ ░░░
░░░▄█▐█▄█▀█████████████▀█▄█▐█▄░░ 
░▄██▌██████▄█▄█▄█▄█▄█▄█████▌██▌░ 
▐████▄▀▀▀▀████████████▀▀▀▀▄███░░ 
▐█████████▄▄▄▄▄▄▄▄▄▄▄▄██████▀░░░ 
░░░▀▀████████████████████░░░░░░░
░░░░░░░Ma'Lady░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
                          Press enter to tip Le'Fedora

                          """

                          "curent player "+ getpass.getuser())
    input() 
    
def play():
    #This is For clearing the screen of text
    def clear():
        print(' \n' * 25)
    print()
    print()
    print()
    print()
    print("AI:::I think I can guess the number that your thinking of")
    print()
    print("Think of a random number and keep it in your mind")
    low = 1
    tries = 0
    high = 100
    got_it = False
    cheater = False
    bae = False
    print()
    print()
    print("Press enter to play my dude " + getpass.getuser())
    input()

    print("Scroll down if you see this ty")
    clear()
    #MAIN CODE MY DUDE
    #aorb = above or below
    while got_it == False:
        guess = (high + low)//2
        print()
        print ("AI:::::::Is it above " + str(guess) + " or below " + str(guess) +"," + getpass.getuser())
        aorb = input("""Type h or l or y.
    H=High
    L=Low
    Y=Yes   """)
        if aorb in [ 'H', 'h', 'High', 'high', 'hug', 'hi', 'higher']:
            if high == low:
                cheater = True
                got_it = True
            low = (guess + 1)
        elif aorb == ("bae"):
            got_it = True
            bae = True
        elif aorb in ['L', 'l', 'Low', 'low', 'lo', 'lol', 'lower']:
            if high == low:
                cheater = True
                got_it = True
            high = (guess - 1)
        elif aorb in ['Y', 'y', 'yes', 'Yes', 'yup', 'ye']:
            got_it = True
        tries = (tries)+1
#All of the if __ then go ___ cause ____             
    if cheater == True:
        clear()
        print()
        print("Sir You lied or you broke it, its a 50/50 so restart")
    else:
        clear()
        print()
        print("AI: I got it ha, " +getpass.getuser() + " and only in " +str(tries))

    if bae == True:
        clear()
        print("Stop looking through my code, or your just a magic mike at guessing")
        
#Credits/play again
def play_again():
    while True:
        print()
        answer = input("Would you like to play again, " + getpass.getuser() + " " )

        if answer in [ 'no', 'n', 'No', 'no', 'Nay', 'bae']:
            return False
        elif answer in ['y', 'yes', 'ye', 'yup', 'Yes', 'Y','Yup']:
            return True
        print()
        print("What?!!! Just say yes or no dont be a smart***.")


# game ends
start_screen()

again = True

while again == True:
    play()
    again = play_again()
    
#Had to redo this cause new section #RIPmyBrain
    def clear():
        print(' \n' * 25)
clear()
print("Game over")
print("""░░░░░░░░░░░░░░░░░░░░ 
░▄▀▄▀▀▀▀▄▀▄░░░░░░░░░ 
░█░░░░░░░░▀▄░░░░░░▄░ 
█░░▀░░▀░░░░░▀▄▄░░█░█ 
█░▄░█▀░▄░░░░░░░▀▀░░█ 
█░░▀▀▀▀░░░░░░░░░░░░█ 
█░░░░░░░░░░░░░░░░░░█ 
█░░░░░░░░░░░░░░░░░░█ 
░█░░▄▄░░▄▄▄▄░░▄▄░░█░ 
░█░▄▀█░▄▀░░█░▄▀█░▄▀░ 
░░▀░░░▀░░░░░▀░░░▀░░░
Hope you had fun, cause my head now hurts from making this
I want to cry....

By~Andrew.Wilomovsky
9/1/2016 - 9/8/2016
7th period



END ME""")

        
        #THIS TOOK FOREVER TO MAKE  :(:::::::
        
        
        
