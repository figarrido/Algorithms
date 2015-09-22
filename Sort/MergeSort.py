# -*- coding: utf-8 -*-
__author__ = 'figarrido'

"""
MergeSort:
Recibe un arreglo de números desordenados y una función que indique según qué
valor se desea ordenar, por defecto es el mismo valor, este los separa en
mitades (mitad izquierda y mitad derecha) ordenando estas con el mismo
algoritmo.
Se crea un arreglo de la misma dimension que el ingresado y se empieza a
completar de inicio a fin con los elementos de los arreglos que están a la
mitad. Se tiene un 'puntero' para cada arreglo que está a la mitad, ambos
comienzan en el primer elemento de cada uno, se verifica cuál es el menor de
estos elementos y este es el que se agrega en el arreglo final y el puntero
del arreglo del que se eligió el elemento se aumenta en una unidad, así
hasta utilizar todos los elementos.

Ejemplo:
A = [2, 5, 3, 1, 6, 4]

MergeSort retorna:
[1, 2, 3, 4, 5, 6]
"""


def MergeSort(A, key=lambda x: x):
    if len(A) == 1:
        return A

    out = [None for _ in A]
    B = MergeSort(A[:len(A) // 2], key)
    C = MergeSort(A[len(A) // 2:], key)

    i, j = 0, 0
    for k in range(len(out)):
        if not (i < len(B) and j < len(C)):
            break

        if key(B[i]) < key(C[j]):
            out[k] = B[i]
            i += 1

        elif key(C[j]) < key(B[i]):
            out[k] = C[j]
            j += 1

    if i < len(B):
        out[i - len(B):] = B[i:]

    if j < len(C):
        out[j - len(C):] = C[j:]

    return out
