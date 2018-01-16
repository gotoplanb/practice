"""Determines least-common multiple of an number of numbers"""

def lcm(numbers):
    """Determines least-common multiple of an number of numbers. Minimum 2.
    numbers: array, an array of integers
    return: integer, the lowest common multiple
    """

    # Ensure there are at least two numbers
    if len(numbers) < 2:
        raise ValueError('You must provide at least two numbers')

    # Start by multiplying the first two numbers
    lcm = numbers.pop(0) * numbers.pop(0)

    # If there are more numbers still to multiply
    if len(numbers) > 0:
        # Loop through each number
        for number in numbers:
            # Remember the starting LCM
            starting_lcm = lcm
            # If the current number does not divide without remainder
            while lcm % number != 0:
                # Count by the starting LCM until the current number divides without a remainder
                lcm = lcm + starting_lcm

    return lcm
