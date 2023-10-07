
'''----------------------------------------------------------------------------------ARRAY / STRINGS --------------------------------------------------------------------------------------------'''
'''345. Reverse Vowels of a String'''
'''Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.'''


s="hello"


def reverse_vowel(s):
    vowels = 'aeiouAEIOU'
    s=list(s) #convert to a list to make it mutable 
    left, right = 0, len(s)-1
    
    while left < right:
        #check if there's a vowel on the left side
        while left < right and s[left] not in vowels:
            left += 1
            
        #check if there's a vowel on the right side
        while left < right and s[right] not in vowels:
            right -= 1
            
        #if we find a vowel 
        if left < right:
            #swap vowels 
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1   
            
    return ''.join(s)

print(reverse_vowel(s))


'''1768. Merge Strings Alternately'''
'''You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.Return the merged string.'''

def merge_alternately(word1, word2):
    lo = 0
    lo2 = 0
    hi = len(word1)
    hi2 = len(word2)
    merged_word = ''
    
    while lo < hi and lo2<hi2:
        merged_word += word1[lo] + word2[lo2]
        lo += 1
        lo2 += 1
        
    if lo < hi:
        merged_word += word1[lo:]
        
    if lo2 < hi2:
        merged_word += word2[lo2:]
    
    return merged_word
    
word1 = 'abc'
word2 = 'pqrdf'
print(len(word1)-1)
print(merge_alternately(word1, word2))