def encrypt(text, rot):
    eMessage = ""
    for i in text:
        eMessage += rotate_character(i, rot)
    return eMessage

def rotate_character(char, rot):
    alphaUp = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    alphaDown = "abcdefghijklmnopqrstuvwxyz"
    newChar = ''
    if char.isalpha() == False:
        return char
    elif char in alphaUp:
        newChar += alphaUp[(alphaUp.index(char) + rot) % 26]
        return newChar
    else:
        newChar += alphaDown[(alphaDown.index(char) + rot) % 26]
        return newChar

def alphabet_position(letter):
    letter = letter.lower()
    alphaPos = string.ascii_lowercase.index(letter)
    return alphaPos
