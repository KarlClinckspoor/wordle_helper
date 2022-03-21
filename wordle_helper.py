import \
    os.path

import unidecode
import click
import typing


def load_termo_wordlist(path: str = "./termooo_list.txt") -> list[str]:
    """
    Loads wordlist from termooo

    :param path: path to string
    :return: list of words
    """
    words = open(path, "r", encoding="utf8").read()
    words = words.replace('"', "").split(",")
    words = list(map(unidecode.unidecode, words))
    return words


def load_wordle_wordlist(path: str = "./wordle_list.txt") -> list[str]:
    """
    Loads wordlist from wordle

    :param path: path to string
    :return: list of words
    """
    words = open(path, "r", encoding="utf8").readlines()
    return words


def filter_wordlist(wordlist, *conditions) -> list[str]:
    """
    Applies functions that take a string and return a bool to a list of words

    :param wordlist: List of words
    :param conditions: Functions to filter the wordlist
    :return: subset of words that obey the conditions
    """
    return [
        i.strip() for i in wordlist if all([condition(i) for condition in conditions])
    ]


def create_rules_from_greens(known_str: str, unknown_char="_") -> list[typing.Callable]:
    """
    Takes in a string where every unknown letter is '_' and every known letter (green) is in the position.

    Example - Possibilities for the word 'slate':
        - '__ate' has the last three letters green
        - 's_a_e' has the letters 's', 'a', 'e' in green
        - '_____' if no known letters

    :param known_str: String where unknown letters are '_'.
    :param unknown_char: Replaces '_' if desired
    :return: a list of functions for each known position
    """
    rules = []
    for i, character in enumerate(known_str):
        if character == unknown_char:
            continue
        else:
            # Need to keep variables within lambda scope only
            rule = lambda x, i=i, character=character: x[i] == character
            rules.append(rule)
    return rules


def create_rules_from_known_letter_unknown_position(
    characters: str,
) -> list[typing.Callable]:
    """
    Takes in a string of every known letter but with unknown position (yellow).

    Example - Possibilities for the word 'slate':
        - 'ela'
        - '' if no yellow letters

    :param characters:
    :return: list of functions with the restrictions
    """
    rules = []
    for character in characters:
        # Need to keep variables within lambda scope only
        rules.append(lambda x, character=character: character in x)
    return rules


def create_rules_from_black_letters(characters: str,) -> list[typing.Callable]:
    """
    Takes in a string of every black letter.

    :param characters: Characters to remove
    :return: list of functions with the restrictions
    """
    rules = []
    for character in characters:
        # Need to keep variables within lambda scope only
        rules.append(lambda x, character=character: character not in x)
    return rules


def create_rules_yellows(characters: str, unknown_char="_") -> list[typing.Callable]:
    """
    Given a list of in yellow positions, provides a list of rules that remove a yellow character from its position,
    and then finds the words that have yellow characters in other positions.

    Example - Possibilities for the word 'slate':
        - 'ate__' has the first three letters in yellow
        - 's_a_e' has the letters 's', 'a', 'e' in green
        - '_____' if no known letters

    :param characters: In the same form as create_rules_from_greens
    :param unknown_char: The character to indicate where it's gray
    :return: list of functions
    """
    rules = []
    for i, character in enumerate(characters):
        if character == unknown_char:
            continue
        rule = lambda x, character=character, i=i: x[i] != character
        rules.append(rule)
    rules.extend(
        create_rules_from_known_letter_unknown_position(
            characters.replace(unknown_char, "")
        )
    )
    return rules

import sys
import os

# From https://stackoverflow.com/questions/7674790/bundling-data-files-with-pyinstaller-onefile
def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

@click.command()
@click.option(
    "--known", "-k", default="_____", help="Known positions. Word=slate. form=__a_e"
)
@click.option(
    "--unknown", "-u", default="", help="Known letters, unknown positions. form=slt"
)
@click.option(
    "--wordlist", "-w", default="wordle", help="Wordlist to use. wordle or termo"
)
@click.option("--blacks", "-b", default="", help="Letters in black. form=slt")
@click.option(
    "--yellows",
    "-y",
    default="_____",
    help="Yellow positions. Word=slate, yellows in ate. form=ate__",
)
@click.option('--path', '-p', default='', help='path to wordlist')
def main(known: str, unknown: str, wordlist: str, yellows: str, blacks: str, path: str):

    if wordlist.lower() not in ["wordle", "termo", "termooo"]:
        raise ValueError(f"Not a valid wordlist! ({wordlist}).")

    if wordlist == "wordle":
        if path:
            if not os.path.exists(path):
                raise NameError("Not a valid path!")
            words = load_wordle_wordlist(path=path)
        else:
            words = load_wordle_wordlist(path=resource_path('wordle_list.txt'))

    elif (wordlist == "termo") or (wordlist == "termooo"):
        if path:
            if not os.path.exists(path):
                raise NameError("Not a valid path!")
            words = load_termo_wordlist(path=path)
        else:
            words = load_termo_wordlist(path=resource_path('termooo_list.txt'))

    green_rules = create_rules_from_greens(known)
    known_letter_rules = create_rules_from_known_letter_unknown_position(unknown)
    yellow_rules = create_rules_yellows(yellows)
    black_rules = create_rules_from_black_letters(blacks)
    all_rules = green_rules + known_letter_rules + yellow_rules + black_rules
    if len(all_rules) == 0:
        choice = input("Warning, no rules passed. Print entire wordlist? [n]/y:")
        if choice == "y":
            print(words)
        return
    print(filter_wordlist(words, *all_rules))


if __name__ == "__main__":
    main()
