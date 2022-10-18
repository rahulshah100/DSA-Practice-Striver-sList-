# https://leetcode.com/problems/reverse-pairs/
# Given an integer array nums, return the number of reverse pairs in the array.
# A reverse pair is a pair (i, j) where 0 <= i < j < nums.length and nums[i] > 2 * nums[j].

# Example 1:
# Input: nums = [1, 3, 2, 3, 1]
# Output: 2

# Example 2:
# Input: nums = [2, 4, 3, 5, 1]
# Output: 3

# Constraints:
# 1 <= nums.length <= 5 * 104
# -231 <= nums[i] <= 231 - 1
# -----------------------------------------------------------------------------------------------------------------------------------------------------
# Approach1: Two for loops. First for loop pointing at one element, second for pointing at all the element after it, one by one. If condition of nums[i] > 2 * nums[j] matches then use a counter variable, and keep on increasing it's value.
# Time Complexity: O(n^2). Explaination: It will take n(n+1)/2 iterations in total for the both the for loops to traverse the entire array.
# Space Complexity: O(1). Explaination: We'll just use one extra variable i.e. count, which will hold only an integer value. So we use constant space i.e.O(1).

# Approach2: Better time, compromised space Complexity. We'll use Merge sort and in there at the stage when elements would be merged, we'll check for nums[i] > 2 * nums[j]. If so, we'll increase a counter variable. For left and right two such arrays, while merging we'll check if arr[i] is lesser than or equal to arr[j] if so
from typing import List

class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        ReversePairCount=0
        MergeSort(nums, ReversePairCount, len(nums))
        return ReversePairCount

def MergeSort(nums, count, n):
    if len(nums) > 1:
        # Dividing arrays
        low = 0
        high = len(nums)
        mid = low + high // 2

        left = MergeSort(nums[:mid], count, n)
        right = MergeSort(nums[mid:], count, n)

        # Sorting Arrays
        i = 0
        j = 0
        k = 0
        while i < len(left) and j < len(right):
            count+=1
            if left[i] < right[j]:
                nums[k] = left[i]
                i += 1
            else:
                nums[k] = right[j]
                j += 1
            k += 1

        # Merging

        if i != len(left):
            while i != len(left):
                nums[k] = left[i]
                i += 1
                k += 1
        if j != len(right):
            while j != len(right):
                nums[k] = right[j]
                j += 1
                k += 1
        if len(left) + len(right) == n:
            return count
        return nums
    else:
        return nums


S=Solution()
print(S.reversePairs([23,12,34,1,232,63]))