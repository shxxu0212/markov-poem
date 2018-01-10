""" Generate markov play from play script """

# import native modules: sys, os, random, math
# import api, packages: python-twitter
# import project files

from random import choice
import sys
import markov

# to-do list:
# make a list of characters (or build into function)
# new make chains function
# current_char variable
#


def make_char_list(words):
    """ from play script (list of words), generate list of characters

    >>> make_char_list(['ESTR:', 'Hello', 'Vlad.\n', 'VLAD:', 'Privyet!'])
    ['ESTR:', 'VLAD:']
    """

    return [word for word in words if word == word.upper]


def make_chains(words, chars, n):
    character_chains = {}




    for i in range(len(words)-n):
        ngram = tuple(words[i:i+n])
        next_word = words[i+n]
        next_words = chains.get(ngram, [])
        next_words.append(next_word)
        chains[ngram] = next_words

    chains[tuple(words[-n:])] = [None]
    return chains




# ------------- Calling the script ------------- #
n = int(raw_input("How many words should be in our ngram? "))
print "\n"

if len(sys.argv) > 1:
    input_path = sys.argv[1]
else:
    input_path = 'waiting_for_godot.txt'

input_text = markov.open_and_read_file(input_path)

# list of words
words = markov.make_word_list(input_text)

# make character list
chars = make_char_list(words)

# Get a Markov chain
chains = make_chains(words, chars, n)

# make starting words for print
start_words = words[0:n]

# Produce random text
random_text = markov.make_text(chains, start_words, n)

print random_text
