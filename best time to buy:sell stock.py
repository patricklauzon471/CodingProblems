# Given an array of prices where prices[i] is the price of a given stock on the ith day
# Want to maximize profit by choosing a single day to buy one stock and a different day to sell the stock
# Return max profit that can be acheived from this transaction

# Example1 prices = [7,1,5,3,6,4]
# Output = 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6) profit 6-1 = 5

class Solution():

    def maxProfit(self, prices):

      # two pointer programming solution, set your left (buy) and right (sell) value
      # l is 0 while r is one because you have to buy before selling
      # buy will always lag behind sell
        l = 0
        r = 1
        maxP = 0

        while r < len(prices):
            # Move through the list
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                # Finds the max profit given the two defined arguments
                maxP = max(maxP, profit)
            else:
                l = r
                # if left is higher than right need to shift it to the right position
                # Right position would be at the minimum
            r += 1
            # if buy is less than sell it stops, which is at the minimum and right continues through
        return maxP


print(Solution().maxProfit([1, 6, 3, 21, 14]))
