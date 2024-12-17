'''
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

 

Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
Example 2:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.

'''

def BuyAndSellStocks(prices):

    # copy list so we can pop first element:
    price_list = list.copy(prices)
    max_profit = 0

    # iterate over each element in prices:
    for i in prices:
        # pop first element so it doesn't get checked anymore afterwards:
        buy = price_list.pop(0)

        # iterate over copied list with popped first elements:
        for j in (price_list):
            # check for a new max_profit higher than 0:
            if (j - buy) > max_profit:
                max_profit = j - buy

    return max_profit

# Test the function
test1 = [7,1,5,3,6,4]
test2 = [7,6,4,3,1]
test3 = [7,4,5,3,6,1]

print(BuyAndSellStocks(test1))
print(BuyAndSellStocks(test2))
print(BuyAndSellStocks(test3))

def BuyAndSellStocksImrpoved(prices):
    # Initialize the buying price with the first price in the list
    buy = prices[0]
    # Initialize profit to zero
    profit = 0 

    # Loop through the prices starting from the second price
    for i in range(1, len(prices)):
        # If the current price is lower than the buying price, update the buying price
        if prices[i] < buy:
            buy = prices[i]
        # If the difference between the current price and the buying price is greater than the current profit
        elif prices[i] - buy > profit:
            # Update profit to the new # maximum profit
            profit = prices[i] - buy

    # Return the maximum profit found
    return profit

# Other Implementations:
def otherSolution(prices):
    localMax = 0
    globalMin = prices[0]
    maxMax=0
    
    for i in prices:
        if i <globalMin:
            globalMin = i
            localMax = i
        elif i > localMax:
            localMax = i
            maxMax = max(localMax - globalMin,maxMax)

    return maxMax