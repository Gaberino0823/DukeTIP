from __future__ import print_function
import numpy
input = open("words_alpha.txt", 'r')
apples = input.read()
words = apples.split("\n")
# Save this file using file save in your browser
# Do not copy paste into PyCharm as it will mess up the indentation
# and thus your code will not run properly.


# Print Hangman's current state
def printHangman(numberWrong):
    # Print the hangman
    print('|----|')  # prints top of noose
    if numberWrong >= 1:
        print("|    0")  # prints head and next segment of noose
    else:
        print("|     ")  # just prints next segment of noose
    if numberWrong >= 2:
        print("|    |")  # prints neck and next segment of noose
    else:
        print("|     ")  # just prints next segment of noose
    if numberWrong >= 3:
        print("|   /|\\")  # prints next body segment
    else:
        print("|     ")  # just prints next segment of noose
    if numberWrong >= 4:
        print("|    |")  # prints last body segment and a noose segment
    else:
        print("|     ")  # just prints next segment of noose
    if numberWrong == 5:  # can't be > here so we get to the else :)
        print("|   /")  # prints left leg and noose segment
    elif numberWrong >= 6:
        print("|   / \\")  # prints both legs and noose segment
    else:
        print("|     ")  # just prints noose segment
    print("|-----|")  # prints last noose segment


def printBlanks(word, correctLetters):
    solved = True
    for l in word:
        l = l.lower()  # not required but nice to have
        # Check if that letter is in the list of correct letters
        if l in correctLetters:
            print(l + " ", end ='')
        else:
            print("_ ", end = ' ')
            solved = False
    print()
    print()
    return solved

# list of words the program is choosing from for game
# words = ["potato", "sandwich", "zealot", "xenophileA"]

# list of correct letters
correctLetters = []
# counts the number of wrong words
numberWrong = 0

# how program is randomly choosing word
rand_word = numpy.random.choice(words)

while True:

    printHangman(numberWrong)

    solved = printBlanks(rand_word, correctLetters)
    
    if numberWrong >= 6:
        print('You lose.') #if user guesses wrong 6 times the game ends
        break

    if solved:
        print('You win!')
        break  # no need to guess again
        
    user = raw_input("Guess a letter: ")  # where the player will guess
    
    # Check if the letter is in the word
    if user in rand_word:
        print("That letter was correct")
        correctLetters.append(user)  # adds the user input letter to the list of correct letters
    else:
        print("That letter was incorrect")
        numberWrong += 1 # adds to the counter of your mistakes

    print()

print(rand_word) # prints the word if you get it wrong