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


#OPTIMIZED SOLUTION
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

# only thing that changes would be the first two integers, we need to add 12 
# check if it's 12 and 'AM', if True change it to '00' and add the remaining 
# check if the last two int -2 == 'PM'. If true 
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

'''MOCK TEST'''
'''Find the median num in a given list'''

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

# def flippingMatrix(matrix):
#     n = len(matrix) // 2
#     count = 0

#     #nested loop 
#     #iterates through rows from 0 to n-1 
#     for i in range(n):
#         #iterates through columns from 0 to n-1 
#         for j in range(n):
#             #increments count variable 
#                         #matrix[i][j]: value at the current row 'i' and column 'j
#                         #matrix[i][~j]: value at the current row i and the corresponding column
#                         #matrix[~i][j]: value at the corresponding row in the lower-left quadrant and the current column j
#                         #matrix[~i][~j]: value at the corresponding row in the lower-right quadrant and the corresponding column.
                        
#             count += max(matrix[i][j], matrix[i][~j], matrix[~i][j], matrix[~i][~j])

#     return count #is the sum of the maximum values from each quadrant of the input matrix


'''ZIG ZAG'''
'''Given an array of  distinct integers, transform the array into a zig zag sequence by permuting the array elements. A sequence will be called a zig zag sequence if the first  elements in the sequence are in increasing order and the last  elements are in decreasing order, where . You need to find the lexicographically smallest zig zag sequence of the given array.'''

# def findZigZagSequence(a, n):
#     a.sort()
#     mid = int((n + 1)/2) - 1
#     a[mid], a[n-1] = a[n-1], a[mid]

#     st = mid + 1
#     ed = n - 2
#     while(st <= ed):
#         a[st], a[ed] = a[ed], a[st]
#         st = st + 1
#         ed = ed - 1

#     for i in range (n):
#         if i == n-1:
#             print(a[i])
#         else:
#             print(a[i], end = ' ')
#     return


'''TOWER BREAKERS'''
'''Two players are playing a game of Tower Breakers! Player 1 always moves first, and both players always play optimally.The rules of the game are as follows:
Initially there are n towers.
Each tower is of height m.
The players move in alternating turns.
In each turn, a player can choose a tower of height  and reduce its height to y , where 1 is less or equal than y and Y is less than x; and y evenly divides x.
If the current player is unable to make a move, they lose the game.
Given the values of  n and m, determine which player will win. If the first player wins, return 1. Otherwise, return 2.'''

# def towerBreakers(n, m):
#     if n == 1 or m == 1 or n% 2 == 0:
#         return 1
#     else:
#         return 2 
    

'''Julius Caesar protected his confidential information by encrypting it using a cipher. Caesar's cipher shifts each letter by a number of letters. If the shift takes you past the end of the alphabet, just rotate back to the front of the alphabet. In the case of a rotation by 3, w, x, y and z would map to z, a, b and c'''    

# def ceaser_cipher(s, k):
#     #initialized a variable to store the encrypted pw 
#     encrypted_pw = ''
    
#     #iterate through the string 
#     for letter in s:
#         #check if the letter is in the alphabet 
#         if letter.isalpha():
#             #returns True if all characters are in upper case, otherwise False 
#             is_upper = letter.isupper()
            
#             #convert all characters to lowercase 
#             letter = letter.lower()
            
#             #ord() returns the unicode code point(int) 
#             #ord('a'): computes the Unicode code point of the lowercase letter 'a'.  used as a reference point to make calculations based on the alphabet's position.
            
#             #(ord(letter) - ord('a')): calculates the position of the character letter within the lowercase alphabet. By subtracting the code point of 'a' from the code point of the character, you get a number that represents the character's position in the alphabet
#             #k - num of positions to shift the character 
#             # %26 ensures that the shifted position remains within the alphabet, which has 26 letters. If it goes beyond 'z' and starts again at 'a'
#             shifted = (ord(letter) - ord('a') + k) % 26
            
#             #convert the unicode into a character 
#             shifted_letter = chr(shifted + ord('a'))
            
            
#             if is_upper:
#                 #convert back to upper if the original pw was uppercase
#                 shifted_letter = shifted_letter.upper()
            
#             encrypted_pw += shifted_letter
            
#         else:
#             encrypted_pw += letter #letter is the character that has undergone the shift
    
#     return encrypted_pw


# s = "There's-a-starman-waiting-in-the-sky"
# k = 3
    
# print(ceaser_cipher(s, k))


'''GRID CHALLENGE'''
'''Given a square grid of characters in the range ascii[a-z], rearrange elements of each row alphabetically, ascending. Determine if the columns are also in ascending alphabetical order, top to bottom. Return YES if they are or NO if they are not.'''

# grid = ['abc', 'ade', 'efg']
# grid1 = ['mpxz', 'abcd', 'wlmf']

# def grid_challenge(grid):
#     #each row of the grid is sorted alphabetically by converting the row string into a list of characters, sorting the list, and then joining the sorted characters back into a string
#     for row in range(len(grid)):
#         sorted_row = sorted((grid[row]))
#         sorted_row=''.join(sorted_row)
#         grid[row] = sorted_row
    
    
#     num_cols = len(grid[0])
#     print(num_cols)
#     for col in range(num_cols):
#         #check whether the columns of the sorted grid are in ascending alphabetical order from top to bottom
 
#         # check whether the columns are sorted
#         #iterates through each row except the last row (len(grid)-1). It compares the character at the current column and row with the character at the same column in the next row. If it finds that the character in the current row is greater (lexicographically) than the character in the next row, it means the columns are not in ascending alphabetical order
#         for row in range(len(grid)-1):
            
#             if grid[row][col] > grid[row + 1][col]:
#                 return "NO"  # Columns are not sorted

#     # Step 3: If all columns are sorted, return "YES"
#     return "YES"
        
# print(grid_challenge(grid1))


'''RECURSIVE DIGIT SUM'''
'''We define super digit of an integer  using the following rules:

Given an integer, we need to find the super digit of the integer.
If  has only  digit, then its super digit is .
Otherwise, the super digit of  is equal to the super digit of the sum of the digits of . Complete the function superDigit in the editor below. It must return the calculated super digit as an integer.
superDigit has the following parameter(s):
string n: a string representation of an integer
int k: the times to concatenate n to make p
Returns
int: the super digit of n repeated k times
'''        


# def superDigit(n, k):
#     def recursive_sum(n):
#         count = 0
#         for num in n:
#             count += int(num)
#         count = str(count)
        
#         if len(count) == 1:
#             return count
#         else: 
#             return recursive_sum(count)

#     #use recursive function
#     p = str(recursive_sum(n)*k)
#     return recursive_sum(p)

# #TEST CASE
# n='9875'
# k=4
# print(superDigit(n,k))


'''NEW YEAR CHAOS'''
'''It is New Year's Day and people are in line for the Wonderland rollercoaster ride. Each person wears a sticker indicating their initial position in the queue from 1 to n. Any person can bribe the person directly in front of them to swap positions, but they still wear their original sticker. One person can bribe at most two others.
Determine the minimum number of bribes that took place to get to a given queue order. Print the number of bribes, or, if anyone has bribed more than two people, print Too chaotic.
'''


# q1 = [1, 2, 3, 5, 4, 6, 7, 8]
# q = [2,1,5,3,4]


# def min_bribes(q):
#     total = 0
#     n=len(q)
    
#     for num in range(n):
        
#         if q[num] - (num + 1) > 2:
#             print('Too chaotic')
#             return
        
            
#         #q[num] - 2 calculates the lowest possible position in the queue from which a person could have bribed the person at position i. This is because a person can only bribe at most two others, so they cannot move more than two positions ahead. Therefore, q[i] - 2 is the lower bound on the position we want to start checking for potential bribers.
#         # ensures that we don't go below the first position in the queue (position 0).
#         #num represents the current position of the person for whom we are counting bribes.
#         for el in range(max(0, q[num]-2), num):
#             if q[el] > q[num]:
#                 total += 1
#     return total 

# print(min_bribes(q))       

'''--------------------------------------------------------------------------------LINKED LISTS---------------------------------------------------------------------------------------------------'''

'''MERGE TWO SORTED LINKED LIST'''
'''Given pointers to the heads of two sorted linked lists, merge them into a single, sorted linked list. Either head pointer may be null meaning that the corresponding list is empty.'''


# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#


# def mergeLists(head1, head2):
#     #if one list is empty, return the other list
#     if not head1:
#         return head2
#     if not head2:
#         return head1
    
#     merged_head = None #keep track of the head of the merged list 
#     current = None #keep track of the current node 
    
#     #iterate through both lists (head1 and head2) simultaneously, comparing the data values of nodes and linking them in ascending order to create the merged list.
#     while head1 and head2: 
#         if head1.data <= head2.data:
#             if merged_head is None: 
#                 merged_head = head1
#                 current = merged_head
#             else: 
#                 current.next = head1
#                 current = current.next
#             head1 = head1.next
#         else:
#             if merged_head is None: 
#                 merged_head = head2
#                 current = merged_head
#             else: 
#                 current.next = head2
#                 current = current.next
#             head2 = head2.next
#     #append remaining nodes, if one list is shorter than the other one 
#     if head1:
#         current.next = head1
#     if head2:
#         current.next = head2
    
#     return merged_head

'''PRINT THE ELEMENTS OF A LINKED LIST'''
'''Given a pointer to the head node of a linked list, print each node's DATA element, one per line. If the head pointer is null (indicating the list is empty), there is nothing to print.
Function Description
-Complete the printLinkedList function in the editor below.
-printLinkedList has the following parameter(s):
-SinglyLinkedListNode head: a reference to the head of the list
Print
-For each node, print its DATA value on a new line (console.log in Javascript)'''
                

# def printLinkedList(head):
#     if head is None:
#         print(None)
    
#     current = head
    
#     while current is not None:
#         print(current.data)
#         current = current.next
        
# '''Insert a node at the head of a linked list'''
# '''Given a pointer to the head of a linked list, insert a new node before the head. The NEXT value in the new node should point to HEAD and the DATA value should be replaced with a given value. Return a reference to the new head of the list. The head pointer given may be null meaning that the initial list is empty.'''

# def insertNodeAtHead(list1, data):
#     new_node = SinglyLinkedListNode(data) #SinglyLinkedListNode Class is given
#     new_node.next = list1
#     list1 = new_node
    
#     return list1 

'''Insert a Node at the Tail of a Linked List'''
'''You are given the pointer to the head node of a linked list and an integer to add to the list. Create a new node with the given integer. Insert this node at the tail of the linked list and return the head node of the linked list formed after inserting this new node. The given head pointer may be null, meaning that the initial list is empty.'''
        
 
# def insertNodeAtTail(head, data):
#     new_node = SinglyLinkedListNode(data)
#     new_node.next = None
#     current = head
  
#     if current is None:
#         head = new_node
#         return head
    
#     while current.next is not None: 
#         current = current.next
#     current.next = new_node
        
#     return head
        
           
'''Print in Reverse'''       
'''Given a pointer to the head of a singly-linked list, print each DATA value from the reversed list. If the given list is empty, do not print anything.'''

# def reversePrint(llist):
#     if llist is None:
#         return
#     #use a recursive function and pass the next element in the list until head is none which means we've reached the end of the list, so the recursion starts to backtrack
#     reversePrint(llist.next)
#     #prints in reverse order (backtrack) because the recursive function is called before the 'print' statement
#     print(llist.data)
          
'''Reverse a linked list'''
'''Given the pointer to the head node of a linked list, change the next pointers of the nodes so that their order is reversed. The head pointer given may be null meaning that the initial list is empty.'''

# def reverse(llist):
#     if llist is None:
#         return 
#     current = llist #points to the head
#     previous = None #previous points to the previous element 
#     following = current.next #points at the second element 

#     while current: #loop till the we reach the tail 
#         current.next = previous #reverse the link
#         previous = current  #move 'previous' one step aheaad
#         current = following #move 'current' one step ahead
#         if following: #if this was not the last element
#             following = following.next #move 'following' one step ahead 
#     llist = previous
#     return llist


'''Delete a Node'''
'''Delete the node at a given position in a linked list and return a reference to the head node. The head is at position 0. The list may be empty after you delete the node. In that case, return a null value.'''

# def delete_at_position(llist, position):
#     current = llist 
#     count = 0 
    
#     # checks if the position to delete is the head of the linked list (position 0). If so, it immediately returns current.next, effectively removing the current head and returning the new head.
#     if position == 0:
#         return current.next
        
#     while current and count < position -1:
#         current = current.next 
#         count += 1
        
#     if current is None or current.next is None: 
#         return None
    
#     current.next = current.next.next  
    
#     return llist


'''CYCLE DETECTION'''
'''A linked list is said to contain a cycle if any node is visited more than once while traversing the list. Given a pointer to the head of a linked list, determine if it contains a cycle. If it does, return 1. Otherwise, return 0.'''


# def has_cycle(head):
#     slow = head
#     fast = head
    
#     if head is None:
#         return None
    
#     while slow != None and fast != None:
#         slow = slow.next
#         fast = fast.next.next
        
#         if slow == fast:
#             return 1
      
#     return 0 
        

'''Inserting a Node Into a Sorted Doubly Linked List'''   
'''Given a reference to the head of a doubly-linked list and an integer, DATA, create a new DoublyLinkedListNode object having data value DATA and insert it at the proper location to maintain the sort.'''

#we need to traversee the list to find the correct position where the node should be inserted


# def sortedInsert(llist, data):
#     #create new node 
#     new_node = DoublyLinkedListNode(data)
    
#     #if the list is empty or the new node's data is smaller than the head's data
#     if llist is None or data < llist.data:
#         new_node.next = llist
#         if llist:
#             llist.prev = new_node
#         return new_node
    
#     current = llist
    
#     #traverse the list 
#     while current.next and current.next.data < data:
#         current = current.next
        
#     #insert 
#     new_node.next = current.next
#     if current.next:
#         current.next.prev = new_node
#     current.next = new_node
#     new_node.prev = current
    
#     return llist
        
        
'''----------------------------------------------------------------------------------TWO POINTERS-------------------------------------------------------------------------------------------------'''
'''1877. Minimize Maximum Pair Sum in Array'''
'''The pair sum of a pair (a,b) is equal to a + b. The maximum pair sum is the largest pair sum in a list of pairs.
-For example, if we have pairs (1,5), (2,3), and (4,4), the maximum pair sum would be max(1+5, 2+3, 4+4) = max(6, 5, 8) = 8.
Given an array nums of even length n, pair up the elements of nums into n / 2 pairs such that:
-Each element of nums is in exactly one pair, and
-The maximum pair sum is minimized.
Return the minimized maximum pair sum after optimally pairing up the elements.
'''


# def minPairSum(nums):
#     nums = sorted(nums)
#     lo = 0 
#     hi = len(nums)-1
    
#     n = len(nums)
#     if n % 2 != 0:
#         return 
    
#     num_sum = 0 # store the maximum pair sum found during the iteration
    
#     #loop stops when these two pointers meet or cross each other 
#     while lo < hi:
#         #In each iteration, calculate the sum of lo and hi in the sorted list. It then updates num_sum to store the maximum of its current value and the newly calculated sum. It ensures that num_sum always contains the maximum pair sum found so far
#         num_sum = max(num_sum, nums[lo] + nums[hi])
#         lo += 1 #after calculating the sum, move lo one step to the right
#         hi -= 1 #after calculating the sum, move hi one step to the left
    
#     return num_sum

# nums = [3,5,2, 3]
# print(minPairSum(nums))      

'''26. Remove Duplicates from Sorted Array'''
'''Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements in nums.

Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially. The remaining elements of nums are not important as well as the size of nums.
Return k.
'''        

# def removeDuplicates(nums):
#     unique_el = 1 #start at 1 as we assume that the first element is unique
    
#     for i in range(1, len(nums)):
#         if nums[i] != nums[i-1]: #check if the current element is not the same as the previous element (nums[i-1])
#             nums[unique_el] = nums[i]  # the unique element is found, it is assigned to the position indicated by the nums[unique_el] pointer
#             unique_el += 1 #increment by 1, which will be the position for the next element

#     #unique_el represents the lenght of the unique elements, nums returs the modified list with duplicates removed or placed at the end of the list
#     #return unique_el, nums
#     return unique_el #problem states: return k or in this case unique_el
    


# nums1 = [0,0,1,1,1,2,2,3,3,4]
# print(removeDuplicates(nums1))
            
'''148. Sort List'''
'''Given the head of a linked list, return the list after sorting it in ascending order.'''

# def sortList(head):
    
    
#     if head is None or head.next is None:
#         return head
        
#     #split the linked list 
#     left = head
#     right = self.findMid(head)
#     current = right.next
#     right.next = None
#     right = current
        
#     #sort both sides 
#     left_sort = self.sortList(left)
#     right_sort = self.sortList(right)
#     return self.merge(left_sort, right_sort)


# def find_mid(self, head):
#     slow=head
#     fast=head 
        
#     while fast.next and fast.next:
#         slow = slow.next #increment slow by one
#         fast = fast.next.next #increment by two 
#     return slow #slow will be at the middle value
    
# def merge(self, list1, list2):
#     dummy = ListNode()
#     tail = dummy
        
#     while list1 and list2:
#         if list1.data < list2.data:
#             tail.next = list1
#             list1 = list1.next
#         else:
#             tail.next = list2
#             list2 = list2.next 
#         tail = tail.next
#     if list1:
#         tail.next = list1
            
#     if list2: 
#         tail.next = list2 
            
#     return dummy.next 
    
'''88. MERGE SORTED ARRAY'''
'''You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.'''    

# def merge(nums1, nums2, n, m):
#     p1 = m-1
#     p2 = n-1
#     merged_pointer = m + n-1
    
#     while p1 >= 0 and p2 >= 0:
#         if nums1[p1] > nums2[p2]:
#             nums1[merged_pointer] = nums1[p1]
#             p1 -= 1
#         else:
#             nums1[merged_pointer] = nums2[p2]
#             p2 -= 1
#         merged_pointer -= 1
    
#     while p2 >= 0:
#         nums1[merged_pointer] = nums2[p2]
#         p2 -= 1
#         merged_pointer -= 1

# nums1  = [1,2,3,0,0,0]
# nums2 = [2,5,6]
# m=3
# n=3
# print(merge(nums1, nums2, m, n))

'''20. VALID PARENTHESES'''
'''Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if:
Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
'''
# s = "(){}}{"

# def isValid(s):
#     stack = []
#     brackets = {')': '(', '}': '{', ']': '['}

#     for char in s:
#         if char in brackets.values():
#             stack.append(char)
#         #Check the dictionary key to see if there's a closing bracket
#         elif char in brackets.keys():
#             # check if the 'stack' is empty. If it is it means there's no matching bracket
#             # checks whether the most recent open bracket matches the current closing bracket
#             print(brackets.keys())
#             if not stack or stack.pop() != brackets[char]: #pop() removes an element at a specified position
#                 return False
#         else:
#             return False

#     return not stack

# print(isValid(s))

'''125. Valid Palindrome'''
'''A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.
Given a string s, return true if it is a palindrome, or false otherwise.'''

# s = ""

# def isPalindrome(s):
#     #Using list-comprehension, convert to lowercase and remove all non-alphanumeric characters     
#     lower_s = ''.join(char.lower() for char in s if char.isalnum())
#     print(lower_s)


#     reversed_s=lower_s[::-1]
#     if lower_s == reversed_s:
#         return True 
#     else:
#         return False

        
# print(isPalindrome(s))

'''----------------------------------------------------------------------------------WINDOW SLIDING TECHNIQUE--------------------------------------------------------------------------------------------'''
'''Given an array of integers of size ‘n’, Calculate the maximum sum of ‘k’ consecutive elements in the array.'''

# def maxSum(arr, k):
#     n=len(arr)
    
#     if n < k:
#         return
    
#     #calculate sum of the first window
#     window_sum = sum(arr[:k])
#     max_sum = window_sum
    
#     #calculate sum of the remaining windows
#     for i in range(n-k):
#         print('arr[i]', arr[i])
#         print('arr[i+k]', arr[i+k])
#         window_sum = window_sum - arr[i] + arr[i+k]
#         max_sum = max(max_sum, window_sum)
        
#     return max_sum


# arr = [1, 4, 2, 10, 2, 3, 1, 0, 20]
# k=4

# print(maxSum(arr, k))


'''643. Maximum Average Subarray I'''
'''You are given an integer array nums consisting of n elements, and an integer k.
Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. Any answer with a calculation error less than 10-5 will be accepted.
'''

# def findMaxAverage(nums, k):
#     n = len(nums)
#     if n == 0 or n < k:
#         return 
    
#     max_sum = sum(nums[:k])
#     current_sum = max_sum 
        
#     for i in range(k, n):
#         # Add the next element and subtract the first element in the window
#         current_sum += nums[i] - nums[i-k]
#         max_sum = max(max_sum, current_sum) 
   
#     avg_sum = max_sum / k
#     return avg_sum
    
# nums = [1,12,-5,-6,50,3]
# k=4
# print(findMaxAverage(nums, k))


# '''56. MERGE INTERVALS'''
# '''Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.'''

# intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]


#First solution 

# def merge_intervals(intervals):
#     #sort the array 
#     intervals.sort(key=lambda index : index[0])
#     #stores the merged intervals as we iterate through the intervals
#     non_overlapping_arr = [intervals[0]] #Output= [[1,3]] first interval located at index 0 
#     print(intervals)
#     print(non_overlapping_arr)
#     # end=non_overlapping_arr[-1][1]
#     # print('end' ,end)

#     for s, e in intervals[1:]:
#         #non_overlapping_arr[-1] -- accesses the last interval in the 'merged_intervals', which is the most recently merged interval. [1] accesses the end element inside the most recently merged interval 
#         end=non_overlapping_arr[-1][1]
#         print('end' ,end)
        
#         #compare the start of the current interval with the end time of the previous interval to check if there' san overlap 
#         if s <= end:                    #end stores the end value of the previous merged interval. While 'e' is the original value of the current interval 
#             #To merge them, we update the end time of the previous_interval to the maximum of the current interval
#             non_overlapping_arr[-1][1] = max(end, e)
            
#         else: 
#             non_overlapping_arr.append([s, e])
#     return non_overlapping_arr
        
        
#Second solution

# def merge_intervals(intervals):
#     if not intervals:
#         return []

#     # Sort the intervals by their start times
#     intervals.sort(key=lambda x: x[0])

#     merged_intervals = [intervals[0]]
    
#     for i in range(1, len(intervals)):
#         current_interval = intervals[i]
#         previous_interval = merged_intervals[-1]

#         # If the current interval overlaps with the previous one, merge them
#         if current_interval[0] <= previous_interval[1]:
#             previous_interval[1] = max(previous_interval[1], current_interval[1])
#         else:
#             # If there is no overlap, add the current interval to the merged_intervals
#             merged_intervals.append(current_interval)
    
#     return merged_intervals

# print( merge_intervals(intervals) )

'''19. BINARY TREE RIGHT SIDE VIEW'''
'''Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom'''

# from collections import deque
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
        
# def rightSideView(root):
#     if not root:
#         return 

#     result = []  # Initialize an empty list to store the values of the rightmost nodes.
#     q = deque()  # Create a deque (a double-ended queue) to perform level-order traversal.
#     q.append(root)  # Add the root node to the queue.

#     while q:
#         rightSide = None  # Initialize a variable to keep track of the rightmost node at each level.
#         n = len(q)  # Get the number of nodes at the current level.

#         for i in range(n):
#             node = q.popleft()  # Dequeue (remove and return) the leftmost node from the queue.
#             if node:
#                 rightSide = node  # Update the rightmost node with the current node.
#                 q.append(node.left)  # Enqueue the left child of the current node.
#                 q.append(node.right)  # Enqueue/add/push the right child of the current node so we can then take the rightmost value and append it to the result

#         if rightSide:
#             result.append(rightSide.val)  # Add the value of the rightmost node to the result list.

#     return result

# root = TreeNode(1)
# root.left = TreeNode(2)
# root.right = TreeNode(3)
# root.left.right = TreeNode(5)
# root.right.right = TreeNode(4)

# print(rightSideView(root))

'''BINARY TREE LEFT SIDE VIEW'''
'''Given the root of a binary tree, imagine yourself standing on the left side of it, return the values of the nodes you can see ordered from top to bottom'''

# from collections import deque
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
        
# def leftSideView(root):
#     if not root:
#         return 

#     result = []  # Initialize an empty list to store the values of the leftmost nodes.
#     q = deque()  # Create a deque (a double-ended queue) to perform level-order traversal.
#     q.append(root)  # Add the root node to the queue.

#     while q:
#         leftSide = None  # Initialize a variable to keep track of the leftmost node at each level.
#         n = len(q)  # Get the number of nodes at the current level.

#         for i in range(n):
#             node = q.popleft()  # Dequeue (remove and return) the leftmost node from the queue.
#             if node:
#                 leftSide = node  # Update the leftmost node with the current node.
#                 q.append(node.right)  # Enqueue the left child of the current node.
#                 q.append(node.left)  # Enqueue/add/push the right child of the current node so we can then take the leftmost value and append it to the result

#         if leftSide:
#             result.append(leftSide.val)  # Add the value of the leftmost node to the result list.

#     return result

# root = TreeNode(1)
# root.left = TreeNode(2)
# root.right = TreeNode(3)
# root.left.right = TreeNode(5)
# root.right.right = TreeNode(4)

# print(leftSideView(root))


'''338. Counting Bits'''
'''Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.'''

# n=2

# def countBits(n):
#     result = [0] * (n+1)
    
#     for i in range(1, n+1):
#         #calculate the number of 1's in the binary representation of the integer i
#         result[i] = result[i >> 1] + (i & 1)
        
#     return result


'''Given two integers x and n, write a function to compute xn. We may assume that x and n are small and overflow doesn’t happen.'''

#Naive Approach. Time ciomplexity: O(n), Space complexity: O(1)
# def power(x, n):
 
#     # initialize result by 1
#     ans = 1
 
#     # Multiply x for n times
#     for i in range(n):
#         ans = ans * x
 
#     return ans
# x=2
# n=3
# print(power(x,n))

#using Divide and conquer approach. Time Complexity O(n), Space Complexity O(n)
# def power_1(x, n):
 
#     # base condition
#     if n == 0:
#         return 1
 
#     # calculate subproblem recursively, pow is the recursive function
#     pow = power(x, n // 2)
 
#     # if n is even
#     if n % 2 == 0:
#         return pow * pow
 
#     # if n is odd
#     else:
#         return x * pow * pow

# print(power_1(x, n))

# #using ** operator. Time Complexity O(log n), Space Complexity O(1)
# def power_2(x, n):
#     return x ** n

# print(power_2(x, n))
