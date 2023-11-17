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
        
        
'''SORTING'''
'''OPTIMIZED BUBLE SORT'''
''' Bubble sort is a simple sorting algorithm that repeatedly steps through the list, compares adjacent elements, and swaps them if they are in the wrong order. The optimization in this code is that it keeps track of the number of iterations performed. Bubble sort is not the most efficient sorting algorithm, especially for large datasets, as it has a worst-case time complexity of O(n^2). However, it is straightforward to implement and can be useful for small datasets or educational purposes '''#this algo is not that efficient but important to understand. This algo can be used to quickly find if the array is sorted 
#An optimized algo for the bubble sort is to find the largest nth element and put it at the end of the array

def bubble_optimized(arr): #takes the list of elements to be sorted
    iterations = 0 #will be used to count the number of iterations(comparisons and swaps) made during the sorting process, useful to understand the efficiency of the sorting algo 
    for i in range(len(arr)): #This loop controls the number of passes through the array. In each pass, the largest unsorted element will "bubble up" to its correct position.

        for j in range(len(arr)-i-1): #nested loop. This loop goes through the unsorted portion of the array. Since after each pass, the largest element is placed at the end of the unsorted portion, we reduce the inner loop's range by i elements to avoid unnecessary comparisons.
            iterations += 1 #With each iteration of the inner loop, the variable iterations is incremented by 1
            if arr[j] > arr[j+1]: #if the current element is greater than the next element, it means they're not in order, so a sawap is performed using a tuple assignment. This swap puts the larger element in its correct position relative to the smaller one 
                arr[j], arr[j+1] = arr[j+1], arr[j] #tuple assignment 
    return arr, iterations

arr = [2, 5, 1, 9, 4, 3, 1]
print(bubble_optimized(arr))


'''INSERTION SORT'''
'''simple sorting algorithm that builds the final sorted array one item at a time.'''
def insert_sort(arr1):
    for element in range(1, len(arr1)): #loop that iterates over the elements of the list starting from the second element (index 1) and going up to the last element. The reason for starting at index 1 is that the first element is considered to be sorted by itself initially.
        key = arr1[element] #The reason for starting at index 1 is that the first element is considered to be sorted by itself initially.
        i = element -1 #i is initialized to element - 1, which is the index of the element immediately before the current element.
        while i >= 0 and arr1[i] > key: #compare the key with elements in the sorted subarray (elements before the current element). The loop continues as long as i is greater than or equal to 0 (ensuring we don't go out of bounds) and the element at arr1[i] is greater than key.
            arr1[i+1] = arr1[i] # if condition is true, it means that the element at arr1[i] should be moved to the right to make space for key. This is done by assigning arr1[i] to arr1[i+1]. Essentially, we shift elements in the sorted subarray to the right until we find the correct position for key.
            i -= 1
        arr1[i + 1] = key #After exiting the while loop, we have found the correct position for key, and we insert it by assigning key to arr1[i + 1].
        
        #The process continues for each element in the list, gradually building the sorted subarray. At the end of the loop, the entire list is sorted in ascending order.The sorted arr1 is modified in-place, so there is no need to return it explicitly from the function.

arr1 = [20, 4, 10, 2, 3, 1]
insert_sort(arr1)
print(arr1)
        

'''SELECTION SORT'''
'''Repeatedly finds the smallest or largest element in the unsorted subarray and places it at the beginning of the unsorted subarray. The sorted subarray is built up one element at a time. '''

def selection_sort(arr):
    for i in range(len(arr)):
        #min_idx is initialized to i, which is the index of the first element in the unsorted subarray.
        min_idx = i
        
        #j iterates over the remaining elements in the unsorted subarray. If an element at index j is smaller than the element at min_idx, then min_idx is updated to j.
        for j in range(i+1, len(arr)):
            if arr[min_idx] > arr[j]:
                min_idx = j
            
        #After finding the smallest element in the unsorted subarray, it is swapped with the element at the beginning of the unsorted subarray.
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        
    return arr

arr = [20, 4, 10, 2, 3, 1]
print(selection_sort(arr))


'''MERGE SORT
Divides an array into two halves, sorts each half separately, and then merges them into a single sorted array. The merge() function is used for merging two halves. The merge(arr, l, m, r) is a key process that assumes that arr[l..m] and arr[m+1..r] are sorted and merges the two sorted subarrays into one. '''


def merge_sort(arr):
    if len(arr) > 1: #checks if the length of the array is greater than 1. If not, it means that the array is already sorted.
        mid = len(arr) // 2 #mid is calculated by dividing the length of the array by 2. This gives us the index of the middle element.
        left = arr[:mid] #left is assigned the first half of the array, from index 0 to mid.
        right = arr[mid:] #right is assigned the second half of the array, from index mid to the end.
        
        merge_sort(left) #The merge_sort() function is recursively called for left and right.
        merge_sort(right)
        
        i = j = k = 0 #i, j, and k are initialized to 0. 
        #i is used to track the index of the left array
        #j is used to track the index of the right array
        #k is used to track the index of the merged array.
        
        while i < len(left) and j < len(right): #The while loop continues as long as i is less than the length of the left array and j is less than the length of the right array.
            if left[i] < right[j]: #If the element at left[i] is smaller than the element at right[j], it is placed in the merged array and i is incremented by 1.
                arr[k] = left[i]
                i += 1
            else: #Otherwise, the element at right[j] is placed in the merged array and j is incremented by 1.
                arr[k] = right[j]
                j += 1
            k += 1 #k is incremented by 1 after each iteration of the while loop.
            
        while i < len(left): #If there are any remaining elements in the left array, they are placed in the merged array.
            arr[k] = left[i]
            i += 1
            k += 1
            
        while j < len(right): #If there are any remaining elements in the right array, they are placed in the merged array.
            arr[k] = right[j]
            j += 1
            k += 1 #k is incremented by 1 after each iteration of the while loop and the loop continues until both i and j are greater than or equal to their respective array lengths
            
    return arr