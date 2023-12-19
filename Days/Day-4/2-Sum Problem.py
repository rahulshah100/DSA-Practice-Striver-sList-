# https://leetcode.com/problems/two-sum/

# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

# Example1:
# Input: nums = [2, 7, 11, 15], target = 9
# Output: [0, 1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

# Example2:
# Input: nums = [3, 2, 4], target = 6
# Output: [1, 2]

# Example3:
# Input: nums = [3, 3], target = 6
# Output: [0, 1]

# Constraints:
# 2 <= nums.length <= 10^4
# -10^9 <= nums[i] <= 10^9
# -10^9 <= target <= 10^9
# Only one valid answer exists.
# ----------------------------------------------------------------------------------------------------------------------------------------------------
# Approach1: Two for loops, first pointing to all elems one by one and second one within the first for loop will check for all the remaining elem if combined with item pointed by first loop, they sum up-to target. If found return it, or else to next iteration.
# Time Complexity: O(n^2) given that nums is represented as n.
# Space Complexity: O(1)


# Approach2: Sorting the given array and in the sorted array using a similar to Binary Search technique to find target elem. So we start with pointing 1st and last item of array using first and last pointer in the sorted array. If these pointer's sum to target, we've found the items. If sum is less we make fist pointer point to array's next item. If sum is more we change our last pointer to a previous item. Thus having found items would return coordinates for sorted array. We further run a loop in original array and locate these 2 items and return these coordinates.
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        tempNums = nums[:]  #As nums dont have any subitems that are derived data types like arrays or tuples we can use shallow copy
        tempNums.sort()     #Remember lists are mutable so we dont have to do assignment i.e. tempNums=tempNums.sort()
        i, j = 0, len(nums) - 1 #In fact sort() has None as it's return type, so tempNums=tempNums.sort() will infact backfire & hence we just use tempNums.sort()
        while i < j:
            if tempNums[i] + tempNums[j] == target:
                break
            elif tempNums[i] + tempNums[j] < target:
                i += 1
            else:
                j -= 1

        firstCoord = secondCoord = None
        for x in range(len(nums)):
            if tempNums[i] == nums[x] and firstCoord is None: #firstCoord is None is imp condition or say in [3,3] target = 6 our firstCoord will be assigned to initally 0th and in later iteration to 1st index whereas secondCoord will stay None
                firstCoord = x
            elif tempNums[j] == nums[x]:
                secondCoord = x

        return firstCoord, secondCoord

S = Solution()
print(S.twoSum([3, 2, 4], 6))
# TC: O(nlogn+2n) Explanation: nlogn to sort and n times for finding elems in the sorted array plus n more time to locate the found elems in original array
# SC: O(n) Explanation: to store nums1


# Approach3: Better Time. In approach 1 reducing a for-loop by using hashDict. One for loop will continuously loop through array, starting which hashDict will be empty. We'll check if target-currentItemPointedByFor is in hashDict if not we store this item and move to next iteration thus up-till last iteration all values are stored in hashMap, and we refer to it at any given iteration alongside item pointed by for-loop to see if it collectively we can find a count equal to target.
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashtable={}
        for i in range(len(nums)):
            if hashtable.get(target-nums[i])!=None: #Note: this line could also be written as "if target-nums[i] in hashtable:" and in both ways, it'll take only a O(1) time in python
                return (hashtable[target-nums[i]], i)
            else:
                hashtable[nums[i]]=i

S=Solution()
print(S.twoSum([2,7,11,15], 13))
# Time Complexity: O(n). Explanation: n time for all iterations in for loop. Also, the dictionary.get() takes only O(1) unless we've complicated keys like arrays which isn't the case here. So in total only O(n) time complexity would occur
# Space Complexity: O(n). For storing n items in hashtable.