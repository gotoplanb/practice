import re

def word_count(phrase):

    # Create an empty dictionary to hold our word counts.
    words = {}

    # Remove non-desireable characters and make letter lowercase.
    raw_words = re.findall(r"[a-z\d]+(?:'[a-z])?", phrase.lower())
    
    for word in raw_words:
        if word in words:
            words[word] += 1
        else:
            words[word] = 1
    
    return words
