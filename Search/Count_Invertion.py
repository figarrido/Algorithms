# -*- coding: utf-8 -*-
from MergeSort import MergeSort

__author__ = 'figarrido'

"""
Count_Invertion:
Recibe un arreglo de número desordenados, este arreglo es dividido a la mitad
(mitad izquierda y mitad derecha) y cada parte es ordenada para luego
contar los pares (i, j) tal que i pertenece a la mitad izquerda, j pertenece
a la mitad derecha  y que cumplen la condición i > j.

Esta función realiza llamadas recursivas para obtener todos los pares dentro
del arreglo en el que un elemento está ubicado antes de otro de menor valor.

Ejemplo:
A = [5, 6, 3, 2, 1, 4]

Invertions:
[(5, 3),(5, 2),(5, 1),(5, 4),(6, 3),(6, 2),(6, 1),(6, 4),(3, 2),(3, 1),(2, 1)]

Count_Invertion(A) retorna:
11
"""


def Count_Invertion(A):
    if len(A) == 1:
        return 0

    X = Count_Invertion(A[:len(A) // 2])
    Y = Count_Invertion(A[len(A) // 2:])

    B = MergeSort(A[:len(A) // 2])
    C = MergeSort(A[len(A) // 2:])

    Z = Count_InvertionSplit(B, C)

    return X + Y + Z


def Count_InvertionSplit(P, Q):

    I = []
    i, j = 0, 0
    n_mayores, n_inv = 0, 0

    for k in range(len(P) + len(Q)):
        if not (i < len(P) and j < len(Q)):
            break

        if P[i] < Q[j]:
            n_inv += n_mayores
            i += 1

        elif Q[j] < P[i]:
            I += [Q[j]]
            j += 1
            n_mayores += 1

    while i < len(P):
        n_inv += n_mayores
        i += 1

    return n_inv
