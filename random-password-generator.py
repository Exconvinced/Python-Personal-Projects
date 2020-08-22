import getch
from os import system, name
import random


# initialize lists. allows functions to modify values so that the printMenu always receives updates
charaBase, passBase, wholeCharaGroup, password, passLength = [], [], [""], [""], [20]


# active toggles fetch character groups from here
charaGroups = [
    "abcdefghijklmnopqrstuvwxyz",           # lowercase
    "ABCDEFGHIJKLMNOPQRSTUVWXYZ",           # uppercase
    "0123456789",                           # digits
    r"!\"#$%&'()*+,-./:;<=>?@[]^_`{|}~",    # punctuations
]


# toggle status in [] on the menu screen
toggles = ["0", "1", "2", "3"]


# the submenu located at the footer of the main menu
footerControls = ["\r[Enter] Generate", "\r[Esc] Exit program"]


# the main and only menu. has intuitive controls and dynamic output
def printmenu():
    checkToggles()
    print(
        "\n",
        "\nWelcome to Random Password Generator!\n",
        "\n",
        "\rToggle any options below to specify your password preference:\n",
        "\n",
        "[" + toggles[0] + "] Lowercase Letters\n",
        "[" + toggles[1] + "] Uppercase Letters\n",
        "[" + toggles[2] + "] Digits\n",
        "[" + toggles[3] + "] Punctuations\n",
        "\n",
        "Password Length:",
        passLength[0],
        "\n",
        "[+] Increase password length\n [-] Decrease password length\n",
        "\n",
        " >",
        password[0],
        "\n",
        "\n",
        "\r--------------------------------------------------------------------\n",
        footerControls[0],
        "\n",
        footerControls[1],
        "\n",
        "\n",
    )


# hides and disables [Enter] key and password display when no toggle is active
def checkToggles():
    if "■" in toggles:
        footerControls[0] = "\r[Enter] Generate"
        processCharaGroup()
    else:
        footerControls[0] = ""
        password[0] = ""


# selects random index n times from the whole character string, where n is the specified password length
def generatePass():
    del passBase[:]
    del password[:]
    for _ in range(0, passLength[0]):
        randChar = random.randint(0, len(wholeCharaGroup[0]) - 1)
        passBase.append(wholeCharaGroup[0][randChar])
    password.append("".join(passBase))


# concatenate the elements of the character base to form a single string of all active character groups
def processCharaGroup():
    del wholeCharaGroup[:]
    wholeCharaGroup.append(str("".join(charaBase)))
    generatePass()


# add a character group to the character base
def addCharGroup(input):
    charaBase.append(charaGroups[input])


# remove a character group to the character base
def remCharGroup(input):
    groupIndex = charaBase.index(charaGroups[input])
    print(groupIndex)
    del charaBase[groupIndex]


# parent function. reads the input and calls the intended functions
def checkInput():
    # if [Esc] is pressed, return to the main program flow to exit
    if input == 27:
        clear()
        print("Thank you for using this program!")
        return True
    # toggle on a setting if toggled off
    elif str(input - 48) in toggles:
        toggles[input - 48] = "■"
        addCharGroup(input - 48)
    # toggle off a setting if toggled on
    elif input in range(48, 52):
        toggles[input - 48] = str(input - 48)
        remCharGroup(input - 48)
    # increase password length, generates password at every increment
    elif input == 43:
        passLength[0] += 1
        checkToggles()
    # decrease password length, generates password at every increment
    elif input == 45:
        if passLength[0] != 1:
            passLength[0] -= 1
            checkToggles()
    # if [Enter] is pressed, generate password based on the current settings
    if input == 13:
        checkToggles()


# a clear screen command invoker
def clear():
    if name == "nt":
        _ = system("cls")
    else:
        _ = system("clear")


# main program flow
while True:
    clear()
    printmenu()
    input = ord(getch.getch())
    inputStatus = checkInput()
    if inputStatus:
        break
    checkToggles()
