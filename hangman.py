import random


def uncovering(letter, win_word, covered_word):
    for i in range(len(win_word)):
        if win_word[i] == letter:
            covered_word[i] = letter
    return covered_word


def input_check(letter, win_word, covered_word, input_set, lives):
    if letter in input_set:
        print('You already typed this letter')
        return covered_word, input_set, lives

    if len(letter) != 1:
        print('You should print a single letter')
    elif not (letter.isascii() and letter.isalpha() and letter.islower()):
        print('It is not an ASCII lowercase letter')
    elif letter not in win_word:
        print('No such letter in the word')
        input_set.add(letter)
        lives -= 1
    else:
        covered_word = uncovering(letter, win_word, covered_word)
        input_set.add(letter)

    return covered_word, input_set, lives


def menu():
    while True:
        game_action = input('Type "play" to play the game, "exit" to quit: ')
        if game_action == 'play':
            game()
        elif game_action == 'exit':
            break


def game():
    win_words = ('python', 'java', 'kotlin', 'javascript')
    win_word = random.choice(win_words)
    input_set = set()
    covered_word = list('-' * len(win_word))
    lives = 8

    while lives > 0:
        print()
        print(*covered_word, sep='')

        if '-' not in covered_word:
            print('You guessed the word!')
            break

        letter = input('Input a letter: ')

        covered_word, input_set, lives = input_check(letter, win_word, covered_word, input_set, lives)

    print('You survived!' if '-' not in covered_word else 'You are hanged!')
    print()


print("H A N G M A N")

menu()
