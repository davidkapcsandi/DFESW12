from ctypes.wintypes import WORD
from importlib.abc import Finder


def reverseword(inword):
    lenword = len(inword)-1
    revwird = ""
    for letter in range(lenword,-1,-1):
        revword = revword + inword[letter]
    return revword
# ~Palumdrome Finder
# User types in a WORD
# I find out if it is a palindrom

userinputvar = input("Type a word")
capturedword = reverseword(userinputvar)

if userinputvar == capturedword:
    print(f"{userinputvar}is not a pallindrome")
else:
    print(f"{userinputvar}is a pallindrome")