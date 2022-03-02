from typing import List
from letter_state import LetterState
from wordle import Wordle
from colorama import Fore
import random


def main():

    word_set = load_word_set('Wordle/word_souce.txt')
    secret = random.choice(list(word_set))
    wordle = Wordle(secret)

    while wordle.can_attempt:
        x = input('\nType your guess: ').upper()

        if len(x) != wordle.word_length:
            print(
                Fore.RED + f'Word must be {wordle.word_length} characters long' + Fore.RESET)
            continue

        if not x in word_set:
            print(Fore.RED + f'{x} not in the word list' + Fore.RESET)
            continue

        wordle.attempt(x)
        display_results(wordle)

    if wordle.is_solved:
        print("You've solved the puzzle.")
    else:
        print('You failed to solve the puzzle!')
        print(f'The word was: {wordle.secret}')


def display_results(wordle: Wordle):
    print('\nResults so far...\n')
    print(f'\n{wordle.remaining_attempts} Remaining attempts...\n')

    lines = []

    for word in wordle.attempts:
        result = wordle.guess(word)
        colored_result_string = convert_result_to_color(result)
        lines.append(colored_result_string)

    for _ in range(wordle.remaining_attempts):
        lines.append(' '.join(['_'] * wordle.word_length))

    draw_border_around(lines)


def load_word_set(path: str):
    word_set = set()
    with open(path, 'r') as f:
        for line in f.readlines():
            word = line.strip().upper()
            word_set.add(word)
    return word_set


def convert_result_to_color(result: List[LetterState]):
    result_with_color = []
    for letter in result:
        if letter.in_position:
            color = Fore.GREEN
        elif letter.in_word:
            color = Fore.YELLOW
        else:
            color = Fore.WHITE
        colored_letter = color + letter.character + Fore.RESET
        result_with_color.append(colored_letter)

    return ' '.join(result_with_color)


def draw_border_around(lines: List[str], size: int = 9, pad: int = 1):
    content_length = size + pad * 2
    top_border = '┌' + '─' * content_length + '┐'
    bottom_border = '└' + '─' * content_length + '┘'
    space = ' ' * pad
    print(top_border)

    for line in lines:
        print('│' + space + line + space + '│')

    print(bottom_border)


if __name__ == '__main__':
    main()
