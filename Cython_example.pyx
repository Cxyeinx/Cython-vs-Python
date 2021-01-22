cpdef list primes(int x):
    cpdef list lst = []
    cdef int i
    cdef int j

    for i in range(2, x):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            lst.append(i)

    return lst
