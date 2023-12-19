# https://leetcode.com/problems/sliding-window-maximum/

# You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.
# Return the max sliding window.

# Example1:
# Input: nums = [1, 3, -1, -3, 5, 3, 6, 7], k = 3
# Output: [3, 3, 5, 5, 6, 7]
# Explanation:
# Window position           Max
# ---------------          -----
#[1  3 -1] -3 5 3 6 7       3
# 1 [3 -1 -3] 5 3 6 7       3
# 1 3 [-1 -3 5] 3 6 7       5
# 1 3 -1 [-3 5 3] 6 7       5
# 1 3 -1 -3 [5 3 6] 7       6
# 1 3 -1 -3 5 [3 6 7]       7

# Example2:
# Input: nums = [1], k = 1
# Output: [1]

# Constraints:
# 1 <= nums.length <= 10^5
# -10^4 <= nums[i] <= 10^4
# 1 <= k <= nums.length
# --------------------------------------------------------------------------------------------------------------------------------
# Approach1: Using a nested for-loop where outer-one iterates over the given array up-till len(nums) -k +1 index, and inner will start from i and go to i+k index. With each iteration the outer for-loop will set a variable which is used a variable to keep track of biggest number amongst iteration of inner for-loop.
from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ansArr = []
        for i in range(0, len(nums) - k + 1):
            maxItem = nums[i]
            for j in range(i + 1, i + k):
                maxItem = max(maxItem, nums[j])
            ansArr.append(maxItem)
        return ansArr

S = Solution()
print(S.maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3))
# TC: O(n*k) Explanation: Outer loop runs for n-k i.e. n times and each time inner one runs for k times
# SC: O(1) Explanation: excluding the space required to store the answer we return, no extra storage occupied


# Approach2: Using a monotonous stack to hold k items (in their index form) for the current window, which are reversely sorted i.e. at bottom we'll have the largest number; we'll traverse the given array using a for-loop. While traversing the given array if we encounter stack to be empty we store the item or if not and current item is greater than top of stack then the past item is no longer going to be biggest in this or upcoming windows now that we have found a greater item, and so we pop the stack till either it's emptied or we encounter a bigger number than currently iterated one, sitting in the stack. Conversely, if currently-iterated number is smaller than stack top then given the possibility that this item still could be bigger than next k-1 items, makes it important to be stored. and so we do store it on top of stack. As we are traversing, it is also important to make sure the current window items are only stored in stack and for ensuring which we identify an insight that the way we've stored items in our stack if we have to delete past window's items then as items are stored as their indices and last one being at the bottom of stack, we keep popping from stack bottom, an item after the other up-till stack's bottom isn't an index bigger than i-k where i being current iteration number of for-loop. After all this for every window we can now find the greatest number at bottom of stack and so we keep appending that once in every for-loop iteration, into ansArr that we return. For first k number as stack is still being formed we avoid storing stack bottom in ansArr using a variable to keep track of first k iterations of for-loop.
from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        stack, ansArr = [], []
        counter = 0
        for i in range(len(nums)):
            while stack and nums[stack[-1]] <= nums[i]: #Here while stack means while stack is not empty which could also be achieved as while len(stack)!=0
                stack.pop()

            while stack and stack[0]<=i-k:
                stack.pop(0)

            stack.append(i)
            counter += 1

            if counter >= k:
                ansArr.append(nums[stack[0]])
        return ansArr


S = Solution()
print(S.maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3))
# TC: O(n) Explanation: for will take n and in which stack operations seperately yet collectively-ever will take n more time.
# SC: O(k) Explanation: stack taking k size
