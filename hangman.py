import random

def random_word():
    words = ["pes", "macka", "kon", "sliepka", "ovca"]
    pos = random.randint(0, 4)
    return words[pos]

def print_formatted(word):
    print(' '.join(word))

secret = random_word()
g_left = 8
used_letters = []
guessed = '_' * len(secret)
#print_formatted(guessed)
import random

def random_word():
    words = ["pes", "macka", "kon", "sliepka", "ovca"]
    pos = random.randint(0, 4)
    return words[pos]

def print_formatted(word):
    print(' '.join(word))

secret = random_word()
g_left = 8
used_letters = []
guessed = '_' * len(secret)
#print_formatted(guessed)

print('Welcome to the game Hangman!')
print(f'I am thinking of a word that is {len(secret)} letters long.')
print("----------")

while (g_left != 0 and secret != guessed):
    print(f'You have {g_left} left.')
    print('Used letters:', end=' ')
    print_formatted(used_letters)
    letter = input("Please guess a letter: ")

print('Welcome to the game Hangman!')
print(f'I am thinking of a word that is {len(secret)} letters long.')
print("----------")

while (g_left != 0 and secret != guessed):
    print(f'You have {g_left} left.')
    print('Used letters:', end=' ')
    print_formatted(used_letters)
    letter = input("Please guess a letter: ")











