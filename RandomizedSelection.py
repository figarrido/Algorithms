# -*- coding: utf-8 -*-
from random import randint

__author__ = "figarrido"
"""
RSelection:
Dentro de una lista de números desordenados retorna el i-ésimo elemento más
pequeño.

Ejemplo:
A = [10, 32, 25, 18, 40, 63]

RSelection(A, 3) retorna:
25

RSelection(A, 5) retorna:
40
"""


def RSelection(A, i):

    n = len(A)

    if i > n:
        return None

    if n == 1:
        return A[0]

    p = randint(0, n - 1)

    A[p], A[0] = A[0], A[p]

    j = 1

    for k in range(1, n):
        if A[k] < A[0]:
            A[j], A[k] = A[k], A[j]
            j += 1
    A[j - 1], A[0] = A[0], A[j - 1]

    if j == i:
        return A[j - 1]
    elif j > i:
        return RSelection(A[:j - 1], i)
    elif j < i:
        return RSelection(A[j:], i - j)
