"""
User enters name and interactively derives anagram phrase from name.

Requires access to an external English word dictionary file
and file-loading module "load_dictionary.py"
"""

from collections import Counter
from itertools import combinations
import load_dictionary


def find_anagrams(name, word_list):
    """Read name & dictionary file & display all anagrams in name."""
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


def phrases_gen(name, word_list):
    """Generate anagram phrases from name."""
    name_letters = Counter(name)
    filtered = []

    phrases = set()
    while len(name):
        anagrams = find_anagrams(name, word_list)
        phrases |= set(anagrams)
        name = name[1:]

    combs = set()
    temp_combs = set(combinations(phrases, 1))
    temp = 1
    while len(temp_combs) or temp < 2:
        combs |= temp_combs
        temp_combs = set(combinations(phrases, temp))
        temp += 1


    phrases = [' '.join(c) for c in combs]
    for phrase in phrases:
        phrase_letters = Counter(phrase.replace(' ', ''))

        if phrase_letters == name_letters:
            filtered.append(phrase)

    return filtered


def main():
    """Load words, format name, get anagrams and print first no more 500 phrases."""
    dict_file = load_dictionary.load('words.txt')

    # ensure "a" & "I" are included
    dict_file.append('a')
    dict_file.append('i')

    dict_file = sorted(dict_file)

    ini_name = input("Enter a name: ")
    name = ''.join(ini_name.lower().split())  # remove spaces & convert to lower case
    name = name.replace('-', '')  # remove hyphens in hyphenated names


    phrases = phrases_gen(name, dict_file)
    print(len(phrases))

    for i in range(500 if len(phrases) > 500 else len(phrases)):
        print(phrases[i])


if __name__ == '__main__':
    main()
