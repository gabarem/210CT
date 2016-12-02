def PerfSquare(a):
    if a >= 0:
        b = a**(1/2)
        b = b - b%1
        b = (b**2)
    return (b)
