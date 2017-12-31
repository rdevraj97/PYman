# Welcome to a Python variation of the popular Hangman game: PYman; which revolves
# around thorough interaction with the Python console. The words the user has to guess
# are only animals

import time # Helps to delay output in the console 

# Prompts the player to enter their name
player_name = input("Please enter your name: ") 

time.sleep(1)

print("Welcome " + player_name + " to PYman. Please read the rules carefully, \
before proceeding to play the game. Enjoy!")

time.sleep(1)

# RULES
# 1. Words can only be guessed letter by letter.
# 2. The word MUST be guessed before running out of the total attempts specified.
# 3. When it asks to guess a letter, make sure to only input a single character.
# 4. Make sure you avoid guessing the same letter in any instance
# 5. All letters are in lowercase.



###########################################################################

import random # helps us get a random number to use as an index in the words_list

animal_file = open("animals.txt", "r")

animals_lst = [] 
# initializes an empty list, to store all the animal words after reading the file

for line in animal_file:
    line = line.replace('\n', '')
    animals_lst.append(line)
    
animal_file.close()

# there are 52 words in animals_lst to guess from
random_index = random.randint(0, 51)

animal_word = animals_lst[random_index]
# a random word is selected each time the game is run from the animals_lst list
print(animal_word)

length = len(animal_word) 
print(length)
# string length of the word selected

fails = length * 2 # Number of attempts to guess the word

print("The word you are to guess is", length, "letters long.")
print("You have", fails, "guesses to guess the word") 
        
all_guesses = '' # will include the letters guessed

while (fails > 0):
    wrong_count = 0 # keeps track of the number of incorrect guesses
    
    for letter in animal_word:
        if str(letter) in all_guesses:
            print (letter)
        else:
            wrong_count += 1
            print("_")
                
    if wrong_count == 0:
        break
    
    guess = input("Guess a letter or the entire word if you know it: ")
    if (guess == animal_word):
        break
    all_guesses += guess
    
    if guess not in animal_word:
        print("The letter: " + guess + " is not in the word")
        fails = fails - 1
        print("You have",fails,"turns left to guess the word!")

if (fails == 0):
    print("You have not guessed the word, the word was " + animal_word + \
          ". Try another word!") #Losing case
else:
    print ("Congrats! You have successfully guessed the word!") #Winning case

        
        
    
    
############################################################################    
    
                
        
    
    











