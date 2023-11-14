
def fizz_buzz(n):
    if (n%3 == 0) and (n%5 == 0):
        return 'FizzBuzz'
    elif n%3 == 0:
        return 'Fizz'
    elif n%5 == 0:
        return 'Buzz'
    else:
        return str(n)
    
print(fizz_buzz(15))

'''412. Fizz Buzz - E
Given an integer n, return a string array answer (1-indexed) where:
answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
answer[i] == "Fizz" if i is divisible by 3.
answer[i] == "Buzz" if i is divisible by 5.
answer[i] == i (as a string) if none of the above conditions are true.'''
    
#Time complexity: O(n) - linear. 
#Space complexity: O(n) because we are creating a list of n elements

def fizz_buzz(n):
    #create an empty list to store the answer
    answer = []
    #loop through the range of 1 to n+1
    for i in range(1, n+1):
        #if i is divisible by 3 and 5, append FizzBuzz to the list
        if (i%3 == 0) and (i%5 == 0):
            answer.append('FizzBuzz')
        #if i is divisible by 3, append Fizz to the list
        elif i%3 == 0:
            answer.append('Fizz')
        elif i%5 == 0:
            answer.append('Buzz')
        #else append the number as a string to the list
        else:
            answer.append(str(i))
    return answer

print(fizz_buzz(15))

'''27. Remove Element - E
Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.

Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the elements which are not equal to val. The remaining elements of nums are not important as well as the size of nums.
Return k.'''
nums = [3,2,2,3]
val = 3

def remove_element(nums, val):
    #use two pointers
    lo = 0
    hi = len(nums)-1
    
    #while the low pointer is less than or equal to the high pointer
    while lo <= hi:
        #if the value at the low pointer is equal to the value we want to remove (val)
        if nums[lo] == val:
            #swap the values at the low and high pointers
            nums[lo], nums[hi] = nums[hi], nums[lo]
            #high pointer goes down by 1
            hi -= 1
        #if the value at the low pointer is not equal to the value we want to remove (val)
        else:
            #low pointer goes up by 1
            lo += 1
    #return the low pointer as the length of the array, we return lo because the low pointer is the index of the first element that is not equal to val
    return int(lo)


print(remove_element(nums, val))

n = 11111111111111111111111111111101


'''190. Reverse Bits - E
Reverse bits of a given 32 bits unsigned integer.'''

def reverse_bits(n):
    reverse_bits = 0
    #loop through 32 given bits
    for i in range(32):
        #shift the reverse_bits to the left by 1 to make room for the next bit
        reverse_bits <<= 1
        print(reverse_bits)
        #if the last bit of n is 1, then add 1 to reverse_bits
        if n & 1:
            reverse_bits += 1
        #shift n to the right by 1
        n >>= 1
    return reverse_bits

print(reverse_bits(n))

'''
14. Longest Common Prefix - E
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".
'''

strs = ["flower","flow","flight"]

def longestCommonPrefix(strs):
    #if the list is empty, return an empty string
    if len(strs) == 0:
        return ''
    #set the prefix to the first element in the list
    prefix = strs[0]
    #loop through the list starting at the second element
    for i in range(1, len(strs)):
        #while the prefix is not in the beginning of the element, remove the last character of the prefix
        while prefix not in strs[i][:len(prefix)]:
           #remove the last character of the prefix
            prefix = prefix[:-1]
    #return the prefix 
    return prefix

print(longestCommonPrefix(strs))



'''217. Contains Duplicate - E
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.'''

nums = [1,2,3,1]

#using a set to remove duplicates and comparing the length of the set to the length of the given list

def contains_duplicate(nums):
    #create a set from the list of numbers. A set removes duplicates
    nums_set = set(nums)
    #if the length of the set is not equal to the length of the list, return True
    if len(nums_set) != len(nums):
        return True
    #else return False
    else:
        return False
    
print(contains_duplicate(nums))

#using count method
def contains_duplicate1(nums):
    for num in nums:
        x = nums.count(num)
        if x > 1:
            return True

print(contains_duplicate1(nums))

'''28. Find the Index of the First Occurrence in a String - E
Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

'''
haystack = 'leeto'
needle = 'leetcode'

def str_str(haystack, needle):
    if  needle not in haystack:
        return -1
    else:
        return haystack.index(needle)
    
print(str_str(haystack, needle))