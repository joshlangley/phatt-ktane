

color = ""
def is_color(test):
    global color
    if color == "":
        color = raw_input("What color is it? -> ").lower()

    if color == test:
        return True
    else:
        return False

if is_color("blue") and True:
    print("Yes")
elif True and is_color("red"):
    print("No")
else:
    print("Ha!")
