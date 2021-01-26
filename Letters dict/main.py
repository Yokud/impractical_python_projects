"""Main programm."""

from collections import Counter
from pprint import pprint

def get_dict_of_letters(text):
    """Return dict of letters in text and their count."""
    dict_of_letters = Counter()

    for letter in text:
        if letter.isalpha():
            dict_of_letters[letter.lower()] += 1

    return dict_of_letters


def main():
    """Test get_dict_of_letters with some text."""
    text = "Kost suck some dicks"

    pprint(get_dict_of_letters(text))


if __name__ == "__main__":
    main()
