# -*- coding: utf-8 -*-
from random import randint

__author__ = 'figarrido'

"""
QuickSort:
Recibe un arreglo de número en desorden, del que se elige un elemento (pivote)
al azar, se intercambia el pivote con el primer elemento del arreglo, luego se
ordenan los elementos del arreglo quedando inmediatamente después del pivote
todos los elementos menores al pivote y luego los elementos mayores a este,
manteniendo la referencia de donde está la separación de los elementos mayores
y menores al pivote para intercambiar el último número de los elementos menores
al pivote con el pivote. Luego se retorna el arreglo que tiene a los elementos
menores y mayores ordenados por el mismo algoritmo con el elemento pivote en
medio.

Ejemplo:
A = [3, 2, 5, 7, 1, 8, 6, 4]

QuickSort retorna:
[1, 2, 3, 4, 5, 6, 7, 8]
"""


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
    A[0], A[j - 1] = A[j - 1], A[0]

    return QuickSort(A[0:j - 1]) + [A[j - 1]] + QuickSort(A[j:])
