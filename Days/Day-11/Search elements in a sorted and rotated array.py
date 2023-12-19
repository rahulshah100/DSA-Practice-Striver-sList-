# https://leetcode.com/problems/search-in-rotated-sorted-array/

# There is an integer array nums sorted in ascending order( with distinct values). Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k(1 <= k < nums.length) such that the resulting array is [nums[k], nums[k + 1], ..., nums[n - 1], nums[0], nums[1], ..., nums[k - 1]](0 - indexed).For example, [0, 1, 2, 4, 5, 6, 7] might be rotated at pivot index 3 and become[4, 5, 6, 7, 0, 1, 2]. Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums. You must write an algorithm with O(log n) runtime complexity.

# Example 1:
# Input: nums = [4, 5, 6, 7, 0, 1, 2], target = 0
# Output: 4

# Example 2: Input: nums = [4, 5, 6, 7, 0, 1, 2], target = 3
# Output: -1

# Example 3: Input: nums = [1], target = 0 Output: -1
# Constraints: 1 <= nums.length <= 5000
# -104 <= nums[i] <= 104
# All values of nums are unique. nums is an ascending array that is possibly rotated.
# -104 <= target <= 104
# ----------------------------------------------------------------------------------------------------------------------------------
# Approach1: Run a for loop and check for all items if they're equal to target, in case of which return that index. Outside for loop return -1.
# TC:O(n)
# SC: O(1)

# Approach2: Binary Search - Array is sorted but just with a catch of left and right such 2 arrays. So everytime while calculating mid, we'll check whether mid when compared with lower indicates that it is left half, then we'll further check if target falls between the lower to mid. If target can be found we'll decrement upper to mid-1. If target cant be found we increment lower to mid+1. Contrarily if we were not in left half we check if target falls in between mid to upper in which case we increase lower to mid+1; and if not then we decrement u to mid-1.
from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, u = 0, len(nums)-1
        while l <= u:
            mid = (l + u) // 2
            if nums[mid] == target:
                return mid
            elif nums[l] <= nums[mid]:
                if nums[l] <= target <= nums[mid]:
                    u = mid - 1
                else:
                    l = mid + 1
            else:
                if nums[mid] <= target <= nums[u]:
                    l = mid + 1
                else:
                    u = mid - 1
        return -1

S = Solution()
print(S.search([5, 1, 3], 3))
# TC: O(logn)
# SC: O(n)