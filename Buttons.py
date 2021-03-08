#!/bin/env python2
# coding=utf-8

color = ""
word = ""
numBatteries = ""
car = ""
frk = ""


def is_color(test_color):
    global color
    if color == "":
        color = raw_input("What color is the button? -> ").lower()
        print("")
    if (color == test_color):
        return True
    else:
        return False


def is_word(test_word):
    global word
    if word == "":
        word = raw_input("What does the button say? -> ").lower()
        print("")
    if word == test_word:
        return True
    else:
        return False


def is_batteries(test_batteries):
    global numBatteries
    if numBatteries == "":
        numBatteries = input("How many batteries are on the bomb? -> ")
        print("")
    if numBatteries > test_batteries:
        return True
    else:
        return False


def is_car(test_car):
    global car
    if car == "":
        car = raw_input("Is there a lit CAR indicator? (y/N)-> ").lower()
        if (car == "n") or (car == "no") or (car == ""):
            car = False
        elif (car == "y") or (car == "yes"):
            car = True
        else:
            print("   ⚠ ERROR! Exit 2: Invalid input. Please double check response and rerun.")
            return 2
        print("")
    if car == test_car:
        return True
    else:
        return False


def is_frk(test_frk):
    global frk
    if frk == "":
        frk = raw_input("Is there a lit FRK indicator? (y/N)-> ").lower()
        if (frk == "n") or (frk == "no") or (frk == ""):
            frk = False
        elif (frk == "y") or (frk == "yes"):
            frk = True
        else:
            print("   ⚠ ERROR! Exit 2: Invalid input. Please double check response and rerun.")
            return 2
        print("")
    if frk == test_frk:
        return True
    else:
        return False


def reset_button_data():
    global color
    global word
    global numBatteries
    global car
    global frk

    color = ""
    word = ""
    numBatteries = ""
    car = ""
    frk = ""


def heldButton():
    print("Press and hold the button. Do not release it.")
    print("")
    color = raw_input("What color did the strip to the right of the button turn? -> ")
    print("")
    if (color == "blue"):
        print("Release when the countdown timer has a 4 in any position.")
    elif (color == "white"):
        print("Release when the countdown timer has a 1 in any position.")
    elif (color == "yellow"):
        print("Release when the countdown timer has a 5 in any position.")
    else:
        print("Release when the countdown timer has a 1 in any position.")


def button():
    print("")
    print("      💣                          ")
    print("💣          ˹     ˺        💣     ")
    print("            💣 ⊹               💣 ")
    print(" 💣         ˻     ˼  💣           ")
    print("           💣             💣      ")
    print("")

    if (is_color("blue") and is_word("abort")):
        heldButton()
    elif (is_batteries(1) and is_word("detonate")):
        print("Press and immediately release the button.")
    elif (is_color("white") and is_car(True)):
        heldButton()
    elif (is_batteries(2) and is_frk(True)):
        print("Press and immediately release the button.")
    elif (is_color("yellow")):
        heldButton()
    elif (is_color("red") and is_word("hold")):
        print("Press and immediately release the button.")
    else:
        heldButton()

    reset_button_data()
    print("")
