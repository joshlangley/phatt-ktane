#!/bin/env python2
# coding=utf-8

from SimpleWires import wires
from Buttons import button
from Simon import simon
from Memory import memory
from Keypad import basicKeypad

print(" ____  _     _       _   _     _  ___                   ")
print("|  _ \| |__ | | __ _| |_| |_  | |/ / |_ __ _ _ __   ___ ")
print("| |_) | '_ \| |/ _` | __| __| | ' /| __/ _` | '_ \ / _ \\")
print("|  __/| | | | | (_| | |_| |_  | . \| || (_| | | | |  __/")
print("|_|   |_| |_|_|\__,_|\__|\__| |_|\_\\\\__\__,_|_| |_|\___|")
print("💣💣💣💣💣💣💣💣💣💣💣💣💣💣💣💣💣💣💣💣💣💣💣💣💣💣💣💣")
print("")

def promptKey():
    print("Enter the module you want to run or \"exit\". Run \"help\" to see this again.")
    print("|    Modules    | Command |            Comment            |")
    print("| ------------- | ------- | ----------------------------- |")
    print("| Simple Wires  | wires   | On the Subject of Wires       |")
    print("| The Button    | button  | On the Subject of The Button  |")
    print("| Simon Says    | simon   | On the Subject of Simon Says  |")
    print("| Memory        | memory  | On the Subject of Memory      |")
    print("| Keypad        | keypad  | On the Subject of Keypads     |")
    print("")


def getCommand():
    command = ""
    while command == "":
        command = str(raw_input("[ktane@PhlattKtane ~]$ ")).lower()
    command = command.split()
    return command

promptKey()
verbose_mode = False

while True:
    command = getCommand()

    is_verbose = False
    if ("--verbose" in command) or ("-v" in command) or verbose_mode:
        is_verbose = True

        print("THE COMMAND IS CURRENTLY: ")
        print(command)
        print("IS VERBOSE?: " + str(is_verbose))
    else:
        is_verbose = False

    if(command[0] == "exit"):
        print("")
        print("                    See you later!        ")
        print("💣💣💣💣💣💣💣💣💣💣💣💣💣💣💣💣💣💣💣💣💣💣💣💣💣💣💣💣")
        print("                        BOOOM!!!           ")
        print("")
        exit()
    elif (command[0] == "help"):
        print("")
        promptKey()
        command = [""]
    elif (command[0] == "wires"):
        print("")
        wires(is_verbose)
        command = [""]
    elif (command[0] == "button"):
        print("")
        button()
        command = [""]
    elif (command[0] == "simon"):
        print("")
        simon(is_verbose)
        command = [""]
    elif (command[0] == "memory"):
        print("")
        memory()
        command = [""]
    elif (command[0] == "keypad"):
        print("")
        basicKeypad(is_verbose)
        command = [""]
    elif (command[0] == "verbose"):
        if command[1] == "true":
            verbose_mode = True
            print("Verbose mode enabled. Debugging information will be shown.")
            print("To disable verbose mode, use \"verbose false\".")
            print("")
        elif command[1] == "false":
            verbose_mode = False
            print("Verbose mode disabled.")
            print("")
    else:
        print("   ⚠ ERROR! Exit 127: Command not found.")
        print("")

