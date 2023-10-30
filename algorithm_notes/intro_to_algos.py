'''LINEAR SEARCH'''
"""Returns the index position of the target if found, else returns None
    Time complexity: O(n)"""
def linear_search(list, target):
    #create a range of numbers from 0 to the length of the list
    for i in range(0, len(list)):
        if list[i] == target:
            return i
    return None

def verify(index):
    if index is not None:
        print("Target found at index: ", index)
    else:
        print("Target not found in list")
        
numbers = [1,2,3,4,5,6,7,8,9,10]

result = linear_search(numbers, 4)
verify(result)

'''BINARY SEARCH'''
'''Returns the index position of the target if found, else returns None. This algorithm assumes that the list is already sorted. Time complexity: O(log n) '''
def binary_search(list, target):
    first=0
    last=len(list-1) #last value in a list is at position len(list)-1 because the index starts at 0
    
    while first <= last:
        midpoint = (first+last)//2
        if list(midpoint) == target:
            return midpoint
        elif list(midpoint) < target:
            first = midpoint + 1
        else:
            last = midpoint - 1
    return None

def verifyb(index):
    if index is not None:
        print("Target found at index: ", index)
    else:
        print("Target not found in list")
        
numbers = [1,2,3,4,5,6,7,8,9,10]
resultb = linear_search(numbers, 4)
verifyb(resultb)

'''recursive binary search'''
def recursive_binary_search(list, target):
    if len(list) == 0:
        return False
    else:
        midpoint = (len(list))//2
        if list[midpoint] == target:
            return True
        else:
            if list[midpoint] < target:
                return recursive_binary_search(list[midpoint+1:], target)
            else:
                return recursive_binary_search(list[:midpoint], target)

def verifyrb(result):
    print("Target found: ", result)

numbers = [1,2,3,4,5,6,7,8,9,10]
result = recursive_binary_search(numbers, 6)
print(result)


'''LINKED LISTS'''

class Node:
    data = None
    next_node = None
    
    def __init__(self, data):
        self.data = data
        

class LinkedList:
  
    def _innit__(self):
        #head is the first node in the list which is used as an entry point for the linked list to traverse the list
        self.head = None
    
    #repr is a built in function that returns a string representation of an object
    def __repr__(self):
        #we'll create a list that will hold the nodes
        nodes = []
        #we'll set the current node to the head of the list
        current = self.head
        
        while current:
            if current is self.head:
                #if the current node is the head, we'll append the string 'Head: ' to the list
                nodes.append('[Head: %s]' % current.data)
            #if the current node is the tail, we'll append the string 'Tail: ' to the list
            elif current.next_node is None:
                nodes.append('[Tail: %s]' % current.data)
            #if the current node is neither the head nor the tail, we'll append the string ' %s ' to the list
            else:
                nodes.append('[%s]' % current.data)
            #set the current node to the next node in the list
            current = current.next_node
        #return the list as a string
        return '-> '.join(nodes)
        
        
    #create another method that takes self and checks if the head is None, if this is True, then the list is empty
    def __is_empty__(self):
        return self.head == None
    
    #this method returns the size of a linked list. We do so by traversing the list and incrementing a counter variable every time we visit a node. Takes O(n) time or linear time
    def size(self):
        #current will be used to keep track of the current node being looked at
        current = self.head
        #count will keep track of the number of nodes in the list
        count = 0
        #we'll create a while loop that will run as long as current is not None
        while current:
            #increment count by 1 everyt time the loop runs
            count += 1
            #set current to the next node in the list
            current = current.next_node
        #return count which will give us the number of nodes
        return count

    #this method searches for a node that contains the data passed in as an argument. Takes O(n) time or linear time
    def search(self, key):
        #current will be used to keep track of the current node being looked at
        current = self.head
        while current:
            if current.data == key:
                return current
            #if the current node is not the node we're looking for, we'll set current to the next node in the list
            else:
                current = current.next_node
        #if we don't find the node, we'll return None
        return None
        
                

    '''There are three ways to add data to a linked list: Insert at the head, insert at the tail, and insert in the middle. We'll start with inserting at the head'''

    #this method inserts a new node at the head of the list. Takes O(1) time or constant time which is our best case scenario
    def insert_at_head(self, data):
        #create a new node
        new_node = Node(data)
        #set the next node of the new node to the current head
        new_node.next_node = self.head
        #set the head to the new node
        self.head = new_node


    '''insert a new node at a given position. Insertion takes o(1) time, but finding the node at the given position takes O(n) linear time. Therefore it takes an overall O(n) time or linear time'''
    def insert_at_position(self, data, position):
        #if position is 0, we'll insert the node at the head using the previous 'insert_at_head' method
        if position == 0:
            self.insert_at_head(data)
            return
        
        #if position is greater than 0, we'll create a new node and traverse the list until we get to the position where we want to insert the node
        if position > 0:
            new_node =  Node(data)
            #if the list is empty, we'll insert the node at the head
            current = self.head
            #iterate through the list until we get to the position where we want to insert the node
            while position > 1:
                #set current to the next node in the list
                current = current.next_node
                #decrement position by 1
                position -= 1
            
    
            prev_node = current
            next_node = current.next_node
            #set the previous node to point to the new node        
            prev_node.next_node = new_node
            #set the new node to point to the next node
            new_node.next_node = next_node
            
                
    '''insert a new node at the tail of the list. Takes O(n) time or linear time'''
    def insert_at_tail(self, data):
        #create a new node
        new_node = Node(data)
        #set current to the head of the list
        current = self.head
        #iterate through the list until we get to the end, we're looking for the node whose next node is None. Once found, we'll set the next node of that node to the new node
        while current.next_node is not None:
            #set current to the next node in the list
            current = current.next_node
        #set the next node of the current node to the new node
        current.next_node = new_node
        
        
    '''remove a node from the list. Takes O(n) time or linear time'''
    def remove(self, key):
        #set current to the head of the list
        current = self.head
        #set previous to None
        previous = None
        #set found to False
        found = False
        #iterate through the list until we find the node we're looking for
        while current and found is False:
            #if the current node is the node we're looking for, we'll set found to True
            if current.data == key and current is self.head:
                found = True
                #set the head to the next node in the list
                self.head = current.next_node
                #set the next node of the current node to None
                current.next_node = None
                return current.data
            #if the current node is not the node we're looking for, we'll set previous to the current node and current to the next node in the list
            elif current.data == key:
                found = True
                previous.next_node = current.next_node
                #set the next node of the current node to None and return the data of the current node 
                current.next_node = None
                return current.data

            else:
                previous = current
                current = current.next_node
        #if we don't find the node, we'll return None
        return None
    
    
    '''SORT A LINKED LIST USING MERGE SORT'''

    '''Recursively divide the linked list into sublists containing a single node. Repeatedly merge the sublists to produce sorted sublists until one remains'''

def merge_sort_ll(linked_list):
    #if the linked list has only one node, return the linked list
    if linked_list.size() == 1:
        return linked_list
    #if the linked list is empty, return the linked list
    elif linked_list.head is None:
        return linked_list
    #else, split the list into two halves and sort each half recursively
    left_half, right_half = split_ll(linked_list)
    left = merge_sort(left_half)
    right = merge_sort(right_half)

    #return the merged sorted list
    return merge(left, right)
    
'''Split the list into two halves, left and right. Takes O(n) time or linear time'''
def split_ll(linked_list):
    #if the list is empty or has only one node, return the list as left and None as right
    if linked_list == None or linked_list.head == None:
        left_half = linked_list
        right_half = None
        #return left and right halves
        return left_half, right_half
    
    #else, we'll traverse the list and count the number of nodes in the list
    else:
        #we use the size method we created earlier to count the number of nodes in the list
        size = linked_list.size()
        #find the mid point of the list
        mid = size//2
        #mid_node will be used to keep track of the node at the mid point
        mid_node = linked_list.node_at_index(mid-1)
    #set the left half of the list to the head of the list     
    left_half = linked_list
    #set the right half to a new linked list
    right_half = LinkedList()
    #set the head of the right half to the node after the mid node
    right_half.head = mid_node.next_node
    #mid node's next node will be set to None
    mid_node.next_node = None

    #return left and right halves
    return left_half, right_half


def merge(left, right):
    """
        Merges two linked lists, sorting by data in nodes
        Returns a new merged list
        Takes O(n) space
        Runs in O(n) time
    """

        # Create a new linked list that contains nodes from merging left and right
    merged = LinkedList()
    # Add a fake head that is discarded later.
    merged.add(0)
        # Set current to the head of the linked list
    current = merged.head

    # Obtain head nodes for left and right linked lists
    left_head = left.head
    right_head = right.head

    # Iterate over left and right as long until the tail node of both
    # left and right
    while left_head or right_head:
    # If the head node of left is None, we're at the tail
    # Add the tail node from right to the merged linked list
        if left_head is None:
            current.next_node = right_head
        # Call next on right to set loop condition to False
            right_head = right_head.next_node 
        # If the head node of right is None, we're at the tail
        # Add the tail node from left to the merged linked list
        elif right_head is None:
            current.next_node = left_head
        # Call next on left to set loop condition to False
            left_head = left_head.next_node
        else:
            # Not at either tail node
            # Obtain node data to perform comparison operations
            left_data = left_head.data
            right_data = right_head.data

            # If data on left is lesser than right set current to left node
            # Move left head to next node
            if left_data < right_data:
                current.next_node = left_head
                left_head = left_head.next_node
            # If data on left is greater than right set current to right node
            # Move right head to next node
            else:
                current.next_node = right_head
                right_head = right_head.next_node

        # Move current to next node
        current = current.next_node

        # Discard fake head and set first merged node as head
    head = merged.head.next_node
    merged.head = head
        
    # Return merged linked list
    return merged
            

ll = LinkedList()
node1 = Node(2)
node2 = Node(4)
print(node1)
#node1 points to node2 
node1.next_node = node2
#will print the data of node2
print(node1.next_node)

#we'll set the head of the linked list to node1
ll.head = node1
print('linked list size:', ll.size())
#add nodes at the head of the list
ll.insert_at_head(3)
ll.insert_at_head(5)
print(ll) #Output: [Head: 5]-> [3]-> [2]-> [Tail: 4]
node_found = ll.search(3)
print(node_found)


'''MERGE SORT
Time complexity: O(n log n). Space complexity: O(n)'''
def merge_sort(list):
    #base case: if the list is a single element, return the list
    if len(list) <= 1:
        return list
    #find the mid point of the list
    mid = len(list)//2
    #recursively call merge_sort on the left half of the list
    left= merge_sort(list[:mid])
    #recursively call merge_sort on the right half of the list
    right = merge_sort(list[mid:])
    
    #create a list to hold the sorted values
    sorted_values = []
    
    #These indices will keep track of the position of the elements in the left and right halves
    left_index = 0
    right_index = 0
    
    #keep looping until we've gone through all the elements in both halves
    while left_index < len(left) and right_index < len(right):
        #if the element at the left index is less than the element at the right index, we'll append the element at the left index to the sorted_values list and increment left_index by 1
        if left[left_index] < right[right_index]:
            sorted_values.append(left[left_index])
            left_index += 1
        #if the element at the right index is less than the element at the left index, we'll append the element at the right index to the sorted_values list and increment right_index by 1
        else:
            sorted_values.append(right[right_index])
            right_index += 1
    #if there's any element left in the left half, we'll append it to the sorted_values list
    sorted_values += left[left_index:]
    #if there's any element left in the right half, we'll append it to the sorted_values list
    sorted_values += right[right_index:]
    #retrun the sorted_values list
    return sorted_values


sort_list=[8,10,3,1,5,2,7,4]
print(merge_sort(sort_list))



'''QUICK SORT
Time complexity: O(n log n) average case, O(n^2) worst case. Space complexity: O(log n)
'''

def quick_sort(list):
    #base case: if the list has only one element or is empty, return the list
    if len(list) <= 1:
        return list
    #set the pivot to the last element in the list
    pivot = list.pop()
    #create two empty lists to hold the elements less than the pivot and the elements greater than the pivot
    left = []
    right = []
    #loop through the list and append elements less than the pivot to the left list and elements greater than the pivot to the right list
    for element in list:
        #if the element is less than the pivot(last element in the list), append it to the left list
        if element < pivot:
            left.append(element)
        else:
            right.append(element)
    #recursively call quick_sort on the left and right lists and concatenate the results with the pivot
    return quick_sort(left) + [pivot] + quick_sort(right)