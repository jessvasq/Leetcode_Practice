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

'''Find number of subarrays that fit an exact criteria'''
'''function called fn that takes two arguments: arr, which is a list of integers, and k, which is also an integer. The function appears to be counting the number of subarrays in arr whose sum is equal to k. It uses a defaultdict from the collections module to efficiently keep track of cumulative counts of partial sums. This code uses a defaultdict to efficiently count the number of subarrays in arr with a sum of k. It maintains a cumulative sum (curr) and updates the count of partial sums encountered so far in the counts dictionary. The ans variable accumulates the count of subarrays with a sum of k.'''

from collections import defaultdict #This class is used to create a dictionary that automatically initializes values to a default type (in this case, integers) if they don't exist in the dictionary.

def fn(arr, k):
    counts = defaultdict(int) #Create a counts dictionary using defaultdict(int). This dictionary will be used to store the cumulative counts of partial sums encountered in the arr.
    counts[0] = 1  #The initial count for the sum of 0 is set to 1 because there's one way to obtain a sum of 0 (i.e., by having an empty subarray).
    ans = curr = 0 #ans is initialized to 0. This variable will store the final count of subarrays with a sum of k. curr is initialized to 0. This variable keeps track of the cumulative sum as we iterate through arr.

    for num in arr: #for loop that iterates through each num in the arr list,  used to process each element of the input array one by one.
        
        # do logic to change curr
        
        ans += counts[curr - k] #ans variable is updated by adding counts[curr - k]. This step counts the number of subarrays that sum to k by checking how many subarrays ending at the current position (curr) have a sum of k. It does this by looking at the cumulative count of partial sums encountered before this position (i.e., counts[curr - k]).
        
        counts[curr] += 1 #ncrement the count of the current cumulative sum (curr) in the counts dictionary by 1. This is done using counts[curr] += 1, indicating that we've encountered one more subarray with the current sum.
        
        #The loop continues to iterate through all the elements in arr, updating curr, ans, and the counts dictionary.
    
    return ans  # the function returns the value of ans, which represents the count of subarrays in arr whose sum is equal to k


'''Monotonic increasing stack'''
'''function called fn that takes a list of integers, arr, as input. This function appears to be using a stack data structure to process the elements of the input list while maintaining a "monotonic increasing" sequence, meaning that the elements in the stack are in non-decreasing order. This code processes an input list arr using a stack to maintain a monotonic increasing sequence, and it appears to perform some operation when elements are removed from the stack. The specific purpose and functionality of this code depend on the problem being solved and the missing logic that should be executed when elements are popped from the stack. '''
def fn(arr):
    stack = [] #stack is initialized as an empty list. This list will serve as a stack data structure, where elements can be pushed onto and popped off the top of the stack.
    ans = 0 # ans is initialized to 0. This variable is likely intended to store some result, although the code does not appear to update it within the loop.

    for num in arr: #for loop that iterates through each num in the arr list. 
        
        # for monotonic decreasing, just flip the > to <
        
        while stack and stack[-1] > num: #This inner loop is used to ensure that the stack remains in a monotonic increasing order. Specifically, it pops elements from the stack if the top element of the stack (stack[-1]) is greater than the current num. This ensures that the stack contains elements in non-decreasing order.
            
            # do logic
            
            stack.pop() #After the while loop has finished, it means that the top of the stack contains an element less than or equal to the current num. This element is popped to maintain the monotonic increasing property.
            
            
        stack.append(num) #After the inner while loop, the current num is appended to the stack. This maintains the stack's property of containing elements in non-decreasing order.
    
    return ans #function returns the value of ans, which is initialized to 0 but does not appear to be updated within the loop. If ans is meant to accumulate some result, you would need to add the appropriate logic to update it within the loop.

'''Binary tree: DFS (recursive)'''
'''function called dfs that appears to be implementing a Depth-First Search (DFS) algorithm to traverse a binary tree. The function takes a single argument, root, which is assumed to be the root node of the binary tree. The goal of this code is not explicitly mentioned in the snippet, but it seems to involve processing each node of the tree and potentially accumulating some result in the variable ans. This code defines a depth-first traversal function (dfs) for a binary tree. It recursively processes the nodes of the tree, potentially accumulating a result in the ans variable. The specific logic for processing the nodes and updating ans is not provided in the code snippet, so you would need to customize the function according to your problem's requirements by replacing the placeholder comment "# do logic" with the actual logic you want to execute on each node.'''

def dfs(root):
    ans = 0 
    
    if not root: #Check if the root node is None (i.e., the tree is empty or the current node is a leaf). If the root is None, the function returns immediately without performing any further actions. This is the base case for the recursive function
        return
    
    ans = 0 #Initialize a variable named ans to 0. This variable is likely intended to store some result that will be computed during the traversal of the tree. It starts at 0 and may be updated within the function

    # do logic
    
    dfs(root.left) #Recursively call the dfs function on the left child of the current node, root.left. This step initiates a DFS traversal of the left subtree of the current node
    
    dfs(root.right) #Recursively call the dfs function on the right child of the current node, root.right. This step initiates a DFS traversal of the right subtree of the current node.
    
    return ans #After processing both the left and right subtrees, the function returns the value of ans. However, as written in the code snippet, ans is initialized to 0 and does not appear to be updated within the function. Therefore, it will always return 0 unless modified elsewhere in the code.

'''Binary tree: DFS (iterative)'''
'''Python function called dfs that implements a Depth-First Search (DFS) traversal on a binary tree. The traversal starts from the root node and explores each node's children, depth-first, using an iterative approach with a stack data structure. The function appears to perform some logic on each visited node and accumulate a result in the variable ans. This code implements a depth-first traversal of a binary tree using an iterative approach with a stack. It allows you to process nodes in a specific order, and you can customize the traversal logic by replacing the placeholder comment "# do logic" with the actual code that operates on the nodes and updates the ans variable as needed for your problem'''

def dfs(root):
    stack = [root] #Initialize a stack data structure stack with the root node root. This is done by creating a list containing the root node, which serves as the starting point for the traversal.
    ans = 0 #Initialize a variable ans to 0. This variable is likely intended to store some result that will be computed during the traversal. It starts at 0 and may be updated within the loop.

    while stack: # This loop continues as long as there are nodes in the stack to be processed, indicating that there are nodes in the tree that have not yet been visited
        node = stack.pop() #Inside the loop, pop a node from the stack using stack.pop(). This node represents the current node being processed.
        
        # do logic, update the ans variable as needed.
        
        if node.left: #Check if the current node has a left child (node.left). If it does, push the left child onto the stack using stack.append(node.left). This ensures that the left child will be processed after the current node's logic is executed.
            stack.append(node.left)
        if node.right: # if the current node has a right child (node.right). If it does, push the right child onto the stack using stack.append(node.right). This ensures that the right child will be processed after the left child (if it exists) and the current node's logic are executed.
            stack.append(node.right)

    #loop continues to process nodes in a depth-first manner, popping nodes from the stack, performing logic, and pushing child nodes onto the stack until all nodes have been visited.
    return ans #After processing all nodes, the function returns the value of ans. This value represents the result that has been accumulated or computed during the traversal.


'''Binary tree: BFS'''

''' function called fn that performs a level-order traversal of a binary tree (also known as a breadth-first search, or BFS). This traversal visits all the nodes in the tree level by level, starting from the root node. The function uses a queue data structure (imported from the collections module) to achieve this traversal. this code implements a level-order (breadth-first) traversal of a binary tree using a queue. It allows you to explore the nodes level by level, and you can customize the traversal logic by replacing the placeholder comments with the actual code that operates on the nodes and updates the ans variable as needed for your problem. '''


from collections import deque #A deque (short for "double-ended queue") is a versatile data structure that supports efficient append and pop operations at both ends, making it suitable for implementing a queue.

def fn(root):
    queue = deque([root]) #Initialize a queue called queue with the root node root. The root node is placed in a deque (double-ended queue) data structure, which is used as a queue for the level-order traversal.
    ans = 0 #Initialize a variable ans to 0. This variable is likely intended to store some result that will be computed during the traversal. It starts at 0 and may be updated within the loop.

    while queue: #Enter a while loop with the condition while queue. This loop continues as long as there are nodes in the queue to be processed, indicating that there are nodes at the current level to explore.
        
        current_length = len(queue) #Before processing the nodes at the current level, obtain the current length of the queue using current_length = len(queue). This step is crucial for keeping track of the number of nodes at the current level. It allows you to process one level at a time.
        
        
        # do logic for current level, replace this comment with the code that processes the nodes at the current level.

        for _ in range(current_length): #for loop that iterates current_length times. This loop is responsible for processing the nodes at the current level
            node = queue.popleft() #Inside the loop, node is dequeued (removed from the left side of the queue) using node = queue.popleft(). This node represents the current node being processed.
            
            # do logic,  replace this comment with the code that processes the current node's value or performs some operation based on the node's data.
            
            if node.left: #Check if the current node has a left child (node.left). If it does, enqueue the left child into the queue using queue.append(node.left). This ensures that the left child nodes will be processed in the next level.
                queue.append(node.left)
                
            if node.right: #check if the current node has a right child (node.right). If it does, enqueue the right child into the queue using queue.append(node.right).
                queue.append(node.right)
                
        #The inner loop processes all nodes at the current level, and then the outer while loop advances to the next level of nodes (if they exist).

    return ans # function returns the value of ans, which represents the result that has been accumulated or computed during the traversal.


'''Graph: DFS (recursive)'''

'''function called fn that performs a depth-first search (DFS) traversal on a graph represented as an adjacency list. The goal of this code is to explore and possibly compute something on each node in the graph starting from a specific "START_NODE." This code defines a function fn that performs a depth-first search (DFS) traversal on a graph represented as an adjacency list. It starts from a specified starting node (START_NODE) and explores all connected nodes while accumulating a result (ans). The specific logic for processing nodes and computing the result should be implemented within the dfs function, where the comment "# do some logic" is indicated. '''

def fn(graph):
    def dfs(node): #Define an inner function dfs(node) within the fn function. This inner function is a recursive DFS traversal function that takes a node as its argument and returns a result (ans).
        
        ans = 0 #Initialize a variable ans to 0. This variable is likely intended to store some result that will be computed during the traversal.
        
        # do some logic
        
        for neighbor in graph[node]: #for loop that iterates over the neighbors of the current node. The graph is represented as an adjacency list, so graph[node] is a list of neighbors for the given node.
            if neighbor not in seen: #For each neighbor in graph[node], check if the neighbor has not been seen before (i.e., not in the seen set). If it hasn't been seen, mark it as seen by adding it to the seen set.
                
                seen.add(neighbor)
                ans += dfs(neighbor) # Then, recursively call the dfs function on the neighbor and accumulate the result in the ans variable.
        
        return ans #Return the final value of ans after processing all the neighbors of the current node.

    seen = {START_NODE} #Initialize a set called seen and add the START_NODE to it. This sets up the initial state for the DFS traversal, indicating that the START_NODE is the starting point for exploration.
    
    return dfs(START_NODE) #Finally, call the dfs function with the START_NODE as an argument, initiating the DFS traversal from the starting node. The result of the traversal will be returned as the result of the fn function.


'''Graph: DFS (iterative)'''
'''Python function called fn that performs a depth-first search (DFS) traversal on a graph represented as an adjacency list. The goal of this code is to explore all nodes in the graph starting from a specified "START_NODE." This code defines a function fn that performs a depth-first search (DFS) traversal on a graph represented as an adjacency list. It explores nodes in a specific order using a stack, and you can customize the traversal logic by replacing the placeholder comment "# do some logic" with the actual code that operates on the nodes and updates the ans variable as needed for your problem.'''

def fn(graph):
    stack = [START_NODE] #Initialize a stack called stack with the START_NODE. This is the starting point for the DFS traversal. The START_NODE is added to the stack as the initial node to be explored
    seen = {START_NODE} #Initialize a set called seen and add the START_NODE to it. This set keeps track of nodes that have been visited during the traversal. The START_NODE is marked as seen because it's the starting node.
    
    ans = 0 #Initialize a variable ans to 0. This variable is likely intended to store some result that will be computed during the traversal. 

    while stack: #Enter a while loop with the condition while stack. This loop continues as long as there are nodes in the stack to be processed, indicating that there are unexplored nodes in the graph.
        
        node = stack.pop() #Inside the loop, pop a node from the top of the stack using node = stack.pop(). This node represents the current node being processed.
        
        # do some logic
        
        for neighbor in graph[node]: #Iterate through the neighbors of the current node by looping over graph[node]. The graph is represented as an adjacency list, and graph[node] provides a list of neighbors for the current node.
            if neighbor not in seen: #For each neighbor in graph[node], check if the neighbor has not been seen before (i.e., not in the seen set). If it hasn't been seen, mark it as seen by adding it to the seen set.
                seen.add(neighbor)
                stack.append(neighbor) #Push the neighbor onto the stack to indicate that it should be explored next. This allows the traversal to continue from the newly added node.
                
    #The loop continues to process nodes in a depth-first manner, popping nodes from the stack, performing logic, and pushing unvisited neighbors onto the stack until all nodes have been visited.
    
    return ans #rocessing all nodes in the graph or until the stack becomes empty, the function returns the value of ans. This value represents the result that has been accumulated or computed during the traversal.


'''Graph: BFS'''
''' function called fn that performs a breadth-first search (BFS) traversal on a graph represented as an adjacency list. The goal of this code is to explore all nodes in the graph starting from a specified "START_NODE."  this code defines a function fn that performs a breadth-first search (BFS) traversal on a graph represented as an adjacency list. It explores nodes level by level using a queue, and you can customize the traversal logic by replacing the placeholder comment "# do some logic" with the actual code that operates on the nodes and updates the ans variable as needed for your problem'''

from collections import deque #deque (short for "double-ended queue") is used to implement a queue data structure, which is ideal for BFS traversal.

def fn(graph):
    queue = deque([START_NODE]) #Initialize a queue called queue with the START_NODE. The START_NODE is the initial node from which the BFS traversal begins. The deque is initialized with a single element, the START_NODE.
    seen = {START_NODE} #Initialize a set called seen and add the START_NODE to it. This set keeps track of nodes that have been visited during the traversal. The START_NODE is marked as seen because it's the starting node.
    
    ans = 0 #Initialize a variable ans to 0. This variable is likely intended to store some result that will be computed during the traversal. 

    while queue: #Enter a while loop with the condition while queue. This loop continues as long as there are nodes in the queue to be processed, indicating that there are unexplored nodes in the graph
        
        node = queue.popleft() #Inside the loop, dequeue (remove from the front of) a node from the queue using node = queue.popleft(). This node represents the current node being processed.
        
        # do some logic
        
        for neighbor in graph[node]: #Iterate through the neighbors of the current node by looping over graph[node]. The graph is represented as an adjacency list, and graph[node] provides a list of neighbors for the current node
            if neighbor not in seen: #For each neighbor in graph[node], check if the neighbor has not been seen before (i.e., not in the seen set). If it hasn't been seen, mark it as seen by adding it to the seen set.
                seen.add(neighbor)
                
                queue.append(neighbor) #Enqueue (add to the back of) the neighbor into the queue to indicate that it should be explored in the next BFS level. This allows the traversal to continue to the newly added nodes
                
    #The loop continues to process nodes in a breadth-first manner, dequeuing nodes from the front of the queue, performing logic, and enqueuing unvisited neighbors to the back of the queue until all nodes have been visited.
    
    return ans #After processing all nodes in the graph or until the queue becomes empty, the function returns the value of ans. This value represents the result that has been accumulated or computed during the traversa


'''Find top k elements with heap'''
'''function called fn that uses a min-heap (priority queue) to find the k smallest elements from a given list arr. This code efficiently finds the k smallest elements from a list arr based on some criteria by using a min-heap. The criteria value for each element determines its priority in the heap, and the code ensures that the heap size remains limited to k, making it an efficient way to find the k smallest elements'''

import heapq #heapq module, which provides functions for heap operations. In this code, heapq.heappush and heapq.heappop are used to manipulate the heap.

def fn(arr, k):
    heap = [] #Initialize an empty heap called heap. This heap will store tuples where the first element represents a certain criteria (to be defined later) and the second element is a number from the input list arr.
    
    for num in arr: #Enter a loop that iterates through each num in the arr list. This loop is used to process each element of the input list one by one.
        
        # do some logic to push onto heap according to problem's criteria
        
        heapq.heappush(heap, (CRITERIA, num)) #Use heapq.heappush to push a tuple (CRITERIA, num) onto the heap. This effectively adds the element num to the heap, and it will be prioritized based on the computed criteria. The smallest elements will be at the top of the heap due to the min-heap property.
        
        if len(heap) > k: #Check if the length of the heap has exceeded k by using len(heap) > k. If it has, it means that there are more than k elements in the heap, and we need to remove the element with the highest criteria (the largest criteria value) to maintain the size of the heap as k. To do this, use heapq.heappop(heap), which removes and returns the smallest element from the heap.
            
            heapq.heappop(heap)#Repeat steps 4-6 for each element in arr. As a result, the heap will always contain the k smallest elements based on the computed criteria.
    
    return [num for num in heap] #After processing all elements in arr, the function returns a list comprehension that extracts the second element (the numbers) from the tuples in the heap. This list contains the k smallest elements in ascending order


'''Binary search'''
''' function called fn that performs binary search on a sorted list arr to find the insertion point of a target element. The insertion point is the index where the target element would be inserted into the sorted list to maintain its sorted order. This code performs binary search on a sorted list arr to find the insertion point of a target element. If the target element is found, it performs some action (specified as "# do something") and returns. If the target element is not found, it returns the index where the target should be inserted into the list to maintain its sorted orde '''

def fn(arr, target):
    #left and right. left is set to 0, which represents the leftmost index of the list, and right is set to len(arr) - 1, which represents the rightmost index of the list. These pointers are used to define the search range within the list.
    left = 0
    right = len(arr) - 1
    
    while left <= right: #Enter a while loop with the condition while left <= right. This loop continues as long as the search range is valid, meaning that there are still elements to search within the list.
        
        mid = (left + right) // 2 #Calculate the middle index, mid, as (left + right) // 2. This index represents the middle of the current search range
        
        if arr[mid] == target: #Check if the element at the mid index, arr[mid], is equal to the target element, target. If it is, you can choose to perform some specific action
            
            # do something
            
            return
        
        if arr[mid] > target: #If arr[mid] is greater than the target (arr[mid] > target), it means that the target element, if present, must be in the left half of the current search range. Therefore, update right to mid - 1 to narrow the search range to the left half.
            right = mid - 1 
            
        else: #If arr[mid] is less than the target (arr[mid] < target), it means that the target element, if present, must be in the right half of the current search range. Therefore, update left to mid + 1 to narrow the search range to the right half.
            left = mid + 1
            
    #The loop continues to search for the target element by repeatedly updating the search range based on whether the target is greater or less than the middle element.
    #If the loop exits without finding the target element, it means that the target element should be inserted into the list to maintain its sorted order. The left pointer at this point represents the insertion point, as it points to the first element greater than the target in the list.
    
    # left is the insertion point
    return left #Return the value of left as the insertion point. This value indicates the index where the target element should be inserted into the list


'''Binary search: duplicate elements, left-most insertion point'''
'''function called fn that performs binary search on a sorted list arr to find the lower bound of a target element. The lower bound is the index of the first occurrence of the target element in the sorted list, or if the target is not found, it returns the index where the target element should be inserted to maintain the sorted order. This code performs binary search on a sorted list arr to find the lower bound of a target element. It efficiently identifies the index of the first occurrence of the target or the index where the target should be inserted to maintain the sorted order. '''


def fn(arr, target):
    left = 0 #Initialize two pointers, left and right. left is set to 0, which represents the leftmost index of the list, and right is set to len(arr), which represents one past the rightmost index of the list. These pointers define the search range within the list
    right = len(arr)
    
    while left < right: #while loop with the condition while left < right. This loop continues as long as the search range is valid, meaning that there are still elements to search within the list.
        
        mid = (left + right) // 2 #Calculate the middle index, mid, as (left + right) // 2. This index represents the middle of the current search range.
        #Check if the element at the mid index, arr[mid], is greater than or equal to the target element, target. This condition is used to find the lower bound of the target element.
        
        #If arr[mid] is greater than or equal to target, it means that the target element, if present, must be in the left half of the current search range. Therefore, update right to mid to narrow the search range to the left half.

        #If arr[mid] is less than target, it means that the target element, if present, must be in the right half of the current search range. Therefore, update left to mid + 1 to narrow the search range to the right half.
        if arr[mid] >= target: 
            right = mid
        else:
            left = mid + 1
            
        #The loop continues to search for the target element by repeatedly updating the search range based on whether the target is greater or equal to the middle element.

#If the loop exits without finding the target element, it means that the target element should be inserted into the list to maintain its sorted order. The left pointer at this point represents the insertion point, as it points to the first element greater than or equal to the target in the list.

#Return the value of left as the lower bound. This value indicates the index of the first occurrence of the target element in the list, or if the target is not found, the index where the target element should be inserted.

    return left

'''Binary search: duplicate elements, right-most insertion point'''
def fn(arr, target):
    left = 0
    right = len(arr)
    while left < right:
        mid = (left + right) // 2
        if arr[mid] > target:
            right = mid
        else:
            left = mid + 1

    return left

'''Binary search: for greedy problems'''
'''If looking for a minimum:'''
def fn(arr):
    def check(x):
        # this function is implemented depending on the problem
        return BOOLEAN

    left = MINIMUM_POSSIBLE_ANSWER
    right = MAXIMUM_POSSIBLE_ANSWER
    while left <= right:
        mid = (left + right) // 2
        if check(mid):
            right = mid - 1
        else:
            left = mid + 1
    
    return left


'''If looking for a maximum:'''
def fn(arr):
    def check(x):
        # this function is implemented depending on the problem
        return BOOLEAN

    left = MINIMUM_POSSIBLE_ANSWER
    right = MAXIMUM_POSSIBLE_ANSWER
    while left <= right:
        mid = (left + right) // 2
        if check(mid):
            left = mid + 1
        else:
            right = mid - 1
    
    return right


'''Backtracking'''
def backtrack(curr, OTHER_ARGUMENTS...):
    if (BASE_CASE):
        # modify the answer
        return
    
    ans = 0
    for (ITERATE_OVER_INPUT):
        # modify the current state
        ans += backtrack(curr, OTHER_ARGUMENTS...)
        # undo the modification of the current state
    
    return ans


'''Dynamic programming: top-down memoization'''
def fn(arr):
    def dp(STATE):
        if BASE_CASE:
            return 0
        
        if STATE in memo:
            return memo[STATE]
        
        ans = RECURRENCE_RELATION(STATE)
        memo[STATE] = ans
        return ans

    memo = {}
    return dp(STATE_FOR_WHOLE_INPUT)

'''Build a trie'''
# note: using a class is only necessary if you want to store data at each node.
# otherwise, you can implement a trie using only hash maps.
class TrieNode:
    def __init__(self):
        # you can store data at nodes if you wish
        self.data = None
        self.children = {}

def fn(words):
    root = TrieNode()
    for word in words:
        curr = root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        # at this point, you have a full word at curr
        # you can perform more logic here to give curr an attribute if you want
    
    return root


'''Dijkstra's algorithm'''
from math import inf
from heapq import *

distances = [inf] * n
distances[source] = 0
heap = [(0, source)]

while heap:
    curr_dist, node = heappop(heap)
    if curr_dist > distances[node]:
        continue
    
    for nei, weight in graph[node]:
        dist = curr_dist + weight
        if dist < distances[nei]:
            distances[nei] = dist
            heappush(heap, (dist, nei))