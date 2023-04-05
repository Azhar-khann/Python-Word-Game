# 6.0001 Problem Set 3
#
# The 6.0001 Word Game
# Created by: Kevin Luu <luuk> and Jenna Wiens <jwiens>
#
# Name          : <your name>
# Collaborators : <your collaborators>
# Time spent    : <total time>

import math
import random
import string

VOWELS = 'aeiou*'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.append(line.strip().lower())
    #print("  ", len(wordlist), "words loaded.")
    return wordlist

def get_frequency_dict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.

    sequence: string or list
    return: dictionary
    """
    
    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x,0) + 1
    return freq
	

# (end of helper code)
# -----------------------------------

#
# Problem #1: Scoring a word
#
def get_word_score(word, n):
    """
    Returns the score for a word. Assumes the word is a
    valid word.

    You may assume that the input word is always either a string of letters, 
    or the empty string "". You may not assume that the string will only contain 
    lowercase letters, so you will have to handle uppercase and mixed case strings 
    appropriately. 

	The score for a word is the product of two components:

	The first component is the sum of the points for letters in the word.
	The second component is the larger of:
            1, or
            7*wordlen - 3*(n-wordlen), where wordlen is the length of the word
            and n is the hand length when the word was played

	Letters are scored as in Scrabble; A is worth 1, B is
	worth 3, C is worth 3, D is worth 2, E is worth 1, and so on.

    word: string
    n: int >= 0
    returns: int >= 0
    """

    SCRABBLE_LETTER_VALUES = {
        'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
    }
    first_component = 0
    total_score = 0
    keys = SCRABBLE_LETTER_VALUES.keys()

    
    for i in word.lower():
        if i in SCRABBLE_LETTER_VALUES.keys():
            first_component = first_component + SCRABBLE_LETTER_VALUES[i]
            second_component = 7*len(word) - 3*(n-len(word))
            total_score = abs(first_component * second_component)
    
    return total_score


#print(get_word_score('weed',6))






#
# Make sure you understand how this function works and what it does!
#
def display_hand(hand):
    """
    Displays the letters currently in the hand.

    For example:
       display_hand({'a':1, 'x':2, 'l':3, 'e':1})
    Should print out something like:
       a x x l l l e
    The order of the letters is unimportant.

    hand: dictionary (string -> int)
    """
    word =''
    for letter in hand.keys():
        for j in range(hand[letter]):
            #print(letter, end='')     # print all on the same line
            word += letter
    return(word)
    print()                              # print an empty line

#
# Make sure you understand how this function works and what it does!
# You will need to modify this for Problem #4.
#
def deal_hand(n):
    """
    Returns a random hand containing n lowercase letters.
    ceil(n/3) letters in the hand should be VOWELS (note,
    ceil(n/3) means the smallest integer not less than n/3).

    Hands are represented as dictionaries. The keys are
    letters and the values are the number of times the
    particular letter is repeated in that hand.

    n: int >= 0
    returns: dictionary (string -> int)
    """
    
    hand={}
    num_vowels = int(math.ceil(n / 3)) #modified by me
    #print(num_vowels)
    wildcard = '*' # modified by me for problem 4
    hand[wildcard] = 1 # modified by me for problem 4

    for i in range(num_vowels-1):  #modified by me for problem 4
        x = random.choice(VOWELS)
        #print(x)
        if x == wildcard:
            x = random.choice('aeiou')
        hand[x] = hand.get(x, 0) + 1

    
    for i in range(num_vowels, n):    
        x = random.choice(CONSONANTS)
        hand[x] = hand.get(x, 0) + 1
    
    return hand

#print(deal_hand(15))
#
# Problem #2: Update a hand by removing letters
#
def update_hand(hand, word):
    """
    Does NOT assume that hand contains every letter in word at least as
    many times as the letter appears in word. Letters in word that don't
    appear in hand should be ignored. Letters that appear in word more times
    than in hand should never result in a negative count; instead, set the
    count in the returned hand to 0 (or remove the letter from the
    dictionary, depending on how your code is structured). 

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not modify hand.

    word: string
    hand: dictionary (string -> int)    
    returns: dictionary (string -> int)
    """

    copy_hand = hand.copy()
    for i in word.lower():
        if i in copy_hand.keys():
            copy_hand[i] -= 1
            if copy_hand[i] == 0:
                del(copy_hand[i])

    return copy_hand

hand = {'a':1, 'q':1, 'l':2, 'm':1, 'u':1, 'i':1} 
#print(update_hand(hand,'quail'))
#
# Problem #3: Test word validity
#
def is_valid_word(word, hand, word_list):
    """
    Returns True if word is in the word_list and is entirely
    composed of letters in the hand. Otherwise, returns False.
    Does not mutate hand or word_list.
   
    word: string
    hand: dictionary (string -> int)
    word_list: list of lowercase strings
    returns: boolean
    """

    copy_hand = hand.copy() #makes a copy of hand so that hand is not mutated

    for i in word.lower():  # checks for if every letter in word is in copyhand and removes words that are used
        if i not in copy_hand:
            return False
        if i in copy_hand:
            copy_hand = update_hand(copy_hand,i)
                

    if  word.find('*') == -1 and word.lower() in word_list: # if * is not found in word and word is in wordlist return true
        #print('1')
        return True

    if word.find('*') == -1 and word.lower() not in word_list:
        #print('2')
        return False
   
    if word.find('*') != -1: # Replaces * with vowels and checks if it becomes a valid word or not
        for i in 'aeiou':
            #print(i)
            replace_word = word.replace('*',i)
            if replace_word in word_list:
                return True
        
    return False
    
        




#hand = {'c': 3, 'o': 1, 'w': 2, 's': 1, '*': 1, 'z': 1}
#print(is_valid_word(word,hand,load_words()))

    

#
# Problem #5: Playing a hand
#
def calculate_handlen(hand):
    """ 
    Returns the length (number of letters) in the current hand.
    
    hand: dictionary (string-> int)
    returns: integer
    """

    hand_keys_list = list(display_hand(hand))
    return(len(hand_keys_list))


#hand = {'c': 3, 'o': 1, 'w': 2, 's': 1, '*': 1, 'z': 1}
#print(calculate_handlen(hand))

def play_hand(hand,word_list):

    """
    Allows the user to play the given hand, as follows:

    * The hand is displayed.
    
    * The user may input a word.

    * When any word is entered (valid or invalid), it uses up letters
      from the hand.

    * An invalid word is rejected, and a message is displayed asking
      the user to choose another word.

    * After every valid word: the score for that word is displayed,
      the remaining letters in the hand are displayed, and the user
      is asked to input another word.

    * The sum of the word scores is displayed when the hand finishes.

    * The hand finishes when there are no more unused letters.
      The user can also finish playing the hand by inputing two 
      exclamation points (the string '!!') instead of a word.

      hand: dictionary (string -> int)
      word_list: list of lowercase strings
      returns: the total score for the hand
      
    """
    
    # BEGIN PSEUDOCODE <-- Remove this comment when you implement this function
    # Keep track of the total score
    
    # As long as there are still letters left in the hand:
    
        # Display the hand
        
        # Ask user for input
        
        # If the input is two exclamation points:
        
            # End the game (break out of the loop)

            
        # Otherwise (the input is not two exclamation points):

            # If the word is valid:

                # Tell the user how many points the word earned,
                # and the updated total score

            # Otherwise (the word is not valid):
                # Reject invalid word (print a message)
                
            # update the user's hand by removing the letters of their inputted word
            

    # Game is over (user entered '!!' or ran out of letters),
    # so tell user the total score

    # Return the total score as result of function

    total_score = 0

    while len(hand.keys()) != 0:
        print()
        print('Current hand:', display_hand(hand))
        user_input = input('Enter word, or "!!" to indicate that you are finished:')



        if user_input == '!!':
            #return('Total score for this hand:' + ' ' + str(total_score))
            print( 'Total score for this hand: ',end='') 
            return(total_score)
            
    

        if is_valid_word(user_input,hand,word_list) == True:
            score = get_word_score(user_input,calculate_handlen(hand))
            total_score = total_score + score
            print(user_input + ' ' + 'earned'+ ' ' + str(score)+ ' '+ 'points.'+ ' ' + 'Total:'+ ' '+ str(total_score) )
            print('')

        if is_valid_word(user_input,hand,word_list) == False:
            print('The word is invalid. You have gained no points, try again')
            print('')

        if calculate_handlen(hand) == 0:
            print('')
            return('You used all the letters. Your Total score is:',+ total_score)
        
        hand = update_hand(hand,user_input)
    

    #return('Ran out of letters. Total score for this hand:' + ' ' + str(total_score))
    print('Ran out of letters. Total score for this hand: ',end='')
    return(total_score)
        
    
#hand = {'d':2,'a':1,'*':1,'o':1,'u':1,'t':1}
#hand = deal_hand(12)
#print(play_hand(hand,load_words()))

#
# Problem #6: Playing a game
# 


#
# procedure you will use to substitute a letter in a hand
#

def substitute_hand(hand, letter):
    """ 
    Allow the user to replace all copies of one letter in the hand (chosen by user)
    with a new letter chosen from the VOWELS and CONSONANTS at random. The new letter
    should be different from user's choice, and should not be any of the letters
    already in the hand.

    If user provide a letter not in the hand, the hand should be the same.

    Has no side effects: does not mutate hand.

    For example:
        substitute_hand({'h':1, 'e':1, 'l':2, 'o':1}, 'l')
    might return:
        {'h':1, 'e':1, 'o':1, 'x':2} -> if the new letter is 'x'
    The new letter should not be 'h', 'e', 'l', or 'o' since those letters were
    already in the hand.
    
    hand: dictionary (string -> int)
    letter: string
    returns: dictionary (string -> int)
    """
    replace_hand = {}
    hand_keys = display_hand(hand)
    key_list = []
    replacer = random.choice('aeiou*bcdfghjklmnpqrstvwxyz')
    done = False

    for i in hand_keys:
        if i in VOWELS or i in CONSONANTS:
            key_list.append(i)
    
    while not done:
        if replacer in hand_keys:
            replacer = random.choice('aeiou*bcdfghjklmnpqrstvwxyz')
        else:
            done = True
        
    for i in range(len(key_list)):
        if key_list[i] == letter:
            key_list[i] = replacer

    for i in key_list:
        if i in replace_hand.keys():
            replace_hand[i] += 1

        else:
            replace_hand[i] = 1
        
    return(replace_hand)




hand = {'h':1,'e':1,'l':2,'o':1}
#print(substitute_hand(hand,'l'))
       
    
def play_game(word_list):
    """
    Allow the user to play a series of hands

    * Asks the user to input a total number of hands

    * Accumulates the score for each hand into a total score for the 
      entire series
 
    * For each hand, before playing, ask the user if they want to substitute
      one letter for another. If the user inputs 'yes', prompt them for their
      desired letter. This can only be done once during the game. Once the
      substitue option is used, the user should not be asked if they want to
      substitute letters in the future.

    * For each hand, ask the user if they would like to replay the hand.
      If the user inputs 'yes', they will replay the hand and keep 
      the better of the two scores for that hand.  This can only be done once 
      during the game. Once the replay option is used, the user should not
      be asked if they want to replay future hands. Replaying the hand does
      not count as one of the total number of hands the user initially
      wanted to play.

            * Note: if you replay a hand, you do not get the option to substitute
                    a letter - you must play whatever hand you just had.
      
    * Returns the total score for the series of hands

    word_list: list of lowercase strings
    """
    
    num_hands = input('Enter total number of hands:')
    total_hands_played = 0
    score = 0
    total_score = 0
    num_replays = 0
    num_substitute_letter = 0
    #current_hand = deal_hand(HAND_SIZE)
    #print('Current hand:', display_hand(current_hand))

    while int(num_hands) != total_hands_played:

        current_hand = deal_hand(HAND_SIZE)
        total_hands_played = total_hands_played + 1

        if num_substitute_letter == 0:
            print('Current hand:', display_hand(current_hand))
    


        if num_substitute_letter == 0:
            sub_letter = input('Would you like to substitute a letter?')
            
        if num_substitute_letter == 1:
            score= play_hand(current_hand,word_list)
            print(score)
            total_score += score
        

        if sub_letter.lower() == 'no':
            score= play_hand(current_hand,word_list)
            total_score += score
            print(score)
            
        
        if sub_letter.lower() == 'yes' and num_substitute_letter == 0:
            letter = input('which letter would you like to replace:')
            substituted_hand = substitute_hand(current_hand,letter)
            print()
            score = play_hand(substituted_hand,word_list)
            num_substitute_letter = num_substitute_letter + 1
            current_hand = substituted_hand
            total_score += score
            print(score)
        
        
        if num_replays == 0:
            print('----------')
            replay = input('would you like to replay the hand?')
        
        if replay.lower() == 'yes' and num_replays == 0:
            num_replays = num_replays + 1
            score_1 = play_hand(current_hand,word_list)
            print(score_1)
            
            if score_1 > score:
                total_score = total_score + score_1 - score


 

    print('-------------')
    print('Total score over all hands:' + ' ' + str(total_score))
    




        

        
        

        


    


#
# Build data structures used for entire session and play game
# Do not remove the "if __name__ == '__main__':" line - this code is executed
# when the program is run directly, instead of through an import statement
#
if __name__ == '__main__':
    word_list = load_words()
    play_game(word_list)
