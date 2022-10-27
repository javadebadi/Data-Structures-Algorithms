"""
The parity of a binary word is 1 if the number of 1s in the word is odd; otherwise, it is 0.
For example, the parity of 1110 is 1, and the parity of 1010 is 0.
"""



def parity(x):
    """parity function.

    Time Complexity = O(n)
    n: number of bits
    """
    sum_of_1s = 0
    while x:
        sum_of_1s += (x - ((x >> 1) << 1))
        x >>= 1

    return sum_of_1s % 2



def test():
    assert parity(0) == 0
    assert parity(1) == 1
    assert parity(2) == 1
    assert parity(4) == 1
    assert parity(8) == 1
    assert parity(16) == 1
    assert parity(17) == 0


test()
