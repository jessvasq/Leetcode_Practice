
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



'''1431. Kids with the greates number of candies '''
'''There are n kids with candies. You are given an integer array candies, where each candies[i] represents the number of candies the ith kid has, and an integer extraCandies, denoting the number of extra candies that you have.
Return a boolean array result of length n, where result[i] is true if, after giving the ith kid all the extraCandies, they will have the greatest number of candies among all the kids, or false otherwise.
Note that multiple kids can have the greatest number of candies.'''

def kids_with_candies(candies, extra_candies):
    #Find the max_num in the array
    max_num_candies = max(candies)
    #iterate through the list 
    for num in range(len(candies)):
        #check if current kid with candies + extra candies is greater or equal to max_num candies
        if candies[num] + extra_candies >= max_num_candies:
            #if yes, return True
            candies[num] = True
            #else False
        else: 
            candies[num] = False
    #return list of candies(will return Boolean values)
    return candies

candies = [2,3,5,1,3]
extra_candies = 3

print(kids_with_candies(candies, extra_candies))