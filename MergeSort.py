__author__ = 'figarrido'


def MergeSort(A):
    if len(A) == 1:
        return A

    out = [None for _ in A]
    B = MergeSort(A[:len(A) // 2])
    C = MergeSort(A[len(A) // 2:])

    i, j = 0, 0
    for k in range(len(out)):
        if not (i < len(B) and j < len(C)):
            break

        if B[i] < C[j]:
            out[k] = B[i]
            i += 1

        elif C[j] < B[i]:
            out[k] = C[j]
            j += 1

    if i < len(B):
        out[i - len(B):] = B[i:]

    if j < len(C):
        out[j - len(C):] = C[j:]

    return out
