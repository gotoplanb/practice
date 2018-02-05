def binary_search(list_of_numbers, number):
    if len(list_of_numbers) == 0:
        raise ValueError('Empty array')
    low = 0
    high = len(list_of_numbers) - 1
    while (low <= high):
        mid = (low + high) // 2
        guess = list_of_numbers[mid]
        if guess == number:
            return mid
        elif guess > number:
            high = mid - 1
        else:
            low = mid + 1
    
    raise ValueError('Key was not found')
