from random import randint

__author__ = 'figarrido'


def QuickSort(A):

    n = len(A)

    if n <= 1:
        return A

    p = randint(0, n - 1)
    A[p], A[0] = A[0], A[p]
    j = 1

    for i in range(1, n):
        if A[i] < A[0]:
            A[j], A[i] = A[i], A[j]
            j += 1

    return QuickSort(A[1:j]) + [A[0]] + QuickSort(A[j:])
