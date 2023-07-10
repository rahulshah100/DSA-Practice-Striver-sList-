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
# TimeComplexity:O(n^2). Explanation: for the first iteration of outer loop, the inner loop will run for n-1 times then for second iteration of outer loop, the inner one will run for n-2... upto lastly it will run for 1 time. We recongnize this as binomial sum and that total iterations here will be n(n+1)/2 which could be generalized as n^2.
# SpaceComplexity: O(1). Just a variable with constant space is required extra by the program hence it's space complexity is O(1).


# Approach2: Improved time complexity. Similar to kedane's algo we're here using a 3 pointer method. Idea here is potential of changing buying date only comes if we find a new less buying, which if so, then from there on we look for the upcoming highest selling price. First pointer i goes through array in one iteration. On every next index it goes, starting from 1 (not 0 because that's with what we have initiated our buylow i.e.bl and sellhigh i.e.sh variables) if we find a val smaller than prev. bl, we update the bl. Now since bl has been updated we can only sell in future and hence if sh had a value of any prev index we update it to bl, so from here on buying-then-selling difference could be counted. On i's visit to next index if we find a val. greater than prev. sh's we update sh and that's when we need to count newly made profit which if greater than maxProf we update newProf to be our maxProf
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        bl = sh = profMax = 0
        for i in range(1, len(prices)):
            if prices[i] < prices[bl]:
                bl = sh = i
            elif prices[i] > prices[sh]:
                sh = i
                if prices[sh] - prices[bl] > profMax:
                    profMax = prices[sh] - prices[bl]
        return profMax


S = Solution()
arr = [7, 1, 5, 3, 6, 4]
arr = [2, 8, 1, 6]
arr = [7, 6, 4, 3, 1]
arr = [3, 2, 1]
S.maxProfit(arr)
# Time Complexity: O(n)
# Space Complexity: O(1)
