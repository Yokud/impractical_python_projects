"""User enters name and interactively derives anagram phrase from name.
Requires access to an external English word dictionary file
and file-loading module "load_dictionary.py"
"""
from collections import Counter
from itertools import permutations
import load_dictionary

dict_file = load_dictionary.load('words.txt')
# ensure "a" & "I" are included
dict_file.append('a')
dict_file.append('i')
dict_file = sorted(dict_file)

ini_name = input("Enter a name: ")

#______________________________________________________________________________

def find_anagrams(name, word_list):
    """Read name & dictionary file & display all anagrams IN name."""
    name_letter_map = Counter(name)
    anagrams = []
    for word in word_list:
        test = ''
        word_letter_map = Counter(word.lower())
        for letter in word:
            if word_letter_map[letter] <= name_letter_map[letter]:
                test += letter
        if Counter(test) == word_letter_map:
            anagrams.append(word)

    for anagram in anagrams:
        if anagram not in word_list:
            anagrams.remove(anagram)

    return anagrams


def phrases_filter(name, phrases):
    """Filter only phrases with the same letters"""
    name_letters = Counter(name)

    for phrase in phrases:
        phrase_letters = Counter(phrase.replace(' ', ''))

        if phrase_letters != name_letters:
            phrases.remove(phrase)

    return phrases


def main():
    """Help user build anagram phrase from their name."""
    # remove spaces & convert to lower case
    name = ''.join(ini_name.lower().split())
    # remove hyphens in hyphenated names
    name = name.replace('-', '')

    phrases = list()

    while len(name):
        anagrams = find_anagrams(name, dict_file)
        phrases.extend(anagrams)
        phrases = list(set(phrases))
        name = name[1:]

    print(phrases)
    phrases = [' '.join(p) for p in permutations(phrases)]

    name = ''.join(ini_name.lower().split())
    phrases = phrases_filter(name, phrases)
    print(*phrases, sep='\n')

#______________________________________________________________________________

if __name__ == '__main__':
    main()
