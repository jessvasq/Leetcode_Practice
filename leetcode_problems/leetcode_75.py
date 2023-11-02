
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

# from collections import deque

# class TreeNode():
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val 
#         self.left = left
#         self.right = right 


# def maxLevelSum(root):
#     #check if the tree is empty 
#         if not root:
#             return 0
        
#         #track the level with the max sum of node values and the max sum so far 
#         max_level = 1
#         max_sum = float('-inf')
#         level=1 #start at level 1 which is the current level being processed 
#         q=[root] #list containing the root 
        
#         while q: 
#             level_sum = 0 #store the sum at each level 
#             next_level = [] #store the nodes at next level
            
#             for node in q: 
#                 level_sum += node.val
#                 #check if there are any children and append them to the list 
#                 if node.left:
#                     next_level.append(node.left)
#                 if node.right:
#                     next_level.append(node.right)
                
#             if level_sum > max_sum: #if this condition is true, update max_sum and max_level accordingly
#                 max_sum = level_sum
#                 max_level = level
                
#             #update q & level to next level for the next iteration
#             q = next_level 
#             level += 1
  
#         return max_level
    
# root = TreeNode(1)
# root.left = TreeNode(7)
# root.right = TreeNode(0)
# root.left.right = TreeNode(-8)
# root.left.left = TreeNode(7)

# print(maxLevelSum(root))
            

    
    
'''102. Binary Tree Level Order Traversal
Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).
'''

#traverse through every level from left to right- BFS 
# from collections import deque 


# def level_order(root):
#     res = []
#     q = deque()
#     q.append(root)
    
#     if root is None:
#         return 
    
#     while q: #run loop while q is not empty, as long as there are levels to process
#         level = []
#         for i in range(len(q)):
#             node = q.popleft()
#             if node != None: 
#                 level.append(node.val)                
#                 q.append(node.left)
#                 q.append(node.right)
                
#         if level:
#             res.append(level)
            
#     return res

# print(level_order(root))

'''700. Search in a Binary Search Tree
You are given the root of a binary search tree (BST) and an integer val.
Find the node in the BST that the node's value equals val and return the subtree rooted with that node. If such a node does not exist, return null.
'''
# class TreeNode():
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val 
#         self.left = left
#         self.right = right 
        
# def searchBST(root, val):
#     if root is None: 
#         return 
    
#     while root:
#         if root.val == val:
#             return root
#         if val < root.val:
#             return searchBST(root.left, val)
#         else:
#             return searchBST(root.right, val)


# root = TreeNode(1)
# root.left = TreeNode(7)
# root.right = TreeNode(2)
# root.left.right = TreeNode(-8)
# root.left.left = TreeNode(7)

# val=2
# print(searchBST(root, val))    


'''450. Delete Node in a BST - M 
Given a root node reference of a BST and a key, delete the node with the given key in the BST. Return the root node reference (possibly updated) of the BST.
Basically, the deletion can be divided into two stages:
Search for a node to remove.
If the node is found, delete the node.'''

#we need to handle three cases for the node to be deleted
# a. If the node to be deleted has no children (a leaf node), you can simply remove it.
# b. If the node to be deleted has one child, you can replace the node with its child.
# c. If the node to be deleted has two children, you need to find the node's in-order 

# def deleteNode(root, key):
#     #base case
#     if root is None:
#         return 
    
#     #search for the node to delete 
#     if key < root.val:
#         #recursively call the left subtree to search for and delete the key 
#         root.left = deleteNode(root.left, key)
#     elif key > root.val:
#         #recursively call the right subtree to search for and delete the key 
#         root.right = deleteNode(root.right, key)
#     #DELETES THE NODE 
#     # if the node is equal to the value
#     else: 
#         if root.left is None and root.right is None:
#             return None
#         #IF THE NODE HAS NO LEFT CHILD 
#         if not root.left:
#             #return the right child to be the replacement for the deleted node
#             return root.right 
#         #B. IF THE NODE HAS NO RIGHT CHILD
#         elif not root.right:
#             #return the left child as the replacement 
#             return root.left
        
#         #C. IF THE NODE HAS TWO CHILDREN: LEFT & RIGHT
#         #find the minimum node value in the right subtree
#         current = root.right
#         #traverse left in the right subtree until it reaches the min value
#         while current.left:
#             current = current.left 
#         #replace the current node with the min value 'in-order sucessor'
#         root.val = current.val
#         #call deleteNode recursively on the right subtree to delete the node with the min value
#         root.right = deleteNode(root.right, root.val)
#     #return the modified 'root', important step to make sure the tree remains connected 
#     return root 
        

'''DFS'''
'''104. Maximum Depth of Binary Tree - E
Given the root of a binary tree, return its maximum depth.
A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.'''

#first solution
# def maxDepth(root):
#     stack = [[root, 1]]
#     level = 0
    
#     while stack:
#         node = stack.pop()
#         depth = stack.pop()
        
#         if node is not None:
#             level = max(level, depth)
#             stack.append([node.left, depth + 1])
#             stack.append([node.right, depth + 1])
#     return level

# #second solution using recurssion 

# def max_depth(root):
#     if root is None:
#         return 0 
    
#     #recursively find the depth of left and right 
#     left_depth = max_depth(root.left)
#     right_depth = max_depth(root.right)
    
#     return max(left_depth, right_depth) + 1 #find the max number between the right and left subtree, plus 1 (from the root)



'''437. Path Sum III
Given the root of a binary tree and an integer targetSum, return the number of paths where the sum of the values along the path equals targetSum.
The path does not need to start or end at the root or a leaf, but it must go downwards (i.e., traveling only from parent nodes to child nodes).'''

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# #countPaths function, which calls the dfs function and initializes a dictionary with a count of 0 for a prefix sum of 0 (used for the root node).
# def countPaths(root, targetSum):
#     #dfs function recursively calculates the currentSum by adding the value of the current node and checks if (currentSum - targetSum) exists in the dictionary. If yes, we increment by (currentSum - targetSum)
    
#     def dfs(node, current_sum, prefix_sum, targetSum):
#         if not node:
#             return 0

#         current_sum += node.val
#         count = prefix_sum.get(current_sum - targetSum, 0)

#         prefix_sum[current_sum] = prefix_sum.get(current_sum, 0) + 1

#         count += dfs(node.left, current_sum, prefix_sum, targetSum)
#         count += dfs(node.right, current_sum, prefix_sum, targetSum)

#         prefix_sum[current_sum] -= 1
#         if prefix_sum[current_sum] == 0:
#             del prefix_sum[current_sum]

#         return count
#     #initializes a dictionary with a count of 0 for a prefix sum of 0 (used for the root node).
#     prefix_sum = {0: 1}  
#     return dfs(root, 0, prefix_sum, targetSum)

# root = TreeNode(10)
# root.left = TreeNode(5)
# root.right = TreeNode(-3)
# root.left.left = TreeNode(3)
# root.left.right = TreeNode(2)
# root.right.right = TreeNode(11)

# targetSum = 8
# print(countPaths(root, targetSum))

'''162. Find Peak Element'''
'''A peak element is an element that is strictly greater than its neighbors.

Given a 0-indexed integer array nums, find a peak element, and return its index. If the array contains multiple peaks, return the index to any of the peaks.

You may imagine that nums[-1] = nums[n] = -∞. In other words, an element is always considered to be strictly greater than a neighbor that is outside the array.

You must write an algorithm that runs in O(log n) time.''' 

#O(log n) meaning use binary search 

# nums = [1,2,3,1]

# def findPeakElement(nums):
#     lo = 0
#     hi = len(nums)-1

#     while lo < hi: 
#         mid = (lo+hi) // 2
#         mid_num = nums[mid]
        
#         #if the mid num is less than the num on its right, then the peak must be on the right side
#         if mid_num < nums[mid+1]:
#             lo = mid+1
#         #else the peak will be on the left side 
#         else: 
#             hi = mid
#     return lo

# print(findPeakElement(nums))
        

'''1926. Nearest Exit from Entrance in Maze
You are given an m x n matrix maze (0-indexed) with empty cells (represented as '.') and walls (represented as '+'). You are also given the entrance of the maze, where entrance = [entrancerow, entrancecol] denotes the row and column of the cell you are initially standing at.
In one step, you can move one cell up, down, left, or right. You cannot step into a cell with a wall, and you cannot step outside the maze. Your goal is to find the nearest exit from the entrance. An exit is defined as an empty cell that is at the border of the maze. The entrance does not count as an exit.
Return the number of steps in the shortest path from the entrance to the nearest exit, or -1 if no such path exists.'''


# from collections import deque #use this to create a queue for the breadth-first search (BFS).

# def nearestExit(maze, entrance):
#     #Get the number of rows and columns in the maze
#     rows, cols = len(maze), len(maze[0])
#     #create a tuple for each movement: up, down, left, right
#     directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

#     #boundary checks 
#     def is_valid(row, column):
#         #return True if the the current row and current col are within the bounds of the maze
#         return 0 <= row < rows and 0 <= column < cols
#     #Initialize a queue with a starting point at the entrance. The queue contains tuples in the format (row, column, steps). Steps is the number of steps = 0 for the entrance cell
    
#     queue = deque([(entrance[0], entrance[1], 0)])
#     # Mark the entrance as visited by changing its value from '.' to '+'
#     maze[entrance[0]][entrance[1]] = '+'  

#     #loop continues as long as the queue is not empty
#     while queue:
#         #use popleft() to remove the front element from the queue
#         row, column, steps = queue.popleft()

#         #Check if the current row and column is not the entrance and if the're located at one of the borders of the maze
#         if (row != entrance[0] or column != entrance[1]) and (row == 0 or row == rows - 1 or column == 0 or column == cols - 1):
#             #return # steps as it's an exit
#             return steps

#         #calculate the new coordinates by adding the rows and columns direction's to the current row, column
#         for current_row, current_column in directions:
#             new_row = row + current_row
#             new_column = column + current_column

#             #check if the new (row, column): is within the boundaries and is an empty cell
#             if is_valid(new_row, new_column) and maze[new_row][new_column] == '.':
#                 #If True, append a tuple (row, column, steps + 1) to the queue, which moves to the new (row, column) with an increased number of steps
#                 queue.append((new_row, new_column, steps + 1))
#                 # Mark the row and columns as visited by changing its value to "+"
#                 maze[new_row][new_column] = '+'  

#     return -1

# # Example usage:
# maze = [
#     ['+', '+', '.', '+', '+', '+'],
#     ['+', '.', '.', '.', '.', '.'],
#     ['+', '.', '+', '.', '+', '.']
# ]
# entrance = [1, 2]
# result = nearestExit(maze, entrance)
# print(result)  # Output: 1


'''547. Number of Provinces
There are n cities. Some of them are connected, while some are not. If city a is connected directly with city b, and city b is connected directly with city c, then city a is connected indirectly with city c.
A province is a group of directly or indirectly connected cities and no other cities outside of the group.
You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city and the jth city are directly connected, and isConnected[i][j] = 0 otherwise. 
Return the total number of provinces.'''



# def findCircleSum(isConnected):
#     #get the number of cities 
#     n = len(isConnected)
#     #all cities are marked as unvisited or False
#     visited = [False] * n
#     #initialize a variable to keep track of provinces
#     count = 0
    
#     #nested function that performs a depth-first search starting from a given city
#     def dfs(current_city):
#         #mark current current_city as visited = True
#         visited[current_city]=True
        
#         #iterate through all cities from 0 to n. For each neighbor,check if there is a direct connection (value is 1) between the current current_city and the neighbor
#         for neighbor in range(n):
#             # If the neighbor is connected and has not been visited yet, call the dfs function on that neighbor
#             if isConnected[current_city][neighbor] == 1 and not visited[neighbor]:
#                 dfs(neighbor)
#     #loop through all cities       
#     for current_city in range(n):
#         #If the current current_city has not been visited yet, we increment count by 1 
#         if not visited[current_city]:
#             count += 1
#             #start a new province by calling the dfs(current_city) function
#             dfs(current_city)
    
#     return count 


# isConnected = [[1,1,0],[1,1,0],[0,0,1]]
# print(findCircleSum(isConnected))




'''convert a list of lists into a dictionary'''
edges = [['i', 'j'], ['k', 'i'], ['m', 'k'], ['k', 'l'], ['o', 'n']]

# Initialize an empty dictionary
graph_dict = {}

# Populate the dictionary based on the edges
for edge in edges:
    node1, node2 = edge
    if node1 not in graph_dict:
        graph_dict[node1] = [node2]
    else:
        graph_dict[node1].append(node2)

print(graph_dict)



'''841. Keys and Rooms - M

There are n rooms labeled from 0 to n - 1 and all the rooms are locked except for room 0. Your goal is to visit all the rooms. However, you cannot enter a locked room without having its key.

When you visit a room, you may find a set of distinct keys in it. Each key has a number on it, denoting which room it unlocks, and you can take all of them with you to unlock the other rooms.

Given an array rooms where rooms[i] is the set of keys that you can obtain if you visited room i, return true if you can visit all the rooms, or false otherwise.

'''

#rooms are the nodes, keys would be the edges
#If we enter a room, we'll grab the set of keys and use the given key in the nested function to open the next room
#use a boolean to keep track of the rooms we've visited

# def canVisitAllRoomss(rooms):
#     n=len(rooms)
#     visited = [False] * n


#     def dfs(current_room):
#             #mark current current_city as visited = True
#             visited[current_room]=True
            
#             #iterate through all connected rooms and marked them as visited 
#             for key in rooms[current_room]:
#                 if not visited[key]:
#                     #call the dfs function 
#                     dfs(key)
                    
#     #start at room 0, which is unlocked
#     dfs(0)       
#     #return true if all rooms have been visited
#     return all(visited) 

# rooms = [[1,3],[3,0,1],[2],[0]]
# print(canVisitAllRoomss(rooms))

'''724. Find Pivot Index - E
Given an array of integers nums, calculate the pivot index of this array.

The pivot index is the index where the sum of all the numbers strictly to the left of the index is equal to the sum of all the numbers strictly to the index's right.

If the index is on the left edge of the array, then the left sum is 0 because there are no elements to the left. This also applies to the right edge of the array.

Return the leftmost pivot index. If no such index exists, return -1.'''
# nums = [2,1,-1]

# def find_pivot(nums):
#     #calculate the sum of all nums
#     total_sum, left_sum = sum(nums), 0
    
#     for idx in range(len(nums)):        
#     #check if the sum to the left of the index == to the right sum 
#         if left_sum == total_sum - left_sum - nums[idx]:
#             return idx
#         left_sum += nums[idx]
#     return -1
        
        
# print(find_pivot(nums))


'''1732. Find the Highest Altitude - E
There is a biker going on a road trip. The road trip consists of n + 1 points at different altitudes. The biker starts his trip on point 0 with altitude equal 0.
You are given an integer array gain of length n where gain[i] is the net gain in altitude between points i​​​​​​ and i + 1 for all (0 <= i < n). Return the highest altitude of a point.'''

# gain = [-5,1,5,0,-7]  #output=1

# def largestAltitude(gain):
#     altitude, current_alt = [0], 0
    
#     for num in range(len(gain)):
#         current_alt += gain[num]
#         altitude.append(current_alt)
#     return max(altitude)

# print(largestAltitude(gain))

# #second solution
# def largestAltitude(gain):
#     current_alt = 0
#     highest_alt = current_alt
    
#     for num in range(len(gain)):
#         current_alt += gain[num]
#         highest_alt = max(current_alt, highest_alt)
        
#     return highest_alt

# print(largestAltitude(gain))


# '''HEAPS'''

# import heapq

# list = [21, 2, 45, 78, 3, 5]
# #use heapq and heapify to rearrange the elements
# heapq.heapify(list)
# print(list)

# #insert into a heap 
# heapq.heappush(list, 1)
# print(list)

# #remove from a heap. Heappop function will always remove the element at the index position 1.
# heapq.heappop(list)
# print(list)

# #Replacing in a Heap.  Heapreplace always removes the smallest element of the heap and inserts the new incoming element at some place not fixed by any order.
# heapq.heapreplace(list, 50)
# print(list)



'''215. Kth Largest Element in an Array - Medium
Given an integer array nums and an integer k, return the kth largest element in the array.
Note that it is the kth largest element in the sorted order, not the kth distinct element.
Can you solve it without sorting?
'''

# nums = [3,2,1,5,6,4]
# k = 3

# def find_kth(nums, k):
#     #create a max-heap by converting all values in the list to negative 
#     max_heap = [-num for num in nums]
    
#     #heapify list
#     heapq.heapify(max_heap)
    
#     #pop k-1 largest elements from the max-heap using a loop
#     for i in range(k-1):
#         heapq.heappop(max_heap)
    
#     #convert the value back to positive and return its result 
#     return -max_heap[0]
    
# print(find_kth(nums, k))

'''2462. Total Cost to Hire K Workers-Medium

You are given a 0-indexed integer array costs where costs[i] is the cost of hiring the ith worker.

You are also given two integers k and candidates. We want to hire exactly k workers according to the following rules:

You will run k sessions and hire exactly one worker in each session.
In each hiring session, choose the worker with the lowest cost from either the first candidates workers or the last candidates workers. Break the tie by the smallest index.
For example, if costs = [3,2,7,7,1,2] and candidates = 2, then in the first hiring session, we will choose the 4th worker because they have the lowest cost [3,2,7,7,1,2].
In the second hiring session, we will choose 1st worker because they have the same lowest cost as 4th worker but they have the smallest index [3,2,7,7,2]. Please note that the indexing may be changed in the process.
If there are fewer than candidates workers remaining, choose the worker with the lowest cost among them. Break the tie by the smallest index.
A worker can only be chosen once.
Return the total cost to hire exactly k workers.

'''

# costs = [17,12,10,2,7,2,11,20,8]
# candidates = 4
# k=3

        
# import heapq

# def minCostToHireWorkers(costs, k, candidates):
#     # Create a list of pairs (cost, index)
#     workers = [(cost, i) for i, cost in enumerate(costs)]
#     # Sort the workers by cost and index
#     workers.sort(key=lambda x: (x[0], x[1]))

#     total_cost = float('inf')  # Initialize total cost to infinity
#     min_heap = []  # Priority queue to track candidates

#     for worker_cost, worker_index in workers:
#         heapq.heappush(min_heap, -worker_cost)  # Add negative cost to min-heap

#         # If the size of the heap exceeds candidates, remove the worker with the highest cost
#         if len(min_heap) > candidates:
#             heapq.heappop(min_heap)

#         # If the size of the heap is equal to candidates, calculate the total cost
#         if len(min_heap) == candidates:
#             total_cost = min(total_cost, -sum(min_heap))

#     return total_cost

# print(minCostToHireWorkers(costs, k, candidates)) 


#use two priority queues (min-heaps) to keep track of two sets of candidates

# def totalCost(costs, k, candidates):
#     # left_workers stores the first candidates
#     left_workers = costs[:candidates]
#     # Calculate the number of workers to be placed in right_workers
#     right_workers = costs[max(candidates, len(costs) - candidates):]
#     #min-heap to ensure that the workers with the lowest costs are at the top of each heap.
#     heapq.heapify(left_workers)
 
#     heapq.heapify(right_workers)

        
#     total_cost = 0
#     #used to keep track of the workers outside the two queues
#     next_left= candidates
#     next_right = len(costs) - 1 - candidates 

#     #iterate k times, representing the hiring sessions for hiring k workers
#     for _ in range(k): 
#         #check if the right_workers heap is empty or if the cost of the worker at the top of left_workers is less than or equal to the cost of the worker at the top of right_workers. If True, the next worker to be hired comes from left_workers
#         if not right_workers or left_workers and left_workers[0] <= right_workers[0]: 
#             #Add the cost of the worker and remove that worker from the left_workers heap using heappop
#             total_cost += heapq.heappop(left_workers)

#             #check if there are more workers outside the two queues (beyond next_left). If so, push the next worker from the costs list into left_workers. Increment next_left to consider the next worker in the next loop 
#             if next_left <= next_right: 
#                 heapq.heappush(left_workers, costs[next_left])
#                 next_left += 1
#         #if previous condition is not met, next worker will come from the right 
#         else: 
#             #Add the cost of the worker and remove that worker from the right_workers heap using heappop
#             total_cost += heapq.heappop(right_workers)

#             #check if there are more workers outside the two queues (beyond next_right). If so, push the next worker from the costs list into right_workers. Decrement right_left to consider the next worker in the next loop 
#             if next_left <= next_right:  
#                 heapq.heappush(right_workers, costs[next_right])
#                 next_right -= 1
                    
#     return total_cost
    
    
# print(totalCost(costs, k,  candidates))


'''374. Guess Number Higher or Lower - Easy
We are playing the Guess Game. The game is as follows:
I pick a number from 1 to n. You have to guess which number I picked.
Every time you guess wrong, I will tell you whether the number I picked is higher or lower than your guess.
You call a pre-defined API int guess(int num), which returns three possible results:
-1: Your guess is higher than the number I picked (i.e. num > pick).
1: Your guess is lower than the number I picked (i.e. num < pick).
0: your guess is equal to the number I picked (i.e. num == pick).
Return the number that I picked.'''


# def guess_num(n):
#     lo=0
#     hi=n
        
#     while lo <= hi:
#         mid = (lo+hi) //2
#         ans = guess(mid)
            
#         if ans == -1:
#             hi = mid - 1
#         elif ans == 1:
#             lo = mid + 1
#         else:
#             return mid


'''1071. Greatest Common Divisor of Strings - E
For two strings s and t, we say "t divides s" if and only if s = t + ... + t (i.e., t is concatenated with itself one or more times).

Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.'''

str1 = "ABCABC"
str2 = "ABC"

import math
def gcdOfStrings(str1, str2):
    # Find the greatest common divisor of the lengths of str1 and str2. Gives us the length of the potential common divisor.
    gcd_len = math.gcd(len(str1), len(str2))

    # take the first potential greatest divisor, gcd_len characters from str1.
    common_divisor = str1[:gcd_len]
    print(common_divisor)

    # Check if the common divisor repeats to form str1 and str2
    if str1 == common_divisor * (len(str1) // gcd_len) and str2 == common_divisor * (len(str2) // gcd_len):
        return common_divisor
    else:
        return ""

print(gcdOfStrings(str1, str2))
#space complexity = O(1) -- uses constant time regardless of the input size, time complexity=O(N) -- where n is the length of the longer of the two input strings


flowerbed = [1,0,0,0,1]
n = 2
## simple solution, will only pass a few test cases##
# def canPlaceFLowers(flowerbed, n):
#     for i in range(len(flowerbed)):
#         if flowerbed[i] == 0 and flowerbed[i+1] == 0 and flowerbed[i-1] == 0:
#             n -= 1
#     if n == 0:
#         return True
#     else: 
#         return False
    
'''605. Can Place Flowers - E
You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.

Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.'''

#optimized solution, takes into account the first and last pot. Space complexity = O(1), time complexity = O(N)

def canPlaceFLowers(flowerbed, n):
    #if n (number of flowers) is 0, return True
    if n == 0:
        return True 
    
    for i in range(len(flowerbed)):
        #check if the current pot is empty and the previous and next pots are empty
        #i==len(flowerbed)-1 ; check if the current pot is the last pot
        #i==0 ; check if the current pot is the first pot
        if flowerbed[i] == 0 and (i==0 or flowerbed[i-1] == 0) and (i==len(flowerbed)-1 or flowerbed[i+1] == 0):
            #if True, plant a flower in the current pot
            flowerbed[i] = 1
            #reduce the number of flowers to plant by 1
            n -= 1
            
            if n == 0:
                return True
    return False
    
    
'''443. String Compression - E'
Given an array of characters chars, compress it using the following algorithm:

Begin with an empty string s. For each group of consecutive repeating characters in chars:

If the group's length is 1, append the character to s.
Otherwise, append the character followed by the group's length.
The compressed string s should not be returned separately, but instead, be stored in the input character array chars. Note that group lengths that are 10 or longer will be split into multiple characters in chars.

After you are done modifying the input array, return the new length of the array.

You must write an algorithm that uses only constant extra space.'''

#Iterate trough the 'chars' array and keep track of the current track and its count 
#If the current character is different from the previous character, append the current character and its count to the 'chars' array

    
chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]

# def compress(chars):
#     #create a variable to keep track of the current character and its count
#     current_char = chars[0]
#     count = 0

#     #loop through the array 
#     for i in chars: 
#         #if the current character is the same as the previous character, increment the count by 1
#         if i == current_char:
#             count += 1
#         else:
#             #append current character and its count to the 'chars' array
#             s.append(current_char)
#             s.append(count)
#             #update the current character to the current character in the loop
#             current_char = i
#             count = 1
#     #append the last character and its count to the 'chars' array
#     s.append(current_char)
#     #if the count is greater than 1, append the count to the 'chars' array
#     s.append(count)
#     print(s)
#     return len(s)

# print(compress(chars))
   
   
def compress(chars):
    #check if the array is empty
    if not chars:
        return 0

    #create a variable to keep track of the current character and its count
    current_char = chars[0]
    count = 1
    #write_index keeps track of the current index where the next character should be written
    idx = 0

    #loop through the array starting at index 1
    for i in range(1, len(chars)):
        #if the current character is the same as the previous character, increment the count by 1
        if chars[i] == current_char:
            count += 1
        #if the current character is different from the previous character, append the current character and its count to the 'chars' array
        else:
            chars[idx] = current_char
            idx += 1
            #if the count is greater than 1, append the count to the 'chars' array
            if count > 1:
                count_str = str(count)
                #loop through the count_str and append each digit to the 'chars' array
                for digit in count_str:
                    chars[idx] = digit
                    idx += 1
            #update the current character to the current character in the loop
            current_char = chars[i]
            print(current_char)
            #reset the count to 1
            count = 1

    #append the last character and its count to the 'chars' array
    chars[idx] = current_char
    idx += 1
    #if the count is greater than 1, append the count to the 'chars' array
    if count > 1:
        count_str = str(count)
        for digit in count_str:
            chars[idx] = digit
            idx += 1
    
    return idx


print(compress(chars))


'''283. Move Zeroes - E'''
nums = [0,1,0,3,12]

def moveZeroes(nums):
    #initialize a variable to keep track of the current position of the non-zero element
    i = 0
  
    #loop through the array
    for j in range(len(nums)):
        #if there's a non-zero element, swap it with the element at the current position 'i'       
        if nums[j] != 0:
            #since the non-zero are moved to the front, the zero elements are moved to the back
            nums[i], nums[j] = nums[j], nums[i]
            #move 'i' to the next idx position by incrementing it by 1 
            i +=1
    return nums

print(moveZeroes(nums))
        

'''392. Is Subsequence - E
Given two strings s and t, return true if s is a subsequence of t, or false otherwise.
A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).
 '''
 
s='abc'
t="ahbgdc"


def isSubsequence(s, t):
    subsequence=0
    #if the length of s is greater than the length of t, return False
    if len(s) > len(t):
        return False
    #if s is an empty string, return True
    if len(s) == 0:
        return True
    #iterate through the length of t
    for i in range(len(t)):
        #if the current character in s is equal to the current character in t, increment subsequence by 1
        if subsequence <= len(s) - 1:
            if s[subsequence] == t[i]:
                subsequence += 1
    return subsequence == len(s)

print(isSubsequence(s, t))


'''2215. Find the Difference of Two Arrays - E
Given two 0-indexed integer arrays nums1 and nums2, return a list answer of size 2 where:

answer[0] is a list of all distinct integers in nums1 which are not present in nums2.
answer[1] is a list of all distinct integers in nums2 which are not present in nums1.
Note that the integers in the lists may be returned in any order.

 '''

#first solution 
def diff_arras1(nums1, nums2):
        #use sets to remove duplicates
        set1 = set(nums1)
        set2 = set(nums2)

        #create two arrays to store distinct integers
        arr1 = []
        arr2 = []

        #iterate through both sets
        for num in set1:
            if num not in set2:
                arr1.append(num)
        
        for num in set2:
            if num not in set1:
                arr2.append(num)
        #return a tuple
        return (arr1, arr2)

 
#second solution using difference method
def diff_arras(nums1, nums2):
    #we use sets to remove duplicates
    set1 = set(nums1)
    set2 = set(nums2)
    
    #we use the difference method to find the difference between the two sets
    return [list(set1.difference(set2)), list(set2.difference(set1))]

nums1 = [1,2,3,3]
nums2 = [1,1,2,2]
print(diff_arras(nums1, nums2))
print(diff_arras1(nums1, nums2))