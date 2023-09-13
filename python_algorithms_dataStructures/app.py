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


