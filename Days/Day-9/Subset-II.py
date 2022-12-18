# https://leetcode.com/problems/subsets-ii/

# Subsets II
#  Given an integer array nums that may contain duplicates, return all possible subsets (the power set). The solution set must not contain duplicate subsets.Return the solution in any order.

# Example1:
# Input: nums = [1, 2, 2]
# Output: [[], [1], [1, 2], [1, 2, 2], [2], [2, 2]]

# Example2:
# Input: nums = [0]
# Output: [[], [0]]

# Constraints:
# 1 <= nums.length <= 10
# -10 <= nums[i] <= 10
# --------------------------------------------------------------------------------------------------------------------------------------------
# Approach1: In Day9/Subset Sums.py in it's optimal solution i.e.pick and non pick approach, if we at last convert the list from a set, we'll not see any duplicates resulting in answer of this question.
from typing import List

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        output=set()
        def func(index,sum,nums,output):
            if index==n:
                output.add(sum)
                return
            func(index+1,sum+nums[index],nums,output)
            func(index + 1, sum, nums, output)
        func(0,0,nums,output)
        return list(output)
S=Solution()
print(S.subsetsWithDup([1,2,2]))
# TC:O(2^n + 2^n) Explanation: Reduction of (2^n)log(2^n) and Addition of 2^n time in pick non pick approach's TC, as no sorting is done here and as we've 2^n numbers are pushed into a list from a set.
# SC:O(2^n) Explanation: Stack space of 2^n will be freed up when 2^n space will be required by set for temporarily storing items.