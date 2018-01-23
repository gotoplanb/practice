""" Verify an ISBN
"""

def verify(isbn):
    """ Verify the ISBN"""
    # remove dashes and convert X to 10 if it's the last digit
    isbn_array = []
    for item in isbn:
        if 'X' in isbn[:-1]:
            return False
        if item != '-':
            if item == 'X':
                isbn_array.append('10')
            else:
                isbn_array.append(item)

    # verify string is 10 characters
    if len(isbn_array) != 10:
        return False

    # verify that the first nine values are indeed numbers
    if ''.join(isbn_array[:8]).isdigit():
        pass
    else:
        return False

    # verify that the last value is a number
    if isbn_array[-1].isdigit():
        pass
    else:
        return False

    # calculate sum of index * counter
    counter = 10
    total = 0
    for i in range(0, len(isbn_array)):
        # print(isbn_array[i] + " " + str(counter))
        total = total + (int(isbn_array[i]) * counter)
        counter = counter - 1

    # valid isbn has total % 11 = 0
    return total % 11 == 0
