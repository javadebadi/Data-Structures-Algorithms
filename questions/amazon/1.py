"""
Determine if the sum of two integers is equal to the given value
​
Given an array of integers and a value,
determine if there are any two integers in the array whose sum is equal to the given value
"""


def are_two_numbers_exist(A, value):
    """Determines whether two number exist such that
    theirs sums be equal to value

    Time complexity = O(n)
    Memory = O(n)
    """
    numbers_to_look = set()  # Time complexity = O(1)
    for index in len(A):  # Time complexity = O(n)
        complement = value - A[index]  # Time complexity = O(1)
        if complement in numbers_to_look:  # Time complexity = O(1)
            return True
        numbers_to_look.add(value - A[index])  # Time complexity = O(1)

    return False

assert are_two_numbers_exist([10, 1, 0, 2, 5], 15) is True