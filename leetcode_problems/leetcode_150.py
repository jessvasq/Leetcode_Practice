'''169. Majority Element'''
# nums = [2,2,1,1,1,2,2]
# print('max', max(nums))

# #use the Boyer-Moore Voting Algorithm. The key idea is to cancel out each occurrence of an element with all the other elements that are different from it. This way, the majority element, if it exists, will eventually stand out.
# def find_majority(nums):
#     x = None
#     count = 0
#     for i in nums:
#         if count == 0:
#             x = i
#         count += 1 if i == x else -1 
#     return x

# print(find_majority(nums))


#find min value to buy a stock
#find max value to sell a stock
# prices = [7,6,4,3,1]

'''121. Best Time to Buy and Sell Stock - E
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

'''

# def maxProfit(prices):
#     #if prices is empty or has only one element
#     if prices is None or len(prices) == 1:
#         return 0
#     #initialize variables 
#     min_price = prices[0]
#     profit = 0
    
#     #iterate through each price 
#     for price in prices:
#         #update the min price to buy 
#         min_price = min(min_price, price)
#         #update the max price 
#         profit = max(profit, price-min_price)    
        
#     return profit
  
# print(maxProfit(prices))


'''80. Remove DUplicates from a sorted array II'''
# nums = [0,0,1,1,1,1,2,3,3]
# #Output: 5, nums = [1,1,2,2,3,_]
    
# #use a pointer to identify if the current element is different from the element two positions back. If so, update the pointer to the current element. We use the pointer to keep track of the length of the array without duplicates.
# def remove_duplicates(nums):
#     #check if the length of the array is less or equal to 2. If so, return len(arr)
#     if len(nums) <= 2:
#         return len(nums) 
#     #initialize a pointer set to 2 
#     pointer = 2
#     #iterate through the array from range 2 to len(arr)
#     for i in range(2, len(nums)):
#         #check if the current index is not equal to pointer -2
#         if nums[i] != nums[pointer-2]:
#             #if so, update the pointer to the current index
#             nums[pointer] = nums[i]
#             #increment the pointer by 1 so that it points to the next index
#             pointer +=1 
#     return pointer
      
# print(remove_duplicates(nums))
     
'''189. Rotate Array - M
Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.'''

# nums = [-1,-100,3,99]
# k = 2
# #first solution using insert and pop. Both insert and pop are O(n) operations.
# def rotate_arr(nums, k):
#     for i in range(k):
#         nums.insert(0, nums[-1])
#         nums.pop(-1)
#     return nums

# print(rotate_arr(nums, k))

# import random, string

# #print list of alphabet letters using string module
# lower = list(string.ascii_lowercase)
# upper = list(string.ascii_uppercase)
# alphabets = list(string.ascii_letters)

# #print list of numbers using range function
# nums = range(0,9)
# chars_list = list(string.ascii_letters) + list(string.digits) + list(string.punctuation) +  list(string.hexdigits) + list(string.octdigits) + list(string.printable) + list(string.ascii_lowercase) + list(string.ascii_uppercase) + list(string.digits)

# #generate random string of length 10
# def generate_random_string(length):
#     random_string = ''
#     for i in range(length):
#         random_string += random.choice(chars_list)
#     return random_string

# print(generate_random_string(12))


'''58. Length of Last Word

Given a string s consisting of words and spaces, return the length of the last word in the string. A word is a maximal 
substring consisting of non-space characters only.'''
 
# s = "   fly me   to   the moon  "

# def last_word_length(s):
#     s1 = s.strip()
#     list_s = s.split()
#     return len(list_s[-1])


'''242. Valid Anagram
Given two strings s and t, return true if t is an anagram of s, and false otherwise.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
'''

# s = 'rat'
# t='car'

# #This solution uses a dictionary to store the frequency of each character in the string. Then, we compare the two dictionaries to see if they are equal.
# def valid_anagram(s, t):
#     if len(t) > len(s):
#         return False
    
#     s_dict = {}
#     for i in s: 
#         s_dict[i] = s_dict.get(i, 0) + 1
#     print(s_dict)
    
#     t_dict = {}
#     for i in t: 
#         t_dict[i] = t_dict.get(i,0) + 1
#     print(t_dict)
        
 
#     return t_dict == s_dict

# print(valid_anagram(s, t))


'''202. Happy Number
Write an algorithm to determine if a number n is happy. A happy number is a number defined by the following process:
Starting with any positive integer, replace the number by the sum of the squares of its digits.
Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy.
Return true if n is a happy number, and false if not.'''

# def happy_number(n):
#     #create a set to store the numbers we have seen
#     seen = set()
#     #iterate through the numbers and add the square of each digit
#     while n != 1 and n not in seen:
#         seen.add(n)
#         #convert the number to a string and iterate through each digit
#         n = sum(int(i)**2 for i in str(n))
#     return n == 1

# print(happy_number(19))


'''290. Word Pattern
Given a pattern and a string s, find if s follows the same pattern.
Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s.
'''
# pattern = 'abba'
# s = 'dog cat cat dog'


# def word_pattern(pattern, s):
#     #split the string 's' into a list of words
#     s_list = s.split()

#     #check if the lengths of pattern and words are equal 
#     if len(pattern) != len(s_list):
#         return False
    
#     #create two dictionaries to store mappings
#     pattern_to_word = {}
#     word_to_pattern = {}
    
#     #iterate over each character in the pattern and its corresponding word
#     for i in range(len(pattern)):
#         current_char = pattern[i]
#         current_word = s_list[i]
        
#         #check if the current pattern character is already mapped
#         if current_char in pattern_to_word:
#             #if yes, check if the mapping is consistent
#             if pattern_to_word[current_char] != current_word:
#                 return False
            
#         else:
#             #if not create a new mapping
#             pattern_to_word[current_char] = current_word
            
#         #check if the current_word is already mapped
#         if current_word in word_to_pattern:
#             if word_to_pattern[current_word] != current_char:
#                 return False
            
#         else:
#             word_to_pattern[current_word] = current_char
            
#     return True

# print(word_pattern(pattern, s))

'''125. Valid Palindrome'''
s = "A man, a plan, a canal: Panama"

def valid_palindrome(s):
    lower_s = ''.join(char.lower() for char in s if char.isalnum())

    reversed_word = lower_s[::-1]

    return lower_s == reversed_word
        
print(valid_palindrome(s))


'''205. Isomorphic Strings
Given two strings s and t, determine if they are isomorphic.
Two strings s and t are isomorphic if the characters in s can be replaced to get t.
All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.'''

s = "egg"
t = "add"

def isomorphic_strings(s, t):
    #check if the lengths of the strings are equal
    if len(s) != len(t):
        return False
    
    #create two dictionaries to store mappings
    s_dict = {}
    t_dict = {}
    
    #iterate through the strings and check if the characters are mapped to the same character
    for i in range(len(s)):
        #check if the character is already mapped
        if s[i] in s_dict:
            #if yes, check if the mapping is consistent
            if s_dict[s[i]] != t[i]:
                return False
        else:
            #if not, create a new mapping
            s_dict[s[i]] = t[i]
            print(s_dict)
        
        #check if the character is already mapped
        if t[i] in t_dict:
            #if yes, check if the mapping is consistent
            if t_dict[t[i]] != s[i]:
                return False
        else:
            #if not, create a new mapping
            t_dict[t[i]] = s[i]
            print(t_dict)
    return True

print(isomorphic_strings(s, t))