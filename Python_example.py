def primes(x):
    lst = []
    for i in range(2, x):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            lst.append(i)
    
    return lst
