#def checkVowel(n):
    #match n:
        #case 'a': return "Vowel alphabet"
        #case 'e': return "Vowel alphabet"
        #case 'i': return "Vowel alphabet"
        #case 'o': return "Vowel alphabet"
        #case 'u': return "Vowel alphabet"
        #case _: return "Consonant alphabet"

#print(checkVowel("a")) # Output: Vowel alphabet
#print(checkVowel("b")) # Output: Consonant alphabet


def checkVowel(n):
    if n in ['a', 'e', 'i', 'o', 'u']:
       return "Vowel alphabet"
    else:
        return "Consonant alphabet"

print(checkVowel("a"))  # Output: Vowel alphabet
print(checkVowel("b"))  # Output: Consonant alphabet