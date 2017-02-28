# 6.00 Problem Set 4
#
# Caesar Cipher Skeleton
#
import string
import random

WORDLIST_FILENAME = "words.txt"

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
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
    wordlist = line.split()
    print "  ", len(wordlist), "words loaded."
    return wordlist

wordlist = load_words()

def is_word(wordlist, word):
    """
    Determines if word is a valid word.

    wordlist: list of words in the dictionary.
    word: a possible word.
    returns True if word is in wordlist.

    Example:
    >>> is_word(wordlist, 'bat') returns
    True
    >>> is_word(wordlist, 'asdf') returns
    False
    """
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
    return word in wordlist

def random_word(wordlist):
    """
    Returns a random word.

    wordlist: list of words  
    returns: a word from wordlist at random
    """
    return random.choice(wordlist)

def random_string(wordlist, n):
    """
    Returns a string containing n random words from wordlist

    wordlist: list of words
    returns: a string of random words separated by spaces.
    """
    return " ".join([random_word(wordlist) for _ in range(n)])

def random_scrambled(wordlist, n):
    """
    Generates a test string by generating an n-word random string
    and encrypting it with a sequence of random shifts.

    wordlist: list of words
    n: number of random words to generate and scamble
    returns: a scrambled string of n random words


    NOTE:
    This function will ONLY work once you have completed your
    implementation of apply_shifts!
    """
    s = random_string(wordlist, n) + " "
    shifts = [(i, random.randint(0, 26)) for i in range(len(s)) if s[i-1] == ' ']
    return apply_shifts(s, shifts)[:-1]

def get_fable_string():
    """
    Returns a fable in encrypted text.
    """
    f = open("fable.txt", "r")
    fable = str(f.read())
    f.close()
    return fable


# (end of helper code)
# -----------------------------------

#
# Problem 1: Encryption
#
def build_coder(shift):
    """
    Returns a dict that can apply a Caesar cipher to a letter.
    The cipher is defined by the shift value. Ignores non-letter characters
    like punctuation and numbers.

    shift: -27 < int < 27
    returns: dict

    Example:
    >>> build_coder(3)
    {' ': 'c', 'A': 'D', 'C': 'F', 'B': 'E', 'E': 'H', 'D': 'G', 'G': 'J',
    'F': 'I', 'I': 'L', 'H': 'K', 'K': 'N', 'J': 'M', 'M': 'P', 'L': 'O',
    'O': 'R', 'N': 'Q', 'Q': 'T', 'P': 'S', 'S': 'V', 'R': 'U', 'U': 'X',
    'T': 'W', 'W': 'Z', 'V': 'Y', 'Y': 'A', 'X': ' ', 'Z': 'B', 'a': 'd',
    'c': 'f', 'b': 'e', 'e': 'h', 'd': 'g', 'g': 'j', 'f': 'i', 'i': 'l',
    'h': 'k', 'k': 'n', 'j': 'm', 'm': 'p', 'l': 'o', 'o': 'r', 'n': 'q',
    'q': 't', 'p': 's', 's': 'v', 'r': 'u', 'u': 'x', 't': 'w', 'w': 'z',
    'v': 'y', 'y': 'a', 'x': ' ', 'z': 'b'}
    (The order of the key-value pairs may be different.)
    """
    assert -27 < shift < 27
    import string
    alphabet = string.ascii_lowercase + ' '
    cypher_dict = {}
    ##assign key value pairs as each lowercase letter in the alphabet and a space
    ## as keys and the letter that results from acting on the key with the shift integer
    ## as the value
    for letter in alphabet:
        key_index = alphabet.index(letter)
        value_index = (key_index + shift) % len(alphabet)
        cypher_dict[letter] = alphabet[value_index]
    #end for
    ##assigns key value paris as each uppercase letter in the alphabet as keys
    ##and the letter that results from acting on the key with the shift integer
    ## as the value
    for letter in alphabet[:-1]:
        key_index = alphabet.index(letter)
        value_index = (key_index + shift) % len(alphabet)
        cypher_dict[letter.upper()] = alphabet.upper()[value_index]
    #end for
    return cypher_dict
    
  

def build_encoder(shift):
    """
    Returns a dict that can be used to encode a plain text. For example, you
    could encrypt the plain text by calling the following commands
    >>>encoder = build_encoder(shift)
    >>>encrypted_text = apply_coder(plain_text, encoder)
    
    The cipher is defined by the shift value. Ignores non-letter characters
    like punctuation and numbers.

    shift: 0 <= int < 27
    returns: dict

    Example:
    >>> build_encoder(3)
    {' ': 'c', 'A': 'D', 'C': 'F', 'B': 'E', 'E': 'H', 'D': 'G', 'G': 'J',
    'F': 'I', 'I': 'L', 'H': 'K', 'K': 'N', 'J': 'M', 'M': 'P', 'L': 'O',
    'O': 'R', 'N': 'Q', 'Q': 'T', 'P': 'S', 'S': 'V', 'R': 'U', 'U': 'X',
    'T': 'W', 'W': 'Z', 'V': 'Y', 'Y': 'A', 'X': ' ', 'Z': 'B', 'a': 'd',
    'c': 'f', 'b': 'e', 'e': 'h', 'd': 'g', 'g': 'j', 'f': 'i', 'i': 'l',
    'h': 'k', 'k': 'n', 'j': 'm', 'm': 'p', 'l': 'o', 'o': 'r', 'n': 'q',
    'q': 't', 'p': 's', 's': 'v', 'r': 'u', 'u': 'x', 't': 'w', 'w': 'z',
    'v': 'y', 'y': 'a', 'x': ' ', 'z': 'b'}
    (The order of the key-value pairs may be different.)

    HINT : Use build_coder.
    """
    assert 0 <= shift < 27
    return build_coder(shift)

def build_decoder(shift):
    """
    Returns a dict that can be used to decode an encrypted text. For example, you
    could decrypt an encrypted text by calling the following commands
    >>>encoder = build_encoder(shift)
    >>>encrypted_text = apply_coder(plain_text, encoder)
    >>>decrypted_text = apply_coder(plain_text, decoder)
    
    The cipher is defined by the shift value. Ignores non-letter characters
    like punctuation and numbers.

    shift: 0 <= int < 27
    returns: dict

    Example:
    >>> build_decoder(3)
    {' ': 'x', 'A': 'Y', 'C': ' ', 'B': 'Z', 'E': 'B', 'D': 'A', 'G': 'D',
    'F': 'C', 'I': 'F', 'H': 'E', 'K': 'H', 'J': 'G', 'M': 'J', 'L': 'I',
    'O': 'L', 'N': 'K', 'Q': 'N', 'P': 'M', 'S': 'P', 'R': 'O', 'U': 'R',
    'T': 'Q', 'W': 'T', 'V': 'S', 'Y': 'V', 'X': 'U', 'Z': 'W', 'a': 'y',
    'c': ' ', 'b': 'z', 'e': 'b', 'd': 'a', 'g': 'd', 'f': 'c', 'i': 'f',
    'h': 'e', 'k': 'h', 'j': 'g', 'm': 'j', 'l': 'i', 'o': 'l', 'n': 'k',
    'q': 'n', 'p': 'm', 's': 'p', 'r': 'o', 'u': 'r', 't': 'q', 'w': 't',
    'v': 's', 'y': 'v', 'x': 'u', 'z': 'w'}
    (The order of the key-value pairs may be different.)

    HINT : Use build_coder.
    """
    assert 0 <= shift < 27
    encoder = build_encoder(shift)
    decoder = {}
    ## build a decoding dictionary by switching the key/value pairs of an encoded dictionary
    for key in encoder.keys():
        decoder[encoder.get(key)] = key
    return decoder
    
 

def apply_coder(text, coder):
    """
    Applies the coder to the text. Returns the encoded text.

    text: string
    coder: dict with mappings of characters to shifted characters
    returns: text after mapping coder chars to original text

    Example:
    >>> apply_coder("Hello, world!", build_encoder(3))
    'Khoor,czruog!'
    >>> apply_coder("Khoor,czruog!", build_decoder(3))
    'Hello, world!'
    """
    cypher_text = ""
    ## check to see if the character in the text string is in the coder dictionary,
    ## if not, add to cypher_text as is, if so, add the value found at that key
    ## in the dictionary to the cypher_text
    for char in text:
        if char not in coder.keys():
            cypher_text += char
        else:
            cypher_text += coder[char]
    return cypher_text
    
        
  

def apply_shift(text, shift):
    """
    Given a text, returns a new text Caesar shifted by the given shift
    offset. The empty space counts as the 27th letter of the alphabet,
    so spaces should be replaced by a lowercase letter as appropriate.
    Otherwise, lower case letters should remain lower case, upper case
    letters should remain upper case, and all other punctuation should
    stay as it is.
    
    text: string to apply the shift to
    shift: amount to shift the text
    returns: text after being shifted by specified amount.

    Example:
    >>> apply_shift('This is a test.', 8)
    'Apq hq hiham a.'
    """
    ## build a dictionary using the given shift amount and use it to return the
    ## given text string shifted by the shift amount
    return apply_coder(text, build_coder(shift))
   
#
# Problem 2: Codebreaking.
#
def find_best_shift(wordlist, text):
    """
    Decrypts the encoded text and returns the plaintext.

    text: string
    returns: 0 <= int 27

    Example:
    >>> s = apply_coder('Hello, world!', build_encoder(8))
    >>> s
    'Pmttw,hdwztl!'
    >>> find_best_shift(wordlist, s) returns
    8
    >>> apply_coder(s, build_decoder(8)) returns
    'Hello, world!'
    """
    shift = 0
    valid_words = 0
    ##apply a shift value to the given text and check it see if the result contains
    ## all valid words, if not, check a new shift, if so, return the string decoded
    ## by that shift
    while shift < 27:
        decoded_text = apply_coder(text, build_decoder(shift))
        for word in decoded_text.split():
            if is_word(wordlist, word):
                valid_words += 1
            #end if
        #end for
        if valid_words == len(decoded_text.split()):
            break
        #end if
        shift +=1
        valid_words = 0
    #end while
    return decoded_text
 
    
   
#
# Problem 3: Multi-level encryption.
#
def apply_shifts(text, shifts):
    """
    Applies a sequence of shifts to an input text.

    text: A string to apply the Ceasar shifts to 
    shifts: A list of tuples containing the location each shift should
    begin and the shift offset. Each tuple is of the form (location,
    shift) The shifts are layered: each one is applied from its
    starting position all the way through the end of the string.  
    returns: text after applying the shifts to the appropriate
    positions

    Example:
    >>> apply_shifts("Do Androids Dream of Electric Sheep?", [(0,6), (3, 18), (12, 16)])
    'JufYkaolfapxQdrnzmasmRyrpfdvpmEurrb?'
    """
    
    decoded_text = text[:]
    for i, (a, b) in enumerate(shifts):
        decoded_text = decoded_text[:a] + apply_coder(decoded_text[a:], build_decoder(b))
    return decoded_text
   
   ## fix this so it goes both ways            
 
#
# Problem 4: Multi-level decryption.
#


def find_best_shifts(wordlist, text):
    """
    Given a scrambled string, returns a shift key that will decode the text to
    words in wordlist, or None if there is no such key.

    Hint: Make use of the recursive function
    find_best_shifts_rec(wordlist, text, start)

    wordlist: list of words
    text: scambled text to try to find the words for
    returns: list of tuples.  each tuple is (position in text, amount of shift)
    
    Examples:
    >>> s = random_scrambled(wordlist, 3)
    >>> s
    'eqorqukvqtbmultiform wyy ion'
    >>> shifts = find_best_shifts(wordlist, s)
    >>> shifts
    [(0, 25), (11, 2), (21, 5)]
    >>> apply_shifts(s, shifts)
    'compositor multiform accents'
    >>> s = apply_shifts("Do Androids Dream of Electric Sheep?", [(0,6), (3, 18), (12, 16)])
    >>> s
    'JufYkaolfapxQdrnzmasmRyrpfdvpmEurrb?'
    >>> shifts = find_best_shifts(wordlist, s)
    >>> print apply_shifts(s, shifts)
    Do Androids Dream of Electric Sheep?
    given a list of strings where the strings are valid words, and a string of characters that resulted from set of words
    being acted on by a multilevel Ceasear Cypher.
    Return a list of tuples where the first item in each tuple is the starting position and the second item is
    the shift amount. Such that when the input string is shifted from the starting position to the end of the string
    for each tuple, the result is a string of valid words where each word is contained in the word list
    """
    return find_best_shifts_rec(wordlist, text, 0)
        
        
def find_best_shifts_rec(wordlist, text, start):
    """
    Given a scrambled string and a starting position from which
    to decode, returns a shift key that will decode the text to
    words in wordlist, or None if there is no such key.

    Hint: You will find this function much easier to implement
    if you use recursion.

    wordlist: list of words
    text: scambled text to try to find the words for
    start: where to start looking at shifts
    returns: list of tuples.  each tuple is (position in text, amount of shift)
    """
    #apply a shift amount to the string until you get to a space and then check to see if the word prior to the shift is a valid word,
    ## if so, apply that shift to the rest of the string and record the shift amount and starting position. Start your check again at the next
    ## index after the space, and restarting your shift at 0
    ##if you find a space but the word prior isn't valid, increase shift by one and restart the for loop
    ## if no spaces and valid words are produced with the existing shift, increase shift by 1 and try again.
    ## alwasy check whether the last word of the string is a valid word to ensure all words all shifts are included
    shift = 0
    while 0<=shift<27:
        decoded_text = text[:start] + apply_coder(text[start:], build_decoder(shift))
        #check to see if the last word is valid after being acted on by the shift
        if is_word(wordlist, decoded_text[start:]) and shift > 0:
            return [(start, shift),]
        #end if
        #check to see if the last word is valid, if the shift was just 0, no need to return final start, shift tuple
        if is_word(wordlist, decoded_text[start:]) and shift == 0:
            return
        #end if
        for index in range(start, len(decoded_text)):
            #iterate over the decoded text, when you find a space, check to see if word prior is valid, if so, pass the shift value used to decode
            #and where you started decode from
            #recurse over the string starting at the next index and restarting your shift value
            if decoded_text[index]== ' ' and is_word(wordlist, decoded_text[start:index]):
                return [(start, shift),] +  (find_best_shifts_rec(wordlist, decoded_text, index+1))
            #end if
            #if you find a space and that the word prior isn't valid, you know that shift doesn't work, so try the next shift
            if decoded_text[index]== ' ' and not is_word(wordlist, decoded_text[start:index]):
                break
            #end if
        #end for
        shift +=1
    #end while
    #if you've gone through all of your shifts and you don't find any spaces and your last word isn't valid, return an empty list
    return []
    
def decrypt_fable(wordlist):
    """
    Using the methods you created in this problem set,
    decrypt the fable given by the function get_fable_string().
    Once you decrypt the message, be sure to include as a comment
    at the end of this problem set how the fable relates to your
    education at MIT.

    returns: string - fable in plain text
    """
    fable = get_fable_string()
    multi_factor_cypher = find_best_shifts(wordlist, fable)
    print multi_factor_cypher
    return apply_shifts(fable, multi_factor_cypher)



    
#What is the moral of the story?
#
#
#
#
#

def test(wordlist):
    s = random_scrambled(wordlist, 15)
    print s, "random words"
    shifts=find_best_shifts(wordlist, s)
    print shifts, "shifts"
    print apply_shifts(s, shifts), "decoded word"
