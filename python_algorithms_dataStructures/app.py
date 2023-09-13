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



