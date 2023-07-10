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
# Approach1: Brute Force Approach. Two for loops, one on each item and other to check its occurence in further part of array. If occurences are found for more than n//3 times, then store the item in a set. Return the set after complete array traversal. Unlike in "Majority Element Greater than N by 2.py", here we could have multiple Majority Elements as (n//2)+1 + (n//2)+1 would exceed the length: n, so array cant have 2 occurence of that. But here n//3+1 + n//3+1 i.e greater than 1/3rd, greater than 1/3rd could come for twice, maximum. And we'll use set, as for all elems as we traverse, the first for loop we may fixate on an another occurence of majority element in the array and for that occurence too, doing further comparisions in 2nd array, we may find more than n//3 repetitions. So if we store the majority elem in set, they'll not be repeated.
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
# Time Complexity: O(n^2). Explaination: To traverse two for loops with second for loop executing one less time, for each iteration of first for looop, we'll require the total n(n+1)/2 iterations.
# Space Complexity: O(n). Explaination: In worst case: The set will store n items. Eg: in [1,2] we'll return both 1 and 2 as our answer, by storing both in set.

# Approach2: Better Approach. Using hashmap, to store all the numbers in dictionary. If their count>n//3, we'll store them in an array, to return it.
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
# Space Complexity: O(n). Explaination: To store n elems in hashmap we'll require n space, and to store n elems in set, n more space. Total:2n space requried. We generalize that to n.

# Approach3: Optimal Approach: Boyer Moore Voting Algorithm. Here we'll use two counters and two candidate items as at max for greater than n//3, we can have 2 such MajorityElements. In begining these all variables will be None or 0. As we encounter the first elem, we'll set candidateItem1 as that elem and counter1 as 1. As we traverse further in the array if we encounter the same elem, we increase its counter by 1. If we encounter a different elem, we'll store that in the candidateItem2, and increase counter2 by 1. If further we encounter candidateItem1 or candidateItem2 in the array,we'll increase counter1 or counter2 respectively. If a different number than candidateItem1 or candidateItem2 is encountered, we'll decrease the counter value of both counter1 and counter2. If either counter becomes 0, then in the next iteration, that candidateItem would be set whose counter==0. If both became 0, we'll only set counterItem1's value. Further after entire array is such traversed we'll check the candidateItem1 and candidateItem2's count using a for loop, as unlike in "Majority Element Greater than N by 2 times.py" here we are not given that "You can consider there will always be atleast 1 Majority element" and hence chances are the condidateItems we have might not be majority elements Eg:[1,2,3,4] where majority element should come for more than 4/3=>atleast 2 times. If we run our algo there, we'll get 3 and 4 as candidate3 and candidate4, which are not the Majority Elements.
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        num1, ct1 = None, 0
        num2, ct2 = None, 0
        for i in range(len(nums)):
            if ct1 == 0 and nums[i] != num2:
                num1 = nums[i]
                ct1 = 1
            elif nums[i] == num1:
                ct1 += 1
            elif ct2 == 0:
                num2 = nums[i]
                ct2 = 1
            elif nums[i] == num2:
                ct2 += 1
            else:
                ct1 -= 1
                ct2 -= 1
        ct3 = ct4 = 0
        for i in range(len(nums)):
            if nums[i] == num1:
                ct3 += 1
            elif nums[i] == num2:
                ct4 += 1
        Arr = []
        if ct3 > (len(nums) // 3):
            Arr.append(num1)
        if ct4 > (len(nums) // 3):
            Arr.append(num2)
        return Arr


S = Solution()
# print(S.majorityElement([1,0,1,1,3,4,7,8]))
# print(S.majorityElement([2,1,1,3,1,4,5,6]))
print(S.majorityElement([2, 9, 1, 9, 4, 3, 8, 9]))
# Time Complexity: O(2n). Explaination: O(n) for traversal to get ct1 and ct2, and further O(n) to check ct3 and ct4. In total:2n; We can generalize it as O(n).
# Space Complexity: O(1). Using only couple of extra variables. All of which uses only constant space.
