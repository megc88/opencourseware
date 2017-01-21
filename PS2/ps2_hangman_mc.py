# 6.00 Problem Set 3
# 
# Hangman
#


# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
import random
import string

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return wordlist

def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------
"""takes in user's guess as a string, the word as a string, the board as a list and returns the updated board considering the user's guess."""
def match_guess (guess, word, board):
    if guess in word:
        print "Nice guess!"
        for idx in range (0, len(word)):
            if word[idx] == guess:
                board[idx] = word[idx]
    else: 
        print "Wrong!"
    return board

"""takes in the user's guess as a string, the word as a string, and the current guess_count as an int and returns the new guess_count"""
def find_guess_count (guess, word, guess_count):
    if guess in word:
        return guess_count
    return guess_count - 1
            
""" takes in board as a list of booleans and prints a hangman board"""
def print_board (board):
    for i in board:
        if i == False:
            print "_ ",
        else:
            print i, 
    print "\n"

""" takes in user's guess as a string, checks to see if it's already been guessed. If not, the guess is added to the list in alpha order. Returns all previous guesses"""    
def previous_guesses (guess, guesses):
    for idx in range (len(guesses)):
        if guess == guesses[idx]:
            print "You already guessed that letter, silly"
            return 
        elif ord(guess) < ord(guesses[idx]):
            guesses.insert(idx,guess)
            return 
    guesses.append(guess)
    return 

"""takes in the users guess as a string, turns it to lowercase. Validates that guess is a single letter, and if so, returns the guess"""
def take_guess ():
    guess = raw_input("Please guess a letter: ")
    guess = guess.lower()
    if len(guess) != 1:
        print "I said A letter"
        return take_guess()
    if ord(guess) < ord("a") or ord(guess) > ord("z"):
        print "That's not as letter"
        return take_guess()
    return guess

def main ():
    word = choose_word(load_words())
    guess_count =5
    guesses = []

    print "Welcome to Hangman. I'm thinking of a word that has " + str(len(word)) + " letters. \n"

    board = []
    for i in range (len(word)):
        board.append(False)
    while (guess_count > 0) and (False in board) == True:
        print_board (board)
        guess = take_guess ()
        board = match_guess (guess, word, board)
        guess_count =  find_guess_count(guess, word, guess_count)
        print "Remaining guesses: " + str(guess_count) 
        previous_guesses (guess, guesses)
        print guesses
    if (False in board):
        print "You lose!"
    else:
        print "winner!"
    print str(word)
        
main ()
