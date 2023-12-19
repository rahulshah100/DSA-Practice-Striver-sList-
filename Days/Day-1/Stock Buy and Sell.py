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
        maxProf=0
        for i in range(len(prices)):
            for j in range(i+1,len(prices)):
                if maxProf<prices[j]-prices[i]:
                    maxProf=prices[j]-prices[i]
        return maxProf

S = Solution()
arr = [7, 1, 5, 3, 6, 4]
# arr = [7, 6, 4, 3, 1]
# arr = [3, 2, 1]
print(S.maxProfit(arr))"""
# TimeComplexity:O(n^2). Explanation: for the first iteration of outer loop, the inner loop will run for n-1 times then for second iteration of outer loop, the inner one will run for n-2... upto lastly it will run for 1 time. We recognize this as binomial sum and that total iterations here will be n(n+1)/2 which could be generalized as n^2.
# SpaceComplexity: O(1). Just a variable with constant space is required extra by the program hence it's space complexity is O(1).


# Approach2: Improved time complexity. Kedane's algo - at each point we decide if it could be a buying point if it's lesser than prev buying point's price. If not we consider it to be a selling point and find the difference between this point's price with prev buying point's price. If difference is greater than maxProfit so far, this will be the new maxProfit.
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit, smallestItem = 0, 0
        for i in range(1, len(prices)):
            maxProfit = max(maxProfit, prices[i] - prices[smallestItem])
            if prices[i] < prices[smallestItem]: smallestItem = i
        return maxProfit


S = Solution()
arr = [7, 1, 5, 3, 6, 4]
arr = [2, 8, 1, 6]
arr = [7, 6, 4, 3, 1]
arr = [3, 2, 1]
S.maxProfit(arr)
# Time Complexity: O(n)
# Space Complexity: O(1)
