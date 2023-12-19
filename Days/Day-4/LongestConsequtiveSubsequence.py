# https://leetcode.com/problems/longest-consecutive-sequence/

# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence. You must write an algorithm that runs in O(n) time.

# Example 1:
# Input: nums = [100, 4, 200, 1, 3, 2]
# Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4].Therefore its length is 4.

# Example 2:
# Input: nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
# Output: 9

# Constraints:
# 0 <= nums.length <= 10^5
# -10^9 <= nums[i] <= 10^9
# --------------------------------------------------------------------------------------------------------------------------------------------------------
# Approach 1: Sort the given array and in that run a for loop starting from second elem, to check if the elem is just one more than its previous elem. Which if is the case we increment a localmax counter which was initially declared to be 1. Each time this happens we update a globalmax counter depending on whether localmax have become greater than globalmax. Conversely, if the elem is same as previous elem we know the order of items in array doesn't matter and can pretend it wasn't at this position, and therefore we can continue quest of finding more consecutive elem, by ignoring this type of iteration. If those are not the case we know the consecutive chain has broken, and we reset the localmax to 1 hoping to find further consecutive chains. At the end we take into consideration an end case where if an empty array is given we return 0 or else globalmax.
from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        localmax=globalmax=1
        for i in range(1,len(nums)):
            if nums[i]==nums[i-1]+1:
                localmax+=1
                globalmax=max(localmax, globalmax)
            elif nums[i]==nums[i-1]:
                continue
            else:
                localmax=1
        return globalmax if len(nums)>0 else 0

# S = Solution()
# S.longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1])
# Time Complexity: O(nlogn + n) Explanation: Assuming that we used Merge sort for sorting the given array, it will take nlogn time. Further, we're running one for loop through n sized arr, hence it'll take n more time.
# Space Complexity: O(n) Explanation: Considering we used Merge Sort for sorting, as merge sort take n space, we have n space complexity here.


# Approach2: Using hashmap to reduce the time complexity. We'll use a hashSet so to avoid repetitions of number in hashmap. After making a hashset from original list, we'll iterate through the original list and for each element encountered, we'll check in hashSet if an element just one smaller than that exists. If so, we'll do nothing and move onto the next iteration. Thusby we're making sure if there has to be chain of consecutives this number ain't starting point and so it cant give us full length of chain if we check for increasing numbers from this point on. However, if the just one smaller number doesn't exist, then we go on checking for the just one bigger number from encountered number, and then just one bigger than that, till we don't find a bigger in this sequence. Going up is when we'll note the count of consecutives and the max of all such counts would be the output.
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashSet = set()
        for i in range(len(nums)):
            hashSet.add(nums[i])

        globalMax=0
        for i in range(len(nums)):
            localMax = 0
            if nums[i] - 1 in hashSet:
                continue
            else:
                j = nums[i]
                while j in hashSet:
                    localMax += 1
                    j += 1
                globalMax = max(localMax, globalMax)

        return globalMax if len(nums) > 0 else 0


S = Solution()
S.longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1])
# Time Complexity: O(n) Explanation: n time for making the hashSet. Further, the for loop will at max iterate through any given array item just twice. Once when it is checked and found a smaller number exists, and second time when from this smaller number discovered earlier when we start iterating and iterate through the prior encountered greater number. Hence, in total this for will take O(2n). Total=O(n+2n)=O(3n)=O(n)
# Space Complexity: O(n) Explanation: for hashSet with n items n space is required.
