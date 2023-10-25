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


    '''There are three ways to add data to a linked list: Insert at the head, insert at the tail, and insert in the middle. We'll start with inserting at the head'''

    #this method inserts a new node at the head of the list. Takes O(1) time or constant time which is our best case scenario
    def insert_at_head(self, data):
        #create a new node
        new_node = Node(data)
        #set the next node of the new node to the current head
        new_node.next_node = self.head
        #set the head to the new node
        self.head = new_node




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


