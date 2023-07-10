# https://practice.geeksforgeeks.org/problems/fractional-knapsack-1587115620/1

# Fractional Knapsack
# Given weights and values of N items, we need to put these items in a knapsack of capacity W to get the maximum total value in the knapsack.
# Note: Unlike 0 / 1 knapsack, you are allowed to break the item.

# Example 1:
# Input: N = 3, W = 50
# values[] = {60, 100, 120}
# weight[] = {10, 20, 30}
# Output: 240.00
# Explanation: Total maximum value of item we can have is 240.00 from the given capacity of sack.

# Example 2:
# Input:
# N = 2, W = 50
# values[] = {60, 100}
# weight[] = {10, 20}
# Output: 160.00
# Explanation: Total maximum value of item we can have is 160.00 from the given capacity of sack.

# Your Task: Complete the function fractionalKnapsack() that receives maximum capacity, array of structure / class and size n and returns a double value representing the maximum value in knapsack.
# Note: The details of structure / class is defined in the comments above the given function.

# Expected Time Complexity: O(NlogN)
# Expected Auxiliary Space: O(1)

# Constraints:
# 1 <= N <= 105
# 1 <= W <= 105
# ------------------------------------------------------------------------------------------------------------------------------------------------
# Approach1:Sort the given arr in descending order of their val/weight ratio. Further we'll devise a val and weight variable to keep track of total val and weight updated at each iteration as we traverse through the sorted array. While traversing if current item's weight added into weight variable stays less or equal to permitted Max weight we'll add curr item's weight and val into weight and val variables respectively. If item's weight added to weight var exceeds the permitted weight then we'll include only fractional weight of that item as much as it doesnt exceed and value for only that much fraction will be added to val variable, before breaking the for loop. We'll return val variable.
"""
class Item:
    def __init__(self,val,w):
        self.value = val
        self.weight = w
"""

class Solution:
    def fractionalknapsack(self, W, arr, n):
        # Here arr is a list of Item objects.
        arr.sort(key=lambda x: x.value / x.weight, reverse=True)
        weight = val = 0
        for item in arr:
            if weight + item.weight <= W:
                weight += item.weight
                val += item.value
            else:
                val += ((W - weight) / item.weight) * (item.value)
                weight += ((W - weight) / item.weight)
                break
        return val
# TC: O(nlogn+n) Explanation: nlogn n to sort the array. n for going through all weights while adding them in total weight and calculating total value we can offer.
# SC: O(1)