def isPrime(number):
    x = True
    for i in range(2,number):
        if number % i == 0:
            x = False
            
    print(x)

isPrime(135)
