import unidecode
import click
import typing

def load_termo_wordlist(path: str = './termooo_list.txt') -> list[str]:
    """
    Loads wordlist from termooo

    :param path: path to string
    :return: list of words
    """
    words = open(path, 'r', encoding='utf8').read()
    words = words.replace('"', '').split(',')
    words = list(map(unidecode.unidecode, words))
    return words

def load_wordle_wordlist(path: str = './wordle_list.txt') -> list[str]:
    """
    Loads wordlist from wordle

    :param path: path to string
    :return: list of words
    """
    words = open(path, 'r', encoding='utf8').readlines()
    return words

def filter_wordlist(wordlist, *conditions) -> list[str]:
    """
    Applies functions that take a string and return a bool to a list of words

    :param wordlist: List of words
    :param conditions: Functions to filter the wordlist
    :return: subset of words that obey the conditions
    """
    return [i.strip() for i in wordlist if all([condition(i) for condition in conditions])]

def create_rules_from_known_location_str(known_str: str, unknown_char = '_') -> list[typing.Callable]:
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

def create_rules_from_unknowns(characters: str) -> list[typing.Callable]:
    """
    Takes in a string of every known letter but with unknown position (yellow).

    Example - Possibilities for the word 'slate':
        - 'ela'
        - '' if no yellow letters

    :param characters:
    :return:
    """
    rules = []
    for character in characters:
        # Need to keep variables within lambda scope only
        rules.append(lambda x, character=character: character in x)
    return rules

def create_rules_yellow_positions(characters: str, unknown_char ='_') -> list[typing.Callable]:
    rules = []
    for i, character in enumerate(characters):
        if character == unknown_char:
            continue
        rule = lambda x, character=character, i=i: x[i] != character
        rules.append(rule)
    rules.extend(create_rules_from_unknowns(characters.replace(unknown_char, '')))
    return rules

@click.command()
@click.option('--known', '-k', default='_____', help='Known positions. Word=slate. form=__a_e')
@click.option('--unknown', '-u', default='', help='Known letters, unknown positions. form=slt')
@click.option('--wordlist', '-w', default='wordle', help='Wordlist to use. wordle or termo')
@click.option('--yellows', '-y', default='_____', help='Yellow positions')
def main(known: str, unknown: str, wordlist: str, yellows: str):
    if wordlist.lower() not in ['wordle', 'termo', 'termooo']:
        raise ValueError(f'Not a valid wordlist! ({wordlist}).')
    if wordlist == 'wordle':
        words = load_wordle_wordlist()
    elif (wordlist == 'termo') or (wordlist == 'termooo'):
        words = load_termo_wordlist()

    known_rules = create_rules_from_known_location_str(known)
    unknown_rules = create_rules_from_unknowns(unknown)
    yellow_rules = create_rules_yellow_positions(yellows)
    all_rules = known_rules+unknown_rules+yellow_rules
    if len(all_rules) == 0:
        choice = input('Warning, no rules passed. Print entire wordlist? [n]/y:')
        if choice == 'y':
            print(words)
        return
    print(filter_wordlist(words, *all_rules))

if __name__ == '__main__':
    main()