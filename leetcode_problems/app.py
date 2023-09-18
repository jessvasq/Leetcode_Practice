'''BINARY SEARCH'''
'''Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.
You must not use any built-in exponent function or operator.
For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.'''

def find_square_root(x):
    lo= 0
    #given integer
    hi= x
    
    while lo <= hi:
        #find the middle element (e.g. 81//2 = 40.5, we use floor division '//' rounds the result down to the nearest whole num (e.g. 40)
        mid_num= (lo+hi) // 2 
        print('mid_num:', mid_num)
        
        if mid_num * mid_num == x: #(if e.g 40 * 40 = to 81, we return the mid_num, since that's not the case we move to the elif statement)
            return mid_num
        
        elif mid_num * mid_num <= x: #(if e.g. 40 * 40 is less or equal than 81, we increment lo + 1. Since this is not the case, we move to the else statement )
            lo = mid_num + 1
            print('lo:', lo)
        
        else:
            hi= mid_num -1 # we use e.g. hi = 40 - 1 which is equal to 39 and continue the loop until we find the answer. 39 would be the new value for 'x'. The mid num for 39 would be 19, skip 'if' and 'elif' statement -> use 19 as x, where mid=9, we test the first condition where 9 * 9 = to x and print the answer 
            print('hi:', hi)
    

    return lo-1

x=81
print(find_square_root(x))
        
   
'''Given two integer arrays nums1 and nums2, sorted in non-decreasing order, return the minimum integer common to both arrays. If there is no common integer amongst nums1 and nums2, return -1. Note that an integer is said to be common to nums1 and nums2 if both arrays have at least one occurrence of that integer.
 '''  

 
def find_common_min(arr1, arr2):

    #find hi and lo elements for both arrays
    lo = 0 
    hi = len(arr1)-1
    arr2_lo = 0
    arr2_hi = len(arr2)-1
    
    while lo <= hi and arr2_lo <= arr2_hi:
        #compare the first two lo elements, if they're equal return lo
        if arr1[lo] == arr2[arr2_lo]:
            return arr1[lo]
        
        #if the lo element in arr1 is less than lo element in list 2, increment arr1 lo by 1 
        elif arr1[lo] < arr2[arr2_lo]:
            lo += 1
            
        #else increment arr2 low by 1     
        else: 
            arr2_lo += 1
  
    #return -1 if there's no common integer
    return -1 
                  
    
nums1 = [1,2,3]
nums2 = [2, 4]

print(find_common_min(nums1, nums2))
     