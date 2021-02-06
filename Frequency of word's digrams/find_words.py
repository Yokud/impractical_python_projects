'''Count frequency of word's digrams in words'''
import collections
import itertools
import pprint
import load_dictionary


def digrams_in_word(word):
    '''Find digrams in word'''
    digrams = [''.join(i) for i in itertools.permutations(word, 2)]

    return set(digrams)


def freq_digrams(digrams, words):
    '''Frequency of meeting digrams in words'''
    dg_counter = collections.Counter()

    for digram in digrams:
        for word in words:
            if digram in word:
                dg_counter[digram] += 1

    return dg_counter


def main():
    '''Print frequency of digrams'''
    word = 'tmvoordle'
    digrams = digrams_in_word(word)
    words = load_dictionary.load('words.txt')
    pprint.pprint(freq_digrams(digrams, words))


if __name__ == '__main__':
    main()
