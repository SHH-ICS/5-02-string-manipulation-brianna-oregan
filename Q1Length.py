# Create a program that will accept a word from a user and return the length of that word. 
# Make this program in a loop with option to exit when the use types in quit.

#start loop
while True:
    #gets word from user
    word = input("Enter a word: ")

    #if user wants to quit   
    if word.lower() == "quit":
        print("Goodbye")
        break 

    #prints length of the word
    print("The input " + '"' + word + '"', "is", len(word), "characters long.")