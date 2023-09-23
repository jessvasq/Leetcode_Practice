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
 
# def ratios(arr):
#     n = len(arr)
     
#     positive = [arr.count(i) for i in arr if i > 0]
#     positive_ratio = '{:6f}'.format(len(positive) / n)
#     print(positive_ratio)
    
#     negative = [arr.count(i) for i in arr if i < 0]
#     negative_ratio = '{:6f}'.format(len(negative) / n)
#     print(negative_ratio)
    
#     zero_nums = [arr.count(i) for i in arr if i == 0]
#     zero_ratio = '{:6f}'.format(len(zero_nums) / n)
#     print(zero_ratio)
    
    
# arr = [1, 1, 0, -1, -1]
# print(ratios(arr))


'''Given five positive integers, find the minimum and maximum values that can be calculated by summing exactly four of the five integers. Then print the respective minimum and maximum values as a single line of two space-separated long integers.
Function Description
*Complete the miniMaxSum function in the editor below. miniMaxSum has the following parameter(s):
*arr: an array of 5 integers
Print
*Print two space-separated integers on one line: the minimum sum and the maximum sum of  of  elements.
Input Format
*A single line of five space-separated integers.
'''

# def minMaxSum(arr):
#     #sort array
#     arr.sort()
#     print(arr)
#     #using slice notation, find the sum of the first 4 int -> min_sum 
#     min_sum = sum(arr[:4])
#     #find the sum of the last 4 int -> max_sum 
#     max_sum = sum(arr[1:])

#     print(min_sum, max_sum)
    
# arr = [2, 5, 3, 4, 1]
# print(minMaxSum(arr))

'''Given a time in 12-hour AM/PM format, convert it to military (24-hour) time.
Note: - 12:00:00AM on a 12-hour clock is 00:00:00 on a 24-hour clock.
- 12:00:00PM on a 12-hour clock is 12:00:00 on a 24-hour clock.'''

#only thing that changes would be the first two integers, we need to add 12 
#check if it's 12 and 'AM', if True change it to '00' and add the remaining 
#check if the last two int -2 == 'PM'. If true 
# def timeConversions(s):
#     if s[-2:] == 'AM' and s[:2] == '12':
#         return '00' + s[2:-2]
#     elif s[-2:] == 'AM':
#         return s[:-2]
#     elif s[-2:] == 'PM' and s[:2] == '12':
#         return s[:-2]
#     else:
#         return str(int(s[:2]) + 12 ) + s[2:-2]

# s='02:20:20AM'
# print(timeConversions(s))

# '''MOCK TEST'''
# '''Find the median num in a given list'''

# test1 = [5, 4, 2, 8, 7]

# def find_median(arr):
#     #sort list 
#     arr.sort()
#     #using binary search, find the middle element/median
#     lo, hi = 0, len(arr)-1
#     mid = (lo+hi) // 2
#     return arr[mid]

# print(find_median(test1))


'''LONELY INTEGER'''
'''Given an array of integers, where all elements but one occur twice, find the unique element.'''

# def lonelyinteger(a):
#     #using count() method, count each element and return the element that occurs once or it's equal 1 
#     for i in a: 
#         if a.count(i) == 1:
#             return i
        

# a = [1,2,3,2,8,2,1]
# print(lonelyinteger(a))

'''DIAGONAL DIFFERENCE'''
'''Given a square matrix, calculate the absolute difference between the sums of its diagonals.'''

# def diagonal_difference(arr):
#     n = len(arr)
#     diagonal_sum1 = 0
#     diagonal_sum2 = 0
    
#     for i in range(n):
#         diagonal_sum1 += arr[i][i]
#         diagonal_sum2 += arr[i][n-i-1]

#     return abs(diagonal_sum1 - diagonal_sum2)

# arr = [
#       [11, 2, 4,],
#       [4, 5, 6,],
#       [10, 8, -12],
# ] 
# print(diagonal_difference(arr))


'''Counting Sort'''
'''Comparison Sorting
Quicksort usually has a running time of nxlog(n), but is there an algorithm that can sort even faster? In general, this is not possible. Most sorting algorithms are comparison sorts, i.e. they sort a list just by comparing the elements to one another. A comparison sort algorithm cannot beat nxlog(n)(worst-case) running time, since n x log(n) represents the minimum number of comparisons needed to know where to place each element.

Alternative Sorting
Another sorting method, the counting sort, does not require comparison. Instead, you create an integer array whose index range covers the entire range of values in your array to sort. Each time a value occurs in the original array, you increment the counter at that index. At the end, run through your counting array, printing the value of each non-zero valued index that number of times.
Challenge
Given a list of integers, count and return the number of times each value appears as an array of integers.'''


# arr1 = [63, 25, 73, 1, 98, 73, 56, 84, 86, 57, 16, 83, 8, 25, 81, 56, 9, 53, 98, 67, 99, 12, 83, 89, 80, 91, 39, 86, 76, 85, 74, 39, 25, 90, 59, 10, 94, 32, 44, 3, 89, 30, 27, 79, 46, 96, 27, 32, 18, 21, 92, 69, 81, 40, 40, 34, 68, 78, 24, 87, 42, 69, 23, 41, 78, 22, 6, 90, 99, 89, 50, 30, 20, 1, 43, 3, 70, 95, 33, 46, 44, 9, 69, 48, 33, 60, 65, 16, 82, 67, 61, 32, 21, 79, 75, 75, 13, 87, 70, 33,]
# arr1.sort()
# print(arr1)

# def count_frequencies(input_list):
    
#     # Initialize a frequency array with 100 elements, all set to 0
#     frequency_array = [0] * 100
    
#     # # Iterate through the input list
#     for num in input_list:
#     #   Increment the corresponding element in the frequency array
#         print('frequency', frequency_array[num])
#         frequency_array[num] += 1
    
#     # return frequency_array
#     return frequency_array

# # Example usage:
# input_list = [63, 25, 73, 1, 98, 73, 56, 84, 86, 57, 16, 83, 8, 25, 81, 56, 9, 53, 98, 67, 99, 12, 83, 89, 80, 91, 39, 86, 76, 85, 74, 39, 25, 90, 59, 10, 94, 32, 44, 3, 89, 30, 27, 79, 46, 96, 27, 32, 18, 21, 92, 69, 81, 40, 40, 34, 68, 78, 24, 87, 42, 69, 23, 41, 78, 22, 6, 90, 99, 89, 50, 30, 20, 1, 43, 3, 70, 95, 33, 46, 44, 9, 69, 48, 33, 60, 65, 16, 82, 67, 61, 32, 21, 79, 75, 75, 13, 87, 70, 33,]
# counts_array = count_frequencies(input_list)
# print(counts_array)  # Output: [2, 2, 1, 3, 1]

'''ZIG ZAG SEQUENCE'''


# def findZigZagSequence(a, n):
#     a.sort()
#     print('a', a)
#     mid = int((n + 1)/2)
#     # mid_num = a[mid]
#     # a[mid], a[n-1] = a[n-1], a[mid]

#     st = 0
#     ed = len(a)- 1
#     while(st <= ed):
#         mid_num = a[mid]
#         a[st], a[ed] = a[ed], a[st]
#         st = st + 1
#         ed = ed + 1

#     for i in range (n):
#         if i == n-1:
#             print(a[i])
#         else:
#             print(a[i], end = ' ')
#     return

# a = [1,2,3,4,5,6,7]  #outout: 1, 2, 3, 7, 6, 5, 4
# print(findZigZagSequence(a, 7))

'''Flipping the matrix'''

def maximize_upper_left_sum(matrix):
    #size of the upper-left quadrant
    n = len(matrix) // 2  
    #num of rows
    rows = len(matrix)
    #num of columns
    cols = len(matrix[0])

    # Sort rows in descending order based on their largest sums
    #key=lambda row: sum(row) is a lambda function that computes the sum of elements in each row. It is used as the sorting key.
    #reverse=True indicates that the sorting should be in descending order, so the rows with the largest sums will come first after sorting.
    matrix.sort(key=lambda row: sum(row), reverse=True)

    # Sort columns in descending order based on their sums
    #To sort columns in descending order based on their sums, we first transpose the matrix. Transposing swaps rows and columns.
    #the rows become columns and the columns become rows 
    transposed_matrix = [[matrix[j][i] for j in range(rows)] for i in range(cols)]
    
    # Sort columns in descending order based on their largest sums
    #key=lambda row: sum(row) is a lambda function that computes the sum of elements in each row. It is used as the sorting key.
    #reverse=True indicates that the sorting should be in descending order, so the columns with the largest sums will come first after sorting.
    #After this line of code, transposed_matrix will be sorted with columns having the largest sums in the upper part.
    transposed_matrix.sort(key=lambda col: sum(col), reverse=True)

    #  calculates the sum of elements in the upper-left quadrant of the original matrix (matrix). It uses nested list comprehensions to iterate over rows and columns within the upper-left quadrant and sums their elements.
    upper_left_sum = sum(sum(row[:n]) for row in matrix[:n])
    
    #calculates the sum of elements in the upper-left quadrant of the transposed matrix (transposed_matrix). Similarly, it uses nested list comprehensions to iterate over columns and rows in the transposed upper-left quadrant.
    transposed_upper_left_sum = sum(sum(col[:n]) for col in transposed_matrix[:n])


    #compare both (original & sorted) and return the largest sum
    if transposed_upper_left_sum > upper_left_sum:
        # If transposed_upper_left_sum is greater than upper_left_sum, it means that transposing the matrix resulted in a better upper-left sum, and you should use the transposed matrix for further processing.
        matrix = transposed_matrix

    #It returns the portion of the matrix that corresponds to the maximized upper-left quadrant
    #matrix[:n] is a list slicing operation. It extracts the first n rows of the matrix list, effectively selecting the upper-left quadrant of the matrix.
    return matrix[:n]
  

# Example usage:
g_matrices = [
    [
        [4, 3, 2, 1],
        [8, 7, 6, 5],
        [12, 11, 10, 9],
        [16, 15, 14, 13]
    ],
    # Add more matrices here
]

for matrix in g_matrices:
    result = maximize_upper_left_sum(matrix)
    print("Maximized Upper-Left Quadrant:")
    for row in result:
        print(row)
    print()
