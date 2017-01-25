import string
def alphabet_position(letter):
    upperCase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if letter in upperCase:
        return ord(letter) - 65
    else:
        return ord(letter) - 97

def rotate_character(char, rot):
    if char.isalpha():
        let= alphabet_position(char)
    else:
        return char
    newval = let+rot
    conval = newval%26
    if char.isupper():
        return chr(conval + 65)
    else:
        return chr(conval + 97)

def encrypt(text,rot):

    encrypted=''
    for char in text:
        if char == '':
            encrypted = encrypted + ''
        else:
            encrypted = encrypted + rotate_character(char,rot)
    return encrypted
