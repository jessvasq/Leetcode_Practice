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


#TEST SOLUTION 

result = find_card(test['input'] ['cards'], test['input']['query'])
print(result) 

# or #

results = find_card(cards, 7)
print(results)  

if result == output:
    print('cards is located at position:', results)

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

#TEST SECOND SOLUTION 

result = find_cards(test['input'] ['cards'], test['input']['query'])
print(result) 

# or #

results = find_cards(cards, 7)
print(results)  

if result == output:
    print('cards is located at position:', results)


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


'''BINARY SEARCH vs. LINEAR SEARCH'''

#TEST large lists 
# large_test = {
#     'input': {
#         "cards": list(range(100000000, 0, -1)), #we're creating a decreasing list by using range() starting at 10000000 and ending at 1 
#         "query": 2
#         }, 
#     'output': 999998
# }

#The binary search is over 55,000 times faster than the linear search version 
#As the size of the input grows larger, the difference only gets bigger. 


'''SECOND QUESTION. #34 LEETCODE'''
'''Given an array of integers nums sorted in ascending order, find the starting and ending position of a given number. If target is not found in the array, return [-1, -1].
You must write an algorithm with O(log n) runtime complexity.'''

#You must write an algorithm with O(log n), meaning a binary search 
#1. numbers are sorted in increasing order 
#2. Assuming the given number is duplicated, we will need to find both: the start index and end index

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
        
        
#TEST

results = get_first_last_position(nums, 8)
print(results)

if results == output:
    print('cards is located at position:', results)       

#######################################################
'''You are given a list of numbers, obtained by rotating a sorted list an unknown number of times. Write a function to determine the minimum number of times the original sorted list was rotated to obtain the givenlist. Your function should have the worst-case complexity of O(logN), where N is the length of the list. You can assume that all the numbers in the list are unique. 
Ex: the list [5,6,9,0,2,3,4] was obtained by rotating the sorted list and assing it before the first element. Eg. rotating the list [3,2,4,1] produces [1,3,2,4]'''

#Understanding the problem 
#trying to find how many the minimum times a list was rotated. 
#all numbers are unique. 
#A rotated list is where the elements are shifted to the left or right by a certain number of positions. These can be rotated to the left and right by a specified number of positions
#rotations is the number of times the sorted list was rotated

#nums represent a sorted rotated list 
nums = [5,6,9,0,2,3,4]

#PSEUDOCODE 

#If a list is rotated 'k' times, then the smallest number in the list ends up at position 'k'
#It is the onlyu number in the list which is smaller than the number before it 
#we need to check whether the value is less than the number before it 
#then our answer is ismply the position of this number. If we can't find this value then the list wasn't rotated at all 

'''linear search solution'''
#PSEUDOCODE 
# Create a variable position with the value 0
# Compare the number is smaller than its predecessor, then return position 
# Otherwise, increment position and repeat till we reach the end of the list

def count_rotations(nums):
    #This variable will be used to keep track of the current position while iterating through the list nums
    position = 0
    
    #iterates through each element of the list.
    while position < len(nums):
        #position > 0: This condition checks if the current position is greater than 0. This is because, in a sorted list with no rotations, each element should be greater than or equal to the previous element. If this condition is not met, it means we've found a point where the list is not sorted as expected.
        #nums[position] < nums[position-1]: checks if the current element at position is less than the element just before it (position-1). If this condition is met, it indicates a point where the list is not sorted as expected.
        if position > 0 and nums[position] < nums[position-1]:
            #return position: If the conditions in the if statement are met, the function returns the position where the unexpected ordering was detected. This position represents the number of rotations needed to restore the original sorted order. Remember we're looking at the index here 
            print('position', position, 'value:', nums[position])
           
            return position 
      
        
        position += 1 #If neither of the conditions in the if statement is met, the code increments the position variable by 1, effectively moving to the next element in the list for further inspection.
    
    return 0 #This means that the list is either sorted or empty, and no rotations are needed to restore the original order.



# TEST CASES # 
#Each dictionary will contain 2 keys. Input: a nested dictionary containing one key for each argument to the function and output (the expected result from the function)

test = {
    'input': {
        'nums': [19, 25, 29, 3, 5, 6, 7, 9, 11, 15 ], 
        
    }, 
    'output': 3 
}


nums0 = test['input']['nums']
output0 = test['output']
result0 = count_rotations(nums0)
result0, result0 == output0
 
test0 = test

#A list of size 8 rotated 5 times
test1 = {
    'input': {
        'nums': [4, 5, 6, 7, 8, 1, 2, 3 ], 
        
    }, 
    'output': 5 
}

#A list that wasn't rotated at all 
test2 = {
    'input': {
        'nums': [1, 2, 3, 4, 5, 6], 
        
    }, 
    'output': 0 
}

#A list that was rotated just once 
test3 = {
    'input': {
        'nums': [7, 3, 5 ], 
        
    }, 
    'output': 1 
}



#A list where n is the size of the list
test4 = {
    'input': {
        'nums': [3, 5, 7, 8, 9, 10 ], 
        
    }, 
    'output': 0
}

tests = [test0, test1, test2, test3, test4]

for test in tests:
   print(count_rotations(**test['input']) == test['output'])
   

#Analyze the algorithm's complexity: O(N)

'''BINARY SEARCH SOLUTION'''

#Same concept, only difference is that we'd need to find the middle element. Given the middle element decide if the answer is in the right or left 
#If the middle answer is smaller than the last element of the range, then the answer is to the left. Otherwiser, the answer is to the right.
   

def count_rotations_binary(nums):
    lo=0
    hi=len(nums)-1
    
    while lo < hi:
        mid = (lo+hi) // 2 
        mid_number = nums[mid]
        
        # if mid > 0 and mid < len(nums)-1:
        #     return mid 
        
        #check if the answer is in the right side by checking if the middle ellement is at the right index. if it is, this indicates that the rotation point is to the right of mid, so set left to mid + 1.
        if mid_number > nums[hi]:
            print('mid_num:', mid_number, 'value:', nums[hi])
            lo = mid + 1
            print('lo:', lo)
        #Otherwise, if the middle element is less than or equal to the element at the right index, this indicates that the rotation point is to the left of mid or at mid itself, so set right to mid.
        else:
            hi = mid
    
    return lo

#TEST
tests = [test0, test1, test2, test3, test4]

for test in tests:
   print(count_rotations(**test['input']) == test['output'])
    
    
#Analyze the algo's complexity: O(logN)

'''BINARY TREES, TRAVERSALS AND BALANCING'''
'''You are tasked with developing a fast in-memory data structure to manage profile information(username, name, email) for 100 million users. It should allow the following operations:
1. Insert the profile info for a new user 
2. FIND the profile info of a user, given their username 
3. UPDATE the profilw information of a user, given their username
4. LIST all the users of the platform, sorted by username. 
You can assume that username are unique'''


#State the problem 
#We need to create a database  to store 100 million records and perform insertion, search, update and list operations efficiently
#inputs: user's info (username, name, email)

'''SIMPLE SOLUTION '''

class User: 
    def __init__(self, name, username, email):
        self.username = username 
        self.name = name 
        self.email = email 
        
    #we can also create methods inside a class 
    def introduction(self, friend_name):
        return f"Hi, {friend_name}! I'm {self.name}, you can reach me at {self.email}"

        
    #returns a printable representation of a given object 
    def __repr__(self):
        return "User(name={}, username={}, email={})".format(self.name, self.username, self.email)
    
    #returns the string representation of a given object
    def __str__(self):
        return self.__repr__() 
    
# #instantiate an object of the user class by calling the class like a function 
# user1 = User('Marcela', 'Chela', 'marcela@gmail.com')
# user1.introduction('Jess')


'''OUTPUT''' 
class UserDatabase: 
    def __init__(self):
        self.users = [] #empty list
        
    #we'll create a function for each operation 
    def insert(self, user):
        i = 0
        
        while i < len(self.users):
            #find the first username greater than the user's username 
            if self.users[i].username > user.username: 
                break
            i += 1 
        self.users.insert(i, user) #we insert the new user at the empty index 
    
    def find(self, username):
        for user in self.users: 
            if user.username == username: 
                return user 
            
        
    def update(self, user):
        target = self.find(user.username)
        if target:
            target.name, target.email = user.name, user.email
    
    def list_all(self):
        return self.users



'''pseudocode''' 
''' Store use objects in a list sorted by usernamees
Functions to be implemented: 
1. Insert: Loop through the list and add the new user at a position that keeps the list sorted 
2. Find: Loop through the list and find the user object with the username matching the query 
3. Update: Loop through the list, find the user object matching the query and update the details
4. List return the list of all user objects
'''


# #Create new database 
# database = UserDatabase()
# print(database)
# #insert new users 
# database.insert(josseline)
# database.insert(miriam)
# print(database)

# #Retrieve data for a user given the username
# user = database.find('Miriam')
# print(user)

# #change the info for a user 
# database.update(User(username='joss', name='Josseline', email='jossy@gmail.com'))
# user = database.find('Josseline')
# print(user)

# #retrieve a list of user in alphabetical order 
# database.list_all()

# database.insert(jennifer)
# database.list_all()

'''TESTCASES'''
#Instantiate new objects
josseline = User('Josseline', 'joss', 'joss@gmail.com')
jennifer = User('Jenny', 'jenn', 'jenn@gmail.com')
miriam = User('Miriam', 'mir', 'miriam@gmail.com')

users = [josseline, jennifer, miriam]
print('List of existing users:', users)

josseline.username, josseline.name
print('String representation:', josseline)

database = UserDatabase()
print(database)

database.insert(josseline)
database.insert(miriam)
print(database.list_all())

user = database.find('mir')
print(user)

database.update(User('Josseline', 'joss', 'jossy@gmail.com'))
user = database.find('joss')
print(user)

database.insert(jennifer)
print(database.list_all())

'''Analyze complexity '''
# Operations insert, find, update involves iterating over list of use, which can take N iterations 
#Insert O(N), Find O(N), Update O(N), getting the List O(1)


'''BINARY TREE'''
#We can limit he number of iterations by using a binary tree 
#A binary tree is like an inverted tree trunk with branches called nodes, top node is called the 'root' where most operations begin 
#Binary tree indicates that each ''node'' in the tree can have 2 children max (left or right)
#Nodes that do not have any children are called 'leaves' 

'''Implement a binary tree using Python and show its usage with some examples'''

#here is a simple class representing a node within a binary tree
class TreeNode: 
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None 
        
#create objects representing each node of the above tree
node0 = TreeNode(3)
node1 = TreeNode(5)
node2 = TreeNode(7)

print(node0) #verifies if is an object of the type 'Treenode' 
print(node0.key) #and has the property key set to 3 

#we can connect the nodes by setting the .left and .right properties to the root node 
node0.left = node1
node0.right = node2

tree = node0
print(tree.key)
print(tree.left.key)
print(tree.right.key)

'''Create a binary tree using the 'TreeNode class defined above'''

#we can use a tuple 
tree_tuple = ((1,3,None), 2, ((None, 3, 4), 5, (6, 7, 8)))

def parse_tuple(data): 
    #If data is a tuple with three elements (indicating a non-empty tree node), it creates a TreeNode object with the middle element as the value of the node (data[1]).
    if isinstance(data, tuple) and len(data) == 3:
        node = TreeNode(data[1])
        
        #It recursively parses the left subtree by calling parse_tuple(data[0]) and assigns it to the left attribute of the node.
        node.left = parse_tuple(data=[0])
        
        #It recursively parses the right subtree by calling parse_tuple(data[2]) and assigns it to the right attribute of the node.
        node.right = parse_tuple(data=[2])
        
    #If data is None, it returns None to indicate an empty subtree.
    elif data is None: 
        node=None
        
    #If data is neither a tuple nor None, it assumes that it's a leaf node value and creates a TreeNode with that value.    
    else: 
        node = TreeNode(data)
    return node


tree2 = parse_tuple(((1,3, None), 2, ((None, 3, 4), 5, (6, 7, 8) )))
print(tree2)
print(tree2.key)
print(tree2.left.key, tree2.right.key)


''''Function to display a binary tree'''
def print_tree(root): 
    #check if there is a tree 
    if root is None: 
        return
    
    #initialized with the root node
    queue = [root] 
    
    #continue as long as the 'queue' is not empty 
    while queue: 
        #find the number of nodes by finding the length of the queue
        level_nodes = len(queue)
        
        #for loop iterates over the nodes in the current level
        for i in range(level_nodes):
            #remove the node at index 0 
            node = queue.pop(0)
            
            #if there's a value,  the code enqueues (appends) the left and right children of the current node to the queue
            if node: 
                print(node.key, end=' ')
                queue.append(node.left)
                queue.append(node.right)
            #if the node is empty(missing child), we print none 
            else: 
                print('None', end= ' ')
    print()
    
root = TreeNode(2)
root.left = TreeNode(1)
root.right = TreeNode(5)
root.left.right = TreeNode(3)
root.right.right = TreeNode(6)
root.right.right.left = TreeNode(7)
root.right.right.right = TreeNode(8)
    
print_tree(root)