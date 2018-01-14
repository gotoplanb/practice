def is_pangram(sentence):
    ''' Check to see if the string contains every letter at least once
    sentence: string, the sentence to check
    return: boolean, true if the sentence is a pangram
    '''

    # create an array to hold new letters
    new_letters = []

    # iterate the given sentence
    for c in sentence:
        # if current char is a letter
        if c.isalpha():
            # transform it to lowercase
            c = c.lower()
            # if letter hasn't been stored yet
            if c not in new_letters:
                # store it in new array
                new_letters.append(c)
    
    # check if array contains all letters
    if (''.join(sorted(new_letters))) == 'abcdefghijklmnopqrstuvwxyz':
        return True

    return False
