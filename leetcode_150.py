'''9. Palindrome Number - Easy'''

def isPalindrome(x):
    #check if the number is negative
    if x < 0:
        return False
    #check if the given number is equal to the reverse of the number
    else:
        return str(x) == str(x)[::-1]
    
'''69. Sqrt(x) - Easy Must not use any built-in library functions such as sqrt.'''
def mySqrt(x):
   #based on the fact that the square root of x is always less than x/2 except for 0 and 1. We can use binary search to find the square root of x 
   
   #for numbers less than 2, the square root is the number itself
    if x < 2: 
      return x
   
    lo = 1
    #find half of the input *Reminder: the square root of x is always less than x/2 
    hi = x//2
    #initialize ans to 0, ans will store the square root of x
    ans=0
    
    while lo <= hi:
        mid = (lo + hi) // 2
        #square the mid value to compare with x
        mid_squared = mid * mid
        #if the mid_squared is equal to x, it means that mid is the square root of x
        if mid_squared == x:
            return mid
        elif mid_squared < x:
            lo= mid+1
            #we store the mid value in ans because we want to return the floor value of the square root of x
            ans=mid
        else:
            hi=mid-1
    return ans
    