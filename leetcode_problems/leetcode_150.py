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

'''125. Valid Palindrome
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.
Given a string s, return true if it is a palindrome, or false otherwise.'''
# s = "A man, a plan, a canal: Panama"

# def valid_palindrome(s):
#     lower_s = ''.join(char.lower() for char in s if char.isalnum())

#     reversed_word = lower_s[::-1]

#     return lower_s == reversed_word
        
# print(valid_palindrome(s))


'''205. Isomorphic Strings
Given two strings s and t, determine if they are isomorphic.
Two strings s and t are isomorphic if the characters in s can be replaced to get t.
All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.'''

# s = "egg"
# t = "add"

# def isomorphic_strings(s, t):
#     #check if the lengths of the strings are equal
#     if len(s) != len(t):
#         return False
    
#     #create two dictionaries to store mappings
#     s_dict = {}
#     t_dict = {}
    
#     #iterate through the strings and check if the characters are mapped to the same character
#     for i in range(len(s)):
#         #check if the character is already mapped
#         if s[i] in s_dict:
#             #if yes, check if the mapping is consistent
#             if s_dict[s[i]] != t[i]:
#                 return False
#         else:
#             #if not, create a new mapping
#             s_dict[s[i]] = t[i]
#             print(s_dict)
        
#         #check if the character is already mapped
#         if t[i] in t_dict:
#             #if yes, check if the mapping is consistent
#             if t_dict[t[i]] != s[i]:
#                 return False
#         else:
#             #if not, create a new mapping
#             t_dict[t[i]] = s[i]
#             print(t_dict)
#     return True

# print(isomorphic_strings(s, t))




'''35. Search Insert Position

Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.
You must write an algorithm with O(log n) runtime complexity.'''

#O(log n) = binary search 

# nums = [1,3,5,6]
# target = 7

# #this solution uses binary search to find the index of the target value. If the target value is not found, the function returns the index where the target value would be if it were inserted in order.
# def search_insert(nums, target):
#     lo=0 
#     hi=len(nums)
#     while lo < hi:
#         #find the middle index
#         mid = (lo+hi) // 2 
#         #find the middle number
#         mid_num = nums[mid]
#         #if the middle number is less than the target, update the lower bound to the middle index + 1
#         if mid_num < target: 
#             #update the lower bound to the middle index + 1
#             lo = mid + 1
#         #if the middle number is greater than the target, update the upper bound to the middle index
#         else:
#             hi = mid
#     #if the target is found, return the middle index
#     return lo

# print(search_insert(nums, target))

'''122. Best Time to Buy and Sell Stock II
You are given an integer array prices where prices[i] is the price of a given stock on the ith day.
On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time. However, you can buy it then immediately sell it on the same day.

Find and return the maximum profit you can achieve.'''

# prices = [7, 6, 4, 3, 1]  #Output=0

# def max_profit(prices):
#     #initialize the profit to 0
#     profit = 0 
#     #Iterate through the numbers and add the difference between the current number and the previous number to the profit
#     for i in range(1, len(prices)):
#         if prices[i] > prices[i-1]:
#             profit += prices[i] - prices[i-1]
    
#     return profit 

# print(max_profit(prices))
    



'''6. ZigZag Conversion
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)'''
# s = 'P   A   H   N A P L S I I G Y   I   R'
# numRows = 3
# #Output: "PAHNAPLSIIGYIR"

# def convert_from_zigzag(s: str, numRows: int) -> str:
#   #base case, check if the number of rows is 1 or greater than the length of the string. If the number of rows is 1, return the string as is. If the number of rows is greater than the length of the string, return the string as is because the string will not form a zigzag pattern.
#     if numRows == 1 or numRows >= len(s):
#         return s

#     #create a list of strings to store the rows
#     rows = [''] * numRows
#     #initialize variables
#     index, step = 0, 1

#   #iterate through the string and add each character to the corresponding row
#     for char in s:
#       #add the character to the current row
#         rows[index] += char
#         #if the index is 0, update the step to 1. If the index is numRows - 1, update the step to -1. We do this to change the direction of the zigzag pattern.
#         if index == 0:
#             step = 1
#         elif index == numRows - 1:
#             step = -1
#         #update the index by the step
#         index += step

#     return ''.join(rows)

# zigzag_pattern = "PAYPALISHIRING"
# num_rows = 3
#print(convert_from_zigzag(zigzag_pattern, num_rows))

'''112. Path Sum
Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.
A leaf is a node with no children.'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

#This function uses recursion to check if the current node is a leaf node, and if the current node value is equal to the targetSum return True. If not, it checks if the left or right subtree has a path sum equal to the targetSum minus the current node value

def has_path_sum(root, targetSum):
    if not root:
        return False
      #check if the current node is a leaf node, and if the current node value is equal to the targetSum return True
    if not root.left and not root.right:
        return targetSum == root.val
    #check if the left or right subtree has a path sum equal to the targetSum minus the current node value  
    return has_path_sum(root.left, targetSum - root.val) or has_path_sum(root.right, targetSum - root.val)
  
root = TreeNode(5, TreeNode(4, TreeNode(11, TreeNode(7), TreeNode(2))), TreeNode(8, TreeNode(13), TreeNode(4, None, TreeNode(1))))
targetSum = 22
print(has_path_sum(root, targetSum))


'''637. Average of Levels in Binary Tree
Given the root of a binary tree, return the average value of the nodes on each level in the form of an array. Answers within 10-5 of the actual answer will be accepted.'''

#This function uses a queue to store the nodes at each level. It iterates through the queue and adds the values of the nodes at each level to a list. It then calculates the average of the values and appends it to the result list.
def average_of_levels(root):
    result = []
    queue = [root]
    while queue:
        #initialize variables
        level_sum = 0
        level_count = 0
        next_level = []
        #iterate through the queue and add the values of the nodes at each level to a list
        for node in queue:
            #update the level_sum and level_count
            level_sum += node.val
            level_count += 1
            #add the left and right nodes to the next_level list
            if node.left:
                next_level.append(node.left)
            if node.right:
                next_level.append(node.right)
        #calculate the average of the values and append it to the result list. We calculate the average as we want to return the average value of the nodes on each level in the form of an array
        result.append(level_sum / level_count)
        #update the queue to the next_level
        queue = next_level
    #return the result list
    return result