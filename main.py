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

MAX_TRIES = 6

print(HANGMAN_ASCII_ART)

player_word = input("Please enter a word: ")
print("_ "*len(str(player_word)))

player_guess = input("Guess a letter: ")
print(player_guess)

# print(random.randint(3, 9))

#
# print("""
#     x-------x
# """)
# print("""
#     x-------x
#     |
#     |
#     |
#     |
#     |""")
#
# print("""
#     x-------x
#     |       |
#     |       0
#     |
#     |
#     |
#
# """)
# print("""
#     x-------x
#     |       |
#     |       0
#     |       |
#     |
#     |
#
# """)
# print("""
#     x-------x
#     |       |
#     |       0
#     |      /|\\
#     |
#     |
#
# """)
# print("""
#     x-------x
#     |       |
#     |       0
#     |      /|\\
#     |      /
#     |
#
# """)
# print("""
#     x-------x
#     |       |
#     |       0
#     |      /|\\
#     |      / \\
#     |
# """)
