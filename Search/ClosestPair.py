# -*- coding: utf-8 -*-
from ..Sort import MergeSort
__author__ = 'figarrido'

"""
ClosestPair_:
Recibe una lista de puntos en un plano (tuplas tamaño 2), la misma lista
ordenada según su primera coordenada (Ax) y misma lista ordenada por su
segunda coordenada (Ay). Se toman la parte izquierda y derecha del arreglo
(Q y R, respectivamente) para luego tener ambas partes ordenadas según su
primera coordenada y segunda coordenada (Qx, Qy, Rx y Ry) y verificar los
pares más cercanos dentro de la primera mitad y segunda mitad.
Se considera la distancia mínima (delta) entre los puntos retornados por las
mitades. Se obtiene el valor de la primera coordenada (xBar) del último
elemento de Ax. Se crea un nuevo arreglo (Sy) que posee a los puntos que su
primera coordenada está entre los valores xBar - delta y xBar + delta, y estos
elementos están ordenados por su segunda coordenada. Luego cada elemento es
comparado con los siguientes 7 elementos en la lista y así encontrar el
par de puntos más cercanos.

Ejemplo:
A = [(4, 3), (6, 4), (2, 6), (8, 7), (1, 2), (3, 8), (5, 1), (7, 5)]

ClosestPair(A) retorna:
((6, 4), (7, 5))
"""


def ClosestPair(A):
    Ax = MergeSort(A, lambda x: x[0])
    Ay = MergeSort(A, lambda x: x[1])
    return ClosestPair_(A, Ax, Ay)


def ClosestPair_(A, Ax, Ay):
    n = len(A)

    if n <= 1:
        return ((0, 0), (10000000000, 10000000000))

    Q = A[:n // 2]
    R = A[n // 2:]

    Qx = MergeSort(Q, lambda x: x[0])
    Qy = MergeSort(Q, lambda x: x[1])

    Rx = MergeSort(R, lambda x: x[0])
    Ry = MergeSort(R, lambda x: x[1])

    p1, q1 = ClosestPair_(Q, Qx, Qy)
    p2, q2 = ClosestPair_(R, Rx, Ry)

    delta = min(distance(p1, q1), distance(p2, q2))

    p3, q3 = ClosestSplitPair(A, Ax, Ay, delta)

    if distance(p1, q1) < distance(p2, q2) and \
            distance(p1, q1) < distance(p3, q3):
        return p1, q1

    if distance(p2, q2) < distance(p1, q1) and \
            distance(p2, q2) < distance(p3, q3):
        return p2, q2

    if distance(p3, q3) < distance(p2, q2) and \
            distance(p3, q3) < distance(p1, q1):
        return p3, q3
    print(p1, q1, p2, q2, p3, q3)


def ClosestSplitPair(P, Px, Py, delta):
    n = len(P)
    xBar = Px[n // 2 - 1][0]
    Sy = []
    for t in Py:
        if t[0] < xBar + delta or t[0] > xBar - delta:
            Sy += [t]

    best = delta
    bestPair = ((0, 0), (10000000000, 10000000000))

    for i in range(n):
        for j in range(i + 1, min(i + 7, n)):
            if distance(Sy[i], Sy[j]) < best:
                bestPair = (Sy[i], Sy[j])

    return bestPair


def distance(d_i, d_j):
    return ((d_i[0] - d_j[0]) ** 2 + (d_i[1] - d_j[1]) ** 2) ** (0.5)
