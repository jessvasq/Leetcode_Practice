'''BINARY SEARCH'''
'''Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.
You must not use any built-in exponent function or operator.
For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.'''

# def find_square_root(x):
#     lo= 0
#     #given integer
#     hi= x
    
#     while lo <= hi:
#         #find the middle element (e.g. 81//2 = 40.5, we use floor division '//' rounds the result down to the nearest whole num (e.g. 40)
#         mid_num= (lo+hi) // 2 
#         print('mid_num:', mid_num)
        
#         if mid_num * mid_num == x: #(if e.g 40 * 40 = to 81, we return the mid_num, since that's not the case we move to the elif statement)
#             return mid_num
        
#         elif mid_num * mid_num <= x: #(if e.g. 40 * 40 is less or equal than 81, we increment lo + 1. Since this is not the case, we move to the else statement )
#             lo = mid_num + 1
#             print('lo:', lo)
        
#         else:
#             hi= mid_num -1 # we use e.g. hi = 40 - 1 which is equal to 39 and continue the loop until we find the answer. 39 would be the new value for 'x'. The mid num for 39 would be 19, skip 'if' and 'elif' statement -> use 19 as x, where mid=9, we test the first condition where 9 * 9 = to x and print the answer 
#             print('hi:', hi)
    

#     return lo-1

# x=81
# print(find_square_root(x))
        
   
# '''Given two integer arrays nums1 and nums2, sorted in non-decreasing order, return the minimum integer common to both arrays. If there is no common integer amongst nums1 and nums2, return -1. Note that an integer is said to be common to nums1 and nums2 if both arrays have at least one occurrence of that integer.
#  '''  

 
# def find_common_min(arr1, arr2):

#     #find hi and lo elements for both arrays
#     lo = 0 
#     hi = len(arr1)-1
#     arr2_lo = 0
#     arr2_hi = len(arr2)-1
    
#     while lo <= hi and arr2_lo <= arr2_hi:
#         #compare the first two lo elements, if they're equal return lo
#         if arr1[lo] == arr2[arr2_lo]:
#             return arr1[lo]
        
#         #if the lo element in arr1 is less than lo element in list 2, increment arr1 lo by 1 
#         elif arr1[lo] < arr2[arr2_lo]:
#             lo += 1
            
#         #else increment arr2 low by 1     
#         else: 
#             arr2_lo += 1
  
#     #return -1 if there's no common integer
#     return -1 
                  
    
# nums1 = [1,2,3]
# nums2 = [2, 4]

# print(find_common_min(nums1, nums2))


'''268. Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.''' 

# #simple solution
# def find_missing_num(arr):
#     n = len(arr)
    
#     for num in range(n+1):
#         if num not in arr:
#             return num

# #TEST CASES
# nums=[9,6,4,2,3,5,7,0,1]
# nums1 = [3,0,1]
# nums2 = [0,1]

# print(find_missing_num(nums))
# print(find_missing_num(nums1))
# print(find_missing_num(nums2))
    
# #Optimized solution 
# def missing_number(nums):
#     n = len(nums)
#     print('N', n)
#     # use the formula for the sum of aithmetic progression. Sum of all numbers from 0 to n
#     total_sum = n * (n + 1) // 2  
#     array_sum = sum(nums)  # Sum of elements in the array
#     print(array_sum) 
#     return total_sum - array_sum #This subtraction will result in the missing number because all the other numbers from 0 to n should have canceled each other out, leaving only the missing number. e.g [0, 1, 3], sum of all numbers from 0 to 3 = (0 + 1 + 2 + 3 = 6) and the sum of the elements in the nums array (3 + 0 + 1 = 4), resulting in the output 2

## Example usage:
# nums = [9,6,4,2,3,5,7,0,1]
# result = missing_number(nums)
# print(result)  

'''287. Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.There is only one repeated number in nums, return this repeated number.You must solve the problem without modifying the array nums and uses only constant extra space.'''

# def find_duplicate_num(nums):
#     # Define the search range
#     lo, hi = 1, len(nums) - 1
#     print(hi)
    
#     while lo < hi:
#         mid = (lo + hi )// 2
#         count = 0
        
#         # Count the number of elements in the array that are less than or equal to mid
#         for num in nums:
#             if num <= mid:
#                 count += 1
        
#         # Adjust the search range based on the count
#         if count <= mid:
#             lo = mid + 1
#         else:
#             hi = mid
    
#     # At this point, lo and hi will converge to the repeated number
#     return lo

# nums = [1,3,4,2,2]
# nums1 = [3,1,3,4,2]
# print(find_duplicate_num(nums))
# print(find_duplicate_num(nums1))



'''DIJKSTRA'S ALGORITHM
Finds the shortest path between two vertices in a graph. It is an algorithm for finding the shortest paths between nodes in a graph. The algorithm exists in many variants. Dijkstra's original algorithm found the shortest path between two given nodes, but a more common variant fixes a single node as the "source" node and finds shortest paths from the source to all other nodes in the graph, producing a shortest-path tree.'''

# graph = {
#     'A': {'B': 5, 'C': 1},
#     'B': {'A': 5, 'C': 2, 'D': 1},
#     'C': {'A': 1, 'B': 2, 'D': 4, 'E': 8},
#     'D': {'B': 1, 'C': 4, 'E': 3, 'F': 6},
#     'E': {'C': 8, 'D': 3},
#     'F': {'D': 6}
# }

# import heapq #import heapq module to use the functions for implementing the priority queue. A priority queue is a data structure that stores elements in a queue and assigns a priority to each element. The element with the highest priority is dequeued first.

# #pass in the graph and the start node
# def dijkstra(graph, start):
#     # Initialize distances with infinity for all nodes except the start node. We use a dictionary to store the distances to all nodes in the graph. We set the distance to the start node to 0 and the distance to all other nodes to infinity. 'Float('infinity')' is used to represent infinity.
#     distances = {node: float('infinity') for node in graph}
#     # Set the distance from the start node to itself is 0
#     distances[start] = 0

#     # Priority queue to store (distance, node) pairs. (0, start) is the initial node with distance 0
#     priority_queue = [(0, start)]

#     # Loop until the queue is empty, if the queue is empty, it means we have visited all nodes
#     while priority_queue:
#         # Get the current node from the queue by getting the node with the smallest distance. Use heapq.heappop() to remove and return the smallest element from the heap
#         current_distance, current_node = heapq.heappop(priority_queue)

#         # Check if the current path is shorter than the known distance
#         if current_distance > distances[current_node]:
#             continue

#         # Explore neighbors of the current node and update distances if necessary
#         for neighbor, weight in graph[current_node].items():
#             distance = current_distance + weight

#             # Update distance if a shorter path is found. We check if the distance to the neighbor is shorter than the current distance + weight of the edge between the current node and the neighbor. If it is shorter, we update the distance and add the neighbor to the priority queue.
#             if distance < distances[neighbor]:
#                 distances[neighbor] = distance
#                 # Use heapq.heappush() to add the neighbor to the priority queue with the updated distance
#                 heapq.heappush(priority_queue, (distance, neighbor))

#     return distances

# # Example usage:
# graph = {
#     'A': {'B': 1, 'C': 4},
#     'B': {'A': 1, 'C': 2, 'D': 5},
#     'C': {'A': 4, 'B': 2, 'D': 1},
#     'D': {'B': 5, 'C': 1}
# }

# start_node = 'A'
# shortest_distances = dijkstra(graph, start_node)

# print(f"Shortest distances from {start_node}: {shortest_distances}")
