import string

def word_count(phrase):

    # Create an empty dictionary to hold our word counts
    words = {}

    # Remove non-desireable characters. This should be a regex.
    letters_only = []
    for letter in phrase:
        if (letter in string.ascii_letters) or (letter == "'") or (letter in string.digits) :
            letters_only.append(letter.lower())
        else:
            letters_only.append(" ")

    # Split the phrase by a space
    raw_words = ''.join(letters_only).split()
    
    for word in raw_words:
        if word in words:
            words[word] += 1
        else:
            words[word] = 1
    
    return words
