#!/bin/env python2
# coding=utf-8

from FriendlyNames import friendly_names
from KeypadChars import chars

code_matrix = [
        ["o", "a", "lam", "zig", "spi", "h", "ccc"],
        ["e", "o", "ccc", "cir", "star", "h", "que"],
        ["cop", "grin", "cir", "w", "r", "lam", "star"],
        ["sig", "pil", "tb", "spi", "w", "que", "smi"],
        ["iu", "smi", "tb", "c", "pil", "dragon", "black"],
        ["sig", "e", "puz", "ae", "iu", "n", "omg"]
        ]

def basicKeypad(is_verbose):

    print("Please enter the characters that appear in your keypad based on the table separated by spaces. They do not need to be in any specific order.")
    print("EXAMPLE:")
    print("charshell -> tb smi spi pil")
    print("")
    print("| Sym |     Name     | Code | Sym |    Name    |  Code  |")
    print("| --- | ------------ | ---- | --- | ---------- | ------ |")
    print("|  Ϙ  | O w/ Foot    | o    |  Ԇ  | Capital R  | r      |")
    print("|  Ѧ  | Cap A w/ T   | a    |  σ  | Sigma      | sig    |")
    print("|  λ  | Lamda        | lam  |  ¶  | Pilcrow    | pil    |")
    print("|  Ϟ  | Zig Zag      | zig  |  ቴ  | T and b    | tb     |")
    print("|  Ѭ  | Spider       | spi  |  Ͼ  | C w/ a Dot | c      |")
    print("|  ϰ  | Cursive H    | h    |  Ѯ  | Dragon     | dragon |")
    print("|  Ͽ  | Rev C w/ Dot | ccc  |  ★  | Black Star | black  |")
    print("|  Ӭ  | E w/ Two Dot | e    |  ҂  | Puzzle     | puz    |")
    print("|  ҩ  | Cursive Cir  | cir  |  ӕ  | a and e    | ae     |")
    print("|  ☆  | Star         | star |  Ҋ  | Rev Cap N  | n      |")
    print("|  ¿  | Inv QMark    | que  |  Ω  | Omega      | omg    |")
    print("|  ©  | Copyright    | cop  |  Ψ  | Cap I w/ U | iu     |")
    print("|  Ѽ  | Wobbly Grin  | grin |  ټ | Smile      | smi    |")
    print("|  Җ  | Reflected W  | w    |     |            |        |")
    print("")

    codes = raw_input("    -> ").lower()
    codes = codes.split()
    print("")

    newcodes = []
    newchars = []
    matches = 0
    codelist_index = 0
    char = 0
    for codelist in code_matrix:
        if is_verbose:
            print("")
            print(codelist)

        char = 0
        for charcode in codelist:
            if charcode in codes:
                newcodes.append(charcode)
                newchars.append(chars[charcode])
                matches += 1
                if is_verbose:
                    print("Char " + str(charcode) + " found in codelist!")
            char += 1

        if matches == 4:
            if is_verbose:
                print("MATCH FOUND!")
                print(newcodes)
                print(newchars)

            print("Choose the keys in the following order:")
            n = 1
            for code in newcodes:
                print("        " + str(n) + ". " + chars[code] + "    " + friendly_names[code] + "   (" + code + ")")
                n += 1
            print("")
            return 0
        else:
            newcodes = []
            newchars = []
        #print("Codelist index:" + str(codelist_index))
        codelist_index += 1
        matches = 0
    print("   ⚠ ERROR! Exit 2: Combination not found. Please double check your symbols and rerun.")
    print("")
