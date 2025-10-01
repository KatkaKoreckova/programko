# https://github.com/KatkaMarcincakova/programko/blob/main/hangman.py

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

print(secret)

print('Welcome to the game Hangman!')
print(f'I am thinking of a word that is {len(secret)} letters long.')

while (g_left != 0 and secret != guessed):
    print("----------")
    print(f'You have {g_left} left.')
    print('Used letters:', end=' ')
    print_formatted(used_letters)
    print_formatted(guessed)
    letter = input("Please guess a letter: ")

    if (len(letter) != 1):
        print("Nevalidny vstup")
    elif (letter in used_letters):
        print("Pismeno uz bolo pouzite")
    else:
        used_letters.append(letter)
        if (letter not in secret):
            g_left -= 1
            print("Toto pismeno nie je v mojom slove")
        else:
            result = ""
            for i in range(len(secret)):
                if (secret[i] == letter):
                    result += letter
                else:
                    result += guessed[i]

            guessed = result

if (g_left == 0):
    print(f'Ooops prehral si. Slovo ktore si hadal bolo {secret}')
else:
    print(f'Hura vyhral si! Uhadol si slovo {secret}')
