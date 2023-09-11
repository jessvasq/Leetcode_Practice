def iterative_factorial(n): #n is the parameter the number we want to calculate
    fact=1 #variable starting at 1
    for i in range(2, n+1): #for loop to iterate over the variable. We're multiplying at any number in range starting at 2 and ending at n + 1     
        fact *= i # we then take our variable and multiply it by i. *= assignment operator reassigns our variable everytime it cycles through our loop
    return fact
print(iterative_factorial(5))

'''Recursive method''' 
#not so efficient as it takes longer than an interation
    
# def recur_factorial(n):
#     if n == 1:
#         return 
    
#     else:
#         temp = recur_factorial(n-1)
#         temp = temp * n
        
#     return temp

# print (recur_factorial(5))

#DRY CODE 
def recur_factorial(n):
    if n == 1: return n
    else: return n * recur_factorial(n-1)
    
print(recur_factorial(4))


#Permutation
'''Recursive method'''
def permute(string, pocket=''): #string of two letter we want to permute, and an empty string 
    if len(string) == 0: #if the lenght of the string is empty, we will return the empty pocket string 
        print(pocket)
    else: 
        for i in range(len(string)): #we will loop through the range which is equal to the length of the string 
            letter = string[i] # this will contain each letter in the string 
            front = string[0:i] # take off the front of the string. Also called head
            back = string[i+1:] # slice off the back of the string. Also called tail
            together = front + back # combines the front and back together 
            permute(together, letter + pocket) #pass two parameters, together(front and back). Second param would be the letter added to the pocket 
print (permute('ABC', ''))


'''ITERATIVE METHOD'''
#using iteration and swapping 
from math import factorial
def permutations(str):
    for p in range(factorial(len(str))):
        print(''.join(str))
        i = len(str) - 1
        while i > 0 and str[i - 1 ] > str[i]:
            i -= 1
        str[i:] = reversed(str[i:])
        if i > 0:
            q = i 
            while str[i - 1] > str[q]:
                q += 1 
            temp = str[i - 1]
            str[i - 1] = str[q]
            str[q] = temp 

s='abc'
s=list(s)
permutations(s)



'''DATA STRUCTURES'''
'''LINEAR SEARCH'''

def search(arr, target):
    for i in range(len(arr)):
        
        if arr[i] == target:
            return i 
        
def find_item(arr, x):
    for i in range(len(arr)):
        
        if arr[i] == x:
            return i
        
arr=[2, 6, 9, 10, 15]
target=15
x=10

print(search(arr, target))
print(find_item(arr, x))


'''BINARY SEARCH'''
'''Binary search is an efficient algorithm for finding a specific element in a sorted array. '''

#Iterative Binary Search 

def binary_itr(arr, start, end, target): #function takes 4 params: array, start, end, and the value we're searching for
    found = False #flag to track if the target is found
    
    while start <= end: #we create a while loop to iterate over our array from start to end 
        mid = (start + end) // 2 # we then proceed to create our midpoint 
        print(mid)
        if arr[mid] < target: #check if our target is in the upper half 
            start = mid + 1 # then reassign 'start' to begin moving to the right of the array 
            
        elif arr[mid] > target: #check if our target is in the lower half (greater than the value we're searching)
            end = mid - 1 # then reassign 'end' to begin moving to the left of the array 
            
        else:
            found = True #set to true if the target is found
            return mid #return mid, which will give us the index of the target
        
    if not found: 
        return -1


arr = [2, 5, 8, 10, 16, 22, 25]
target = 16
result = binary_itr(arr, 0, len(arr)-1, target) #start is equal to 0, end is equal to the last item in the array meaning len(arr)-1 
print(result)
if result != -1:
    print('element is present at index:', result)
else: 
    print('element is not present in array')  
    
#Recursive Binary Search, using recursion

def binary_recursearch(arr, start, end, target):
    if end >= start: #checks if 'end' is greater than or equl to 'start'. If 'end; is less than 'start' it means that the search range is invalidd and returns -1, indicating that the target is not found in the array 
        mid = start + end -1 // 2 
    
        if arr[mid] < target:
            return binary_recursearch(arr, mid+1, end, target) #recursively calls binary_recursearch with the updated search range, mid + 1 as the new start and end remaining the same.
        
        elif arr [mid] > target: 
            return binary_recursearch(arr, end, mid-1, target) #recursively calls binary_recursearch with the updated search range, start remaining the same and mid - 1 as the new end.
        else: 
            return mid 
    else: 
        return - 1 
    
 
arr = [2, 5, 8, 10, 16, 22, 25]
target = 25
result = binary_recursearch(arr, 0, len(arr)-1, target) #start is equal to 0, end is equal to the last item in the array meaning len(arr)-1 

if result != -1:
    print('element is present at index:' + str(result))
else: 
    print('element is not present in array')  
        
        