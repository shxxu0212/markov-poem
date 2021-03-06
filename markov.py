"""Generate Markov text from text files."""

from random import choice
import sys

n = int(raw_input("How many words should be in our ngram? "))
print "\n"

def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    with open(file_path) as file_data:
        text = file_data.read()
        # returns text as a large string
        return text


def make_word_list(text_string):
    """ takes input text as string; creates list of individual words """
    words = text_string.split(" ")
    punctuations = "?!."
    # creates tuple of index and word
    for i, word in enumerate(words):
        # if word has a line break in it
        if "\n" in word:
            # remove the line break & put into temporary variable tokens
            tokens = word.split("\n")
            # if word is not False, put word in array
            tokens = [word for word in tokens if word]  # != ""]
            if tokens[0][-1] in punctuations:
                tokens[0] = tokens[0] + "\n"
            words[i:i+1] = tokens
    return words


def make_chains(words, n):
    """Take input words as list; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains("hi there mary hi there juanita")

    Each ngram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']
        
        >>> chains[('there','juanita')]
        [None]
    """

    chains = {}

    for i in range(len(words)-n):
        # creates ngram from first two words in text string,
        # with each iteration moves down one word
        # assigns ngram as key in chains dictionary
        ngram = tuple(words[i:i+n])
        # to i+n because the tuple will exclude i+n, then i+n is next word
        next_word = words[i+n]
        # if ngram exists as a key, get its value then add next word,
        # if not create empty list
        next_words = chains.get(ngram, [])
        next_words.append(next_word)
        chains[ngram] = next_words

    # to prevent printing error, assign value of end of text file key to empty
    chains[tuple(words[-n:])] = [None]
    return chains


def make_text(chains, start_words, n):
    """Return text from chains."""
    # explicit start
    words = start_words

    while True:
        ngram = tuple(words[-n:])
        # ngram = (words[-2], words[-1])
        # stop loop when you get to the end
        # if chains[ngram] == []:
        #     break
        # randomly choose a word from value set of each ngram key and add to
        # word list, which we will join & print as string
        next_word = choice(chains[ngram])
        if next_word is None:
            break
        words.append(next_word)

    words[0] = " " + words[0]
    return " ".join(words)


if len(sys.argv) > 1:
    input_path = sys.argv[1]
else:
    input_path = 'green-eggs.txt'

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# list of words
words = make_word_list(input_text)

# Get a Markov chain
chains = make_chains(words, n)

# make starting words for print
start_words = words[0:n]

# Produce random text
random_text = make_text(chains, start_words, n)

print random_text
