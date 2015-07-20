# -*- coding: utf-8 -*-
from MergeSort import MergeSort

__author__ = 'figarrido'

"""
Invertion:
Recibe un arreglo de número desordenados, este arreglo es dividido a la mitad
(mitad izquierda y mitad derecha) y cada parte es ordenada para luego
almacenar los pares (i, j) tal que i pertenece a la mitad izquerda, j pertenece
a la mitad derecha  y que cumplen la condición i > j.

Esta función realiza llamadas recursivas para obtener todos los pares dentro
del arreglo en el que un elemento está ubicado antes de otro de menor valor.

Ejemplo:
A = [5, 6, 3, 2, 1, 4]

Invertion(A) retorna:
[(5, 3),(5, 2),(5, 1),(5, 4),(6, 3),(6, 2),(6, 1),(6, 4),(3, 2),(3, 1),(2, 1)]
"""


def Invertion(A):
    global per
    if len(A) == 1:
        return []

    X = Invertion(A[:len(A) // 2])
    Y = Invertion(A[len(A) // 2:])

    B = MergeSort(A[:len(A) // 2])
    C = MergeSort(A[len(A) // 2:])

    Z = InvertionSplit(B, C)

    return X + Y + Z


def InvertionSplit(P, Q):

    I = []
    i, j = 0, 0

    for k in range(len(P) + len(Q)):
        if not (i < len(P) and j < len(Q)):
            break

        if P[i] < Q[j]:
            for l in I:
                l[1] += [P[i]]

            i += 1

        elif Q[j] < P[i]:
            I += [[Q[j], []]]
            j += 1

    if i < len(P):
        for l in I:
            l[1] += P[i:]

    out = []
    for l in I:
        for m in l[1]:
            out.append((m, l[0]))

    return out
