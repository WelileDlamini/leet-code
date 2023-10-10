def convert_to_pig_latin(word):
    word = word.lower()
    vowels = "aeiou"
    
    
    if word[0] in vowels:
        return word + "way"
        
    else:
       
        for index, letter in enumerate(word):
            if letter in vowels:
                return word[index:] + word[:index] + "ay"
                
    
    return word + "ay"

word = input("Enter a word: ")
print("Pig Latin: " + convert_to_pig_latin(word))