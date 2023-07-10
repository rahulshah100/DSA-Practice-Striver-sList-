# https://leetcode.com/problems/max-consecutive-ones/

# Max Consecutive Ones
# Given a binary array nums, return the maximum number of consecutive 1's in the array.

# Example 1:
# Input: nums = [1,1,0,1,1,1]
# Output: 3
# Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.

# Example 2:
# Input: nums = [1,0,1,1,0,1]
# Output: 2

# Constraints:
# 1 <= nums.length <= 105
# nums[i] is either 0 or 1.
#------------------------------------------------------------------------------------------------------------------------------------------------
# Approach1: take 2 counts maxOnes and tempCt. Traverse entire array and if item value is found as 1 increase tempCt. If an item different than one is found, we'll make tempCt 0 but before which we'll check if tempCt is greater than maxOnes and if so, update maxOnes to tempCt. Return max amongst tempCt and maxOnes as answer.
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxOnes = tempCt = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                tempCt += 1
            else:
                maxOnes = max(maxOnes, tempCt)
                tempCt = 0
        return max(tempCt, maxOnes)
# TC: O(N)
# SC: O(1)