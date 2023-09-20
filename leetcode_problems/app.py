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

'''33. Search in Rotated Sorted Array'''
'''There is an integer array nums sorted in ascending order (with distinct values).
Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].
Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.
You must write an algorithm with O(log n) runtime complexity.'''

def search_target(nums, target):
    lo, hi = 0, len(nums)-1  
      
    while lo <= hi:
        mid = (lo + hi) // 2
        mid_num = nums[mid]
        
        if mid_num == target: 
            return mid
            
        elif mid_num >= nums[lo]:
            if target >= nums[lo] and target < mid_num:
                hi = mid - 1
            else:
                lo = mid + 1
        
        else:
            if target > mid_num and target <= nums[hi]:
                lo = mid + 1
            else: 
                hi = mid - 1 
    return -1 


nums_search = [4,5,6,7,0,1,2]
target = 3

print(search_target(nums_search, target))

            
        