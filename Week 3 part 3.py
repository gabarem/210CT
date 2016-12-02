def removeVowels(word):

    vowels = ['a','e','i','o','u']
    
    for i in word:
        if i in vowels:
            word = word.replace(i, "")
    print('word: ',word)
        
        

removeVowels('beautiful')
