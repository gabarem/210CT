import math

factlist = []


def trailnum():
    number = int(input("What is the number: "))   #N
    num = math.factorial(number)                  #1
    numstr = str(num)                             #1
    factlist = list(numstr)                       #1
    count = 0                                     #1
    for i in reversed(factlist):                  #N
        if i == '0':                              #N
            count += 1                            #N
        elif i != '0':                            #N
            break                                 #N
    print (count)


trailnum()
