# https://leetcode.com/problems/majority-element-ii/

# Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.

# Example 1:
# Input: nums = [3,2,3]
# Output: [3]

# Example 2:
# Input: nums = [1]
# Output: [1]

# Example 3:
# Input: nums = [1,2]
# Output: [1,2]

# Constraints:
# 1 <= nums.length <= 5 * 104
# -10^9 <= nums[i] <= 10^9
# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Approach1: Brute Force Approach. Two for loops, one on each item and other to check its occurrence in further part of array. If occurrences are found for more than n//3 times, then store the item in a set. Return the set after complete array traversal. Unlike in "Majority Element Greater than N by 2.py", here we could have multiple Majority Elements as (n//2)+1 + (n//2)+1 would exceed the length: n, so array cant have 2 occurrence of that. But here n//3+1 + n//3+1 i.e greater than 1/3rd, greater than 1/3rd could come for twice, maximum. And we'll use set, as for all elems as we traverse, the first for loop we may fixate on an another occurrence of majority element in the array and for that occurrence too, doing further comparisons in 2nd array, we may find more than n//3 repetitions. So if we store the majority elem in set, they'll not be repeated.
from typing import List

"""
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        MajElems= set()
        for i in range(len(nums)):
            count=0
            for j in range(i, len(nums)):
                if nums[i]==nums[j]:
                    count+=1
                if count>(len(nums)//3):
                    MajElems.add(nums[i])
                    break
        return MajElems

S=Solution()
print(S.majorityElement([3,2,3]))"""
# Time Complexity: O(n^2). Explanation: To traverse two for loops with second for loop executing one less time, for each iteration of first for looop, we'll require the total n(n+1)/2 iterations.
# Space Complexity: O(n). Explanation: In worst case: The set will store n items. Eg: in [1,2] we'll return both 1 and 2 as our answer, by storing both in set.


# Approach2: Better Approach. Using hashmap, to store all the numbers in dictionary. If their count>n//3, we'll store them in a set, to return it.
"""class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        hashmap = {}
        MajElems = set()
        for i in range(len(nums)):
            if nums[i] not in hashmap:
                hashmap[nums[i]] = 1
            else:
                hashmap[nums[i]] += 1
            if hashmap[nums[i]] > (len(nums) // 3):
                MajElems.add(nums[i])
        return MajElems


S = Solution()
print(S.majorityElement([3, 2, 3]))"""
# Time Complexity: O(n).
# Space Complexity: O(n). Explanation: To store n elems in hashmap we'll require n space, and to store n elems in set, n more space. Total: 2n space required. We generalize that to n.


# Approach3: Optimal Approach: Boyer Moore Voting Algorithm. Here we'll use two counters and two candidate items as at max for greater than n//3, as we can have 2 such MajorityElements. In beginning these all variables will be None or 0. As we encounter the first elem, we'll set candidateItem1 as that elem and counter1 as 1. As we traverse further in the array if we encounter the same elem, we increase it's counter by 1. If we encounter a different elem, we'll store that in the candidateItem2, and increase counter2 by 1. If further we encounter candidateItem1 or candidateItem2 in the array,we'll increase counter1 or counter2 respectively. If a different number than candidateItem1 or candidateItem2 is encountered, we'll decrease the counter value of both counter1 and counter2. If either counter becomes 0, then in the next iteration, that candidateItem would be set whose counter==0. If both became 0, we'll only set counterItem1's value. Further, after entire array is such traversed we'll check the candidateItem1 and candidateItem2's count using a for loop, as unlike in "Majority Element Greater than N by 2 times.py" here we are not given that "You can consider there will always be atleast 1 Majority element" and hence chances are the candidateItems we have might not be majority elements. Eg:[1,2,3,4] where majority element should come for more than 4/3 => at-least 2 times. But if we run our algo there, we'll get 3 and 4 as candidate3 and candidate4, which are not the Majority Elements.
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        pt1 = pt2 = None
        ct1 = ct2 = 0
        for i in range(len(nums)):
            if ct1 == 0 and nums[i] != pt2:
                pt1 = nums[i]
                ct1 = 1
            elif ct2 == 0 and nums[i] != pt1:
                pt2 = nums[i]
                ct2 = 1
            elif pt1 == nums[i]:
                ct1 += 1
            elif pt2 == nums[i]:
                ct2 += 1
            else:
                ct1 -= 1
                ct2 -= 1

        ct1 = ct2 = 0
        for i in range(len(nums)):
            if nums[i] == pt1:
                ct1 += 1
            elif nums[i] == pt2:
                ct2 += 1

        ansArr = [] #Here set is not required as for all same items it'll be either ct1, or ct2 only one which'll every time increment removing possibility of other pointer i.e. pt2, or pt1 to hold same item
        if ct1 > len(nums) // 3:
            ansArr.append(pt1)
        if ct2 > len(nums) // 3:
            ansArr.append(pt2)

        return ansArr


S = Solution()
print(S.majorityElement([2, 9, 1, 9, 4, 3, 8, 9]))
# Time Complexity: O(2n). Explanation: O(n) for traversal to get ct1 and ct2, and further O(n) to check ct3 and ct4. In total:2n; We can generalize it as O(n).
# Space Complexity: O(1). Using only a couple of extra variables. All of which uses only constant space.
