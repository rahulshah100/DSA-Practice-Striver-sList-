# https://leetcode.com/problems/top-k-frequent-elements/description/

# Given an integer array nums and an integer k, return the k most frequent elements.You may return the answer in any order.

# Example1:
# Input: nums = [1, 1, 1, 2, 2, 3], k = 2
# Output: [1, 2]

# Example2:
# Input: nums = [1], k = 1
# Output: [1]

# Constraints:
# 1 <= nums.length <= 105
# -104 <= nums[i] <= 104
# k is in the range[1, the number of unique elements in the array]
# It is guaranteed that the answer is unique.

# Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
# -----------------------------------------------------------------------------------------------------------------------------------
# Approach1: Store items in a Dictionary with item as key and it's count as value. Further traverse the dictionary and push the pair of count i.e. value and item i.e.key from dictionary into a maxHeap. Pop k times from maxHeap and store these items into an ansArr which is returned.
import heapq
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashDict = {}
        for i in range(len(nums)):
            if nums[i] not in hashDict:
                hashDict[nums[i]] = 1
            else:
                hashDict[nums[i]] += 1

        maxHeap = []
        for key in hashDict:
            heapq.heappush(maxHeap, (-hashDict[key], key))

        ansArr = []
        for i in range(k):
            value, key = heapq.heappop(maxHeap)
            ansArr.append(key)
        return ansArr
# TC: O(n + 2nlogn) Explanation: n for making hashDict, nlogn for pushing n items into heap, klogn for popping k items which in worst case could be n and hence this one becomes nlogn
# SC: O(2n) Explanation: Dictionary using n extra space and so does heap. As ansArr is required space to return answer it is not been accounted for


# Approach 2: In approach1 what bugs is nlogn time which if somehow managed in n our TC would be generalized as O(n). For this we think of substituting heap with a hashArr where to constraint the size of array we will use index as count - as in how many times that number is repeated and as there could be multiple numbers repeating say 2 times or 3 times we'll use a hashArr as an array of arrays. So from hashDict items are thus transferred into hashArr and then we traverse it in descending order, transferring first k items into a resArr which is returned.
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashDict = {}
        for i in range(len(nums)):
            if nums[i] not in hashDict:
                hashDict[nums[i]] = 1
            else:
                hashDict[nums[i]] += 1

        ctArr = [[] for i in range(len(nums) + 1)]
        for key in hashDict:
            ctArr[hashDict[key]].append(key)

        resArr = []
        for i in range(len(ctArr) - 1, 0, -1):
            for j in range(len(ctArr[i])):
                resArr.append(ctArr[i][j])
                if len(resArr) == k:
                    break
        return resArr

S = Solution()
print(S.topKFrequent([1, 1, 1, 2, 2, 3], 2))
# TC: O(3n) Explanation: n time each for creating hashDict, and ctArr. Further using 2 for-loops we are essentially only traversing ctArr which has n items for k times, which in worse case can be equal to n and hence resArr takes n time too for being built up. Thus in total we've 3n TC
# SC: O(2n) Explanation: hashDict and ctArr taking n space each, while resArr is the expected space to return the answer and is excluded