def piglatin(word):
    if word[0] not in 'aeiou':

        first_vowel = ""

        for letter in word:

            if letter in 'aeiou':
                first_vowel = letter

                break


        
        index_of_first_vowel = word.find(first_vowel)

        letter_before_first_vowel = word[:index_of_first_vowel]
        