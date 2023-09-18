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
        
   
   