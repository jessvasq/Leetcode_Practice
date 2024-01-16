'''169. Majority Element'''
# nums = [2,2,1,1,1,2,2]
# print('max', max(nums))

# #use the Boyer-Moore Voting Algorithm. The key idea is to cancel out each occurrence of an element with all the other elements that are different from it. This way, the majority element, if it exists, will eventually stand out.
# def find_majority(nums):
#     x = None
#     count = 0
#     for i in nums:
#         if count == 0:
#             x = i
#         count += 1 if i == x else -1 
#     return x

# print(find_majority(nums))


#find min value to buy a stock
#find max value to sell a stock
# prices = [7,6,4,3,1]

'''121. Best Time to Buy and Sell Stock - E
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

'''

# def maxProfit(prices):
#     #if prices is empty or has only one element
#     if prices is None or len(prices) == 1:
#         return 0
#     #initialize variables 
#     min_price = prices[0]
#     profit = 0
    
#     #iterate through each price 
#     for price in prices:
#         #update the min price to buy 
#         min_price = min(min_price, price)
#         #update the max price 
#         profit = max(profit, price-min_price)    
        
#     return profit
  
# print(maxProfit(prices))


'''80. Remove DUplicates from a sorted array II'''
nums = [0,0,1,1,1,1,2,3,3]
#Output: 5, nums = [1,1,2,2,3,_]
    
#use a pointer to identify if the current element is different from the element two positions back. If so, update the pointer to the current element. We use the pointer to keep track of the length of the array without duplicates.
def remove_duplicates(nums):
    #check if the length of the array is less or equal to 2. If so, return len(arr)
    if len(nums) <= 2:
        return len(nums) 
    #initialize a pointer set to 2 
    pointer = 2
    #iterate through the array from range 2 to len(arr)
    for i in range(2, len(nums)):
        #check if the current index is not equal to pointer -2
        if nums[i] != nums[pointer-2]:
            #if so, update the pointer to the current index
            nums[pointer] = nums[i]
            #increment the pointer by 1 so that it points to the next index
            pointer +=1 
    return pointer
      
print(remove_duplicates(nums))
     
