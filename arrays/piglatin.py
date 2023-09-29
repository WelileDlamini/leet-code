def piglatin(word):

    vowels = "aeiouAEIOU"

    if word[0] not in vowels:
        return f"{word[1:]} {word[0]} ay"
    
    
    elif word[0] in vowels:
        return f' {word} way'
    

word = input("enter the word")
print(piglatin(word))

