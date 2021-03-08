#!/bin/env python2
# coding=utf-8

def simon(is_verbose):
    print("                                  /\\                     ")
    print("                                 /  \\                    ")
    print("                                /    \\                   ")
    print("                               /\\    /\\                 ")
    print("                              /  \\  /  \\                ")
    print("                             /    \\/    \\               ")
    print("                             \\    /\\    /               ")
    print("                              \\  /  \\  /                ")
    print("                               \\/    \\/                 ")
    print("                                \\    /                   ")
    print("                                 \\  /                    ")
    print("                                  \\/                     ")

    callResponse = dict()
    print("Hello! Simon says to check to see if the serial number contains a vowel.")
    vowel = raw_input("Is there a vowel? (Y/n)-> ").lower()
    if vowel == "":
        vowel = "y"
    if vowel == "yes":   # <-- Change to single letter response
        vowel = "y"
    elif vowel == "no":
        vowel = "n"

    strikes = raw_input("How many strikes do you have? (0)-> ")
    print("")
    if strikes == "":
        strikes = 0
    else:
        try:
            strikes = int(strikes)
        except:
            print("   ⚠ ERROR! Exit 2: Invalid input. Please ensure your strikes as an integer and rerun.")
            print("")
            return 2

    if is_verbose:
        print("Is a vowel in the serial number: " + vowel)
        print("Accumulated strikes: " + str(strikes))

    if (vowel == "y"):
        if (strikes == 0):
            callResponse["red"] = "blue"
            callResponse["blue"] = "red"
            callResponse["green"] = "yellow"
            callResponse["yellow"] = "green"
        elif (strikes == 1):
            callResponse["red"] = "yellow"
            callResponse["blue"] = "green"
            callResponse["green"] = "blue"
            callResponse["yellow"] = "red"
        elif (strikes == 2):
            callResponse["red"] = "green"
            callResponse["blue"] = "red"
            callResponse["green"] = "yellow"
            callResponse["yellow"] = "blue"
    else:
        if (strikes == 0):
            callResponse["red"] = "blue"
            callResponse["blue"] = "yellow"
            callResponse["green"] = "green"
            callResponse["yellow"] = "red"
        elif (strikes == 1):
            callResponse["red"] = "red"
            callResponse["blue"] = "blue"
            callResponse["green"] = "yellow"
            callResponse["yellow"] = "green"
        elif (strikes == 2):
            callResponse["red"] = "yellow"
            callResponse["blue"] = "green"
            callResponse["green"] = "blue"
            callResponse["yellow"] = "red"

    called = ""
    combo = ""

    print("Input \"done\" when module is completed.")
    print("What color is flashing?")
    while True:

        if is_verbose:
            print("STAGE " + str(stage))
            print("Current combo: " + combo)
            print("")

        print("What new color is flashing?")
        called = raw_input("    -> ").lower()
        if called == "done":
            print("")
            print("Congratulations! You got it!")
            print("")
            break

        combo += (callResponse[called] + " ")

        print("")
        print("        Respond with " + combo)
        print("")

