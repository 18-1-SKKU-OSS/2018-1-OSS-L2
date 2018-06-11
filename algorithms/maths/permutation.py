def permutation(n, r):
    # This function calculates nPr
    return factorial(n)/factorial(n-r)

def factorial(n):
    #This function calculates factorial
    fac = 1
    for i in range(1, n+1):
        fac *= i
    return fac
