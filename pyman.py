# Welcome to a Python variation of the popular Hangman game: PYman; which revolves
# around thorough interaction with the Python console.

import time # Helps to delay output in the console 

# Prompts the player to enter their name
player_name = input("Please enter your name: ") 

time.sleep(1)

print("Welcome " + player_name + " to PYman. Please read the rules carefully, \
before proceeding to play the game. Enjoy!")

time.sleep(1)

# RULES
# 1. Words that are either a name or place start with a capital letter!
# 2. Words can only be guessed letter by letter
# 3. The word MUST be guessed before running out of the total attempts specified.
# 4. When it asks to guess a letter, make sure to only input a single character
# 5. Make sure you avoid guessing the same letter in any instance



###########################################################################

import urllib.request # extracts the words from the website and puts them in a list
import random # helps us get a random number to use as an index in the words_list



words_site = "http://svnweb.freebsd.org/csrg/share/dict/words?view=co&content-type=text/plain"

read_words = urllib.request.urlopen(words_site)
site_txt = read_words.read()

all_words = site_txt.splitlines()

# there are 25487 words in all_words extracted from the word bank in the website
random_index = random.randint(0, 25486)

original_word = all_words[random_index].decode("utf-8")
# a random word is selected each time the game is run from the all_words list
# converts original_word from bytes to a string using .decode() method
print(original_word)

length = len(original_word)
# string length of the word selected

fails = length * 2 # Number of attempts to guess the word

print("The word you are to guess is", length, "letters long.")
print("You have", fails, "guesses to guess the word") 
        
all_guesses = '' # will include the letters guessed

while (fails > 0):
    wrong_count = 0 # keeps track of the number of incorrect guesses
    
    for letter in original_word:
        if str(letter) in all_guesses:
            print (letter)
        else:
            wrong_count += 1
            print("_")
                
    if wrong_count == 0:
        break
    
    guess = input("Guess a letter: ")
    all_guesses += guess
    
    if guess not in original_word:
        print("The letter: " + guess + " is not in the word")
        fails = fails - 1
        print("You have",fails,"turns left to guess the word!")

if (fails == 0):
    print("You have not guessed the word, the word was " + original_word + \
          ". Play again!")
else:
    print ("Congrats! You have successfully guessed the word!")

        
        
    
    
############################################################################    
    
                
        
    
    











