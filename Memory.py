#!/bin/env python2
# coding=utf-8

def memory():
    print("          ⸮                   ¿                        ?          ")
    print("                   ?              ⸮          ⸮              ¿     ")
    print("     ?                    ?                        ⸮              ")
    print("   ⸮          ¿                      ?                  ?       ⸮ ")
    print("                      ⸮       ¿             ¿                     ")
    print("           ⸮             ¿        ?              ⸮        ¿       ")

    print("                              STAGE 1                               ")
    print("====================================================================")
    display1 = raw_input("What is the big number displayed? -> ")
    buttons1 = raw_input("Enter the numbers on the buttons, separated by a space, from right to left. -> ")
    print("")
    smallNums1 = buttons1.split()

    position1 = ""
    label1 = ""

    if (display1 == "1"):
        print("Press the " + smallNums1[1])
        position1 = 1
        label1 = smallNums1[position1]
    elif (display1 == "2"):
        print("Press the " + smallNums1[1])
        position1 = 1
        label1 = smallNums1[position1]
    elif (display1 == "3"):
        print("Press the " + smallNums1[2])
        position1 = 2
        label1 = smallNums1[position1]
    elif (display1 == "4"):
        print("Press the " + smallNums1[3])
        position1 = 3
        label1 = smallNums1[position1]

    print("")
    print("                              STAGE 2                               ")
    print("====================================================================")
    display2 = raw_input("What is the big number displayed? -> ")
    buttons2 = raw_input("Enter the numbers on the buttons, separated by a space, from right to left. -> ")
    print("")
    smallNums2 = buttons2.split()

    position2 = ""
    label2 = ""

    if (display2 == "1"):
        print("Press the 4.")
        position2 = smallNums2.index("4")
        label2 = "4"
    elif (display2 == "2"):
        print("Press the " + smallNums2[position1])
        position2 = position1
        label2 = smallNums2[position1]
    elif (display2 == "3"):
        print("Press the " + smallNums2[0])
        position2 = 0
        label2 = smallNums2[position2]
    elif (display2 == "4"):
        print("Press the " + smallNums2[position1])
        position2 = position1
        label2 = smallNums2[position1]

    print("")
    print("                              STAGE 3                               ")
    print("====================================================================")
    display3 = raw_input("What is the big number displayed? -> ")
    buttons3 = raw_input("Enter the numbers on the buttons, separated by a space, from right to left. -> ")
    print("")
    smallNums3 = buttons3.split()

    position3 = ""
    label3 = ""

    if (display3 == "1"):
        print("Press the " + label2)
        position3 = smallNums2.index(label2)
        label3 = label2
    elif (display3 == "2"):
        print("Press the " + label1)
        position3 = smallNums3.index(label1)
        label3 = label1
    elif (display3 == "3"):
        print("Press the " + smallNums3[2])
        position3 = 2
        label3 = smallNums3[position3]
    elif (display3 == "4"):
        print("Press the 4.")
        position3 = smallNums3.index("4")
        label3 = "4"

    print("")
    print("                              STAGE 4                               ")
    print("====================================================================")
    display4 = raw_input("What is the big number displayed? -> ")
    buttons4 = raw_input("Enter the numbers on the buttons, separated by a space, from right to left. -> ")
    print("")
    smallNums4 = buttons4.split()

    position4 = ""
    label4 = ""

    if (display4 == "1"):
        print("Press the " + smallNums4[position1])
        position4 = position1
        label4 = smallNums4[position1]
    elif (display4 == "2"):
        print("Press the " + smallNums4[0])
        position4 = 0
        label4 = smallNums4[position4]
    elif (display4 == "3" or display4 == "4"):
        print("Press the " + smallNums4[position2])
        position4 = position2
        label4 = smallNums4[position4]

    print("")
    print("                              STAGE 5                               ")
    print("====================================================================")
    display5 = raw_input("What is the big number displayed? -> ")
    buttons5 = raw_input("Enter the numbers on the buttons, separated by a space, from right to left. -> ")
    print("")
    smallNums5 = buttons5.split()

    position5 = ""
    label5 = ""

    if (display5 == "1"):
        print("Press the " + label1)
        position5 = smallNums5.index(label1)
        label5 = label1
    elif (display5 == "2"):
        print("Press the " + label2)
        position5 = smallNums5.index(label2)
        label5 = label2
    elif (display5 == "3"):
        print("Press the " + label4)
        position5 = smallNums5.index(label4)
        label5 = label4
    elif (display5 == "4"):
        print("Press the " + label3)
        position5 = smallNums5.index(label3)
        label5 = label3

    print("")
