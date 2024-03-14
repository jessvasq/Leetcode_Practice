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

'''141.Linked List Cycle
Given head, the head of a linked list, determine if the linked list has a cycle in it. There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter. Return true if there is a cycle in the linked list. Otherwise, return false.'''

#Linked list has a head, and a tail equal to Null
#A Singly LL is made up of nodes, each node contains data and a pointer 'next' that indicates where the next node is located
# Q: if the linked list has a cycle in it ?
# Return True if there is a cycle, otherwise False 

#This function uses two pointers, slow and fast, to iterate through the linked list. The slow pointer moves one node at a time, while the fast pointer moves two nodes at a time. If the slow and fast pointers are equal, it means there is a cycle in the linked list and the function returns True. If the fast pointer reaches the end of the linked list, it means there is no cycle and the function returns False.
def hasCycle(head):
    #initialize two pointers, slow and fast
    slow = head
    fast = head

    #iterate through the linked list
    while fast and fast.next:
        #update the slow pointer to the next node
        slow = slow.next
        #update the fast pointer to the next next node
        fast = fast.next.next
        #check if the slow and fast pointers are equal
        if slow == fast:
            return True
    return False

'''104. Maximum Depth of Binary Tree
Given the root of a binary tree, return its maximum depth. A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.'''

# Check if the root is None
# Traverse the left subtree and right subtree 
# We can use recursion to traverse both subtrees 
# add 1 at the end to account for the root level 

def maxDepth(root):
    if root is None: 
        return 0 
    
    left_subtree = maxDepth(root.left)
    right_subtree = maxDepth(root.right)
    
    return max(left_subtree, right_subtree) + 1

'''21. Merge Two Sorted Lists
Merge two sorted linked lists and return it as a sorted list. The list should be made by splicing together the nodes of the first two lists. You are given two linked lists: l1 and l2. You need to merge them into a single sorted linked list.'''

# head and tail 
# nodes (data and pointer)

# 1 -> 2 -> 4
# 1 -> 3 -> 4

# def mergeTwoLists(list1, list2):
#     #initialize a dummy node for the merging process
#     dummy_node = ListNode(-1)
#     # Current tracks the current node in the merged list 
#     current = dummy_node
   
#     #Traverse both lists simultaneously 
#     while list1 is not None and list2 is not None:
#         #compare the values of the current node
#         if list1.val < list2.val:
#             # Attach the node to the merged list 
#             current.next = list1
#             # Move to the next node 
#             list1 = list1.next
#         else:
#             current.next = list2
#             #move to the next node
#             list2 = list2.next
#         #Move the pointer in the merged list
#         current = current.next
        
#     # Attach the remaining nodes from l1 and l2 
#     # If we have not reached the tail(null) of the ll
#     if list1 is not None: 
#         current.next = list1
#     else:
#         current.next = list2
        
#     #Return the merged list starting from the dummyNode.next as we don't want to include -1 
#     return dummy_node.next


'''54. Spiral Matrix
Given an MxN matrix, return all elements of the matrix in spiral order'''

matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]

def spiralOrder(matrix):
    #Check if the matrix is empty
    if not matrix:
        return []
    
    rows = len(matrix)
    cols = len(matrix[0])
    # Initialize the top, bottom, left, and right pointers
    top= 0
    # The bottom pointer is equal to the number of rows - 1 because the index starts from 0
    bottom = rows -1
    left = 0
    right = cols -1 
    # initialize the result list 
    result = []
    
    # Iterate through the matrix in a spiral order, while the top pointer is less than or equal to the bottom pointer and the left pointer is less than or equal to the right pointer
    while top <= bottom and left <= right:
        # Iterate through the top row from left to right
        for i in range(left, right + 1):
            # Append the elements to the result list
            # matrix[top][i] is the current element in the top row. Top is the row index and i is the column index
            result.append(matrix[top][i])
        # Move the top pointer to the next row
        top += 1
        
        # Iterate through the right column from top to bottom
        for i in range(top, bottom + 1):
            # Append the elements to the result list
            result.append(matrix[i][right])
        # Move the right pointer to the previous column because we have already iterated through the right column
        right -= 1
        
        # Check if the top pointer is less than or equal to the bottom pointer
        if top <= bottom:
            # Iterate through the bottom row from right to left
            for i in range(right, left - 1, -1):
                # Append the elements to the result list
                result.append(matrix[bottom][i])
            # Move the bottom pointer to the previous row because we have already iterated through the bottom row  
            bottom -= 1
        # Check if the left pointer is less than or equal to the right pointer
        if left <= right:
            # Iterate through the left column from bottom to top
            for i in range(bottom, top-1, 1):
                # Append the elements to the result list
                result.append(matrix[i][left])
            # Move the left pointer to the next column
            left -= 1
    # Return the result list
    return result


#print(spiralOrder(matrix))  

'''20. Valid Parentheses
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid. An input string is valid if:
Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.'''

s = "()[]{}"

def isValid(s):
    stack = []
    #hasmap to store all the characters
    closed_characters = {
        ')' : '(',
        '}' : '{',
        ']' : '['
    }


    for i in s:
        if i in closed_characters:
            if stack and stack[-1] == closed_characters[i]:
                print(closed_characters[i])
                stack.pop()
            else: 
                return False
        else:
            stack.append(i)
        
    return True if not stack else False

#print(isValid(s))

'''71. Simplify Path
Given a string path, which is an absolute path (starting with a slash '/') to a file or directory in a Unix-style file system, convert it to the simplified canonical path.
In a Unix-style file system, a period '.' refers to the current directory, a double period '..' refers to the directory up a level, and any multiple consecutive slashes (i.e. '//') are treated as a single slash '/'. For this problem, any other format of periods such as '...' are treated as file/directory names.'''

path = "/../"

def simplifyPath(path):
    #Initialize a stack to keep track of directories
    stack = []

    #split the path by '/'
    dir = path.split('/')
    
    #iterate through each directory in the path 
    for i in dir:
        # ignore empty string or .
        if i == '' or i == '.':
            continue
        # if we encounter .., pop the last directory from the stack
        elif i == '..':
            if stack:
                stack.pop()
                print('popStack', stack)
             
        # otherwise, append the directory to the stack   
        else:
            stack.append(i)
            print('addStack', stack)
            
    #join the directories in the stack and return the simplified canonical path
    return '/' + '/'.join(stack)

#print(simplifyPath(path))

'''100. Same Tree
Given the roots of two binary trees p and q, write a function to check if they are the same or not. Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.'''

#we need to traverse the binary tree
#we'll check p node's value with q node's value, If these are equal -> True 
#How are we traversing the tree? We can use either a DFS OR BFS 
#We'll use a iterative BFS

class TreeNode:
    def __init__(self, val=0, right=None, left=None):
        self.val = val
        self.right = right
        self.left = left

p = TreeNode(1)
p.left = TreeNode(2)
p.right = TreeNode(3)
        
q = TreeNode(1)    
q.left = TreeNode(2)
q.right = TreeNode(3)



#Optimized Solution
def isSameTree(p, q):
    #initialize a stack containing a tuple, this tuple contains the root nodes of the two binary trees
    stack = [(p,q)]
    
    #iterate through both trees while the stack is not empty 
    while stack:
        #initialize two variables 
        node1, node2 = stack.pop()

        #if both node are None then we'll simply continue 
        if not node1 and not node2:
            continue 
        #If either node is None or if the values are not equal -> False
        if not node1 or not node2 or node1.val != node2.val:
            return False
        #Otherwise, we'll push the nodes (left1, left2) and (right1, right2) onto the stack
        stack.append((node1.left, node2.left))
        stack.append((node1.right, node2.right))
    
    #if the loop continues, then the trees are identical so we return -> True
    return True

        
print(isSameTree(q, p))

'''22. Invert Binary Tree
Given the root of a binary tree, invert the tree, and return its root'''

#Traverse the tree using a BFS, meaning we'll need to start a queue so we can enqueue and deuque nodes 
#Question: is the inversion performed in place, should the tree be modified directly?

from collections import deque

def invertTree(root):
    if root is None: 
        return None
    
    queue = deque([root])
    
    while len(queue) > 0:
        current = queue.popleft()
        
        current.left, current.right = current.right, current.left
        
        if current.left:
            queue.append(current.left)
            
        if current.right:
            queue.append(current.right)
    
    return root

root = TreeNode(4)
root.right = TreeNode(7)
root.left = TreeNode(2)
root.right.right = TreeNode(9)
root.right.left = TreeNode(6)
root.left.right = TreeNode(3)
root.left.left = TreeNode(1)

print(invertTree(root))

    
'''14. Longest Common Prefix
Write a function to find the longest common prefix string amongst an array of strings. If there is no common prefix, return an empty string "".  '''

strs = ["flower", "flow", "flight"]
#Output: 'fl'  

def longestCommonPrefix(strs):
    if len(strs) == 0:
        return ' '

    prefix = strs[0] #O(m) where m is the lenght of strings
    
    for i in range(1, len(strs)): #o(n) where n is the len of the strinf
        while prefix not in strs[i][:len(prefix)]: #o(m)
            prefix = prefix[:-1]
    
    return prefix
            
#Time: O(n X m)  Space: O(m)
print(longestCommonPrefix(strs))

'''392. Is Subsequence
 Given two strings s and t, return true if s is a subsequence of t, or false otherwise.
 A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).'''
    
#Return a booleam 
s = 'acb'
t = 'ahsdc'
#Output: Tru

#Time: O(n log n) where n is the len of the longest string. Space: O(n), as we use additional space to store sorted strings 
def is_subsequence(s,t):
    if len(t) < len(s):
        print('false')

    t = ''.join(sorted(t))
    s = ''.join(sorted(s))

    for i, j in zip(s, t):
        if i != j:
            print("false")
        else: 
            print('true')

#Time: O(len(t)) as we iterate through the len of t. Space: O(1), constant amount of extra space
def is_subsequence1(s, t):
    sub = 0
    for i in range(len(t)):
        if sub <= len(s)-1:
            if s[sub] == t[i]:
                sub += 1
    if sub == len(s):
        print("true")
    

#optimized solution
#Time: O(n) where n is the length of the string. Space: O(1) as we're not using any additional data structure
def is_subsequence2(s,t):
    if not s:
        return True
    if len(s) > len(t):
        return False
    
    s_pointer = 0
    t_pointer = 0
    
    while t_pointer < len(t):
        if s[s_pointer] == t[t_pointer]:
            s_pointer += 1

            if s_pointer == len(s):
                return True
        
        t_pointer += 1
    return False

print(is_subsequence2(s, t))

'''209. Minimum Size Subarray Sum
Given an array of positive integers nums and a positive integer target, return the minimal length of a contiguous subarray [numsl, numsl+1, ..., numsr-1, numsr] of which the sum is greater than or equal to target. If there is no such subarray, return 0 instead.'''

def min_sub_sum(nums, target):
    left = 0
    total = 0
    ans = float('inf')

    for right in range(len(nums)):
        total += nums[right]
        print('total', total)
        while total >= target:
            ans = min(right - left + 1, ans)
            print('ans', ans)
            total -= nums[left]
            print('new total', total)
            left += 1
            
    return 0 if ans == float('inf') else ans

nums = [2,3,1,2,4,3]
target = 7
#print(min_sub_sum(nums, target))

'''128. Longest Consecutive Sequence
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
You must write an algorithm that runs in O(n) time.
'''

nums = [100,4,200,1,3,2]
#output 4
#what to do with repeated numbers? 
#set 

#create a set to store all elements of the array 
num_set = set(nums)
max_length = 0

for num in num_set:
    #check if the predecessor of the current num exists in the set
    if num - 1 not in num_set:
        current_num = num 
        current_length = 1
        
        #count the length of the consecutive sequence starting from current_num 
        while current_num + 1 in num_set:
            current_num += 1
            current_length += 1
        
        #update max length 
        max_length = max(max_length, current_length)
    
print(max_length)

'''67. Add Binary 
Given two binary strings a and b, return their sum as a binary string'''

a = '11' 
b = '1' 

result = []
carry = 0
i = len(a) -1
j = len(b) -1

#iterate over the strings from right to left
while i >= 0 or j >= 0:
    bit_a = int(a[i]) if i >= 0 else 0
    bit_b = int(b[j]) if j >= 0 else 0
    
    #calculate the sum of the bits and the carry
    total = bit_a + bit_b + carry
    
    #Append the sum bit to the result 
    result.append(str(total % 2))
    
    #update the carry for the next iteration 
    carry = total // 2
    
    #move to the next bit
    i -= 1
    j -= 1
    
#if there's a carry, add to the result 
if carry:
    result.append(str(carry))
    
#reverse the result and join to form the binary string
print(''.join(result[::-1]))
    

'''49. Group Anagrams
Given an array of strings strs, group the anagrams together. You can return the answer in any order.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.'''

strs = [""]
#Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

def group_anagrams(strs):
    val_dict = {}
    #iterate through the string, sort and check if the key already exists 
    for word in strs:
        #sort the word and add it as a key to a dictionary 
        value = ''.join(sorted(word))
        #if the key has not beend added, add it to the dictionary
        #else, create a new key 
        val_dict[value] = val_dict.get(value, [])
        
        if value in val_dict.keys():
            val_dict[value].append(word)
    #return the dictionary's values, which should return a list of all the anagrams grouped together
    return val_dict.values()
 
print(group_anagrams(strs))   

'''STACKS'''

'''155. Min Stack - Medium

Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the MinStack class:
MinStack() initializes the stack object.
void push(int val) pushes the element val onto the stack.
void pop() removes the element on the top of the stack.
int top() gets the top element of the stack.
int getMin() retrieves the minimum element in the stack.
You must implement a solution with O(1) time complexity for each function.'''

# A stack uses a LIFO approach, we can insert, pop, peek
# Similar to a list, we can use append/pop to remove the last added element

class MinStack:
    def __init__(self):
        self.stack = []
        #initialize a min_stack to achieve constant time complexity for the get_min operation
        self.min_stack = []
        
    def push(self, val):
        self.stack.append(val)
        #when a new element is pushed onto the stack, check if the min_stack is empty or if it's less or equal to the current mininum element(last item). If so, push it onto the min_stack
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)
      
    def pop(self):
        #check if the stack is not empty
        if self.stack:
            #check if the last item in the stack is equal to the last item in min_stack, if these are equal. Remove value from both stacks
            if self.stack[-1] == self.min_stack[-1]:
                self.min_stack.pop()
            self.stack.pop()
        
    def top(self):
        #check if the stack is not empty
        if self.stack:
            #return the last item added to the stack which is the top element. (LIFO)
            return self.stack[-1]
    
    def get_min(self):
        #check if the min_stack is not empty 
        if self.min_stack:
            #return the last element added, we always have access to the min element whenever we push/pop an element 
            return self.min_stack[-1]


'''200. Number of Islands - Medium

Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.
An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.'''

#An island is a 1 or multiple 1s surrounded by 0s

grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
#output: 3

#Time complexity: O(rows * colums). Space complexity: O(rows * colums)

def islandCount(grid):
    #find the size of the grid 
    rows = len(grid)
    cols = len(grid[0])

    #initialize a set to keep track of visited cells
    visited = set()
    #initialize a variable 'count' to keep track of the number of islands 
    count = 0
    #inner loop to ierate through the grid 
    for row in range(rows):
        for col in range(cols):
            #calls the explore function to explore neighboring cells and determines if it's part of an insland
            if explore(grid, row, col, visited):
                #if it is, increment the island count
                count += 1
    return count
            
#row and col are the coordinates of the current cell being explored
def explore(grid, row, col, visited):
    #check if the current cell is out of bounds
    rowInbounds = 0 <= row and row < len(grid)
    colInbounds = 0 <= col and col < len(grid[0])
    
    #if the cell is out of bounds, return False
    if not rowInbounds or not colInbounds:
        return False
    
    #if the cell contains '0', return False as it indicates that this cell is not part of the island
    if grid[row][col] == '0':
        return False

    #we add a comma to get our current position and check if we've already visited it
    current = str(row) + ',' + str(col)
    if current in visited:
        return False
        
    #Otherwise, mark the current cell as visited by adding its coordinates
    else:
        visited.add(current)
        
    #Recursive Depth-first traversal, explore neighboring cells(up, down, left, right) by calling itself with updated coordinates
    explore(grid, row-1, col, visited)
    explore(grid, row+1, col, visited)  
    explore(grid, row, col-1, visited) 
    explore(grid, row, col+1, visited)
    
    #return True to indicate that the current cell is part of an island
    return True

print(islandCount(grid))