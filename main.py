import random

HANGMAN_ASCII_ART = """
  _    _                                         
 | |  | |                                        
 | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
 |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
 | |  | | (_| | | | | (_| | | | | | | (_| | | | |
 |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                      __/ |                      
                     |___/
"""

HANGMAN_PHOTOS = {
    "picture 1":
        """ 
        x-------x
        """
    ,
    "picture 2":
        """
        x-------x
        |
        |
        |
        |
        |"""
    ,
    "picture 3":
        """
        x-------x
        |       |
        |       0
        |
        |
        |
        """
    ,
    "picture 4":
        """
         x-------x
         |       |
         |       0
         |       |
         |
         |
         """
    ,
    "picture 5":
        """
         x-------x
         |       |
         |       0
         |      /|\\
         |
         |
         """
    ,
    "picture 6":
        """
        x-------x
        |       |
        |       0
        |      /|\\
        |      /
        |
        """
    ,
    "picture 7":
        """
        x-------x
        |       |
        |       0
        |      /|\\
        |      / \\
        |
        """
}


def choose_word(file_path, index):  # IN SET Duplicates Not Allowed
    fil = open(file_path, "r")
    list_of_words = list(w.lower() for w in open(str(file_path), 'r').read().split())
    return list_of_words[index - 1], len(list_of_words)


def print_hangman(num_of_tries):
    print(HANGMAN_PHOTOS["picture " + str(num_of_tries)])


def check_valid_input(_letter_guessed, _old_letters_guessed):
    if not _letter_guessed.isalpha():
        print("X")
        return False
    elif len(_letter_guessed) > 1:
        print("X")
        return False
    if len(_old_letters_guessed) == 0:
        _old_letters_guessed += [_letter_guessed]
        print(":(")
        return False
    if _letter_guessed in _old_letters_guessed:
        print(":(")
        return False
    else:
        return True


def try_update_letter_guessed(letter_guessed, _old_letters_guessed):
    letter_guessed = letter_guessed.lower()
    if check_valid_input(letter_guessed, _old_letters_guessed):
        _old_letters_guessed += [letter_guessed]
        return True
    else:
        temp_old_letters_guessed = _old_letters_guessed
        # print("X")

        temp_old_letters_guessed.sort()

        print(*temp_old_letters_guessed, sep="-> ")
        return False


def show_hidden_word(secret_word, old_letters_guessed):
    for letter in secret_word:
        if letter not in old_letters_guessed:
            print("_", end=" ")
        else:
            print(letter, end=" ")


def check_win(secret_word, old_letters_guessed):
    for letter in secret_word:
        if letter not in old_letters_guessed:
            return False

    return True


# --------------------------------------------------------------------------------

MAX_TRIES = 6
num_of_tries = 0
old_letters_guessed = []

print(HANGMAN_ASCII_ART)

# file_path = input("Enter file path: ")  # words.txt
file_path = "words.txt"

secret_word = ('', 0)
secret_word = choose_word(file_path, random.randint(0, secret_word[1]))

print("> ", secret_word[0])
print_hangman(MAX_TRIES - (5 - num_of_tries))
show_hidden_word(secret_word[0], old_letters_guessed)

while num_of_tries != MAX_TRIES:
    num_of_tries = num_of_tries - 1
    if try_update_letter_guessed(input("\nGuess a letter: "), old_letters_guessed):
        if check_win(secret_word[0], old_letters_guessed):
            print("you won!\n")
            break
        show_hidden_word(secret_word[0], old_letters_guessed)
    else:
        print_hangman(MAX_TRIES - (5 + num_of_tries))
        show_hidden_word(secret_word[0], old_letters_guessed)

print("you lose!")

# print("_ " * len(str(player_word)))

# try_update_letter_guessed(player_word, old_letters)

# print(check_win(player_word, old_letters))
