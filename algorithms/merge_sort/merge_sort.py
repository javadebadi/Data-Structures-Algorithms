"""Module that implements the Merge Sort Algorithm

In this module, I implement the merge sort algorithm as an exercise.
"""

def merge(left:list, right:list) -> list:
    """Function to merge to lists"""
    n = len(left)
    m = len(right)
    c = [None] * (m + n)
    pl = 0
    pr = 0
    for i in range(m + n):
        if pl < n and pr < m:
            if left[pl] < right[pr]:
                c[i] = left[pl]
                pl += 1
            elif right[pr] < left[pl]:
                c[i] = right[pr]
                pr += 1
            elif right[pr] == left[pl]:
                if pl < n:
                    c[i] = left[pl]
                    pl += 1
                elif pr < m:
                    c[i] = right[pr]
                    pr += 1
        elif pl == n:
            for i in range(n + pr, n + m):
                c[i] = right[i - n]
        elif pr == m:
            for i in range(m + pl, m + n):
                c[i] = left[i - m]
    return c

def merge_sort(array: list) -> list:
    """Function to perform merge list"""
    n = len(array) // 2
    left = array[:n]
    right = array[n:]

    if n > 1:
        return merge(merge_sort(left), merge_sort(right))
    elif n % 2 == 1:
        return merge(
            left,
            merge_sort(right),
        )
    else:
        return merge(left, right)


