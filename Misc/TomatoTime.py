import time
import winsound
from tkinter import Tk, Label, Button

"""""""""""""""""""""""""""""""""""""""""
TomatoTime by Bryce Hickle 

Version 5.1.2020

Coach Tomato is a motivational coach dedicated to making individuals as rugged and independent as itself.

alert() and alert2() sound the alarms

run() is, well, the runner function

main() is, well, the system main function for calling run() in a command line

"""""""""""""""""""""""""""""""""""""""""


def alert():

    freq = 2500  # sound frequency in hertz
    dur = 250 #duration in ms
    winsound.Beep(freq, dur)

    freq = 1000  # sound frequency in hertz
    dur = 250  # duration in ms
    winsound.Beep(freq, dur)

    freq = 120  # sound frequency in hertz
    dur = 800  # duration in ms
    winsound.Beep(freq, dur)

def alert2():

    freq = 2500  # sound frequency in hertz
    dur = 500  # duration in ms
    winsound.Beep(freq, dur)


def run(timer):

    aTime = (timer * 60)
    rest = (10 * 60)
    round = 4
    roundCount = 0

    time.sleep(2)
    alert2()
    print("START WORKING SPORT!")
    while round > 0:

        #work period
        for i in range(1, (aTime + 1)):
            if((i % 60) == 0):
                print("MINUTE " + str(i / 60) + "!!!!!!\n I SAID MINUTE " + str(i / 60) + "!!!!!\n CRIPES!!!!")
            time.sleep(1)
        alert()
        print("REST!!!!!!!!!!!! REST!!!!!!!!!!!! REST!!!!!!!!!!!! REST!!!!!!!!!!!! REST!!!!!!!!!!!! REST!!!!!!!!!!!!")

        # rest period
        for i in range(1, (rest + 1)):
            if(( i % 60 ) == 0):
                print(i / 60) #minute you're on
                print("Keep Breathin' sport.\n  You're gonna get the project done on time.\n I'm right here with ya.")
            time.sleep(1)
        alert()
        roundCount += 1
        print("ROUND " + str(roundCount) + " DONE!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        round -= 1

    again = input("ALL ROUNDS COMPLETED\n again? (y/n) ")

    if(again.isalpha() and again == "y"):
        run(timer)
    else:
        print("\nYou worked hard today, sport. It'll get easier over time.\n Get some sleep and stop by my gym anytime.")


def main():
    print("Hello world. I'm Coach Tomato. I'm here to help.")
    time.sleep(3)
    print("Now...")
    time.sleep(2)
    sessionType = input("is the work ahead of you fun, tedious, or tough? ")
    print("\nThen it is Tomato Time.\n***********************")
    if(sessionType.isalpha() and sessionType == "fun"):
        run(120)
    elif(sessionType.isalpha() and sessionType == "tedious"):
        run(60)
    elif(sessionType.isalpha() and sessionType == "tough"):
        run(30)
    else:
        print("error: rerun program")

if __name__ == "__main__":
    main()
