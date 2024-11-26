# Create a program that will accept a word and output the word one letter at a time in reverse.
#get user input for the word
word = input("Enter a word: ")

# initialize empty strign to build the triangle
current = ""

#build the word triangle
for char in word:
    current += char #adds 1 character to current at a time
    print(current)