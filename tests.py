from wordle_helper import load_termo_wordlist, load_wordle_wordlist, create_rules_from_known_letter_unknown_position, create_rules_from_greens, filter_wordlist
import unidecode

def test1():
    wordlist = load_termo_wordlist()
    word = "táxis"
    word = unidecode.unidecode(word)

    guess1 = lambda x: x[0] == 't'
    guess2 = lambda x: x[2] == 'x'

    print(filter_wordlist(wordlist, guess1, guess2))

def test2():
    wordlist = load_wordle_wordlist()
    word = 'slate'

    guess1 = lambda x: x[0] == 's'
    guess2 = lambda x: 'l' in x
    guess3 = lambda x: 'e' in x

    print(filter_wordlist(wordlist, guess1, guess2, guess3))

def test3():
    wordlist = load_termo_wordlist()
    word = 'táxis'
    known_letters_and_pos = '_a__s'
    known_letters = 'i'
    rules1 = create_rules_from_greens(known_letters_and_pos)
    rules2 = create_rules_from_known_letter_unknown_position(known_letters)
    print(filter_wordlist(wordlist, *(rules1+rules2)))

def test4():
    wordlist = load_wordle_wordlist()
    word = 'slate'
    known_letters_and_pos = '__ate'
    known_letters = ''
    rules1 = create_rules_from_greens(known_letters_and_pos)
    rules2 = create_rules_from_known_letter_unknown_position(known_letters)
    print(filter_wordlist(wordlist, *(rules1+rules2)))
