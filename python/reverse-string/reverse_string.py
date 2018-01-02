def reverse(input=''):
    ''' Reverse a string
    input: string, the string to be reversed
    return: string, the reversed string
    '''

    # create a new empty array
    new_array = []
    new_string = ''

    # iterate the old string and append to new array
    for i in input:
        new_array.append(i)

    # reverse the new array in place
    new_array.reverse()

    # iterate through new array
    for i in new_array:
        # append each item to new string
        new_string += i

    # return new string
    return new_string
