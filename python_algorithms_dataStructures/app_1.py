# '''PRACTICE'''
# '''A user forgot the password of his linkedin account. But he knows the ASCII values of his password in reverse order. Help the user to find the password.
# Given the string, decode the password'''

# #Loop 
# #Reverse the string  
# #convert from ASCI values to strings or integers 
# #return the answer in a string (.join method)
# #does the password have alphabets only? or does it include blank spaces? or numbers? 

# password1="101109971110"

# def find_pw(str):
#     #reverse the string '' by using the slicing notation used with strings 
#     reverse_str = str[::-1] #first empty part indicates you want to start slicing at the beginning of the string, the second empty part indicates we want to end at the beginning of the string. The -1 means that we want to move through the string in reverse order, from the end towards the beginning
#     print(reverse_str)
    
#     #initial value
#     i = 0
#     #result = empty string
#     result = ''
    
#     while i < len(str)-1:
#         ascii_value = str[i] + str[i+1]
#         if ascii_value == '32':
#             result = result + ''
#         elif int(ascii_value) in range(65, 91) or int(ascii_value) in range(97, 100):
#             result = result + chr(int(ascii_value))
#         elif i+2<len(str):
#             ascii_value = ascii_value + str[i+2]
#             result = result + chr(int(ascii_value))
#             i+=1
#         i+=2
#     return result

# print(find_pw(password1))

# '''There is a group of people which also includes two monsters in this group and they split these groups among the people to kill them. When monsters come into the group of people, then at that time people leave their group.
# After that, the breaking of the group will continue due to the monster's entry. And at last, the group with the minimum length will be killed by the monsters. Two types of monsters are present there namely '@' and '$'. People are presented as a string 'P'. Now you have to find out the minimum length of the group which will be killed by monsters '''

# #find the min

# def find_min(str): 
#     #splits the string using the @ character as the delimiter
#     groups = str.split('$')
#     #This line initializes a variable min_length to positive infinity (float('inf')). This initial value is used to ensure that the first minimum length found in the subsequent loop will be smaller than this initial value.
#     min_length= float('inf')
    
#     for group in groups: 
#         #further splits each group using the @ character as the delimiter
#         subgroups = group.split('@')
#         #creates a list called lengths using a list comprehension. It calculates the length of each substring in the subgroups list and stores these lengths in the lengths list.
#         lenghts = [len(subgroup) for subgroup in subgroups]
#         #compare the min length found within the current group (min(lengths)) with the current minimum length stored in the min_length variable. 
#         min_length = min(min_length, min(lenghts))
    
#     return min_length

# test1= 'PPPPPP@PPP@PP$PP'
# #test 
# print(find_min(test1))

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