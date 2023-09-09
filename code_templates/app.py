#CODE TEMPLATES EXPLAINED 

'''Two pointers: one input, opposite ends'''
#framework for traversing an array from both ends based on a condition. 
def fn(arr):
    left = ans = 0  #left is initially set to 0, representing the index of the leftmost element in the input array. ans is initially set to 0. This variable is likely intended to store some result, and it will be returned at the end of the function.
    right = len(arr) - 1 # right is initially set to len(arr) - 1, representing the index of the rightmost element in the input array.

    while left < right: #Enter a while loop with the condition left < right. This loop continues as long as the left pointer is less than the right pointer. The purpose of this loop is to traverse the elements of the input array from both ends and perform some logic.
        # do some logic here with left and right
        if CONDITION: #if statement with a placeholder condition CONDITION. This condition is not defined in the provided code, so you would need to replace it with a specific condition that suits your requirements. The actual logic that is performed on the elements of the array is dependent on this condition.
            left += 1 #If the condition CONDITION is evaluated as True, the left pointer is incremented by 1, effectively moving it to the right in the array.
        else: 
            right -= 1 #If the condition is False, the right pointer is decremented by 1, effectively moving it to the left in the array.
    
    #The loop continues to iterate, and the pointers move towards each other until left is no longer less than right. This means that the pointers have met or crossed each other in the array, and the loop terminates.
    
    return ans  #After the loop, the function returns the value of the ans variable. It's important to note that the code provided does not update the ans variable within the loop.



'''Two pointers: two inputs, exhaust both'''
#Iterate through two arrays
#function called fn that takes two input arrays, arr1 and arr2. The function appears to perform some logic on these arrays, and it uses two pointers, i and j, to iterate through the arrays and accumulate a result in the variable ans

def fn(arr1, arr2): #loop continues as long as both i and j are within the bounds of their respective arrays.
    i = j = ans = 0 #i is initially set to 0, representing the index for arr1, j is initially set to 0, representing the index for arr2. 
                     #ans is initially set to 0. This variable is likely intended to store some result and will be returned at the end of the function.

    while i < len(arr1) and j < len(arr2): #loop continues as long as both i and j are within the bounds of their respective arrays
        # do some logic here
        if CONDITION: #Depending on whether CONDITION is True or False, either i or j is incremented by 1. This logic will determine how the pointers move through the arrays
            i += 1
        else:
            j += 1
    
    while i < len(arr1): #second while loop (while i < len(arr1)) continues to operate on arr1 if there are remaining elements in it. Inside this loop, you can place additional logic to process elements of arr1. The i pointer is incremented with each iteration.
        # do logic
        i += 1 #The i pointer is incremented with each iteration.
    
    while j < len(arr2): #continues to operate on arr2 if there are remaining elements in it. 
        # do logic
        j += 1 #j pointer is incremented with each iteration
    
    return ans #modify this code if you need to calculate or accumulate some results based on the elements of 'arr1' and 'arr2'


'''Sliding window'''
#framework is designed to implement a sliding window algorithm
#function called fn that takes a single input array, arr

def fn(arr):
    left = ans = curr = 0 #left is initially set to 0, representing the left boundary of a sliding window.
                        #ans is initially set to 0. This variable is likely intended to store some result, and it will be returned at the end of the function.
                        #curr is initially set to 0. This variable is likely used to accumulate some intermediate result within the sliding window.

    for right in range(len(arr)): # iterates over the indices of the arr array using the range(len(arr)) function.This loop essentially moves the right boundary of the sliding window from left to right.
        
        # do logic here to add arr[right] to curr

        while WINDOW_CONDITION_BROKEN:  #loop used for adjusting the sliding window by removing elements from the left side
            
            #purpose of this loop is to maintain the size and position of the sliding window based on some condition. You would need to define the actual condition that determines when the window should be adjusted and what elements should be removed from curr. The left pointer is incremented to move the left boundary of the window to the right.

            # remove arr[left] from curr
            
            left += 1 
            
            #The loop continues to iterate through the entire arr array, adjusting the sliding window and updating the ans variable as necessary.
            
        # define the logic for computing the final result based on the contents of the sliding window

        # update ans
    
    return ans #ans variable, contains the result of the sliding window operation after processing all elements of the input array.


'''Build a prefix sum'''

'''function called fn that takes a single input argument, arr, which is assumed to be a list or array of elements. The purpose of this function is to calculate and return a new list called prefix, where each element at index i in prefix is the sum of all elements in arr from index 0 to i'''

def fn(arr):
    prefix = [arr[0]] #Initialize a list called prefix with the first element of arr as its initial element. 
    for i in range(1, len(arr)): #iterates over the indices of arr from 1 to len(arr) - 1. The loop variable i takes on values from 1 to one less than the length of arr. This loop is used to calculate the prefix sum for each element in arr.
        prefix.append(prefix[-1] + arr[i]) #append a new element to the prefix list. The appended element is calculated as the sum of the last element in the prefix list (accessed using prefix[-1]) and the current element in arr (accessed using arr[i]). This effectively accumulates the sum of elements from index 0 up to the current index i in arr. The loop continues to iterate through all elements of arr, and for each iteration, a new element is appended to the prefix list, representing the cumulative sum up to that point.
    
    return prefix #Once the loop has processed all elements in arr, the prefix list contains the cumulative sum for each element, and it is returned as the result of the function

'''Efficient string building'''
'''Python function called fn that takes a list of characters, arr, as input. The function's goal is to create a new string by concatenating all the characters from the input list and return that string. Takes a list of characters, iterates through each character, appends them to a new list (ans), and then joins all the characters in the list together to create a single string. '''
# arr is a list of characters
def fn(arr):
    ans = [] #Initialize an empty list called ans. This list will be used to store individual characters from the input list arr
    for c in arr: #for loop that iterates through each character c in the input list arr. This loop is designed to process each character one by one.
        ans.append(c) #each character c from arr is appended to the ans list using the append method. This means that ans will contain all the characters from arr in the same order.
    
    return "".join(ans) #.join() method to concatenate the characters in the ans list into a single string. The join method takes the elements of a list (in this case, characters) and joins them together into a single string using the specified separator. In this code, an empty string "" is used as the separator, which means that the characters will be joined together without any spaces or separators between them.


'''Linked list: fast and slow pointer'''
'''Python function called fn that appears to operate on a linked list, specifically a singly-linked list with a head node. This code is implementing a common algorithm known as the "Floyd's Tortoise and Hare" algorithm or the "two-pointer" technique. The goal of this algorithm is often to detect cycles in a linked list. the code provides a structure for traversing a linked list using two pointers (slow and fast) with the potential goal of detecting cycles or performing some other operation on the nodes. The specific logic for detecting cycles or other operations should be added inside the loop, and the ans variable may be used to store any relevant result'''

def fn(head):
    slow = head #Python function called fn that appears to operate on a linked list, specifically a singly-linked list with a head node. This code is implementing a common algorithm known as the "Floyd's Tortoise and Hare" algorithm or the "two-pointer" technique. The goal of this algorithm is often to detect cycles in a linked list
    fast = head #fast is also initially set to the head of the linked list.
    ans = 0 #ans is initialized to 0. This variable is likely intended to store some result, although the code does not update it within the loop.

    while fast and fast.next: #This loop continues as long as both fast and fast.next are not None. This is a common technique for traversing a linked list where fast moves twice as fast as slow
        # in the context of the Floyd's Tortoise and Hare algorithm, this loop is used to detect cycles in a linked list or to perform some specific operation on the nodes within the list
        # do logic
        
        slow = slow.next #The slow pointer is advanced by one node by setting slow to slow.next.
        
        fast = fast.next.next #The fast pointer is advanced by two nodes by setting fast to fast.next.next.
        
        #The loop continues to iterate through the linked list until one of two conditions is met:
        #If there is no cycle in the list, the fast pointer will eventually reach the end of the list (fast or fast.next becomes None), and the loop will exit.
        #If there is a cycle in the list, the fast and slow pointers will eventually meet at the same node within the cycle, and the loop will exit.
    
    return ans #the function returns the value of the ans variable. Here, ans is not updated within the loop, so it remains 0 unless modified elsewhere in the code.


'''Reversing a linked list'''

'''function called fn that operates on a singly-linked list. The goal of this function is to reverse the linked list and return the new head of the reversed list'''
def fn(head):
    curr = head  #curr is initially set to the head of the linked list. This is often a reference to the first node in the list and serves as the current node that we are processing
    prev = None #is initially set to None. This variable will be used to keep track of the previous node in the reversed list.
    while curr: #loop continues as long as curr is not None, which means it will iterate through all the nodes in the original linked list.
        next_node = curr.next #next_node is assigned the reference to the next node in the original linked list. This step is essential because we will be modifying the curr.next pointer in the next step, and we need to keep a reference to the next node before we change it.
        
        curr.next = prev #curr.next is set to prev. This is the key step in reversing the linked list. By setting the next pointer of the current node (curr) to point to the previous node (prev), we reverse the direction of the link. Initially, this makes the current node the new head of the reversed list
        
        prev = curr #prev is updated to curr. This prepares prev for the next iteration, where it will become the previous node for the next current node.
        
        curr = next_node  #curr is updated to next_node, which allows us to move to the next node in the original list for the next iteration of the loop
        
        #The loop continues until curr becomes None, indicating that we have reached the end of the original linked list.
        
    return prev  #returns prev, which now points to the new head of the reversed linked list. This is because prev was the last node processed in the original list, and after reversing, it becomes the first node in the reversed list.

