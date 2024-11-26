# Create a program that will prompt the user for a word, and return a 'word triangle'. For example, if the user types in the word "PYTHON", your program will output:
# P
# PY
# PYT
# PYTH
# PYTHO
# PYTHON

word = input("Enter a word: ")
current = ""

for char in word:
    current += char #adds 1 character to current at a time
    print(current)