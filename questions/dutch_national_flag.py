"""Write a program that takes an array A and an index i rnto A,
and rearranges the elements such that all elements less than A[r] (the "pivot")
appear first,
followed by elements equal to the pivot,
followed by elements greater than the pivot.
"""


def dutch_national_flag(A, i):
    pivot = A[i]
    probing_index = 0
    pivot_index = i
    for index in range(len(A)):
        probing_index = index
        if A[probing_index] < pivot:
            pass




assert dutch_national_flag([0,2,2,1,0,1,2], 3) = [0,]