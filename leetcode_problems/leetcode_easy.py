
# def fizz_buzz(n):
#     if (n%3 == 0) and (n%5 == 0):
#         return 'FizzBuzz'
#     elif n%3 == 0:
#         return 'Fizz'
#     elif n%5 == 0:
#         return 'Buzz'
#     else:
#         return str(n)
    
# print(fizz_buzz(15))

'''412. Fizz Buzz - E
Given an integer n, return a string array answer (1-indexed) where:
answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
answer[i] == "Fizz" if i is divisible by 3.
answer[i] == "Buzz" if i is divisible by 5.
answer[i] == i (as a string) if none of the above conditions are true.'''
    
#Time complexity: O(n) - linear. 
#Space complexity: O(n) because we are creating a list of n elements

# def fizz_buzz(n):
#     #create an empty list to store the answer
#     answer = []
#     #loop through the range of 1 to n+1
#     for i in range(1, n+1):
#         #if i is divisible by 3 and 5, append FizzBuzz to the list
#         if (i%3 == 0) and (i%5 == 0):
#             answer.append('FizzBuzz')
#         #if i is divisible by 3, append Fizz to the list
#         elif i%3 == 0:
#             answer.append('Fizz')
#         elif i%5 == 0:
#             answer.append('Buzz')
#         #else append the number as a string to the list
#         else:
#             answer.append(str(i))
#     return answer

# print(fizz_buzz(15))

'''27. Remove Element - E
Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.

Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the elements which are not equal to val. The remaining elements of nums are not important as well as the size of nums.
Return k.'''
nums = [3,2,2,3]
val = 3

# def remove_element(nums, val):
#     #use two pointers
#     lo = 0
#     hi = len(nums)-1
    
#     #while the low pointer is less than or equal to the high pointer
#     while lo <= hi:
#         #if the value at the low pointer is equal to the value we want to remove (val)
#         if nums[lo] == val:
#             #swap the values at the low and high pointers
#             nums[lo], nums[hi] = nums[hi], nums[lo]
#             #high pointer goes down by 1
#             hi -= 1
#         #if the value at the low pointer is not equal to the value we want to remove (val)
#         else:
#             #low pointer goes up by 1
#             lo += 1
#     #return the low pointer as the length of the array, we return lo because the low pointer is the index of the first element that is not equal to val
#     return int(lo)


# print(remove_element(nums, val))




'''190. Reverse Bits - E
Reverse bits of a given 32 bits unsigned integer.'''
# n = 11111111111111111111111111111101
# def reverse_bits(n):
#     reverse_bits = 0
#     #loop through 32 given bits
#     for i in range(32):
#         #shift the reverse_bits to the left by 1 to make room for the next bit
#         reverse_bits <<= 1
#         print(reverse_bits)
#         #if the last bit of n is 1, then add 1 to reverse_bits
#         if n & 1:
#             reverse_bits += 1
#         #shift n to the right by 1
#         n >>= 1
#     return reverse_bits

# print(reverse_bits(n))

'''
14. Longest Common Prefix - E
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".
'''

# strs = ["flower","flow","flight"]

# def longestCommonPrefix(strs):
#     #if the list is empty, return an empty string
#     if len(strs) == 0:
#         return ''
#     #set the prefix to the first element in the list
#     prefix = strs[0]
#     #loop through the list starting at the second element
#     for i in range(1, len(strs)):
#         #while the prefix is not in the beginning of the element, remove the last character of the prefix
#         while prefix not in strs[i][:len(prefix)]:
#            #remove the last character of the prefix
#             prefix = prefix[:-1]
#     #return the prefix 
#     return prefix

# print(longestCommonPrefix(strs))



'''217. Contains Duplicate - E
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.'''

nums = [1,2,3,1]

#using a set to remove duplicates and comparing the length of the set to the length of the given list

# def contains_duplicate(nums):
#     #create a set from the list of numbers. A set removes duplicates
#     nums_set = set(nums)
#     #if the length of the set is not equal to the length of the list, return True
#     if len(nums_set) != len(nums):
#         return True
#     #else return False
#     else:
#         return False
    
# print(contains_duplicate(nums))

# #using count method
# def contains_duplicate1(nums):
#     for num in nums:
#         x = nums.count(num)
#         if x > 1:
#             return True

# print(contains_duplicate1(nums))

'''28. Find the Index of the First Occurrence in a String - E
Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

'''
# haystack = 'leeto'
# needle = 'leetcode'

# def str_str(haystack, needle):
#     if  needle not in haystack:
#         return -1
#     else:
#         return haystack.index(needle)
    
# print(str_str(haystack, needle))


        
'''136. Single Number - E
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.'''

# nums2 = [4,1,2,1,2]
# #first solution using count method
# def single_number(nums):
#     for num in nums:
#         if nums.count(num) == 1:
#             return num
            
# print(single_number(nums2))    
# #second solution using XOR operation 
# def singleNumber(nums):
#     ans = 0 
#     for num in nums:
        #we use the XOR operator to find the single number. XOring a number with itself is 0. XOring a number with itself results in 0 and the duplicates cancel each other out leaving the single number. The XOR operation returns 1 if the number of inputs is odd and 0 if the number of inputs is even.
        
    # | A | B | A XOR B |
    # |---|---|---------|
    # | 0 | 0 |    0    |
    # | 0 | 1 |    1    |
    # | 1 | 0 |    1    |
    # | 1 | 1 |    0    |


#         ans ^= num 
#     return ans

# print(singleNumber(nums2))

'''94. Binary Tree Inorder Traversal - W
Given the root of a binary tree, return the inorder traversal of its nodes' values.
'''


# class TreeNode:
#     def __init__(self, val, left, right):
#         self.val = val
#         self.left = None
#         self.right = None
        
#     #recursive solution
#     def inorder_traversal(self, root):
#         resrtult = []
#         #check if the root is not None
#         if root:
#             #recursively call the function on the left subtree
#             result += self.inorder_traversal(root.left)
#             #print the value of the root
#             result.append(root.val)
#             #recursively call the function on the right subtree
#             result += self.inorder_traversal(root.right)
            
#     #iterative solution
#     def inorder_traversal1(self, root):
#         #create an empty stack
#         stack = []
#         result = []
#         #while the current node is not None or the stack is not empty
#         while root or stack:
#             #while the root node is not None
#             while root:
#                 #append the root node to the stack
#                 stack.append(root)
#                 #set the root node to the left node
#                 root = root.left
#             #pop the root node from the stack
#             root = stack.pop()
#             #append the root node value to the result list
#             result.append(root.val)
#             #set the root node to the right node
#             root = root.right
#         return result
            

'''108. Convert Sorted Array to Binary Search Tree - E
Given an integer array nums where the elements are sorted in ascending order, convert it to a height-balanced binary search tree.
'''

#select the middle element of the array as the root node
#recursively create the right and left subtrees using the elements on the left and right of the mid element

# nums = [-10,-3,0,5,9]

# def arrToBst(nums):

#     def sortedArrtoBST(nums, start, end):
#         #base case checks if the start is less than the end. If it is continue with the recursion
#         if start <= end:
#             #find the mid 
#             mid = (start + end) // 2
#             #mid element of the array is the root node
#             mid_num = nums[mid]
#             root = TreeNode(mid_num)
            
#             #recursively create the left and right subtree
#             #left subtree is created using the elements on the left of the mid element, mid-1 is the end of the left subtree
#             root.left = sortedArrtoBST(nums, start, mid-1)
#             #right subtree is created using the elements on the right of the mid element, mid+1 is the start of the right subtree
#             root.right = sortedArrtoBST(nums, mid+1, end)
#             #rertun the root node
#             return root
#     #call the helper function and pass in the array, start=0 and end index=len(nums)-1
#     return sortedArrtoBST(nums, 0, len(nums)-1)

# print(arrToBst(nums))

'''33. Search in Rotated Sorted Array'''
'''There is an integer array nums sorted in ascending order (with distinct values).
Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].
Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.
You must write an algorithm with O(log n) runtime complexity.'''

# def search_target(nums, target):
#     lo, hi = 0, len(nums)-1  
      
#     while lo <= hi:
#         mid = (lo + hi) // 2
#         mid_num = nums[mid]
        
#         if mid_num == target: 
#             return mid
            
#         elif mid_num >= nums[lo]:
#             if target >= nums[lo] and target < mid_num:
#                 hi = mid - 1
#             else:
#                 lo = mid + 1
        
#         else:
#             if target > mid_num and target <= nums[hi]:
#                 lo = mid + 1
#             else: 
#                 hi = mid - 1 
#     return -1 


# nums_search = [4,5,6,7,0,1,2]
# target = 3

# print(search_target(nums_search, target))

            


'''66. Plus One - E
You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.
Increment the large integer by one and return the resulting array of digits.'''

        
# nums = [1, 2, 3]

#first solution 
# def plusOne(nums):
#     #loop through the array backwards
#     #-1 is the starting index, -1 is the ending index, -1 is the step
#     for i in range(len(nums)-1, -1, -1):
#         #if the number is 9, set the number to 0
#         if nums[i] == 9:
#             nums[i] = 0
     
#         #if the number is less than 9, add 1 to the number and return the array
#         else:
#             nums[i] += 1
#             return nums
    
#         #if all the numbers are 9, add 1 to the beginning of the array and return the array
#         return [1] + nums 
            
# print(plusOne(nums))


b ='aab'
a='aa'
c = {}

for i in b:
    c[i] = c.get(i, 0) + 1
print(c)

for i in a:
    if i in c:
        c[i] -= 1
        print('t')
    else:
        print('f')
        break

print(c)
   
  
'''
383. Ransom Note - E
Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.'''

def canConstruct(ransomNote, magazine):
    #create a dictionary from the magazine string
    mag_dict = {}
    for i in magazine:
        #if the letter is in the dictionary, add 1 to the value of the letter. .get() method returns the value of the key. If the key does not exist, it returns 0 
        mag_dict[i] = mag_dict.get(i, 0) + 1
    #loop through the ransomNote string
    for i in ransomNote:
        #if the letter is in the magazine dictionary
        if i in mag_dict:
            #subtract 1 from the value of the letter
            mag_dict[i] -= 1
            #if the value of the letter is less than 0, return False
            if mag_dict[i] < 0:
                return False
        #if the letter is not in the magazine dictionary, return False
        else:
            return False
    return True

print(canConstruct(a,b))

'''242. Valid Anagram - E
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

'''

s='anagram'
t='gramana'

def isAnagram(s, t):
    if len(s) != len(t):
        return False
    
    #use dictionaries  
    s_dict = {}
    t_dict = {}
    
    for i in s:
        s_dict[i] = s_dict.get(i,0) + 1
        
    for i in t:
        t_dict[i] = t_dict.get(i, 0) + 1
        
    return t_dict == s_dict
        

print(isAnagram(s,t))

nums = [0,1,2,4,5,7]


'''228. Summary Ranges - E
You are given a sorted unique integer array nums.

A range [a,b] is the set of all integers from a to b (inclusive).

Return the smallest sorted list of ranges that cover all the numbers in the array exactly. That is, each element of nums is covered by exactly one of the ranges, and there is no integer x such that x is in one of the ranges but not in nums.
Each range [a,b] in the list should be output as:'''


def summaryRanges(nums):
    #create an empty list to store the ranges
    ranges = []
    #loop through the nums array
    for i in nums:
        #if the ranges list is empty or the last element of the ranges list is not equal to the current element - 1, append the current element to the ranges list
        if not ranges or ranges[-1][-1] + 1 != i:
            ranges.append([])
        #append the current element to the last element of the ranges list
        ranges[-1][1:] = [i]
    #return the ranges list
    return ['->'.join(map(str, r)) for r in ranges]

print(summaryRanges(nums))