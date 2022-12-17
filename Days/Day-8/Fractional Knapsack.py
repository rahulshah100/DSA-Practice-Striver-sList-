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
# Expected Auxilliary Space: O(1)

# Constraints:
# 1 <= N <= 105
# 1 <= W <= 105
# ------------------------------------------------------------------------------------------------------------------------------------------------
# Approach1: Sort the items in descending order of value/weight. For the given max-weight-allowed in question, keep adding value from the sorted array and keep the track of total weight, up untill the total weight becomes more. Output the total Value.
class Solution:
    # Function to get the maximum total value in the knapsack.
    def fractionalknapsack(self, W, Items, n):
        # Here Items is a list of objects. Every object has a value and weight key.
        ItemsArr = [] #Making an Array of arrays from array of objects which I think is redundant/avoidable
        for i in Items:
            ItemsArr.append([i.value, i.weight])

        ItemsArr.sort(key=lambda x: x[0] / x[1], reverse=True) #Sort as per highest value per unit of weight

        totalVal, totalWeight, i = 0, 0, 0
        while totalWeight <= W and i < len(ItemsArr): #total weight of all items could be together less than allowed weight and hence i<len(ItemsArr) is necessary or we see error in below ItemsArr[i][1]
            if totalWeight + ItemsArr[i][1] <= W: #If addition of entire current weight would still keep total weight less than max Allowed then this is case
                totalWeight += ItemsArr[i][1]
                totalVal += ItemsArr[i][0]
            else:
                WeightTaken = W - totalWeight
                if WeightTaken > 0:             #We'll check if partial weight could be added from this item to keep weight less than or equal to max-weight-allowed. If so this is the case
                    totalWeight += WeightTaken
                    totalVal += (ItemsArr[i][0] / ItemsArr[i][1]) * WeightTaken #Calculating value for one unit of weight for this item and then multiplying value with the fraction weight we chose here.
                else:    break                     #If not even partial is added then we have no more weight which could be further added and so we break out of the loop
            i += 1
        # print(totalVal, totalWeight)
        return totalVal
# TC: O(n+nlogn+n) Explanation: n for making an array of arrays. nlogn n to sort the array. n for going through all weights while adding them in total weight and calculating total value we can offer.
# SC: O(n) Explanation: for making an array of arrays