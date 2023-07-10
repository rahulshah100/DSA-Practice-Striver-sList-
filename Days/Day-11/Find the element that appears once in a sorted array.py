# https://leetcode.com/problems/single-element-in-a-sorted-array/

# You are given a sorted array consisting of only integers where every element appears exactly twice, except for one element which appears exactly once. Return the single element that appears only once. Your solution must run in O(log n) time and O(1) space.

# Example1:
# Input: nums = [1, 1, 2, 3, 3, 4, 4, 8, 8]
# Output: 2

# Example2:
# Input: nums = [3, 3, 7, 7, 10, 11, 11]
# Output: 10

# Constraints:
# 1 <= nums.length <= 10^5
# 0 <= nums[i] <= 10^5
# ----------------------------------------------------------------------------------------------------------------------------------------
# Approach1: Traversing the given Array if i==0 we'll just compare current item with next one and if it's not equal we'll return arr[i]. For other items we'll match them with their previous and their next if none matches we return this item. Now as for last item in arr if we match it with array item of next index we'll get error. So we'll traverse upto only last 2nd item in array. And outside the for-loop we return last item.
from typing import List

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        for i in range(0, len(nums) - 1):
            if i == 0 and nums[i] != nums[i + 1]:
                return nums[i]
            elif nums[i] != nums[i - 1] and nums[i] != nums[i + 1]:
                return nums[i]
        return nums[-1]

S = Solution()
print(S.singleNonDuplicate([3, 3, 7, 7, 10, 11, 11]))
print(S.singleNonDuplicate([1, 1, 2]))
# TC: O(n)
# SC: O(1)


# Approach2: Binary Search could be used as array is sorted. We'll use intuition of the mid being equal to it's next number if it's at an even index, or equal to it's prev number if it's at an odd index. If it is so, we know so far inconsistency has not come, meaning we are in left part of our array, wherein starting from number that shows only once we'll be in right part of array. If we find ourselves to be in left part we'll change the low to mid+1. If we're in right part we change upper to mid-1. As lower pointer crosses upper we return the item at upper.
from typing import List


class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        l, u = 0, len(nums)-2 #Capping u to 2nd last item of given Arr so when l exceeds u at farthest it'll be on last item and not out of array
        while l <= u: #Always remember as even for the number where and l and u meet we would want to check if it's in meeting the condition so it's alway '<=' not just '<'
            mid = (l + u) // 2
            if ((mid + 1) % 2 != 0 and nums[mid] != nums[mid + 1]) or ((mid+1)%2==0 and nums[mid] != nums[mid - 1]):
                u=mid-1
            elif ((mid + 1) % 2 != 0 and nums[mid] == nums[mid + 1]) or ((mid+1)%2==0 and nums[mid]== nums[mid-1]):
                l=mid+1
        return nums[l]

S = Solution()
print(S.singleNonDuplicate([1, 1, 2, 3, 3, 4, 4, 8, 8]))
# print(S.singleNonDuplicate([3, 3, 7, 7, 10, 11, 11]))
# print(S.singleNonDuplicate([1, 1, 2, 2, 3]))
# TC: O(logn)
# SC: O(1)