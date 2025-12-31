#  Convert Sorted Array to Binary Search Tree

# DESCRIPTION
# You are given an array prices where prices[i] is the price of a given stock on the ith day.
# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

# EXAMPLE
# Example 1:
# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
# Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
# Example 2:
# Input: prices = [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transactions are done and the max profit = 0.

# CONSTRAINTS
# 1 <= prices.length <= 105
# 0 <= prices[i] <= 104

# SOLUTION
class Solution:
  def maxProfit(self, prices: List[int]) -> int:
    buy = prices[0] # Initialize the minimum buying price as the first day's price
    profit = 0      # Variable to store the maximum profit found so far

    # Iterate through each price in the list from the second day onwards
    for price in prices[1:]:
      # If current price is lower than previous buy price,
      # update buy to get a cheaper buying day
      if price < buy:
        buy = price

      # Otherwise, check if selling at current price
      # gives a higher profit than before
      elif price - buy > profit:
        profit = price - buy

    # Return the maximum profit (0 if no profit is possible)
    return profit
