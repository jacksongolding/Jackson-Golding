#funcy.py
import time

# terminal print commands
ANSI_CLEAR_SCREEN = u"\u001B[2J"
ANSI_HOME_CURSOR = u"\u001B[0;0H\u001B[2"
GRASS_COLOR = u"\u001b[42m"
PERSON_COLOR = u"\u001b[34;1m"
RESET_COLOR = u"\u001B[0m\u001B[2D"

def grass_print():
    # print ocean
    print(ANSI_CLEAR_SCREEN, ANSI_HOME_CURSOR)
    print("\n\n\n\n")
    print(GRASS_COLOR + "  " * 35)


# print ship with colors and leading spaces
def person_print(position):
    print(ANSI_HOME_CURSOR)
    print(RESET_COLOR)
    sp = " " * position
    print(PERSON_COLOR, end="")
    print(sp + "    /\   ")
    print(sp + "    \/   ")
    print(sp + "   /|\   ")
    print(sp + "   / \ ")
    print(RESET_COLOR)


# ship function, iterface into this file
def ship():
    # only need to print ocean once
    grass_print()

    # loop control variables
    start = 0  # start at zero
    distance = 60  # how many times to repeat
    step = 2  # count by 2

    # loop purpose is to animate ship sailing
    for position in range(start, distance, step):
        person_print(position)  # call to function with parameter
        time.sleep(.1)
