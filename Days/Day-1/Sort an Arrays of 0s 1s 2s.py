# Sort Colors
# https://leetcode.com/problems/sort-colors/

# Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue. We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively. You must solve this problem without using the library's sort function.

# Input: nums = [2,0,2,1,1,0] Output: [0,0,1,1,2,2]
# Input: nums = [2,0,1] Output: [0,1,2]
# Input: nums = [0] Output: [0]
# Input: nums = [1] Output: [1]

# Constraints:
# n == nums.length
# 1 <= n <= 300
# nums[i] is either 0, 1, or 2.
#-----------------------------------------------------------------------------------------------------------
# Approach 1: My Original Approach
from typing import List

"""class Solution:
    def sortColors(self, nums: List[int]) -> None:
        # Do not return anything, modify nums in-place instead.
        
        hashmap=[0,0,0]
        for i in nums:
            if i==0:
                hashmap[0]=hashmap[0]+1
            elif i==1:
                hashmap[1]=hashmap[1]+1
            else:
                hashmap[2]=hashmap[2]+1

        count1=0
        count2=0
        for j in hashmap:
            for i in range(j):
                nums[count2]=count1
                count2+=1
            count1+=1

        print(nums)

S=Solution()
S.sortColors([2,0,2,1,1,0])
S.sortColors([2,0,1])
"""
# Time Complexity:O(2N) given nums array is shown as N. Explaination: the first for loop runs for N times. For the second for loop which is a nested one the outer one will run for 3 times, in effect making the inner one run in-total for N times as the hashmap is storing total N counts i.e.hashmap[0]+hashmap[1]+hashmap[2]=N; So we can it will make the inner for loop run in total for N times and that is what it is doing, so N more time complexity gets added due to this for loop. Therefore, total=N+N=2N Time Complexity.
# Space Complexity: O(1). We are using hashmap and count1, count2 as variables occupying any extra space in the program. Those 3 having constant space requirement we get O(1) here.


# Approach 2: Better Time Complexity
# If unlike Approach1 where we had to make 2 passes i.e. two for loops: one for storing counts in hashmap and another for storing those many values in nums, if we could make it in one pass then the time complexity would be divided in half. We'll do it by using two pointers low and high. To the left of low, values of 0 would be there. Between low and high (including positions of low and high) we'll have 1s and on the right-side of high we'll have 2s. We'll use an interim pointer mid to check all the items, and accordingly increase values of low and high.
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        # Initiating indexes as the position of array items.
        mid = 0
        low = 0
        high = len(nums)-1
        while mid <= high:
            if nums[mid] == 0:
                temp = nums[mid]
                nums[mid] = nums[low]
                nums[low] = temp
                mid += 1
                low += 1
            elif nums[mid] == 1:
                mid += 1
            elif nums[mid] == 2:
                temp = nums[mid]
                nums[mid] = nums[high]
                nums[high] = temp
                high -= 1
        print(nums)


S = Solution()
S.sortColors([2, 0, 2, 1, 1, 0])
S.sortColors([2, 0, 1])
# Time Complexity: O(N).
# Space Complexity: O(1)