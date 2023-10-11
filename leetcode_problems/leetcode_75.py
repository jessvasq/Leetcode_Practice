
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
'''1207. Unique Number of Occurrences - E
Given an array of integers arr, return true if the number of occurrences of each value in the array is unique or false otherwise.'''

# arr = [1,2,2,1,1,3]

# def uniqueOccurrence(arr):
#     occurrence_dict = {}
#     unique_count = {}
    
#     #count the occurence of each unique value 
#     for num in arr:
#         occurrence_dict[num] = occurrence_dict.get(num, 0) + 1 #use .get() to retrieve the value associated with the key 'num'. If 'num' is not already a key in the dictionary, it return '0', then increments by 1 
        
#     #check if all counts are unique 
#     for count in occurrence_dict.values():
#         if count in unique_count:
#             return False
#         unique_count[count] = True
#     return True 


# print(uniqueOccurrence(arr))

'''2352. Equal Row and Column Pairs - M
Given a 0-indexed n x n integer matrix grid, return the number of pairs (ri, cj) such that row ri and column cj are equal.
A row and column pair is considered equal if they contain the same elements in the same order (i.e., an equal array).'''

# def equal_pairs(grid):
# grid = [[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]

# def countEqualRowColumnPairs(grid):
#     count = 0

#     for row in range(len(grid)):
#         for column in range(len(grid)):
#             if grid[row] == [grid[k][column] for k in range(len(grid))]:
#                 count += 1
#     return count

# print(countEqualRowColumnPairs(grid)) 


'''49. Group Anagrams - M
Given an array of strings strs, group the anagrams together. You can return the answer in any order.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.'''

# strs = ["eat","tea","tan","ate","nat","bat"]
# def group_anagrams(strs):
#     anagrams = {}

#     for word in strs:
#         #sort the word to create a key to be added to the dict
#         sorted_word = ''.join(sorted(word))
#            #create a new list if the key is not in the dict
#         if sorted_word not in anagrams:
#             anagrams[sorted_word] = [word]
#         else:
#             #append the word to the list of anagrams 
#             anagrams[sorted_word].append(word)
#             print('dict', anagrams)
            
#     #convert the values into a list   
#     return list(anagrams.values())

# print(group_anagrams(strs))


'''----------------------------------------------- QUEUES/STACKS--------------------------------------------------------------------------------------------'''

'''933. Number of Recent Calls - E

You have a RecentCounter class which counts the number of recent requests within a certain time frame.
Implement the RecentCounter class:
RecentCounter() Initializes the counter with zero recent requests.
int ping(int t) Adds a new request at time t, where t represents some time in milliseconds, and returns the number of requests that has happened in the past 3000 milliseconds (including the new request). Specifically, return the number of requests that have happened in the inclusive range [t - 3000, t].
It is guaranteed that every call to ping uses a strictly larger value of t than the previous call.'''

# from collections import deque

# class RecentCounter:
#     def __init__(self):
#         #initialize an empty double ended queue, allow quicker pop and append operations 
#         self.requests = deque()

#     def ping(self, t):
#         # Remove requests that are older than 3000 milliseconds
#         while self.requests and self.requests[0] < t - 3000:
#             #pop elements from the left side[0] until we find the request within 3000 
#             self.requests.popleft()

#         # Add the current request at time 't'
#         self.requests.append(t)

#         # Return the lenght of the deque, which return the number of requests within the past 3000 milliseconds
#         return len(self.requests)

# counter = RecentCounter()
# print(counter.ping(1))  # Output: 1
# print(counter.ping(100))  # Output: 2
# print(counter.ping(3001))  # Output: 3
# print(counter.ping(3002))  # Output: 3


'''394. Decode String - M 
Given an encoded string, return its decoded string.
The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.
You may assume that the input string is always valid; there are no extra white spaces, square brackets are well-formed, etc. Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there will not be input like 3a or 2[4].
The test cases are generated so that the length of the output will never exceed 105.'''

# s = "3[a]2[bc]"

# def decoded_string(s):
#     stack = []
#     current_num = 0
#     current_str = ""

#     #iterate through each character in the string
#     for char in s:
#         #check if char is a digit 
#         if char.isdigit():
#             current_num = current_num * 10 + int(char) #if it is update to current_num 
#         elif char == "[":
#             #push/append current_str and num to the stack 
#             stack.append(current_str)
#             stack.append(current_num)
#             #reset to its original value
#             current_str = ""
#             current_num = 0
#         elif char == "]":
#             num = stack.pop()
#             prev_str = stack.pop()
#             #update the string by multiplying previous string 'num' times
#             current_str = prev_str + num * current_str
#         else:
#             #append all other chars
#             current_str += char

#     return current_str

# print(decoded_string(s))  # Output: "accaccacc"

'''----------------------------------------------- BINARY TREE-DFS/BFS--------------------------------------------------------------------------------------------'''
'''1161. Maximum Level Sum of a Binary Tree
Given the root of a binary tree, the level of its root is 1, the level of its children is 2, and so on.
Return the smallest level x such that the sum of all the values of nodes at level x is maximal.
'''

from collections import deque

class TreeNode():
    def __init__(self, val=0, left=None, right=None):
        self.val = val 
        self.left = left
        self.right = right 


def maxLevelSum(root):
    #check if the tree is empty 
        if not root:
            return 0
        
        #track the level with the max sum of node values and the max sum so far 
        max_level = 1
        max_sum = float('-inf')
        level=1 #start at level 1 which is the current level being processed 
        q=[root] #list containing the root 
        
        while q: 
            level_sum = 0 #store the sum at each level 
            next_level = [] #store the nodes at next level
            
            for node in q: 
                level_sum += node.val
                #check if there are any children and append them to the list 
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
                
            if level_sum > max_sum: #if this condition is true, update max_sum and max_level accordingly
                max_sum = level_sum
                max_level = level
                
            #update q & level to next level for the next iteration
            q = next_level 
            level += 1
  
        return max_level
    
root = TreeNode(1)
root.left = TreeNode(7)
root.right = TreeNode(0)
root.left.right = TreeNode(-8)
root.left.left = TreeNode(7)

print(maxLevelSum(root))
            

    
    
'''102. Binary Tree Level Order Traversal
Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).
'''

#traverse through every level from left to right- BFS 
# from collections import deque 


def level_order(root):
    res = []
    q = deque()
    q.append(root)
    
    if root is None:
        return 
    
    while q: #run loop while q is not empty, as long as there are levels to process
        level = []
        for i in range(len(q)):
            node = q.popleft()
            if node != None: 
                level.append(node.val)                
                q.append(node.left)
                q.append(node.right)
                
        if level:
            res.append(level)
            
    return res

print(level_order(root))

'''700. Search in a Binary Search Tree
You are given the root of a binary search tree (BST) and an integer val.
Find the node in the BST that the node's value equals val and return the subtree rooted with that node. If such a node does not exist, return null.
'''
class TreeNode():
    def __init__(self, val=0, left=None, right=None):
        self.val = val 
        self.left = left
        self.right = right 
        
def searchBST(root, val):
    if root is None: 
        return 
    
    while root:
        if root.val == val:
            return root
        if val < root.val:
            return searchBST(root.left, val)
        else:
            return searchBST(root.right, val)


root = TreeNode(1)
root.left = TreeNode(7)
root.right = TreeNode(2)
root.left.right = TreeNode(-8)
root.left.left = TreeNode(7)

val=2
print(searchBST(root, val))    


'''450. Delete Node in a BST - M 
Given a root node reference of a BST and a key, delete the node with the given key in the BST. Return the root node reference (possibly updated) of the BST.
Basically, the deletion can be divided into two stages:
Search for a node to remove.
If the node is found, delete the node.'''

#we need to handle three cases for the node to be deleted
# a. If the node to be deleted has no children (a leaf node), you can simply remove it.
# b. If the node to be deleted has one child, you can replace the node with its child.
# c. If the node to be deleted has two children, you need to find the node's in-order 

def deleteNode(root, key):
    #base case
    if root is None:
        return 
    
    #search for the node to delete 
    if key < root.val:
        #recursively call the left subtree to search for and delete the key 
        root.left = deleteNode(root.left, key)
    elif key > root.val:
        #recursively call the right subtree to search for and delete the key 
        root.right = deleteNode(root.right, key)
    #DELETES THE NODE 
    # if the node is equal to the value
    else: 
        if root.left is None and root.right is None:
            return None
        #IF THE NODE HAS NO LEFT CHILD 
        if not root.left:
            #return the right child to be the replacement for the deleted node
            return root.right 
        #B. IF THE NODE HAS NO RIGHT CHILD
        elif not root.right:
            #return the left child as the replacement 
            return root.left
        
        #C. IF THE NODE HAS TWO CHILDREN: LEFT & RIGHT
        #find the minimum node value in the right subtree
        current = root.right
        #traverse left in the right subtree until it reaches the min value
        while current.left:
            current = current.left 
        #replace the current node with the min value 'in-order sucessor'
        root.val = current.val
        #call deleteNode recursively on the right subtree to delete the node with the min value
        root.right = deleteNode(root.right, root.val)
    #return the modified 'root', important step to make sure the tree remains connected 
    return root 
        

'''DFS'''
'''104. Maximum Depth of Binary Tree - E
Given the root of a binary tree, return its maximum depth.
A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.'''

#first solution
def maxDepth(root):
    stack = [[root, 1]]
    level = 0
    
    while stack:
        node = stack.pop()
        depth = stack.pop()
        
        if node is not None:
            level = max(level, depth)
            stack.append([node.left, depth + 1])
            stack.append([node.right, depth + 1])
    return level

#second solution using recurssion 

def max_depth(root):
    if root is None:
        return 0 
    
    #recursively find the depth of left and right 
    left_depth = max_depth(root.left)
    right_depth = max_depth(root.right)
    
    return max(left_depth, right_depth) + 1 #find the max number between the right and left subtree, plus 1 (from the root)
