# Best Time to Buy and Sell Stock
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

# You are given an array prices where prices[i] is the price of a given stock on the ith day. You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock. Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

# Input: prices = [7,1,5,3,6,4] Output: 5 Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5. Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
# Input: prices = [7,6,4,3,1] Output: 0 Explanation: In this case, no transactions are done and the max profit = 0.

# Constraints:
# 1 <= prices.length <= 10^5
# 0 <= prices[i] <= 10^4
# ------------------------------------------------------------------------------------------------------------------------


# Approach1: My Original Approach. Checking all possibilities.
from typing import List

"""
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        highestProfit=-1
        for i in range(len(prices)):
            for j in range(i+1, len(prices)):
                if prices[j]-prices[i]>highestProfit:
                    highestProfit=prices[j]-prices[i]
        if highestProfit<0:
            highestProfit=0
        return highestProfit

S = Solution()
arr = [7, 1, 5, 3, 6, 4]
# arr = [7, 6, 4, 3, 1]
# arr = [3, 2, 1]
print(S.maxProfit(arr))"""
# TimeComplexity:O(n^2). Explaination: for the first iteration of outer loop, the inner loop will run for n-1 times then for second iteration of outer loop, the inner one will run for n-2... upto lastly it will run for 1 time. We recongnize this as binomial sum and that total iterations here will be n(n+1)/2 which could be generalized as n^2.
# SpaceComplexity: O(1). Just a variable with constant space is required extra by the program hence it's space complexity is O(1).


# Approach2: Improved time complexity. If in one pass we can start from begining and go on to the end, at every point we can check and update the lowestValue in array till that point and use that for further counting difference i.e.Profit at that point from the lowest buying point found that far. If at any iteration, the difference i.e. Profit is found more than the most profit found that far, then we update the global max profit. If we find a number lower than lowest then we'll update the lowest so we'll keep on getting the highest profit for all the array items when traversing forward in the array is performed.
class Solution:
    def maxProfit(self, prices) -> int:
        lowest = prices[0]
        currentProfit = -1
        GlobalMaxProfit = 0
        for i in range(1, len(prices)):
            if prices[i] < lowest:
                lowest = prices[i]
            currentProfit = prices[i] - lowest
            if currentProfit >= GlobalMaxProfit:
                GlobalMaxProfit = currentProfit
                # print(i, len(prices), prices[i])
        print(GlobalMaxProfit)
        return GlobalMaxProfit


S = Solution()
arr = [7, 1, 5, 3, 6, 4]
arr = [2, 8, 1, 6]
arr = [7, 6, 4, 3, 1]
arr = [3, 2, 1]
S.maxProfit(arr)
# Time Complexity: O(n)
# Space Complexity: O(1)
