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

def is_word_guessed(secret_word, letters_guessed):
    '''
    A function that checks if all the letters of the secret word have been guessed.

    Args:
        secret_word (string): the random word the user is trying to guess.
        letters_guessed (list of strings): list of letters that have been guessed so far.

    Returns: 
        bool: True only if all the letters of secret_word are in letters_guessed, False otherwise
    '''
    for i, letter in enumerate(secret_word):
        if letter != letters_guessed[i]:
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

#Checks for invalid guess
def invalid_guess(guess):
    if len(guess) > 1 or not guess.isalpha():
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
    letters_guessed = []

    print(f"Welcome to spaceman! You have {guesses_left} guesses left. \n")

    while(guesses_left > 0):
        guess = 'Placeholder'
        while(invalid_guess(guess)):
            guess = input("Please enter a letter to guess \n")

        #Add guess to list
        letters_guessed.append(guess)
        #Check if guess is in secretword show word if not decrement guesses left and show word
        if is_guess_in_word(guess, secret_word):
            letters_guessed.append(guess)
            print(f"You Guessed {guess}. \n")
        else:
            guesses_left -= 1
            print(f"Incorrect guess. You have {guesses_left} guesses left. \n")

        print(f"Current word state is {get_guessed_word(secret_word, letters_guessed)}. \n")

        if is_word_guessed(secret_word, letters_guessed):
            print(f"You Won with {guesses_left} guesses left!!!\n")

    print(f"The word was: {secret_word}")
            

#These function calls that will start the game
play_again = "y"
while play_again == "y":
    secret_word = load_word()
    spaceman(secret_word)
    play_again = input("Play again? (y/n): ")

