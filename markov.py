"""Generate Markov text from text files."""

from random import choice


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    with open(file_path) as file_data:
        text = file_data.read()
        # returns text as a large string
        return text


def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains("hi there mary hi there juanita")

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']
        
        >>> chains[('there','juanita')]
        [None]
    """

    chains = {}

    words = text_string.split(" ")

    for i in range(len(words)-2):
        # creates bigram from first two words in text string, 
        # with each iteration moves down one word
        # assigns bigram as key in chains dictionary
        bigram = (words[i], words[i+1])
        next_word = words[i+2]
        # if bigram exists as a key, get its value then add next word,
        # if not create empty list
        next_words = chains.get(bigram, [])
        next_words.append(next_word)
        chains[bigram] = next_words

    # to prevent printing error, assign value of end of text file key to empty
    chains[(words[-2], words[-1])] = []
    return chains


def make_text(chains):
    """Return text from chains."""
    # explicit start
    words = ['Would', 'you']

    while True:
        bigram = (words[-2], words[-1])
        # stop loop when you get to the end
        if chains[bigram] == []:
            break
        # randomly choose a word from value set of each bigram key and add to
        # word list, which we will join & print as string
        next_word = choice(chains[bigram])
        words.append(next_word)

    return " ".join(words)


input_path = "green-eggs.txt"

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print random_text
