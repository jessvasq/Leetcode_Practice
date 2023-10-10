
'''----------------------------------------------------------------------------------ARRAY / STRINGS --------------------------------------------------------------------------------------------'''
'''345. Reverse Vowels of a String'''
'''Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.'''


# s="hello"


# def reverse_vowel(s):
#     vowels = 'aeiouAEIOU'
#     s=list(s) #convert to a list to make it mutable 
#     left, right = 0, len(s)-1
    
#     while left < right:
#         #check if there's a vowel on the left side
#         while left < right and s[left] not in vowels:
#             left += 1
            
#         #check if there's a vowel on the right side
#         while left < right and s[right] not in vowels:
#             right -= 1
            
#         #if we find a vowel 
#         if left < right:
#             #swap vowels 
#             s[left], s[right] = s[right], s[left]
#             left += 1
#             right -= 1   
            
#     return ''.join(s)

# print(reverse_vowel(s))


'''1768. Merge Strings Alternately'''
'''You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.Return the merged string.'''

# def merge_alternately(word1, word2):
#     lo = 0
#     lo2 = 0
#     hi = len(word1)
#     hi2 = len(word2)
#     merged_word = ''
    
#     while lo < hi and lo2<hi2:
#         merged_word += word1[lo] + word2[lo2]
#         lo += 1
#         lo2 += 1
        
#     if lo < hi:
#         merged_word += word1[lo:]
        
#     if lo2 < hi2:
#         merged_word += word2[lo2:]
    
#     return merged_word
    
# word1 = 'abc'
# word2 = 'pqrdf'
# print(len(word1)-1)
# print(merge_alternately(word1, word2))



'''1431. Kids with the greates number of candies '''
'''There are n kids with candies. You are given an integer array candies, where each candies[i] represents the number of candies the ith kid has, and an integer extraCandies, denoting the number of extra candies that you have.
Return a boolean array result of length n, where result[i] is true if, after giving the ith kid all the extraCandies, they will have the greatest number of candies among all the kids, or false otherwise.
Note that multiple kids can have the greatest number of candies.'''

# def kids_with_candies(candies, extra_candies):
#     #Find the max_num in the array
#     max_num_candies = max(candies)
#     #iterate through the list 
#     for num in range(len(candies)):
#         #check if current kid with candies + extra candies is greater or equal to max_num candies
#         if candies[num] + extra_candies >= max_num_candies:
#             #if yes, return True
#             candies[num] = True
#             #else False
#         else: 
#             candies[num] = False
#     #return list of candies(will return Boolean values)
#     return candies

# candies = [2,3,5,1,3]
# extra_candies = 3

# print(kids_with_candies(candies, extra_candies))

'''151.Reverse Words in a String
Given an input string s, reverse the order of the words.
A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.
Return a string of the words in reverse order concatenated by a single space.
Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.
'''

# s = "the sky is blue"

# def reverseWords(s):
#     s = s.strip()
#     s = s.split()
#     lo=0
#     hi=len(s)-1
    
#     while lo <= hi:
#         s[lo], s[hi] = s[hi], s[lo]
#         lo += 1
#         hi -= 1
#     return(' '.join(s))

'''334. Increasing Triplet Subsequence
Given an integer array nums, return true if there exists a triple of indices (i, j, k) such that i < j < k and nums[i] < nums[j] < nums[k]. If no such indices exists, return false.'''

# nums = [2,1,5,0,4,6]

# def increasing_triplet(nums):
#     #check if the list has at least three values
#     if len(nums) < 3:
#         return False
#     #initialize two variables to keep track of the smallest elements 
#     first_num = float('inf')
#     second_num = float('inf')
    
#     #loop through the list 
#     for num in nums: 
#         if num <= first_num:
#             first_num = num
#         elif num <= second_num:
#             second_num = num 
#         else: 
#             return True 
    
#     return False

# print(increasing_triplet(nums))

'''135. Candy
There are n children standing in a line. Each child is assigned a rating value given in the integer array ratings.
You are giving candies to these children subjected to the following requirements:
Each child must have at least one candy.
Children with a higher rating get more candies than their neighbors.
Return the minimum number of candies you need to have to distribute the candies to the children.
'''

ratings = [1, 2, 2]
# n = len(ratings)
# for rating in range(n-2, -1, -1):
#     print('current', ratings[rating])
#     print('next', ratings[rating+1])

# for rating in range(1, n):
#     print('current', ratings[rating])
#     print('next', ratings[rating-1])
    
# def candy(ratings):
#     n = len(ratings)
#     #initialize an array to start at 1, since all children have at least 1 candy 
#     candies = [1] * n 
#     print(candies)
    
#     #check left to right 
#     for rating in range(1, n):
#         if ratings[rating] > ratings[rating-1]: #check if the current rating is greater than the rating to its left
#             candies[rating] = candies[rating-1] + 1 #ensure that the current child has more than its left neighbor
        
#     #check right to left, backwards loop
#     for rating in range(n-2, -1, -1): #start at second to last, stop at the last index(0)
#         if ratings[rating] > ratings[rating + 1]:
#             candies[rating] = max(candies[rating], candies[rating+1] + 1)
            
#     #find total candies 
#     total_candies = sum(candies)
#     return total_candies 


# print(candy(ratings))


'''-----------------------------------------------HASH MAP / SET --------------------------------------------------------------------------------------------'''
'''1207. Unique Number of Occurrences
Given an array of integers arr, return true if the number of occurrences of each value in the array is unique or false otherwise.'''

arr = [1,2,2,1,1,3]

def uniqueOccurrence(arr):
    occurrence_dict = {}
    unique_count = {}
    
    #count the occurence of each unique value 
    for num in arr:
        occurrence_dict[num] = occurrence_dict.get(num, 0) + 1 #use .get() to retrieve the value associated with the key 'num'. If 'num' is not already a key in the dictionary, it return '0', then increments by 1 
        
    #check if all counts are unique 
    for count in occurrence_dict.values():
        if count in unique_count:
            return False
        unique_count[count] = True
    return True 


print(uniqueOccurrence(arr))

'''2352. Equal Row and Column Pairs - M
Given a 0-indexed n x n integer matrix grid, return the number of pairs (ri, cj) such that row ri and column cj are equal.
A row and column pair is considered equal if they contain the same elements in the same order (i.e., an equal array).'''

# def equal_pairs(grid):
grid = [[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]

def countEqualRowColumnPairs(grid):
    count = 0

    for row in range(len(grid)):
        for column in range(len(grid)):
            if grid[row] == [grid[k][column] for k in range(len(grid))]:
                count += 1
    return count

print(countEqualRowColumnPairs(grid)) 
