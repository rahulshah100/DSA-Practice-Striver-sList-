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
# Approach1: take 2 counts currCount and globalCount. Traverse entire array and if item value is found as 1 increase currCount, after which check if it is greater than globalCount in which scenario we'll update globalCount with currCount. If an item different than one is found, we'll make currCount 0 at that point. Return globalCount as answer.
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        currCount, globalCount=0, 0
        for i in range(0,len(nums)):
            if nums[i]==1:
                currCount+=1
                if currCount>globalCount:globalCount=currCount
            else:
                currCount=0
        print(globalCount)
        return globalCount
# TC: O(N)
# SC: O(1)