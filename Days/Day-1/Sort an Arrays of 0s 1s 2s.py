# Sort Colors
# https://leetcode.com/problems/sort-colors/

# Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue. We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively. You must solve this problem without using the library's sort function.

# Input: nums = [2,0,2,1,1,0] Output: [0,0,1,1,2,2]
# Input: nums = [2,0,1] Output: [0,1,2]
# Input: nums = [0] Output: [0]
# Input: nums = [1] Output: [1]

# Constraints:
# n == nums.length
# 1 <= n <= 300
# nums[i] is either 0, 1, or 2.
#-----------------------------------------------------------------------------------------------------------
# Approach 1: My Original Approach - Array Hashmap
from typing import List

"""class Solution:
    def sortColors(self, nums: List[int]) -> None:
        # Do not return anything, modify nums in-place instead.
        hasArr = [0, 0, 0]
        for i in range(len(nums)):
            if nums[i] == 0:
                hasArr[0] += 1
            elif nums[i] == 1:
                hasArr[1] += 1
            else:
                hasArr[2] += 1

        ct=0
        for i in range(len(hasArr)):
            for j in range(hasArr[i]):
                nums[ct]=i
                ct+=1
        print(nums)

S=Solution()
S.sortColors([2,0,2,1,1,0])
S.sortColors([2,0,1])
"""
# Time Complexity:O(2N) given nums array is shown as N. Explanation: the first for loop runs for N times. For the second for loop which is a nested one the outer one will run for 3 times, in effect making the inner one run in-total for N times as the hashmap is storing total N counts i.e.hashmap[0]+hashmap[1]+hashmap[2]=N; Therefore, total=N+N=2N Time Complexity.
# Space Complexity: O(1). We are using hashmap and ct as variables occupying any extra space in the program. Those having constant space requirement we get O(1) here.


# Approach2: Bubble Sort - Worst Complexities
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] > nums[j]:
                    nums[i], nums[j] = nums[j], nums[i]
        print(nums)
# TC: O(n(n+1)/2)
# SC: O(1)


# Approach 3: Better Time Complexity - Three Pointer
# If unlike Approach1 where we had to make 2 passes i.e. two for loops: one for storing counts in hashmap and another for storing those many values in nums, if we could make it in one pass then the time complexity would be divided in half. We'll do it by using three pointers lower, upper and current i.e. l, u and c which are initiated from index 0,0 and last index of array respectively. These pointer have the following use: c is current pointer which will traverse the array. It'll work to filter items in a way that all 0s will be before u and all 2s will be after l. Once in traversal c crosses l we know the sorting has been done.
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        u, c, l = 0, 0, len(nums) - 1
        while c <= l:
            if nums[c] == 0:
                nums[c], nums[u] = nums[u], nums[c]
                u += 1
            elif nums[c] == 2:
                nums[c], nums[l] = nums[l], nums[c]
                l -= 1
            else:
                c += 1

            if c < u: #In case where c has been lapsed behind u
                c = u
        print(nums)

S = Solution()
# S.sortColors([2, 0, 2, 1, 1, 0])
S.sortColors([2, 1, 1 ,1, 0, 1, 1])
# Time Complexity: O(N)
# Space Complexity: O(1)