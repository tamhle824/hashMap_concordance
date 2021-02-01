# word_count.py
# ===================================================
# Implement a word counter that counts the number of
# occurrences of all the words in a file. The word
# counter will return the top X words, as indicated
# by the user.
# ===================================================
# Tam H. Le
#reworked on 6/9/2020

import re
from hash_map import HashMap

"""
This is the regular expression used to capture words. It could probably be endlessly
tweaked to catch more words, but this provides a standard we can test against, so don't
modify it for your assignment submission.
"""
rgx = re.compile("(\w[\w']*\w|\w)")

def hash_function_2(key):
    """
    This is a hash function that can be used for the hashmap.
    """

    hash = 0
    index = 0
    for i in key:
        hash = hash + (index + 1) * ord(i)
        index = index + 1
    return hash


def top_words(source, number):
    """
        Takes a plain text file and counts the number of occurrences of case insensitive words.
        Returns the top `number` of words in a list of tuples of the form (word, count).

        Args:
            source: the file name containing the text
            number: the number of top results to return (e.g. 5 would return the 5 most common words)
        Returns:
            A list of tuples of the form (word, count), sorted by most common word. (e.g. [("a", 23), ("the", 20), ("it", 10)])
        """
    keys = set()
    word_list = []

    ht = HashMap(2500,hash_function_2)

    # This block of code will read a file one word as a time and
    # put the word in `w`. It should be left as starter code.
    with open(source) as f:
        for line in f:
            words = rgx.findall(line)
            count = 1
            for w in words:
                w = w.lower()
                ht.put_count(w,1)    # using helper put method to just add the key and keep track of value
                word_list.append(w)  # creating a new list of just words


    word_list = list(dict.fromkeys(word_list)) # removing duplicates
    word_tuple = []

    for i in word_list:
        word_tuple.append((i,ht.get(i))) #appends a tuple with the word key and its corresponding value


    word_tuple = sorted(word_tuple, key=lambda x: x[1],reverse=True) # sorting the tuple from Greatest to Least based on Value
    top_list = []

    for i in range(number):
        top_list.append(word_tuple[i])  # appending tuple index key/value up to arg number, keys with highest value at index 0
    return top_list



#x =  (top_words("alice.txt",10))  # COMMENT THIS OUT WHEN SUBMITTING TO GRADESCOPE



