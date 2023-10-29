'''DATA STRUCTURES AND ALGORITHMS IN PYTHON - COURSE NOTES'''

'''LINEAR SEARCH'''
'''Alice has some cards with numbers written on them. She arranges the cards in decreasing order, and lays them out face down in a sequence on a table. She challenges Bob to pick out the card containing a given number by turning over as few cards as possible. Write a dunction to help Bob locate the card. '''


# #Function signature
# def locate_card(cards, query): 
#     pass #a function cannot have an empty body so we're using 'pass' as it doesn't do anything 

#QUESTIONS 
#any limits? Are the numberse positive, negative, integers, decimals? 

#SOLUTION 
cards = [12, 10, 8, 7, 4, 3, 1, 0]
query = 7
output = 3

def locate_card(cards, query):
#1. Create a variable position with the value 0 
    position = 0 
    
#set up a loop for repetition 
    while True: 
#2.Check whether the number at index position in card equals query
        if cards[position] == query: 
            
#3. If it does, position is the answer and can be returned from the function 
            return position
        
#4. If not, increment the value of position by 1, and repeat steps 2 to 5 till we reach the end of the array
        position += 1
         
#5. If the number was not found, return -1 
        if position == len(cards): 
            return -1 
        

# OR # 
def locate_cards(cards,  query):
    position = 0
    while position < len(cards):
        if cards[position] == query:
            return position
        position += 1
    return -1 

#TEST CASES - we can test our function by passing values and check if we get the same answer as the ouput. Represent test cases as dictionaries to make it easier to test once we implement our function. You should create at least 3 test cases 

test = {
    'input': {
        'cards': [12, 10, 8, 7, 4, 3, 1], 
        'query': 7
    }, 
    'output': 3    
}

    
#test 2. Query is in the middle 

tests = [] #lists containing all tests 
tests.append(test)

tests.append({
    'input': {
        'cards': [12, 10, 8, 7, 4, 3, 1, 0], 
        'query': 1
    },
    'output': 6
})

#test 3. Query is in the first element 
tests.append({
    'input': {
        'cards': [4, 2, 1, -1],
        'query': 4
    },
    'output': 0 
}) 

#test 4, Query is in the last element 

tests.append({
    'input': {
        'cards': [3, -1, -8, -13],
        'query': -13
    },
    'output': 3
}) 


#TEST OUR SOLUTION 
#FIRST SOLUTION
result = locate_card(test['input'] ['cards'], test['input']['query'])
print(result) 

# or #

results = locate_card(cards, 7)
print(results)

if result == output:
    print('cards is located at position:', results)
    

for test in tests: 
    print(locate_cards(**test['input']) == test['output'])

#SECOND SOLUTION 
result = locate_cards(test['input'] ['cards'], test['input']['query'])
print(result) 

# or #

results = locate_cards(cards, 7)
print(results)  

if result == output:
    print('cards is located at position:', results)
    

#ALGO'S COMPLEXITY 
#Time complexity of linear search is O(N) and its space complexity is O(1)

'''BINARY SEARCH'''
#Note: We're using the same cards problem
#The best idea would be to pick a random card and use the fact that the list is sorted, to determine whether the target card lies to the left or right. If we pick the middle card, we can reduce the number of additional cards to be tested to half the size of the list. Then we can simply repeat the process with each half. 

#PSEUDECODE
#1. Find the middle element of the list
#2. It it matches the query number, return the middle position as the answe
#3. If it is less than the query number, then search the first half of the list 
#4. If it is greater than the queried number, then search the second half of the list 
#5. If we reach the end of the list, return -1 

#SOLUTION 

def find_card(cards, query):
    lowest, highest = 0, len(cards) - 1 #lowest will have the value 0, meaning it will start at index 0 
                                        #highest will be the last item in the list. We access this element by lenght of cards - 1
    
    #check if there are items in the list 
    while lowest <= highest:
        #remember we're working with indexes, not the actual values meaning that we'll use index starting at 0 plus the last index in the list, we add them and divide them by two to find the middle number
        middle = (lowest + highest) // 2 # we use '//' to get a whole number not decimals or floating numbers
        mid_number = cards[middle]
        
        #test whethe the values are working as expected
        print('lowest:', lowest, ', highest:', highest, ', middle:', middle, ', middle_number:', mid_number)
        
        
        if mid_number == query:
            return middle
        elif mid_number < query:
            highest = middle - 1
        elif mid_number > query:
            lowest = middle + 1
    return -1 


# #TEST SOLUTION 

# result = find_card(test['input'] ['cards'], test['input']['query'])
# print(result) 

# # or #

# results = find_card(cards, 7)
# print(results)  

# if result == output:
#     print('cards is located at position:', results)

#SECOND SOLUTION 

#the test function tells us whether we need to look on the left or right side of the list 
def test_location(cards, query, mid):
    mid_number = cards[mid]
    print('mid:', mid, ',mid_number:', mid_number)
    
    if mid_number == query:
        #check if the index is valid by using (mid-1) >= 0 and if the element before the mid number is less than the query, we need to go left
        if mid-1 >= 0 and cards[mid-1] == query:
            return 'left'
        else:
            return 'found'
    #check if the middle number is less than the query, print left
    elif mid_number < query:
        return 'left'
    #check if the middle number is greater than the query, print right
    else: 
        return 'right'
    
def find_cards(cards, query):
    lowest, highest = 0, len(cards)-1
    
    while lowest <= highest:
        print('lowest:', lowest, ', highest:', highest,)
        middle = (lowest + highest) // 2 
        result = test_location(cards, query, middle)
        
        if result == 'found':
            return middle
        if result == 'left':
            highest = middle -1 
        elif result == 'right':
            lowest = middle + 1
    return -1 

# #TEST SECOND SOLUTION 

# result = find_cards(test['input'] ['cards'], test['input']['query'])
# print(result) 

# # or #

# results = find_cards(cards, 7)
# print(results)  

# if result == output:
#     print('cards is located at position:', results)


#COMPLEXITY 
#count number of iterations in the algo. If we start out with an array of N elements, then each time the size of the array reduces to half (N/2) for the next iteration , until we are left with just one element 

#initial length - N 
#iteration 1 - N/2 
#iteration 1 - N/4
#iteration 1 - N/8 
# #iteration 1 - N/16 
#...
#iteration - N/2^k 

#since the final length of the array is 1, we can find the N/2^k = 1 
#Rearranging the terms, we get
#N = 2^k
#Taking the logarithm 
#k = logN 

#where log refers to the log to the base of 2. Therefore, our algo has the time complexity O(log N)
#The space complexity of binary search is 0(1)

'''GENERIC BINARY SEARCH '''

def binary_search(low, high, condition): #it takes a low, high, and condition
    while low <= high:  
        middle = (low + high) // 2 
        result = condition(middle)
        if result == 'found': 
            return middle
        elif result == 'left':
            high = middle - 1
        else: 
            low = middle + 1
    return -1 


#using the algo 

def get_card(cards, query):
    
    def condition(mid): 
        if cards[mid] == query: 
            #we check if the mid is within the list 
            if mid>0 and cards[mid-1] == query:
                return "left"
            else: 
                return 'found'
        elif cards[mid] < query:
            return 'left'
        else: 
            return 'right'
                        #low  #high    #condition function
    return binary_search(0, len(cards)-1, condition)

#TEST

results = get_card(cards, 7)
print(results)

if result == output:
    print('cards is located at position:', results)
    

for test in tests: 
    print(get_card(**test['input']) == test['output'])


# '''BINARY SEARCH vs. LINEAR SEARCH'''

# #TEST large lists 
# # large_test = {
# #     'input': {
# #         "cards": list(range(100000000, 0, -1)), #we're creating a decreasing list by using range() starting at 10000000 and ending at 1 
# #         "query": 2
# #         }, 
# #     'output': 999998
# # }

# #The binary search is over 55,000 times faster than the linear search version 
# #As the size of the input grows larger, the difference only gets bigger. 


# '''SECOND QUESTION. #34 LEETCODE'''
# '''Given an array of integers nums sorted in ascending order, find the starting and ending position of a given number. If target is not found in the array, return [-1, -1].
# You must write an algorithm with O(log n) runtime complexity.'''

# #You must write an algorithm with O(log n), meaning a binary search 
# #1. numbers are sorted in increasing order 
# #2. Assuming the given number is duplicated, we will need to find both: the start index and end index

nums = [5,7,7,8,8,10]
target = 8
output = [3,4]

#using the binary search algo 

#find the start index 
def first_position(nums, target):
    def condition(mid):
        if nums[mid] == target: 
            if mid > 0 and nums[mid-1] == target:
                 return 'left'
            return 'found'
        
        elif nums[mid] < target: 
            return 'right'
        else: 
            return 'left'
    return binary_search(0, len(nums)-1, condition)

def last_position(nums, target):
    def condition(mid):
        if nums[mid] == target: 
            #we're checking the right of the list
            if mid < len(nums)-1 and nums[mid+1] == target:
                 return 'right'
            return 'found'
        
        elif nums[mid] < target: 
            return 'right'
        else: 
            return 'left'
    return binary_search(0, len(nums)-1, condition)

def get_first_last_position(nums, target):
    return first_position(nums, target), last_position(nums, target)
        
        
# #TEST

# results = get_first_last_position(nums, 8)
# print(results)

# if results == output:
#     print('cards is located at position:', results)       

# #######################################################
# '''You are given a list of numbers, obtained by rotating a sorted list an unknown number of times. Write a function to determine the minimum number of times the original sorted list was rotated to obtain the givenlist. Your function should have the worst-case complexity of O(logN), where N is the length of the list. You can assume that all the numbers in the list are unique. 
# Ex: the list [5,6,9,0,2,3,4] was obtained by rotating the sorted list and assing it before the first element. Eg. rotating the list [3,2,4,1] produces [1,3,2,4]'''

# #Understanding the problem 
# #trying to find how many the minimum times a list was rotated. 
# #all numbers are unique. 
# #A rotated list is where the elements are shifted to the left or right by a certain number of positions. These can be rotated to the left and right by a specified number of positions
# #rotations is the number of times the sorted list was rotated

# #nums represent a sorted rotated list 
# nums = [5,6,9,0,2,3,4]

# #PSEUDOCODE 

# #If a list is rotated 'k' times, then the smallest number in the list ends up at position 'k'
# #It is the onlyu number in the list which is smaller than the number before it 
# #we need to check whether the value is less than the number before it 
# #then our answer is ismply the position of this number. If we can't find this value then the list wasn't rotated at all 

# '''linear search solution'''
# #PSEUDOCODE 
# # Create a variable position with the value 0
# # Compare the number is smaller than its predecessor, then return position 
# # Otherwise, increment position and repeat till we reach the end of the list

# def count_rotations(nums):
#     #This variable will be used to keep track of the current position while iterating through the list nums
#     position = 0
    
#     #iterates through each element of the list.
#     while position < len(nums):
#         #position > 0: This condition checks if the current position is greater than 0. This is because, in a sorted list with no rotations, each element should be greater than or equal to the previous element. If this condition is not met, it means we've found a point where the list is not sorted as expected.
#         #nums[position] < nums[position-1]: checks if the current element at position is less than the element just before it (position-1). If this condition is met, it indicates a point where the list is not sorted as expected.
#         if position > 0 and nums[position] < nums[position-1]:
#             #return position: If the conditions in the if statement are met, the function returns the position where the unexpected ordering was detected. This position represents the number of rotations needed to restore the original sorted order. Remember we're looking at the index here 
#             print('position', position, 'value:', nums[position])
           
#             return position 
      
        
#         position += 1 #If neither of the conditions in the if statement is met, the code increments the position variable by 1, effectively moving to the next element in the list for further inspection.
    
#     return 0 #This means that the list is either sorted or empty, and no rotations are needed to restore the original order.



# # TEST CASES # 
# #Each dictionary will contain 2 keys. Input: a nested dictionary containing one key for each argument to the function and output (the expected result from the function)

# test = {
#     'input': {
#         'nums': [19, 25, 29, 3, 5, 6, 7, 9, 11, 15 ], 
        
#     }, 
#     'output': 3 
# }


# nums0 = test['input']['nums']
# output0 = test['output']
# result0 = count_rotations(nums0)
# result0, result0 == output0
 
# test0 = test

# #A li_bubblest of s_bubbleize 8 r_bubbleotated _bubble5 times
# test1 = {
#     'input': {
#         'nums': [4, 5, 6, 7, 8, 1, 2, 3 ], 
        
#     }, 
#     'output': 5 
# }

# #A list that wasn't rotated at all 
# test2 = {
#     'input': {
#         'nums': [1, 2, 3, 4, 5, 6], 
        
#     }, 
#     'output': 0 
# }

# #A list that was rotated just once 
# test3 = {
#     'input': {
#         'nums': [7, 3, 5 ], 
        
#     }, 
#     'output': 1 
# }



# #A list where n is the size of the list
# test4 = {
#     'input': {
#         'nums': [3, 5, 7, 8, 9, 10 ], 
        
#     }, 
#     'output': 0
# }

# tests = [test0, test1, test2, test3, test4]

# for test in tests:
#    print(count_rotations(**test['input']) == test['output'])
   

# #Analyze the algorithm's complexity: O(N)

# '''BINARY SEARCH SOLUTION'''

# #Same concept, only difference is that we'd need to find the middle element. Given the middle element decide if the answer is in the right or left 
# #If the middle answer is smaller than the last element of the range, then the answer is to the left. Otherwiser, the answer is to the right.
   

# def count_rotations_binary(nums):
#     lo=0
#     hi=len(nums)-1
    
#     while lo < hi:
#         mid = (lo+hi) // 2 
#         mid_number = nums[mid]
        
#         # if mid > 0 and mid < len(nums)-1:
#         #     return mid 
        
#         #check if the answer is in the right side by checking if the middle ellement is at the right index. if it is, this indicates that the rotation point is to the right of mid, so set left to mid + 1.
#         if mid_number > nums[hi]:
#             print('mid_num:', mid_number, 'value:', nums[hi])
#             lo = mid + 1
#             print('lo:', lo)
#         #Otherwise, if the middle element is less than or equal to the element at the right index, this indicates that the rotation point is to the left of mid or at mid itself, so set right to mid.
#         else:
#             hi = mid
    
#     return lo

# #TEST
# tests = [test0, test1, test2, test3, test4]

# for test in tests:
#    print(count_rotations(**test['input']) == test['output'])
    
    
# #Analyze the algo's complexity: O(logN)

# '''BINARY TREES, TRAVERSALS AND BALANCING'''
# '''You are tasked with developing a fast in-memory data structure to manage profile information(username, name, email) for 100 million users. It should allow the following operations:
# 1. Insert the profile info for a new user 
# 2. FIND the profile info of a user, given their username 
# 3. UPDATE the profilw information of a user, given their username
# 4. LIST all the users of the platform, sorted by username. 
# You can assume that username are unique'''


# #State the problem 
# #We need to create a database  to store 100 million records and perform insertion, search, update and list operations efficiently
# #inputs: user's info (username, name, email)

# '''SIMPLE SOLUTION '''

# class User: 
#     def __init__(self, name, username, email):
#         self.username = username 
#         self.name = name 
#         self.email = email 
        
#     #we can also create methods inside a class 
#     def introduction(self, friend_name):
#         return f"Hi, {friend_name}! I'm {self.name}, you can reach me at {self.email}"

        
#     #returns a printable representation of a given object 
#     def __repr__(self):
#         return "User(name={}, username={}, email={})".format(self.name, self.username, self.email)
    
#     #returns the string representation of a given object
#     def __str__(self):
#         return self.__repr__() 
    
# # #instantiate an object of the user class by calling the class like a function 
# # user1 = User('Marcela', 'Chela', 'marcela@gmail.com')
# # user1.introduction('Jess')


# '''OUTPUT''' 
# class UserDatabase: 
#     def __init__(self):
#         self.users = [] #empty list
        
#     #we'll create a function for each operation 
#     def insert(self, user):
#         i = 0
        
#         while i < len(self.users):
#             #find the first username greater than the user's username 
#             if self.users[i].username > user.username: 
#                 break
#             i += 1 
#         self.users.insert(i, user) #we insert the new user at the empty index 
    
#     def find(self, username):
#         for user in self.users: 
#             if user.username == username: 
#                 return user 
            
        
#     def update(self, user):
#         target = self.find(user.username)
#         if target:
#             target.name, target.email = user.name, user.email
    
#     def list_all(self):
#         return self.users



# '''pseudocode''' 
# ''' Store use objects in a list sorted by usernamees
# Functions to be implemented: 
# 1. Insert: Loop through the list and add the new user at a position that keeps the list sorted 
# 2. Find: Loop through the list and find the user object with the username matching the query 
# 3. Update: Loop through the list, find the user object matching the query and update the details
# 4. List return the list of all user objects
# '''


# # #Create new database 
# # database = UserDatabase()
# # print(database)
# # #insert new users 
# # database.insert(josseline)
# # database.insert(miriam)
# # print(database)

# # #Retrieve data for a user given the username
# # user = database.find('Miriam')
# # print(user)

# # #change the info for a user 
# # database.update(User(username='joss', name='Josseline', email='jossy@gmail.com'))
# # user = database.find('Josseline')
# # print(user)

# # #retrieve a list of user in alphabetical order 
# # database.list_all()

# # database.insert(jennifer)
# # database.list_all()

# '''TESTCASES'''
# #Instantiate new objects
# josseline = User('Josseline', 'joss', 'joss@gmail.com')
# jennifer = User('Jenny', 'jenn', 'jenn@gmail.com')
# miriam = User('Miriam', 'mir', 'miriam@gmail.com')

# users = [josseline, jennifer, miriam]
# print('List of existing users:', users)

# josseline.username, josseline.name
# print('String representation:', josseline)

# database = UserDatabase()
# print(database)

# database.insert(josseline)
# database.insert(miriam)
# print(database.list_all())

# user = database.find('mir')
# print(user)

# database.update(User('Josseline', 'joss', 'jossy@gmail.com'))
# user = database.find('joss')
# print(user)

# database.insert(jennifer)
# print(database.list_all())

# '''Analyze complexity '''
# # Operations insert, find, update involves iterating over list of use, which can take N iterations 
# #Insert O(N), Find O(N), Update O(N), getting the List O(1)


# '''BINARY TREE'''
# #We can limit he number of iterations by using a binary tree 
# #A binary tree is like an inverted tree trunk with branches called nodes, top node is called the 'root' where most operations begin 
# #Binary tree indicates that each ''node'' in the tree can have 2 children max (left or right)
# #Nodes that do not have any children are called 'leaves' 

# '''Implement a binary tree using Python and show its usage with some examples'''

# #here is a simple class representing a node within a binary tree
# class TreeNode: 
#     def __init__(self, key):
#         self.key = key

#         self.left = None
#         self.right = None 
        
# #create objects representing each node of the above tree
# node0 = TreeNode(3)
# node1 = TreeNode(5)
# node2 = TreeNode(7)

# print(node0) #verifies if is an object of the type 'Treenode' 
# print(node0.key) #and has the property key set to 3 

# #we can connect the nodes by setting the .left and .right properties to the root node 
# node0.left = node1
# node0.right = node2

# tree = node0
# print(tree.key)
# print(tree.left.key)
# print(tree.right.key)

# '''Create a binary tree using the 'TreeNode class defined above'''

# #we can use a tuple 
# tree_tuple = ((1,3,None), 2, ((None, 3, 4), 5, (6, 7, 8)))

# def parse_tuple(data): 
#     #If data is a tuple with three elements (indicating a non-empty tree node), it creates a TreeNode object with the middle element as the value of the node (data[1]).
#     if isinstance(data, tuple) and len(data) == 3:
#         node = TreeNode(data[1])
        
#         #It recursively parses the left subtree by calling parse_tuple(data[0]) and assigns it to the left attribute of the node.
#         node.left = parse_tuple(data=[0])
        
#         #It recursively parses the right subtree by calling parse_tuple(data[2]) and assigns it to the right attribute of the node.
#         node.right = parse_tuple(data=[2])
        
#     #If data is None, it returns None to indicate an empty subtree.
#     elif data is None: 
#         node=None
        
#     #If data is neither a tuple nor None, it assumes that it's a leaf node value and creates a TreeNode with that value.    
#     else: 
#         node = TreeNode(data)
#     return node


# tree2 = parse_tuple(((1,3, None), 2, ((None, 3, 4), 5, (6, 7, 8) )))
# print(tree2)
# print(tree2.key)
# print(tree2.left.key, tree2.right.key)


# ''''Function to display a binary tree'''
# def print_tree(root): 
#     #check if there is a tree 
#     if root is None: 
#         return
    
#     #initialized with the root node
#     queue = [root] 
    
#     #continue as long as the 'queue' is not empty 
#     while queue: 
#         #find the number of nodes by finding the length of the queue
#         level_nodes = len(queue)
        
#         #for loop iterates over the nodes in the current level
#         for i in range(level_nodes):
#             #remove the node at index 0 
#             node = queue.pop(0)
            
#             #if there's a value,  the code enqueues (appends) the left and right children of the current node to the queue
#             if node: 
#                 print(node.key, end=' ')
#                 queue.append(node.left)
#                 queue.append(node.right)
#             #if the node is empty(missing child), we print none 
#             else: 
#                 print('None', end= ' ')
#     print()
    
# root = TreeNode(2)
# root.left = TreeNode(1)
# root.right = TreeNode(5)
# root.left.right = TreeNode(3)
# root.right.right = TreeNode(6)
# root.right.right.left = TreeNode(7)
# root.right.right.right = TreeNode(8)
    
# print_tree(root)


# '''TRAVERSAL'''
# #implementation of inorder taversal of a binary tree
# def traverse_in_order(node): #node represents the root of the subtree 
#     if node is None: #if the node is empty
#         return [] #it returns an empty list
#     #recursively traverses the left subtree of the current node. This returns a list of keys/values from the left subtree in in-order.
#     #[node.key] represents the key (or value) of the current node itself. This is a single-element list containing the key/value of the current node.
#     #traverse_in_order(node.right) recursively traverses the right subtree of the current node. This returns a list of keys/values from the right subtree in in-order.
#     # the + operator creates a single list that represents the in-order traversal of the entire subtree rooted at the current node
#     return(traverse_in_order(node.left)) + [node.key] + traverse_in_order(node.right)

# '''Height and size of a Binary Tree'''
# '''Write a function to calculate the heigh/depth of a binary tree'''

# def tree_height(node): #takes the root node 
#     if node is None: #If the node is not None, the function recursively calculates the height
#         return 0 
#     return 1 + max(tree_height(node.left), tree_height(node.right)) #tree_height(node.left) calculates the height of the left subtree of the current node by making a recursive call.
#                                                                     #tree_height(node.right) calculates the height of the right subtree of the current node by making a recursive call.
#                                                                     #max: computes the max height between the left and right subtree because the height of the entire tree is determied by the longer of the two subtrees 
#                                                                     #adds 1 to the maximum height of the subtrees to account for the current level (the level of the current node). (since we're looking at the index)
                                                                    
                                                                    
# # class TreeNodes(): 
# #     def __init__(self, key): 
# #         self.key = key
# #         self.left = None
# #         self.right = None
    
# #     def height(self): 
# #         if self is None: 
# #             return 0 
# #         return 1 + max(TreeNode.height(self.left), TreeNode.height(self.right))
    
# #     def size(self):
# #         if self is None: 
# #             return 0 
# #         return 1 + TreeNode.size(self.left) + TreeNode.size(self.right)
    
# #     def traverse_in_order(self): 
# #         if self is None: 
# #             return []
# #         return (TreeNode.traverse_in_order(self.left)+ [self.key] + TreeNode.traverse_in_order(self.right))
    
# #     def display_keys(self, space='\t', level=0):
# #         #if the node is empty
# #         if self is None: 
# #             print(space*level + 'o')
# #             return
        
# #         #if the node is a leaf 
# #         if self.left is None and self.right is None: 
# #             print(space*level + str(self.key))
# #             return
        
# #         #if the node has children
# #         display_keys(self.right, space, level+1)
# #         print(space*level + str(self.key))
# #         display_keys(self.left, space, level+1)
    
# #     def to_tuple(self):
# #         if self is None: 
# #             return None
# #         if self.left is None and self.right is None: 
# #             return self.key 
# #         return TreeNode.to_tuple(self.left), self.key, TreeNode.to_tuple()
    
    
# '''BINARY SEARCH TREE (BST)'''
# #A binary search tree that satisfies these conditions: 
# #1. Left subtree of any node only contains nodes with keys less than the node's key 
# #2. RIght subtree of any node only contains nodes with keys greater than the node's key 
 
# '''Write a function to check if a binary tree is a binary search tree (BST). 
#  Write a function to find the maximum key in a binary tree
#  Write a function to find the minimum key in a binary tree'''
 
#  #The function below addresses all questions 
# #  check whether a given binary tree is a binary search tree (BST). It does so by recursively traversing the tree while maintaining the minimum and maximum values allowed for the nodes at each level of the tree
 
# def remove_none(nums): 
#     #returns a new list containing only the non-None values. It uses a list comprehension to filter out None values from the input list.
#      return [x for x in nums if x is not None]
 
# def is_binary_search_tree(node):
#     # check if the binary tree rooted at node is a BST. If node is None (i.e., an empty tree or leaf node), it returns True because an empty tree is considered a BST. It also returns None for both the minimum and maximum values for this subtree.
#     if node is None: 
#         return True, None, None

#     #  It obtains the results from these recursive calls, including whether each subtree is a BST (is_binary_search_tree_l and is_binary_search_tree_r), and the minimum and maximum values for each subtree (min_l, max_l, min_r, max_r).
#     is_binary_search_tree_l, min_l, max_l = is_binary_search_tree(node.left)
#     is_binary_search_tree_r, min_r, max_r = is_binary_search_tree(node.right)
    
#     #checks whether the current node itself is part of a BST. It does this by ensuring that both the left and right subtrees are BSTs (is_binary_search_tree_l and is_binary_search_tree_r are True), and that the node.key (assuming node has a key attribute) is greater than the maximum value allowed in the left subtree (max_l) and less than the minimum value allowed in the right subtree (min_r)
#     is_bst_node = (is_binary_search_tree_l and is_binary_search_tree_r and 
#                    (max_l is None or node.key > max_l) and
#                    (min_r is None or node.key < min_r))
    
#     #calculates the minimum and maximum values for the current subtree. It uses the remove_none function to filter out None values from the list of minimum and maximum values calculated for the left subtree, node.key, and the values calculated for the right subtree. This ensures that the min_key and max_key do not include None values.
#     min_key = min(remove_none([min_l, node.key, min_r]))
#     max_key = max(remove_none([max_l, node.key, max_r]))
    
#     # returns whether the current node is part of a BST (is_bst_node), as well as the minimum and maximum values for the subtree rooted at node.
#     return is_bst_node, min_key, max_key


# '''PROBLEM# 4: OPTIMAL SOLUTION'''
# #keys would be the username and user objects as values:
# class BSTNode():
#     def __init__(self, key, value=None):
#         self.key = key 
#         self.value = value 
#         self.left = None 
#         self.right = None
#         self. parent = None
        
# #level 0 
# bstree = BSTNode(josseline.username, josseline)
# print(bstree.key, bstree.value)

# #level 1
# bstree.left = BSTNode(miriam.username, miriam)
# bstree.left.parent = bstree 
# bstree.right = BSTNode(jennifer.username, jennifer)
# bstree.right.parent = bstree
# print(bstree.left.key, bstree.left.value, bstree.right.key, bstree.right.value)

# #display tree
# print_tree(bstree)

# ###### PARAMETERS #######
# #  key is the key(username) of the node to be inserted 
# #  'value' is the value (entire user's object which includes name, email & username) associated with the new node
# ############


# '''Write a function to INSERT a new node into a BST'''
# '''we need to recursively traverse the tree to find the appropriate location for the new node and updates the tree structure accordingly'''
# def insert(node, key, value): #node is the root of the current subtree, key is the key(username) of the node to be inserted, and 'value' is the value (entire user's object which includes name, email & username) associated with the new node
# #    check if the current node is None, indicating that the function has reached an empty (null) node. If this is the case, it creates a new BSTNode with the specified key and value, effectively creating the new node and assigning it to node
#     if node is None: 
#         node = BSTNode(key, value)
        
# # checks whether the key to be inserted (key) is less than the key of the current node (node.key). If it is, the insertion process continues in the left subtree.
#     elif key < node.key:
# #         recursively calls the insert function on the left subtree. It assigns the result (the updated left subtree) to node.left, effectively linking the new node to the left subtree.
# # node.left.parent = node sets the parent of the newly inserted node (node.left) to be the current node (node).
#         node.left = insert(node.left, key, value)
#         node.left.parent = node
#     elif key > node.key:
#         node.right = insert(node.right, key, value)
#         node.right.parent = node
#     return node
#                       #key                #value
# bstree = insert(None, josseline.username, josseline)
# print(bstree.key, bstree.value)
# insert(bstree, miriam.username, miriam)
# insert(bstree, jennifer.username, jennifer)
# #display tree
# print_tree(bstree)


# '''FINDING A NODE IN BST(Binary Search Tree)'''
# '''Find the value associated with a given key in a BST'''

# #we'll use a recursive strategy, we're calling the same function over and over again
# def find(node, key): #node is the root of the current subtree, key is the key (username) of the node we're looking for
#     if node is None: 
#         return node 
#     if node.key == key: 
#         return node
#     if key < node.key: 
#         return find(node.left, key)
#     if key > node.key: 
#         return find(node.right, key)
    
    
# node = find(bstree, 'joss')
# print('key:', node.key, 'value:', node.value)


# '''UPDATING A VALUE IN A BST'''
# '''Write a function to update the value associated with a given key'''

# def update(self, key, value):
#     #we first find the node
#     target = find(node, key)

#     if target is not None:
#     #we update the target with the new value  
#         target.value = value
        
# update(bstree, 'jenn', User('jenn', 'Jennifer', 'jenny@gmail.com'))
# node = find(bstree, 'jenn')
# print('Updated node value: ', node.value)  


# '''RETRIEVE LIST'''
# '''Write a funtion to retrieve all the key-value pairs stored in a BST in the sorted order of keys'''
# #nodes can be listed in a sorted order by performing an inorder traversal(meaning that we visit the leftmost node first, then the root, and lastly the right node) of the BST

# def list_all(node):
#     if node is None: 
#         return []
#     else:                           #insert the key and value from the current node 
#         return list_all(node.left) + [(node.key, node.value)] + list_all(node.right)
    
# print(list_all(bstree))

# ######################
# '''BALANCED TREE'''
# '''Write a function to determine if a binary tree is balanced'''

# #Recursive strategy 
# # 1. Ensure that the left subtree is balanced
# # 2. Ensure that the right subtree is balanced
# # 3. Ensure that the difference between heights of the left subtree and right subtree is not more than 1

# def is_balanced(node):
#     if node is None: 
#         return True, 0
#     balanced_l, height_l = is_balanced(node.left)
#     balanced_r, height_r = is_balanced(node.right)
#     balanced = balanced_l and balanced_r and abs(height_l - height_r ) <= 1 
#     height = 1 + max(height_l, height_r)
#     return balanced, height

# print(is_balanced(bstree))

# '''BALANCED BINARY SEARCH TREES'''
# '''Write a function to create a balance BST from a sorted list/array of key-value pairs'''
# # Use recursion
# # Similar to binary search, we find the middle element and use that as our root node 
# # then take the left half of the list and use that to create a balanced binary search tree and make it the left child element of the root node 
# # Same process for the right side, we take the right elements, create a balanced binary search tree and link it to be the right child element of the root node (middle element)\
# #use the recursive algo below if the data is sorted to create a balanced binary search tree. If the data is not sorted, it could lead to unbalanced recursion.

# def make_balanced_bst(data, lo=0, hi=None, parent=None): #data which a list of key value pair  #set lo to 0, initial index in the list  
#     hi= len(data) -1 #the last item in the list 
    
#     if lo>hi:
#         return None
    
#     #find the middle element 
#     mid= (lo+hi) // 2 
#     #we get the user's username and the user's object 
#     key, value = data[mid]
    
#     #we create the root node
#     root = BSTNode(key, value)
#     root.parent = parent 
#     #recursive function. Here we're passing the list of key-value pairs, the range would start at lo= 0 and end at the middle element - 1, and our root 
#     root.left = make_balanced_bst(data, lo, mid-1, root)
#     #we're passing the list of key-value pairs, the range would start at mid_element + 1 and end at the given hi value which is the end of the list , and our root
#     root.right = make_balanced_bst(data, mid+1, hi, root)
    
#     return root

# data = [(user.username, user) for user in users]
# print('Balanced binary search tree: ', data)
   
# # 
# # balanced_tree = make_balanced_bst(data)
# # print(balanced_tree)


# '''BALANCING AN UNBALANCED BST'''

# '''Write a function to balance unbalanced binary search tree'''
# #perform an inorder traversal, then create a balanced BST using the function defined earlier 

# def balance_bst(node): 
#                           #we're doing an inorder traversal to call the sorted array and passing that into the 'make_balanced_bst' function' 
#     return make_balanced_bst(list_all(node))

# unbalancedt1 = None 
# #insert the values one by one
# for user in users: 
#     unbalancedt1 = insert(unbalancedt1, user.username, user)
    
# # print(unbalancedt1)


# # unbalancedt2 = balance_bst(unbalancedt1)


# '''OPTIMIZED SOLUTION'''
# # Define a class for user profiles
# class UserProfile:
#     def __init__(self, username, name, email):
#         self.username = username
#         self.name = name
#         self.email = email

# # Define a class for the user database
# class UserDatabase:
#     def __init__(self):
#         self.profile_dict = {}  # Hash table for profiles (username -> UserProfile)
#         self.sorted_usernames = []  # Balanced Binary Search Tree for sorted usernames

#     def insert(self, username, name, email):
#         # Create a new user profile
#         new_profile = UserProfile(username, name, email)

#         # Insert into the hash table
#         self.profile_dict[username] = new_profile

#         # Insert into the BST for sorting
#         self.insert_into_bst(username)

#     def find(self, username):
#         if username in self.profile_dict:
#             return self.profile_dict[username]
#         else:
#             return None

#     def update(self, username, name, email):
#         if username in self.profile_dict:
#             # Update the profile information
#             self.profile_dict[username].name = name
#             self.profile_dict[username].email = email

#     def list_all(self):
#         # Perform an in-order traversal of the BST to list all users sorted by username
#         sorted_users = [self.profile_dict[username] for username in self.sorted_usernames]
#         return sorted_users

#     def insert_into_bst(self, username):
#         # Helper function to insert a username into the BST
#         self.sorted_usernames = self._insert_into_bst(self.sorted_usernames, username)

#     def _insert_into_bst(self, usernames, username):
#         # Recursive helper function to insert a username into the BST
#         if not usernames:
#             return [username]

#         root_index = len(usernames) // 2
#         root_username = usernames[root_index]

#         if username < root_username:
#             # Insert into the left subtree
#             return self._insert_into_bst(usernames[:root_index], username) + [root_username] + usernames[root_index:]
#         else:
#             # Insert into the right subtree
#             return usernames[:root_index + 1] + [username] + self._insert_into_bst(usernames[root_index + 1:], username)

# # Example usage:
# if __name__ == "__main__":
#     db = UserDatabase()

#     # Insert user profiles
#     db.insert('user3', 'Alice', 'alice@example.com')
#     db.insert('user1', 'Bob', 'bob@example.com')
#     db.insert('user2', 'Charlie', 'charlie@example.com')

#     # Find and update user profiles
#     user = db.find('user1')
#     if user:
#         print(f"Found user: {user.name}, {user.email}")
#         db.update('user1', 'Bobby', 'bobby@example.com')

#     # List all users sorted by username
#     users = db.list_all()
#     print("All users:")
#     for user in users:
#         print(f"{user.username}: {user.name}, {user.email}")

###############################################################################################################
'''SORTING'''

'''Write a function to sort a list of notebooks in decreasing order of hikes. Keep in mind that up to millions of notebooks can be created every week, so your function needs to be as efficient as possible. 

#2 Write a program to sort a list of numbers'''

#We need to write a fucntion to sort a list of numbers in increasing order



#TEST CASES 
# List of numbers in random order 
test_bubble0 = {
    'input': {
        'nums': [ 2, 3, 5, 8, 4, 1, 33, 12]
    },
    'output': [1, 2, 3, 4, 5, 8, 12, 33 ]
}
# A list that's already sorted 
test_bubble1 = {
    'input': {
        'nums': [ 1, 2, 3, 4, 5]
    },
    'output': [ 1, 2, 3, 4, 5]
}
# A list that's sorted in descending order 
test_bubble2 = {
    'input': {
        'nums': [99, 10, 7, 2]
    },
    'output': [2, 7, 10, 99 ]
}
# A list containing repeating elements 
test_bubble3 = {
    'input': {
        'nums': [5, -12, 2, 6, 7, 7, -12]
    },
    'output': [-12, -12, 2, 5, 6, 7, 7]
}

# An empty list
test_bubble4 = {
    'input': {
        'nums': []
    },
    'output': [ ]
}

#A list contaning just one element 
test_bubble5 = {
    'input': {
        'nums': [10]
    },
    'output': [10]
}


# A list containing one element repeated many times
test_bubble6 = {
    'input': {
        'nums': [55, 55, 55, 55, 55]
    },
    'output': [55, 55, 55, 55, 55]
}


#pseudocode 
# 1. Iteratre over the list, starting from the left 
# 2. Compare each number with the number that follows it 
# 3. If the number is greater than the one that follows it, swap the two elements 
# 4. Repeat steps 1 to 3 till the list is sorted 
### This method is called 'bubble sort' ###

'''SOLUTION'''

def bubble_sort(nums):
  
    
    print('buble_sort: ', nums)
    for num in range(len(nums)-1):
        print('iteration: ', num)
        #iterate over the array except the last element because there's no other element left to compare it with 
        for i in range(len(nums)-1):
            print('i', i, nums[i], nums[i+1])
            #compare the number with 
            if nums[i] > nums[i+1]: 
                #Swap the two elements
                nums[i], nums[i+1] = nums[i+1], nums[i]
                
        #return the sorted list
        return nums
                
            
# nums = [ 2, 3, 5, 8, 4, 1, 33, 12]
# output = [1, 2, 3, 4, 5, 8, 12, 33 ]               

tests_bubble = [test_bubble0, test_bubble1, test_bubble2, test_bubble3, test_bubble4, test_bubble5]

for tests in tests_bubble: 
    print(bubble_sort(tests['input']['nums']) == tests['output'])
    
#TIme complexity: O(n2) - so many loops
#SPace complexity: O(N) - we use extra space as we're creating a new list

'''SOLUTION 2'''

def sort_list(nums):
    sorted_nums = sorted(nums)
    print('sorted numbers:', sorted_nums)
    return sorted_nums

for tests in tests_bubble: 
    print(sort_list(tests['input']['nums']) == tests['output'])

#Time complexity: O(n log n)
#SPace complexity: O(N) 


'''INSERTION SORT'''
#We move elements to the right until we find the correct position for the key element. In insertion sort, you can think of the left part of the list as the "sorted" portion and the right part as the "unsorted" portion. Starting with the second element allows us to consider the first element (at index 0) as already sorted because there are no elements to its left.


def insertion_sort(arr):
    for i in range(1, len(arr)): #iterate through the list starting from the second element (index 1) to the end.
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key #place the key element in its correct position in the sorted part of the list.

# Input: List of numbers
numbers = [5, 2, 9, 1, 5, 6]

# Call the insertion_sort function to sort the list in-place
insertion_sort(numbers)

# Output the sorted list
print("Sorted Numbers:", numbers)



'''Write a function to merge two sorted arrays'''
def merge_sort(nums):
    if len(nums) <= 1:
        return nums
    
    #find the mid element 
    mid=len(nums) // 2
    
    #split the list into two halves 
    left=nums[:mid]
    right=nums[mid:]
    
    #solve the problem for each half recursively 
    left_sorted = merge_sort(left)
    right_sorted = merge_sort(right)
    
    #combine the results of the two halves 
    sorted_nums = merge(left_sorted, right_sorted)
    
    return sorted_nums

def merge(arr1, arr2):
#create a list to store the results
    merged = []

    # Pointers for both arrays to traverse the two input arrays arr1 and arr2, respectively.
    i = 0
    j = 0

    # Merge elements while both arrays have elements
    while i < len(arr1) and j < len(arr2):
        
        #compare the elements at the current positions i and j and append the smaller element to the merged list. We then increment the pointer of the array from which we took the element.
        if arr1[i] < arr2[j]:
            merged.append(arr1[i])
            i += 1
        #repeat this process until one of the arrays is exhausted.    
        else:
            merged.append(arr2[j])
            j += 1

    # Append remaining elements from arr1 (if any)
    while i < len(arr1):
        merged.append(arr1[i])
        i += 1

    # Append remaining elements from arr2 (if any)
    while j < len(arr2):
        merged.append(arr2[j])
        j += 1

    #return the merged list containing the merged and sorted elements
    return merged


#TEST 
arr1 = [1, 3, 5, 7]
arr2 = [2, 4, 6, 8]
merged_array = merge(arr1, arr2)
print("Merged Array:", merged_array)