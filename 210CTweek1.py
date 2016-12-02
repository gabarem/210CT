import random

def numbershuf(list1):                                
    for x in list1:                                   #N    
      p1 = list1.index(x)                             #N
      p2 = random.randint(0, len(list1)-1)            #N
      print("Old Position of Element = " + str(p1))   #N
      print("New Poistion of Element = " + str(p2))   #N
      list1[p1], list1[p2] = list1[p2], list1[p1]     #N
      print("Current state of the Element: ")         #N
      print(list1)                                    #N
      print("")                                       #N
    return(list1)
    
print (numbershuf([5,3,8,9,1,9,2,7]))


# Big O for this piece of code is O(N)
