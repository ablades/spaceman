import random

def load_word():
    '''
    A function that reads a text file of words and randomly selects one to use as the secret word
        from the list.

    Returns: 
           string: The secret word to be used in the spaceman guessing game
    '''
    f = open('words.txt', 'r')
    words_list = f.readlines()
    f.close()
    words_list = words_list[0].split(' ')
    secret_word = random.choice(words_list)

    return secret_word

'''
#Changes the word to a different word of same length and guessed characters
def change_word(guessed_word, words_list):

    guessed_list = list(guessed_word)

    word_dict = pass
    contains_letters = False
    word_choices = pass

    #Get words from words list that have the same length
    #Check all indexes in word for characters that have been guessed at same index
    #if it contains all the letters in the right positions add it to a list of possible words
    #if the length of that list is > 0 randomly choose a word
    #if it is not keep the current word

    for item in words_list:
        countains_letters = False
        for index, letter in enumerate(word_dict):


    for index, letter in enumerate(word_dict):
        contains_letters = False
        for item in words_list:
            if len(item) == guessed_word and item[index] == letter:
                contains_letters = True
            else:
                contains_letters = False
            
            
        if contains_letters:
            #add that word to list
            pass

        TODO: Complete Sinister Spaceman
'''




def is_word_guessed(secret_word, letters_guessed):
    '''
    A function that checks if all the letters of the secret word have been guessed.

    Args:
        secret_word (string): the random word the user is trying to guess.
        letters_guessed (list of strings): list of letters that have been guessed so far.

    Returns: 
        bool: True only if all the letters of secret_word are in letters_guessed, False otherwise
    '''
    for letter in secret_word:
        if letter not in letters_guessed:
            return False

    return True

def get_guessed_word(secret_word, letters_guessed):
    '''
    A function that is used to get a string showing the letters guessed so far in the secret word and underscores for letters that have not been guessed yet.

    Args: 
        secret_word (string): the random word the user is trying to guess.
        letters_guessed (list of strings): list of letters that have been guessed so far.

    Returns: 
        string: letters and underscores.  For letters in the word that the user has guessed correctly, the string should contain the letter at the correct position.  For letters in the word that the user has not yet guessed, shown an _ (underscore) instead.
    '''
    guessed_word = ''
    #Check each letter in secret word
    for letter in secret_word:
        if letter in letters_guessed:
            guessed_word += letter
        else:
          guessed_word += '_'
    
    return guessed_word

def is_guess_in_word(guess, secret_word):
    '''
    A function to check if the guessed letter is in the secret word

    Args:
        guess (string): The letter the player guessed this round
        secret_word (string): The secret word

    Returns:
        bool: True if the guess is in the secret_word, False otherwise

    '''
    for letter in secret_word:
        if guess == letter:
            return True

    return False
#Ascii art    
def art():
    spaceman = []
    spaceman.append("             _..._")
    spaceman.append("           .'     '.      _")
    spaceman.append("          /    .-""-\   _/ \ ")
    spaceman.append("        .-|   /:.   |  |   |")
    spaceman.append("        |  \  |:.   /.-'-./")
    spaceman.append("        | .-'-;:__.'    =/")
    spaceman.append("        .'=  *=|NASA _.='")
    spaceman.append("        /   _.  |    ;")
    spaceman.append("        ;-.-'|    \   |")
    spaceman.append("        /   | \    _\  _\ ")
    spaceman.append("        \__/'._;.  ==' ==\ ")
    spaceman.append("                \    \   |")
    spaceman.append("                /    /   /")
    spaceman.append("                /-._/-._/")
    spaceman.append("               \   `\  \ ")
    spaceman.append("                `-._/._/")
    spaceman.append("       _____________________")

    return spaceman

def print_art(secret_word, guesses_left):
    spaceman = art()
    guesses_avaliable = len(secret_word)
    size = len(spaceman)
    step_size = size / guesses_avaliable
    print_amount = guesses_avaliable - guesses_left

    i = 0
    step = 0
    j = 0
    while i < print_amount:
        step = 0
        while step < step_size and j < size:
            print("\u001b[31m" + spaceman[j] + "\x1b[0m")
            j += 1
            step += 1

        i += 1


#Checks for invalid guesses True: Invalid Guesses False: Valid Guess
def invalid_guess(guess, letters_guessed):
    if guess in letters_guessed:
        print(f"You have already guessed \033[96m{guess}\x1b[0m\n")
        return True
    #Checks if guess is length or is non alphabetic
    elif len(guess) != 1 or not guess.isalpha():
        return True
    else:
        return False


def spaceman(secret_word):
    '''
    A function that controls the game of spaceman. Will start spaceman in the command line.

    Args:
      secret_word (string): the secret word to guess.
    '''
    guesses_left = len(secret_word)
    correct_guesses = []
    letters_guessed = []
    

    print(f"Welcome to spaceman! You have \033[96m{guesses_left}\x1b[0m guesses left. \n")

    #Run game until no guesses are left
    while(guesses_left > 0):
        guess = 'Placeholder'
        #Check for invalid guesses
        while(invalid_guess(guess, letters_guessed)):
            guess = input("Please enter a letter to guess: ").lower()

        #Add guess to list
        letters_guessed.append(guess)
        #Check if guess is in secret_word show word if not decrement guesses left and show word
        if is_guess_in_word(guess, secret_word):
            correct_guesses.append(guess)
            print(f"Correct!! You Guessed \033[96m{guess}\x1b[0m \n")
        else:
            guesses_left -= 1
            print(f"Incorrect guess. You have \033[96m{guesses_left}\x1b[0m guesses left. \n")
            print_art(secret_word, guesses_left)
            print("\n")

        print(f"Current word state is \033[96m{get_guessed_word(secret_word, correct_guesses)}\x1b[0m \n")

        if is_word_guessed(secret_word, correct_guesses):
            print(f"You Won with \033[96m{guesses_left}\x1b[0m guesses left!!!\n")
            guesses_left = 0
        elif guesses_left == 0:
            print("You Lose.")

        print("----------------------------------------------------------------------")

    print(f"The word was: \033[96m{secret_word}\x1b[0m")
            


play_again = "y"
while play_again == "y":
    
    secret_word = load_word()
    print_art(secret_word, 0)
    spaceman(secret_word)
    play_again = input("Play again? (y/n): ")

print("Thanks for playing!")

'''
spaceman image taken from: https://www.asciiart.eu/space/astronauts
        _..._
      .'     '.      _
     /    .-""-\   _/ \
   .-|   /:.   |  |   |
   |  \  |:.   /.-'-./
   | .-'-;:__.'    =/
   .'=  *=|NASA _.='
  /   _.  |    ;
 ;-.-'|    \   |
/   | \    _\  _\
\__/'._;.  ==' ==\
         \    \   |
         /    /   /
         /-._/-._/
  jgs    \   `\  \
          `-._/._/
'''