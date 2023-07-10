# Maximum Sub-array
# https://leetcode.com/problems/maximum-subarray/

# Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum. A subarray is a contiguous part of an array.

# Input: nums = [-2,1,-3,4,-1,2,1,-5,4] Output: 6 Explanation: [4,-1,2,1] has the largest sum = 6.
# Input: nums = [1] Output: 1
# Input: nums = [5,4,-1,7,8] Output: 23

# Constraints:
# 1 <= nums.length <= 10^5
# -10^4 <= nums[i] <= 10^4
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Approach 1: Brute Force- Finding maxSum by calculating all the possible contigous arrays. Use 2 for loop; the first for loop to locate every element one after other and the second for loop inside the first one, for adding the remainig elements of the array after the located element, one by one, to the located element.
from typing import List

"""class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum=nums[0]
        for i in range(len(nums)):
            prevSum=nums[i]
            for j in range(i+1, len(nums)):
                prevSum+=nums[j]
                if prevSum>maxSum:
                    maxSum=prevSum
            if nums[i]>maxSum: #in case where the very last array number is by solo means, the biggest sum then that endcase is captured here
                maxSum=nums[i]
        return maxSum


S = Solution()
S.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4])
# S.maxSubArray([1])
# S.maxSubArray([-2, 1])
# S.maxSubArray([-2, -1])
# S.maxSubArray([1, -3, 4, -1, 2, 1])
"""
# Time Complexity:O(n(n+1)/2). Explaination: Consider for nums = [1, -3, 4, -1, 2, 1]. Here for the last value of i which is 4, the inner for loop for j will run for only 1 time with its value being j=5. for i=3 i.e.nums[i]=-1, j will run twice with matrix[j] being 2 and then 1. Similarly for i=2 i.e. matrix[i]=4 the j will run for three times making matrix[j]=-1 then 2 and then 1. Hence because of this pattern being there, the total iterations we know will be n(n+1)/2 and that is the time complexity. Also, consider that for nums=[-2, 1] i will initially be 0 i.e. matrix[i]=-2 when j will run for only once, there being j=1 i.e.matrix[j]=1. In this case the total iterations are not 2(2+1)/2 but instead they are N i.e.2. However as we are concerned with the worst case, so we can safely consider n(n+1)/2 as time complexity. This time complexity could be generalised as O(n^2).
# Space Complexity: O(1). We are only using variables which are using constant space.


# Approach 2: Better Time Complexity. Instead of finding all the possibilities of contiguos arrays and comparing the sum for each possibility, if we keep on going one one step in the array from the starting of array in such a way that at each step we'll calculate and would be recording the maximumSum of contgous items till that step, and further figure for the new maximum as new items keeps on getting traversed through, then we'll just need one Traversal through array making O(n) Time Complexity.
# Intution: At any given item either it could be a starting point i.e. first item of a possibly contigous array having the Maxsum, or it could be a part of the previously continued contigous subarray. At every element we can decide if the element itself, or that element combined with the sum of its previously coninued contigous array, which value is greater. If the element alone is greater then we'll drop the previous contigous array and would focus on developing the new array from this point onwards including current element as first item of array. Now as we add newer elements in this new array, we'll need to keep checking the summation of this newly formed array and we'd need a variable to compare the maximum value amongst all the checked summation.
# Steps:
"""Def kadane(A):
        max_current = max_global=nums[0] #NOTE: As these are integer variable i.e. basic data-types we can declare them as such and not max_current, max_global = 0,0. This is because basic data types are never stored in referrenced manner, unlike derived datatypes such as arrays and dictionary that we'll see going forward how in derived datatype's case we need to make a cope.deepcopy() 
        for i in range(1,len(nums)):
            max_current = max(nums[i], max_current+nums[i])
            if max_current>max_global:
                max_global=max_current
        return max_global
        
Example: Given array=[-2,1,-3,4,-1,2,1,-5,4]. We can observe and say max contigous subarray is [4,-1,2,1]. The sum of these elements is 6.

#Solving example according to steps of kadane's algorithm 
maxCur=-2 maxG=-2
i=1, value=1  maxCur=1 maxG=1
i=2  v=-3     mC=-2    mG=1
i=3  v=4      mC=4     mG=4
i=4  v=-1     mC=3     mG=4 
i=5  v=2      mC=5     mG=5
i=6  v=1      mC=6     mG=6
i=7  v=-5     mC=1     mG=6
i=8  v=4      mC=5     mG=6       
"""
# Time Complexity: O(n). Explaination: One for loop going for n-1 times. So O(n-1), generalized as O(n) in the answer.
# Space Complexity: O(1).
