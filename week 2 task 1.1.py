def PerfSquare(a):
    if a > 0:
        b = a**(1/2)
        c = b - b%1
    return c**2
