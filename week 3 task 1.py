def reverseString(string):
    newstring = string.split()
    print (newstring)
    counter = len(newstring) -1
    
    while counter != -1:
        print(newstring[counter])
        counter -= 1
reverseString('my name is mir')
