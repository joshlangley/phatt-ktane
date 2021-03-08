#!/bin/env python2
# coding=utf-8

def serial(which_state):
    if which_state == "odd":
        if raw_input("Is the last digit of the serial number odd? (y/n)-> ").lower() == "y":
            print("")
            return True
        else:
            print("")
            return False


def wires(is_verbose):
    print("                       ________________|         ")
    print("                    ✀ |                         ")
    print("                       |                         ")

    print("Input the wires in order from top to bottom, separated by spaces.")
    print("")
    print("Accepted values (⚠CASE SENSITIVE⚠):")
    print("    - \"red\" or \"r\"")
    print("    - \"blue\", \"blu\", or \"b\"")
    print("    - \"yellow\" or \"y\"")
    print("    - \"black\", \"bla\", or \"B\"")
    print("    - \"white\" or \"w\"")
    print("")
    print("Example 1: -> red blue blue black white")
    print("Example 2: -> r b b B w")
    print("")
    wires = ""
    while(wires == ""):
        wires = raw_input("    -> ")
    print("")
    wires = wires.split()

    n_wires = 0
    red_wires = 0
    blue_wires = 0
    yellow_wires = 0
    black_wires = 0
    white_wires = 0

    for wire in wires:
        n_wires += 1
        if (wire == "r") or (wire == "red"):
            red_wires += 1
        if (wire == "blu") or (wire == "b") or (wire == "blue"):
            blue_wires += 1
        if (wire == "y") or (wire == "yellow"):
            yellow_wires += 1
        if (wire == "bla") or (wire == "B") or (wire == "black"):
            black_wires += 1
        if (wire == "w") or (wire == "white"):
            white_wires += 1

    if is_verbose == True:
        print("     DEBUGGING INFO:     ")
        print("=========================")
        print("Number of wires: "+str(n_wires))
        print("Number of red wires: "+str(red_wires))
        print("Number of blue wires: "+str(blue_wires))
        print("Number of yellow wires: "+str(yellow_wires))
        print("Number of black wires: "+str(black_wires))
        print("Number of white wires: "+str(white_wires))
        print("The last wire is: "+str(wires[-1]))
        print("")


    if n_wires == 3:
        if red_wires == 0:
            print "Cut the second wire."
        elif (wires[-1] == "w") or (wires[-1] == "white"):
            print "Cut the last wire."
        elif blue_wires > 1:
            print "Cut the last blue wire."
        else:
            print "Cut the last wire."

    elif n_wires == 4:
        if (red_wires > 1) and (serial("odd")):
            print "Cut the last red wire."
        elif ((wires[-1] == "y") or (wires[-1] == "yellow")) and (red_wires == 0) or (blue_wires == 1):
            print "Cut the first wire."
        elif yellow_wires > 1:
            print "Cut the last wire."
        else:
            print "Cut the second wire."

    elif n_wires == 5:
        if (wires[-1] == "bla") or (wires[-1] == "B") or (wires[-1] == "black") and (serial("odd")):
            print "Cut the fourth wire."
        elif (red_wires == 1) and (yellow_wires > 1):
            print "Cut the first wire."
        elif black_wires == 0:
            print "Cut the second wire."
        else:
            print "Cut the first wire."

    elif n_wires == 6:
        if (yellow_wires == 0) and (serial("odd")):
            print "Cut the third wire."
        elif (yellow_wires == 1) and (white_wires > 1):
            print "Cut the fourth wire."
        elif (red_wires == 0):
            print "Cut the last wire."
        else:
            print "Cut the fourth wire."

    elif n_wires < 3:
        print("   ⚠ ERROR! Exit 3: Scenario does not exist; too few wires. Please check your input and rerun.")
    elif n_wires > 6:
        print("   ⚠ ERROR! Exit 4: Scenario does not exist; too many wires. Please check your input and rerun.")
    else:
        print("   ⚠ ERROR! Exit 2: Scenario does not exist. Check your input and rerun.")

    print("")


