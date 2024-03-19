# Name: Andre Sealy
# Email: andre.sealy72@myhunter.cuny.edu
# Date: February 16th, 2024
# This program encodes a string using a caesar cipher

import string

alphabet = string.ascii_lowercase                   # imports the lowercase alphabet

codeWord = input('Enter a word: ')

encoded = ""

for char in codeWord:
    idx = (ord(char) - ord('a')) - 13

    encoded = encoded + alphabet[idx]

print(encoded)
