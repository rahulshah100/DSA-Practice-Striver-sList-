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
# Approach 1: Merge sort the given array and in that run a for loop to check till the sequence breaks that was the consequtive count found. Find all such consecutive count and mark the max of those as Answer.
from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:  # To handle case where array is empty and we wont want to return GlobalMaxCount which is 1
            return 0
        nums.sort()
        GlobalMaxCount = 1
        localMaxCount = 1
        i = 0
        while i < len(nums) - 1:
            if nums[i + 1] == nums[i] + 1:
                localMaxCount += 1
            elif nums[i + 1] == nums[i]:
                pass
            else:
                if GlobalMaxCount < localMaxCount: GlobalMaxCount = localMaxCount
                localMaxCount = 1
            i += 1
        GlobalMaxCount = max(GlobalMaxCount, localMaxCount)
        return GlobalMaxCount


# S = Solution()
# S.longestConsecutive([100, 4, 200, 1, 3, 2])
# S.longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1])
# Time Complexity: O(nlogn + n) Explanation: Assuming that we used Merge sort for sorting the given array, it will take nlogn time. Further, we're running one for loop through n sized arr, hence it'll take n more time. Total = nlogn+n
# Space Complexity: O(n) Explanation: Considering we used Merge Sort for sorting, as merge sort take n space, we have n space complexity here.


# Approach2: Using hashmap to reduce the time complexity. We'll use a hashSet so to avoid repetitions of number in hashmap. After making a hashset from original list, we'll iterate through the original list and for each element encountered, we'll check in hashSet if an element just one smaller than that exists. If so, we'll do nothing and move onto the next iteration. Thusby we're making sure if there has to be chain of consequtives this number aint starting point and so it cant give us full length of chain if check for increasing numbers from this point on. However, if the just one smaller number doesnt exist, then we go on checking for the just one bigger number from encountered number, and then just one bigger than that, till we don't find a bigger in this sequence. Going up is when we'll note the count of consequtives and the max of all such counts would be the output.
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        hashSet = set()
        for i in range(len(nums)):
            hashSet.add(nums[i])
        maxConseq = 1
        for i in range(len(nums)):
            if nums[i] - 1 in hashSet: continue
            j = nums[i]
            currConseq = 1
            while j + 1 in hashSet:
                j += 1
                currConseq += 1
            maxConseq = max(maxConseq, currConseq)
        return maxConseq


S = Solution()
S.longestConsecutive([100, 4, 200, 1, 3, 2])
S.longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1])
# Time Complexity: O(n) Explanation: n time for making the hashSet. Further, the for loop we have will at max iterate through any given array item just twice. Once when it is checked and found a smaller number exists, and second time when from this smaller number discovered earlier when we start iterating and iterate through the prior encountered greater number. Hence in total this for will take O(2n). Total=O(n+2n)=O(3n)=O(n)
# Space Complexity: O(n) Explanation: for hashSet with n items n space is required.
