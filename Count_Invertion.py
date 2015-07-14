from MergeSort import MergeSort

__author__ = 'figarrido'


def Invertion(A):
    global per
    if len(A) == 1:
        return 0

    X = Invertion(A[:len(A) // 2])
    Y = Invertion(A[len(A) // 2:])

    B = MergeSort(A[:len(A) // 2])
    C = MergeSort(A[len(A) // 2:])

    Z = InvertionSplit(B, C)

    return X + Y + Z


def InvertionSplit(P, Q):

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
