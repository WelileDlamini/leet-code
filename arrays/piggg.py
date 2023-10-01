def convert_to_pig_latin(word):
    word = word.lower()
    vowels = "aeiou"
    
    # Check if the first letter is a vowel
    if word[0] in vowels:
        return word + "way"
        
    else:
        # Find the first vowel in the word
        for index, letter in enumerate(word):
            if letter in vowels:
                return word[index:] + word[:index] + "ay"
                
    # If the word has no vowels
    return word + "ay"

word = input("Enter a word: ")
print("Pig Latin: " + convert_to_pig_latin(word))