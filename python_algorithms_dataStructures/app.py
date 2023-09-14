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


   
   

