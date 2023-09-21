'''HACKERRANK'''
'''An array is a type of data structure that stores elements of the same type in a contiguous block of memory. In an array, , of size , each memory location has some unique index,  (where ), that can be referenced as  or .
Reverse an array of integers.

Function Description
Complete the function reverseArray in the editor below.
reverseArray has the following parameter(s):
int A[n]: the array to reverse
Returns
int[n]: the reversed array
Input Format

The first line contains an integer, , the number of integers in .
The second line contains  space-separated integers that make up .

'''

# def reverse_arr(arr):
#     reversed_arr = arr[::-1]
#     print(reversed_arr)
#     return reversed_arr


# test0 = [1, 4, 3, 2]
# print(reverse_arr(test0))

'''2D ARRAY'''
'''Declare a 2-dimensional array, , of  empty arrays. All arrays are zero indexed.
Declare an integer, , and initialize it to .
There are  types of queries, given as an array of strings for you to parse:

Query: 1 x y
Let .
Append the integer  to .
Query: 2 x y
Let .
Assign the value  to .
Store the new value of  to an answers array.
Note:  is the bitwise XOR operation, which corresponds to the ^ operator in most languages. Learn more about it on Wikipedia.  is the modulo operator.
Finally, size(arr[idx]) is the number of elements in arr[idx]

Function Description

Complete the dynamicArray function below.

dynamicArray has the following parameters:
- int n: the number of empty arrays to initialize in 
- string queries[q]: query strings that contain 3 space-separated integers

Returns
int[]: the results of each type 2 query in the order they are presented
Input Format

The first line contains two space-separated integers, , the size of  to create, and , the number of queries, respectively.
Each of the  subsequent lines contains a query string, .

'''

#dynamic array that processes a series of queries, appending values to specific dynamic arrs based on type 1 queries and retrieving values from dynamic arrs for type 2 queries 

# def dynamicArray(n, queries):
#     #initialize lastAns to 0
#     lastAns = 0 
#     arr = list() #empty list
#     ans_arr = list() #empty list 
    
#     #initializes the arr list by appending n empty lists to it, creating an array of empty lists, where each list represents a dynamic array.
#     for value in range(0, n):
#         arr.append(list())
        
#     #loop through each query in the input queries 
#     for query in queries: 
#         query_type = query[0]
#         x = query[1]
#         y = query[2]
        
#         #check the type of query, if it's 1 it means it's a type 1 query 
#         if query_type == 1: 
#             #calculate idx based on the formula provided, THis formula determines which dynamic arr we should append 'y' to
#             idx = (x^lastAns)%n
#             #appends y 
#             arr[idx].append(y)
            
#         #check if it's a type 2 query
#         elif query_type == 2: 
#             #calculate idx using the same formula 
#             idx = (x^lastAns)%n
#             #retrieve the value at the index 'y' from the dynamic arr 
#             lastAns = arr[idx][y%len(arr[idx])]
#             #append the retrieved value of lastAns to the ans list 
#             ans_arr.append(lastAns)
#     #return list containing all the results of all type 2 queries 
#     return ans_arr  

 
'''A left rotation operation on an array of size n  shifts each of the array's elements 1 unit to the left. Given an integer, d , rotate the array that many steps left and return the result. 

Function Description

Complete the rotateLeft function in the editor below.
rotateLeft has the following parameters:
int d: the amount to rotate by
int arr[n]: the array to rotate
Returns

'''   

# #SIMPLE SOLUTION 

# def rotate_left(arr, d):
#     last = len(arr)-1
    
#     #iterates d times 
#     for i in range(0, d): 
#         print(i)
#         #assign the value of the first element to 'first'
#         first = arr[0]
        
        
#         for e in range(0, last):
#             #Inside the loop, each element at index e is replaced with the element at index e+1
#             arr[e] = arr[e+1]
#             print(arr[e])
    
#     #After the second loop, the first element is assigned to the last position of the array
#         arr[last] = first
#     return arr 


# #OPTIMIZED SOLUTION
# def rotate_l(arr, d):
#     #slice notation 
#     rotated_arr = arr[d:] + arr[:d]
#     return rotated_arr
    
    
# arr = [1,2,3,4,5]
# arr1 = [1,2,3,4,5]
# d=2
# print(rotate_left(arr, d))
# print(rotate_l(arr1, d))


'''There is a collection of input strings and a collection of query strings. For each query string, determine how many times it occurs in the list of input strings. Return an array of the results.'''

# def matchingStrings(stringList, queries):
#     #count() --> return the number of times a specific value appears in a certain list 
#     #use list comprehension
#     match = [stringList.count(query) for query in queries]

#     return match
      
    

# stringList = ['ab', 'ab', 'abc']
# queries = ['ab', 'abc', 'bc']


# print(matchingStrings(stringList, queries))

'''PLUS MINUS'''
'''Given an array of integers, calculate the ratios of its elements that are positive, negative, and zero. Print the decimal value of each fraction on a new line with  places after the decimal.

Note: This challenge introduces precision problems. The test cases are scaled to six decimal places, though answers with absolute error of up to  are acceptable.'''

#find positive nums 
#count negative nums 
#count 0 
#divide positive by n to find the ratio
#divide negative #s by n to find the ratio

def ratios(arr):
    n = len(arr)
     
    positive = [arr.count(i) for i in arr if i > 0]
    positive_ratio = '{:6f}'.format(len(positive) / n)
    print(positive_ratio)
    
    negative = [arr.count(i) for i in arr if i < 0]
    negative_ratio = '{:6f}'.format(len(negative) / n)
    print(negative_ratio)
    
    zero_nums = [arr.count(i) for i in arr if i == 0]
    zero_ratio = '{:6f}'.format(len(zero_nums) / n)
    print(zero_ratio)
    
    
arr = [1, 1, 0, -1, -1]
print(ratios(arr))