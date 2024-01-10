import random

def is_word_guessed(secret, guessed):
    # ak su slova zo vstupu rovnake return True
    # inak return False
    if (secret == guessed):
        return True
    else:
        return False

def update_guessed(l, guessed, secret):
    # doplni nove pismeno do uhadnuteho
    result = ""
    for i in range(len(guessed)):
        if (secret[i] == l):
            result += l
        else:
            result += guessed[i]
    return result

def get_available_letters(alphabet, letter):
    # vyhodi guessed_letter z alphabet a vrati novy abecedu
    result = ""
    for a in alphabet:
        if (a != letter):
            result += a

    return result

def is_in_word(secret, letter):
    if (letter in secret):
        return True
    else:
        return False
    
def print_formatted(word):
    result = ' '.join(word)
    print(result)

def get_random_word():
    words = [ 'hollow', 'frequent', 'poke', 'tongue', 'quick', 'market', 'butter']
    pos = random.randint(0, len(words) - 1)
    return words[pos]


#samotny program
secret = get_random_word()
guessed = len(secret) * '_'
g_left = 8
alphabet = "abcdefghijklmnopqrstuvwxyz"
print(secret)
print('Welcome to the game, Hangman!')
print(f'I am thinking of a word that is {len(secret)} letters long.')
print('-------------')

while (is_word_guessed(secret, guessed) == False):
    print('Available letters:', end=' ')
    print_formatted(alphabet)
    letter = input('Please guess a letter: ')

    if (len(letter) != 1):
        print("Oops! That's not a letter:", end=' ')
    elif (is_in_word(alphabet, letter) == False):
        print("Oops! That's not a letter:", end=' ')
    elif (is_in_word(secret, letter) == False):
        print('Oops! That letter is not in my word:', end=' ')
    else:
        print('Good guess:', end=' ')
        guessed = update_guessed(letter, guessed, secret)

    alphabet = get_available_letters(alphabet, letter)
    print_formatted(guessed)
    print('-------------')


print("Congratulations, you won!")




