import os
import errors.e as er
import libs.colors as clr

def run(args):
    try:
        file = open(args[1], "r+")
        f = file.read().split("\n")
        #ready = "".join(string)
        #print(ready)
        curr_line = 0
        color = 0
        for line in f:
            if (color > 12):
                color = 0
            elif (color == 0):
                c = clr.Colors.BLUE
            elif (color == 1):
                c = clr.Colors.BROWN
            elif (color == 2):
                c = clr.Colors.CYAN
            elif (color == 3):
                c = clr.Colors.DARK_GRAY
            elif (color == 4):
                c = clr.Colors.LIGHT_CYAN
            elif (color == 5):
                c = clr.Colors.GREEN
            elif (color == 6):
                c = clr.Colors.LIGHT_BLUE
            elif (color == 7):
                c = clr.Colors.LIGHT_GREEN
            elif (color == 8):
                c = clr.Colors.PURPLE
            elif (color == 9):
                c = clr.Colors.LIGHT_PURPLE
            elif (color == 10):
                c = clr.Colors.RED
            elif (color == 11):
                c = clr.Colors.LIGHT_RED
            elif (color == 12):
                c = clr.Colors.YELLOW

            curr_line += 1
            color += 1
            print(c + line)

    except FileNotFoundError as e:
        e = str(e).split("]")[1]
        print(e)