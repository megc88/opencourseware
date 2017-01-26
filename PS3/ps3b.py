from ps3a import *
import time
from perm import *

HAND_SIZE = 7

#
#
# Problem #6A: Computer chooses a word
#
#
def comp_choose_word(hand, word_list):
    """
	Given a hand and a word_dict, find the word that gives the maximum value score, and return it.
   	This word should be calculated by considering all possible permutations of lengths 1 to HAND_SIZE.

    hand: dictionary (string -> int)
    word_list: list (string)
    """

    max_score = 0
    max_perm = None
    for n in range(len(hand)):
        for perm in get_perms(hand, n):
            if is_valid_word(perm, hand, word_list):
                perm_score = get_word_score(perm, HAND_SIZE)
                if perm_score > max_score:
                    max_score = perm_score
                    max_perm = perm
    return max_perm
    

#
# Problem #6B: Computer plays a hand
#
def comp_play_hand(hand, word_list):
    """
     Allows the computer to play the given hand, as follows:

     * The hand is displayed.

     * The computer chooses a word using comp_choose_word(hand, word_dict).

     * After every valid word: the score for that word is displayed, 
       the remaining letters in the hand are displayed, and the computer 
       chooses another word.

     * The sum of the word scores is displayed when the hand finishes.

     * The hand finishes when the computer has exhausted its possible choices (i.e. comp_play_hand returns None).

     hand: dictionary (string -> int)
     word_list: list (string)
    """
    # TO DO ...
    total_score = 0
    print "Computer's letters: "
    display_hand(hand)
    word = comp_choose_word(hand, word_list)
    while (word != None):
        print "The computer's play is: ", word
        print "That word earned: " + str(get_word_score(word, HAND_SIZE)) + " points!"
        print "Computer's letters: "
        hand = update_hand(hand, word)
        display_hand(hand)
        total_score = total_score + get_word_score(word, HAND_SIZE)
        word = comp_choose_word(hand, word_list)
    print "The computer's turn is done! Final score is ", total_score
    
    
#
# Problem #6C: Playing a game
#
#
def play_game(word_list):
    """Allow the user to play an arbitrary number of hands.

    1) Asks the user to input 'n' or 'r' or 'e'.
    * If the user inputs 'n', play a new (random) hand.
    * If the user inputs 'r', play the last hand again.
    * If the user inputs 'e', exit the game.
    * If the user inputs anything else, ask them again.

    2) Ask the user to input a 'u' or a 'c'.
    * If the user inputs 'u', let the user play the game as before using play_hand.
    * If the user inputs 'c', let the computer play the game using comp_play_hand (created above).
    * If the user inputs anything else, ask them again.

    3) After the computer or user has played the hand, repeat from step 1

    word_list: list (string)
    """
    hand = deal_hand(HAND_SIZE)

    print "Welcome to our word game!"
    while True: 
        user_choice = raw_input("If you'd like to play a new hand, type 'n'.\nIf you'd like to play the last hand again, type 'r'.\nIf you'd like to exit the game, type 'e'.\n")
        if user_choice == "r":
            while True:
                player_choice = raw_input("If you'd like to play, type 'u'. If you'd like your computer to play, type 'c'.")
                if player_choice == "u":
                    play_hand(hand, word_list)
                    break
                if player_choice == "c":
                    comp_play_hand(hand, word_list)
                    break
                print "Invalid choice, try again."
            #break
                                                                 
        if user_choice =="n":
            hand = deal_hand(HAND_SIZE)
            while True: 
                player_choice = raw_input("If you'd like to play, type 'u'. If you'd like your computer to play, type 'c'.")
                if player_choice == "u":
                    play_hand(hand, word_list)
                    break
                if player_choice == "c":
                    comp_play_hand(hand, word_list)
                    break
                print "Invalid choice, try again."
            #break
   
        if user_choice == "e":
            print "Ok. Hope to see you again soon!"
            break
        
word_list = load_words()
play_game(word_list)


    
