import os


# a clear screen command invoker
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def chartype(char):
    if char.isalpha(): return 'isAlpha'
    elif char.isnumeric(): return 'isNumeric'
    else: return 'isNon'


def aggregate(string):
    subCharSet, charSet = [], []
    for i in range(0, len(string)):
        if len(subCharSet) == 0:
            subCharSet.append(string[i])
        elif chartype(string[i]) == chartype(subCharSet[-1]):
            subCharSet.append(string[i])
        elif chartype(string[i]) != chartype(subCharSet[-1]):
            charSet.append(subCharSet.copy())
            del subCharSet[:]
            subCharSet.append(string[i])
        if i == (len(string) - 1):
            charSet.append(subCharSet.copy())
    return charSet


def shiftAlpha(alpha, shiftNum):
    for index in range(0, len(alpha)):
        i = alpha[index]
        if ord(i) + shiftNum > ord('Z'):
            alpha[index] = chr(ord(i) + shiftNum - ord('Z') + ord('A') - 1)
        else:
            alpha[index] = chr(ord(i) + shiftNum)
    return ''.join(alpha)


def complement(num):
    numeric = ''.join(num)
    nines = len(numeric) * '9'
    return str(int(nines) - int(numeric))


def manipulate(strAgr):
    for grp in strAgr:
        i = strAgr.index(grp)
        if (grp[0]).isalpha():
            grpShifted = shiftAlpha(grp, shift)
            strAgr[i] = grpShifted
        elif grp[0].isnumeric():
            grpComplement = complement(grp)
            strAgr[i] = grpComplement
        else: 
            strAgr[i] = ''.join(strAgr[i])

    return ''.join(strAgr)


clear()
print('Welcome to Passphrase Strengthener!\n')
string, shift = input('Input a passphrase: \n'), 1

strAgr = list(manipulate(aggregate(string)))
for i in range(0, len(strAgr)):
    if i % 2 != 0: strAgr[i] = strAgr[i].lower()
strAgr = (''.join(strAgr))[::-1]

clear()
print('Here is your strengthened passphrase:\n')
print(strAgr)