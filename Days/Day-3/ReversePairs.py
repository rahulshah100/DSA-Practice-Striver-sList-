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
# Approach1: Two for loops. First for loop pointing at one element, second for pointing at all the element after it one by one. If condition of nums[i] > 2 * nums[j] matches then use a counter variable, and keep on increasing it's value.
"""class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        count=0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]> 2*nums[j]:
                    count+=1
        return count"""
# Time Complexity: O(n^2). Explanation: It will take n(n+1)/2 iterations in total for the both the for loops to traverse the entire array.
# Space Complexity: O(1). Explanation: We'll just use one extra variable i.e. count, which will hold only an integer value. So we use constant space i.e.O(1).

# Approach2: Better time, compromised space Complexity. We'll use Merge sort and in there at the stage when elements would be merged, we'll check for nums[i] > 2 * nums[j]. If so, we'll increase a counter variable.
from typing import List

class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        nums, count = merge(nums)
        return count


def merge(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L, ct1 = merge(arr[:mid])
        R, ct2 = merge(arr[mid:])
    else:
        return arr, 0

    l = u = ct3 = 0
    while l < len(L) and u < len(R): #Unlike the Day-2's inversion Pair problem where inside merge block itself we incorporated the count increment here we are not simply asked if L[l] is greater than R[u] but specifically if L[l] is greater than 2*R[u]. Hence consider L=[1,3,8] and [2,3,7]. So first L[l]=1 and R[u]=2 hence no inversions. Second L[l]=3 and R[u]=2 here inside #--1 simple inversion Pair is triggered & ct3 is incremented by len(L)-l but if we had put L[l]>2*R[u] inside #--1 then L[l]>2*R[u] wont be triggered and u will immediately be incremented. So Despite having elem such as L[2] which is greater than 2*R[u], it wont be accounted for. And that is why we have to use this seperate while block here.
        if L[l] > 2 * R[u]:
            ct3 += len(L) - l
            u += 1
        else:
            l += 1

    l = u = 0
    for i in range(len(arr)):
        if l < len(L) and u >= len(R):
            arr[i] = L[l]
            l += 1
        elif u < len(R) and l >= len(L):
            arr[i] = R[u]
            u += 1
        elif L[l] <= R[u]:
            arr[i] = L[l]
            l += 1
        elif L[l] > R[u]:   #--1
            arr[i] = R[u]
            u += 1
    ct = ct1 + ct2 + ct3
    return arr, ct


S = Solution()
print(S.reversePairs([2, 4, 3, 5, 1]))
# Time Complexity: O(nlogn) Explaination: Total time taken here is (N i.e. Time taken for updating ct3 + N i.e.Time taken for merging) * (log(N) i.e. Number of Times Recursion Will Happen) => (N+N)logN => O(2NlogN) => O(NlogN)
# Space Complexity: O(n) Explaination: Apart from what mergesort uses, here we are using couple of more variables with constant space allocation like count, index_i. Hence O(n)+o(1)=O(n).
