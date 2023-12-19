# https://leetcode.com/problems/kth-largest-element-in-an-array/

# Given an integer array nums and an integer k, return the kth largest element in the array.
# Note that it is the kth largest element in the sorted order, not the kth distinct element.
# Can you solve it without sorting?

# Example 1:
# Input: nums = [3, 2, 1, 5, 6, 4], k = 2
# Output: 5

# Example 2:
# Input: nums = [3, 2, 3, 1, 2, 4, 5, 5, 6], k = 4
# Output: 4

# Constraints:
# 1 <= k <= nums.length <= 10^5
# -10^4 <= nums[i] <= 10^4
# -------------------------------------------------------------------------------------------------------------------------------------------
# Approach1: Build a max-heap, and as it'll not be sorted completely like it could be 6,5,4,3,2 or 6,4,5,2,3 or many other possibilities, but we know top element will always be greatest. So we heap-pop for k-1 times, and we know thus found heap must have kth the biggest item at top at this time, which is what we return
from typing import List
import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        maxHeap=[]
        for i in range(len(nums)):
            heapq.heappush(maxHeap, -nums[i])

        for i in range(k-1):
            heapq.heappop(maxHeap)
        return -maxHeap[0]

S = Solution()
print(S.findKthLargest([3,2,1,5,6,4], 2))
print(S.findKthLargest([3,2,3,1,2,4,5,5,6], 4))
# TC: O(2nlogn) Explanation: pushing n items in maxHeap takes logn time each and thus nlogn here and heappop takes logn time each time for k times which can at worst be n, making this additional nlogn time.
# SC: O(n) Explanation: to store n items in maxHeap.


# Approach2: To avoid iterative heapPush, we can use heapify and sort the given nums itself, in minHeap fashion (as heapify by default does) and again as we cant pin whether we'll have 2,3,4,5,6 or 2,4,3,5,6 we'll keep popping the items for len(nums)-k times and thus element present at top is kth biggest one, which we return.
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)

        for i in range(len(nums) - k):  # Here we think if in nums of length 6 we were asked to return 6th largest item then as we are using  minHeap, it's going to be the 0th index of the Heap and hence we'd want to avoid any popping to take place; thus we identify len(nums)-k as the condition we use
            heapq.heappop(nums)
        return nums[0]
# TC: O(n+nlogn) Explanation: Than approach1, here nlogn won't be pushing TC, but it'd just be n
# SC: O(1)