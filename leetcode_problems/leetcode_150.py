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
prices = [7,6,4,3,1]

'''121. Best Time to Buy and Sell Stock - E
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

'''

def maxProfit(prices):
    #if prices is empty or has only one element
    if prices is None or len(prices) == 1:
        return 0
    #initialize variables 
    min_price = prices[0]
    profit = 0
    
    #iterate through each price 
    for price in prices:
        #update the min price to buy 
        min_price = min(min_price, price)
        #update the max price 
        profit = max(profit, price-min_price)    
        
    return profit
    
    
    
    
    
    
    
    
    
    min_x = prices.index(min(prices))
    max_num = max(prices[min_x:])
    profit = max_num - min(prices)
    
    if profit > 0:
        return profit
    else:
        return 0


print(maxProfit(prices))

