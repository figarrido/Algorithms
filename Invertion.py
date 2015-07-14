from MergeSort import MergeSort

__author__ = 'figarrido'


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
