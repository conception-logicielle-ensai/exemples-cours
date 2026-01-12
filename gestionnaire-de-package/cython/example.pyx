# example.pyx

def add(int a, int b):
    """
    Addition rapide en Cython
    """
    return a + b


def sum_array(int[:] arr):
    """
    Somme des éléments d'un tableau
    """
    cdef int total = 0
    cdef int i

    for i in range(arr.shape[0]):
        total += arr[i]

    return total
