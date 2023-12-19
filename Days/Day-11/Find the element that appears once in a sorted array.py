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
# Approach1: Traversing the given Array we compare the current item with next. If they are not same we check if current is equal to previous even if which is false, we'll return the current item. Considering the corner cases 1) When i=0 and next item doesn't match, to match current with previous, we don't have a prev so we separate this case 2) If we don't get a return in for-loop the last item which can't be checked with the item after it, is the one we return,
from typing import List

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        for i in range(len(nums) - 1):
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


# Approach2: Binary Search could be used as array is sorted. We'll use intuition of the mid being equal to it's next number if mid is an even index, or equal to it's prev number if it's at an odd index. If it is so, we know so far inconsistency has not come, meaning we are in left part of our array, wherein starting from number that shows only once we'll be in right part of array. If we find ourselves to be in left part we'll change the low to mid+1. If we're in right part we change upper to mid-1. As lower pointer crosses upper we return the item at upper.
from typing import List

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        l, u = 0, len(nums) - 2  # Capping u to 2nd last item of given Arr so when nums[mid] != nums[mid + 1] is checked there is always one item left after mid
        while l <= u:  # Always remember that even for the number where l and u meet, we want to check the condition for that number, and so condition is always '<=' and not just '<'
            mid = (l + u) // 2
            if mid % 2 == 0 and nums[mid] != nums[mid + 1] or mid % 2 != 0 and nums[mid] != nums[mid - 1]:
                u = mid - 1
            else:
                l = mid + 1
        return nums[l] #As we're incrementing l such that onto it's left no inconsistency is there, thus starting l onto right array we know we've captured inconsistency and we return nums[l] which is the source of inconsistency that goes forward in that part.

S = Solution()
print(S.singleNonDuplicate([1, 1, 2, 3, 3, 4, 4, 8, 8]))
# print(S.singleNonDuplicate([3, 3, 7, 7, 10, 11, 11]))
# print(S.singleNonDuplicate([1, 1, 2, 2, 3]))
# TC: O(logn)
# SC: O(1)