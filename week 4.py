def binarySearch(alist, Min, Max):
    first = 0
    last = len(alist)-1
    found = False

    while first<=last and not found:
        midpoint = (first + last)//2
        if (alist[midpoint] >= Min) and (alist[midpoint] <= Max):
            found = True
        else:
            if Min < alist[midpoint]:
                last = midpoint-1
            else:
                first = midpoint+1

    return found

Numberlist = [2,3,5,7,9,13]
print(binarySearch(Numberlist, 3,5))
print(binarySearch(Numberlist, 14,20))
