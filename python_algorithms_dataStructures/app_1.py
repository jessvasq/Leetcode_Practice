'''PRACTICE'''
'''A user forgot the password of his linkedin account. But he knows the ASCII values of his password in reverse order. Help the user to find the password.
Given the string, decode the password'''

#Loop 
#Reverse the string  
#convert from ASCI values to strings or integers 
#return the answer in a string (.join method)
#does the password have alphabets only? or does it include blank spaces? or numbers? 

password1="101109971110"

def find_pw(str):
    #reverse the string '' by using the slicing notation used with strings 
    reverse_str = str[::-1] #first empty part indicates you want to start slicing at the beginning of the string, the second empty part indicates we want to end at the beginning of the string. The -1 means that we want to move through the string in reverse order, from the end towards the beginning
    print(reverse_str)
    
    #initial value
    i = 0
    #result = empty string
    result = ''
    
    while i < len(str)-1:
        ascii_value = str[i] + str[i+1]
        if ascii_value == '32':
            result = result + ''
        elif int(ascii_value) in range(65, 91) or int(ascii_value) in range(97, 100):
            result = result + chr(int(ascii_value))
        elif i+2<len(str):
            ascii_value = ascii_value + str[i+2]
            result = result + chr(int(ascii_value))
            i+=1
        i+=2
    return result

print(find_pw(password1))

'''There is a group of people which also includes two monsters in this group and they split these groups among the people to kill them. When monsters come into the group of people, then at that time people leave their group.
After that, the breaking of the group will continue due to the monster's entry. And at last, the group with the minimum length will be killed by the monsters. Two types of monsters are present there namely '@' and '$'. People are presented as a string 'P'. Now you have to find out the minimum length of the group which will be killed by monsters '''

#find the min

def find_min(str): 
    #splits the string using the @ character as the delimiter
    groups = str.split('$')
    #This line initializes a variable min_length to positive infinity (float('inf')). This initial value is used to ensure that the first minimum length found in the subsequent loop will be smaller than this initial value.
    min_length= float('inf')
    
    for group in groups: 
        #further splits each group using the @ character as the delimiter
        subgroups = group.split('@')
        #creates a list called lengths using a list comprehension. It calculates the length of each substring in the subgroups list and stores these lengths in the lengths list.
        lenghts = [len(subgroup) for subgroup in subgroups]
        #compare the min length found within the current group (min(lengths)) with the current minimum length stored in the min_length variable. 
        min_length = min(min_length, min(lenghts))
    
    return min_length

test1= 'PPPPPP@PPP@PP$PP'
#test 
print(find_min(test1))

#######################

'''1.Given a string, write a function to reverse it'''
 
#SOLUTION 1
#use the slicing notation. -1 indicates that we want to move through the string in reverse order, from the end towards the beginning
def reverse_str(str):
    reversed_list = str[::-1]
    return reversed_list
    
#test
test0 = 'tsil'
print(reverse_str(test0))


'''Implement a binary search tree and write a function to find the kth smallest element in the tree.'''
#implement a binary search tree
class TreeNode: 
    def __init__(self, value): 
        self.value = value
        self.left = None
        self.right = None
        
#write a funtion that performs the inorder traversal(visit the leftmost node) keeping track of the nodes visited
class BST: 
    def __init__(self): 
        self.root = None
        
    def insert(self, value): #self referes to the instance of the BST class, allows us to access and modify the object's attributes and call other methods within the class 
        
        #self.root represents the node of the BST, which could be none if it is empty 
        self.root = self._insert(self.root, value) #passes the root and the value 
        
    def _insert(self, node, value): #node is the root of the current subtree
        
        # check if the current node is None, indicating that the function has reached an empty (null) node. If this is the case, it creates a new BSTNode with the specified key and value,
        if node is None: 
            node = TreeNode(value)
            
        # checks whether the VALUE to be inserted is less than the VALUE of the current node (node.VALUE). If it is we insert to the left 
        elif value < node.value:
            node.left = self._insert(node.left, value)
            node.left.parent = node
            
         # checks whether the VALUE to be inserted is greater than the VALUE of the current node (node.VALUE). If it is we insert to the right
        elif value > node.value: 
            node.right = self._insert(node.right, value)
            node.right.parent = node 
        return node 
    
        
    def find_kth(self, k): 
        count = [0] #keep track of the nodes we visit 
        return self._kth_num(self.root, k, count)
    
                            #k is the smallest number 
    def _kth_num(self, node, k, count): #node represents the current node being considered in the traversal. Starts with the root node and during recursion moves to the left and right
        if node is None:
            return None #if it returns none, indicates that the node has not been found in this branch
        
        #visit the left side first 
        min_l = self._kth_num(node.left, k, count) #recursively calls _kth_num function and uses the node.left as the current node in the traversal
        if min_l is not None: 
            return min_l
        count[0] += 1 #This line increments the count of visited nodes by 1. This is done for each node visited during the traversal.
        
        if count[0] == k: #This line checks if the count of visited nodes has reached the desired kth value. If it has, this means the current node's value is the kth smallest element, so it returns node.value
            return node.value 
        return self._kth_num(node.right, k, count) #continues to search on the right branch until it finds kth or exhausts all nodes 
    
    
#TEST 
bst = BST()
bst.insert(8)
bst.insert(3)
bst.insert(10)
bst.insert(5)

k = 1
kth_smallest = bst.find_kth(k)
print(f"The {k}th smallest element is {kth_smallest}")


'''Write a function to find the longest common prefix of an array of strings.'''

#loop through the array 
#compare each character and compare to the other characters in other strings 


def longest_common_prefix(strs):
    # Handle the case of an empty input array
    if not strs:
        return ""

    # Find the minimum length string in the array
    min_length = min(len(s) for s in strs)

    print('min length: ', min_length)
    
    # Initialize the longest common prefix
    common_prefix = ""

    # Iterate through characters at the same position in all strings
    for i in range(min_length):
        char = strs[0][i]  # Get the character from the first string
        print('char: ', char)
        
        for s in strs:
            if s[i] != char:
                print('common prefix: ', common_prefix)
                return common_prefix
               
        common_prefix += char
        print('loop: ', common_prefix)

    return common_prefix


# Example usage:
strings = ["unhappy", "unsatisfied", "unified"]
result = longest_common_prefix(strings)
print("Longest Common Prefix:", result)



'''Write a function to generate the first n numbers of the Fibonacci sequence.'''
#Fibonacci sequence is a series of numbers where each number is the sum of the two preceding ones
#the first and 2nd elements of the fibonacci series are 0 and 1 
#iterate from 1 to n-1 and print f2 then store f2 in a variable and update f2 with f2+f1 and f1 as f2

def print_fibonacci(n):
    # Initialize the first two Fibonacci numbers
    f1=0
    f2=1
    
    if (n<1):
        return
    print(f1, end='')
    
    for _ in range(1,n):
        print(f2, end='')
        # Calculate the next Fibonacci number by adding the last two
        next_num = f1+f2 
        #we assign f1 to f2
        f1 = f2
        f2 = next_num

#Time Complexity: O(n) 
#Auxiliary Space: O(1)
n=5
print_fibonacci(n)



'''Given an array of integers, write a function to find the largest sum of any contiguous subarray.'''
#Kadane's algorithm is used to find the maximum sum of any contiguous subarray within a one-dimensional array of numbers, whether the numbers are positive, negative, or zero.

def max_subarray_sum(nums):
    if not nums:
        return 0

    #We initialize max_sum and current_sum to the first element of the array nums[0]
    max_sum = current_sum = nums[0]

    for num in nums[1:]: #iterate starting at the second element
        
        #update current_sum by taking the maximum of the current element or the sum of the current element and the previous
        current_sum = max(num, current_sum + num) 
        
        #store the maximum subarray sum encountered so far.
        max_sum = max(max_sum, current_sum)

    return max_sum

# Example usage:
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
result = max_subarray_sum(nums)
print("Largest sum of contiguous subarray:", result)



'''You have to complete a function getNumber which receives a single argument H, where H is the head of a linked list. Each node of the linked list contains an integer which is either 1 or 0. Placing all the integers present in the linked list in a order from left to right, forms a binary number. Return the decimal representation of the binary number to the base 10'''

class ListNode: #represents a node in the linked list 
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next #reference to the next node

def getNumber(head):
    binary_representation = 0
    
    # Traverse the linked list
    current = head #keeps track of the current node
    while current is not None:
        # Left-shift the binary representation and add the current node's value
        binary_representation = (binary_representation * 2) | current.value  
        current = current.next
    
    return binary_representation

# Example usage:
# Create a linked list: 1 -> 0 -> 1 -> 0
node4 = ListNode(0)
node3 = ListNode(1, node4)
node2 = ListNode(0, node3)
node1 = ListNode(1, node2)

decimal_representation = getNumber(node1)
print("Decimal Representation:", decimal_representation)


'''You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.'''


def merge(nums1, m, nums2, n):
    # Initialize pointers for nums1 and nums2
    p1 = m - 1
    p2 = n - 1
    
    # Initialize a pointer for the merged array (nums1)
    p = m + n - 1
    
    # Merge nums1 and nums2 from the end
    while p1 >= 0 and p2 >= 0:
        if nums1[p1] > nums2[p2]:
            nums1[p] = nums1[p1]
            p1 -= 1
        else:
            nums1[p] = nums2[p2]
            p2 -= 1
        p -= 1
    
    # If there are remaining elements in nums2, copy them to nums1
    while p2 >= 0:
        nums1[p] = nums2[p2]
        p -= 1
        p2 -= 1

# Example usage:
nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3

merge(nums1, m, nums2, n)
print(nums1)  # The merged array should be [1, 2, 2, 3, 5, 6]

