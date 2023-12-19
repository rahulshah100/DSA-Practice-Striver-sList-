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
# Approach1:Sort the given arr in descending order of their val/weight ratio. Further, in a for loop we'll traverse over the given array each time checking if deducting the current weight from given weight gives 0 or a positive number. If so, we'll subtract from given weight, the weight of current item and add in totVal the val of this item. Conversely if subtraction results in a negative number we know the full item cant be accomodated and in totVal we'll only increment a unit's val * leftWeight i.e. arr[i].val/arr[i].weight * W, at this point we break the for-loop as given weight W is all exhausted and we return totVal.
"""
class Item:
    def __init__(self,val,w):
        self.value = val
        self.weight = w
"""

class Solution:
    def fractionalknapsack(self, W, arr, n):
        arr.sort(key=lambda x: x.value / x.weight, reverse=True)
        totVal = 0
        for i in range(len(arr)):
            if W - arr[i].weight >= 0:
                W -= arr[i].weight
                totVal += arr[i].value
            else:
                totVal += (arr[i].value / arr[i].weight) * W
                break
        return totVal
# TC: O(nlogn+n) Explanation: nlogn n to sort the array. n for going through all weights while adding them in total weight and calculating total value we can offer.
# SC: O(1)