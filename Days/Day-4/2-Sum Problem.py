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
# Approach1: Two for loops, first pointing to all elems one by one and second one within the first for loop will check for all the remaining elem if there os an elem with value target-nums[i[. If found return it, or else i will go to next iteration.
# Time Complexity: O(n^2) given that nums is represented as n.
# Space Complexity: O(1)


# Approach2: Sorting the given array and using Binary Search to find target elems. Later locating those elems in unsorted/original array and returning those indices
from typing import List
import copy

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums1 = copy.deepcopy(nums)
        nums1.sort()
        val1 = val2 = None
        l, u = 0, len(nums) - 1
        while l < u: #Retrieving elems that sum upto target
            if nums1[l] + nums1[u] == target:
                val1, val2 = nums1[l], nums1[u]
                break
            elif nums1[l] + nums1[u] < target:
                l += 1
            elif nums1[l] + nums1[u] > target:
                u -= 1
        val1NotFound = True
        for i in range(len(nums)): #Retrieving the indices of elems that sum upto target
            if nums[i] == val1 and val1NotFound:
                val1 = i
                val1NotFound = False
            elif nums[i] == val2:
                val2 = i
        return [val1, val2]

S = Solution()
print(S.twoSum([-18, 12, 3, 0], -6))
# TC: O(nlogn+2n) Explanation: nlogn to sort and n times for finding elems, plus n time to find the indices of those elem.
# SC: O(n) Explanation: to store nums1


# Approach3: Better Time. As there are two elems that'll sum upto target, hence if we traverse the array storing the items and their indexes in a hashmap, and alongside if we keep checking at each traversal if target-nums[i] could be found in the hashmap, then when 2nd number of pair will be encounterd, at that time it's counter part i.e.target-nums[i] would certainly be found in the hashmap. We can return both of these indexes.
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashtable={}
        for i in range(len(nums)):
            if hashtable.get(target-nums[i])!=None: #Note: this line could also be written as "if target-nums[i] in hashtable:" and in both ways, it'll take only a O(1) time in python
                return (hashtable[target-nums[i]], i)
            else:
                hashtable[nums[i]]=i
        print(hashtable)
S=Solution()
print(S.twoSum([2,7,11,15], 13))
# Time Complexity: O(n). Explaination: n time for all iterations in for loop. Also the dictionary.get() takes only O(1) so in total only O(n) time complexity would occur
# Space Complexity: O(n). For storing n items in hashtable.