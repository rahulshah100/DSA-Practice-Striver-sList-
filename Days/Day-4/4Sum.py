# https://leetcode.com/problems/4sum/

# Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:
# 0 <= a, b, c, d < n
# a, b, c, and d are distinct.
# nums[a] + nums[b] + nums[c] + nums[d] == target
# You may return the answer in any order.

# Example 1:
# Input: nums = [1, 0, -1, 0, -2, 2], target = 0
# Output: [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]

# Example 2:
# Input: nums = [2, 2, 2, 2, 2], target = 8
# Output: [[2, 2, 2, 2]]

# Constraints:
# 1 <= nums.length <= 200
# -10^9 <= nums[i] <= 10^9
# -10^9 <= target <= 10^9
# -------------------------------------------------------------------------------------------------------------------------
# Approach1: Using 4 for loops to check all the combinations, and see if the target is achieved from the addition from values of respective for loops. If so, we'll insert all such combinations into a Set. We use set here as only unique combinations should be printed and also, the order of the items dont matter. Further, as we have to return an array, we'll make a list of lists from set.
from typing import List

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        quadraplets=set() #Set is like: {}, just as dict is. But to define an empty Set syntax is Set = set(). Defining dictionary would be like dict = {}.
        if len(nums)<4:
            return nums
        for i in range(0,len(nums)-3):
            for j in range(i+1,len(nums)-2):
                for k in range(j+1, len(nums)-1):
                    for l in range(k+1, len(nums)):
                        if nums[i]+nums[j]+nums[k]+nums[l]==target:
                            quadraplets.add(tuple([nums[i], nums[j], nums[k], nums[l]]))
        nums = [list(items) for items in quadraplets]
        print(nums)
        return nums

# S=Solution()
# S.fourSum([1, 0, -1, 0, -2, 2],0)
# S.fourSum([2, 2, 2, 2, 2],8)
# Time Complexity: O(n^4)+O(n). Explaination: 4 for loops taking n^4 time to fill the set. Further in worst case, 1 for loop to convert set into array.
# Space Complexity: O(n). Explaination: Extra space for set, to store n elements.


# Approach2: Reducing 1 of 4 for Loops by using Binary Sort. We'll use 3 for loop pointers for pointing at total of 3 elements at a time. Deducting the sum of this 3 items from the given target is what the 4th value should be. For checking if that fourth value is present we will use a binary sort in the later portion from where the 3rd for loop pointer is pointing. If 4th value is found, we have a combination and we'll put that in our output list. Also for binary sort to work, we must have a sorted array. So we'll sort array at starting. Later, to return just unique elements we'll turn that list into a Set and turn it back in a list.
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
            nums.sort()
            combinations=[]
            for i in range(0,len(nums)-3):
                for j in range(i+1, len(nums)-2):
                    for k in range(j+1, len(nums)-1):
                        fourthItem = target - (nums[i] + nums[j] + nums[k])
                        if fourthItem in nums[k+1: len(nums)]: #Here we can use Binary Sort which has a logn time complexity #Also note: For slicing and such operations, as set doesnt have indexation, there are no such functions as slicing too. Or here instead of bringing a list in b/n we'd have directly put values in a set.
                           combinations.insert(0,[nums[i],nums[j],nums[k], fourthItem])
            combinations = {tuple(i) for i in combinations} #See how only one variable is used and no extra/other space is required
            combinations = [list(i) for i in combinations]
            print(combinations)
            return combinations

# S = Solution()
# S.fourSum([1, 0, -1, 0, -2, 2], 0)
# S.fourSum([2, 2, 2, 2, 2], 8)
# Time Complexity: O((n^3)logn + 2n + nlogn) Explaination: nlogn for sorting (from using merge sort). Plus n^3 from using three nested for loops. In third for loop we're using binary sort everytime which makes three loops' total time complexity as (n^3)logn. Later n+n i.e. 2n time to convert set from list and then to convert it back into list.
# Space Complexity: O(n)


# Approach3: Reducing 2 of 4 for loops by using 2 extra pointers. Sort the array. In sorted array, we use 2 for loops and in the range later than what is pointed by second loop, we'll use one pointer at starting and one at ending. We'll look for target element and see if the sum of elems pointed by two for loops and elems pointed by two pointers is equal to the target. If sum is equal to target, we'll add corresponding values in output list. If not and if we figure the target is higher than sum, then as array is sorted, we'll shift startPointer to right by one decrease our total and we'll check again if target is now equal to the new sum. On the other hand if we find target being smaller than sum, we'll shift ending pointer to left by one. We'll keep on shifting pointer's till start<end. Also, to avoid duplicate elements we'll skip all the same elements while shifting start(pointer)/end(pointer)/i(loop)/j(loop) during their every iteration.
from typing import List

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        quadraplets=[]
        i = 0
        while i < len(nums)-3:
            j=i+1
            while j < len(nums) - 2:
                start = j+1
                end = len(nums)-1
                while start<end:
                    sum=nums[start]+nums[end]+nums[i]+nums[j]
                    if target==sum:
                        quadraplets.insert(0,[nums[i],nums[j],nums[start],nums[end]])
                        while start < end and nums[start] == quadraplets[0][2]: start += 1
                        while start < end and nums[end] == quadraplets[0][3]: end -= 1
                    elif target>sum:
                        start+=1
                    else:
                        end-=1
                while j + 1 < len(nums) - 1 and nums[j + 1] == nums[j]:j+=1
                j+=1
            while i + 1 < len(nums) - 2 and nums[i + 1] == nums[i]: i += 1
            i += 1
        print(quadraplets)
        return quadraplets

S = Solution()
S.fourSum([1, 0, -1, 0, -2, 2], 0)
S.fourSum([2, 2, 2, 2, 2], 8)
S.fourSum([-2,-1,-1,1,1,2,2], 0)
# Time Complexity: O(n^3) Explaination: Two nested for loops take n^2 time in total. Here, in second for loop, we have a while loop, which will traverse the rest-of the portion from what's pointed by 2nd for loop. This while loop should be checking ofcourse less than n elements in any given iterations, but for worst case and taking the bigger round figure we can say while takes n time. Therefor inside each iteration of n^2, we are taking n time more. Hence n^3 time in total.
# Space Complexity: O(n) Explaination: only quadraplets variable is taking space which should be n in worst case.