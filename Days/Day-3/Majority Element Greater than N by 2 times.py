# https://leetcode.com/problems/majority-element/

# Given an array nums of size n, return the majority element.

# The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

# Example1:
# Input: nums = [3, 2, 3]
# Output: 3

# Example2:
# Input: nums = [2, 2, 1, 1, 1, 2, 2]
# Output: 2

# Constraints:
# n == nums.length
# 1 <= n <= 5 * 10^4
# -10^9 <= nums[i] <= 10^9
# -------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Approach1: Use two for loops, first for loop for selecting one item and the other for traversing all the remaining items after that. While traversing in 2nd for loop, if number of times the item occurs is more than n//2, return it.
# Time Complexity: O(n^2). Explanation: This wouldn't exactly be 0(n^2) as we have the repeating number for more than n//2 i.e. almost half the array would always be occupied by that element. So in worst case the first for loop should be able to discover that item on the (((n+1)//2)+1)th iteration. Eg: [7,1,12,23,2,6,6,6,6]. Hence even in worst case we'll have the first for loop run for n-(((n+1)//2)+1) iterations. For each of that iteration we'll be checking one one less number each time, with max being n items, so due to this pattern the total complexity will follow the pattern x(x+1)/2. Thus total complexity is (n-(((n+1)//2)+1))*(n+1)/2. Ofcourse generalized as n^2.
# Space Complexity: O(1)


# Approach2: sort and then in one iteration starting from 2nd item, as far as we have same item as the prev one we keep incrementing ct variable. As ct crosses len(arr)//2 we return. Conversely if before crossing the required threshold if the current item doesnt match with prev one, we reset the ct to 1
"""class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        ct = 1

        if len(nums) == 1: return nums[0] #Edge Case

        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                ct += 1
                if ct > len(nums) // 2:
                    return nums[i]
            else:
                ct = 1"""
# TC: O(nlogn+n). For sorting and then iterating over the array
# SC: O(1)


# Approach3: Sort out the array using merge sort which will take nlogn time. In the sorted array we are given there are more than floor(n/2) occurrences of the number we have to find. Here the n could be even or odd. If even 8/2=>4; so here, we will've at-least 5 occurrences of target number in an array of size 8. If odd floor(9/2)=>4; here, we will've at-least 5 occurrences in an array of size 9. Now as there are these many occurrences, if we look in the sorted array, we should have the target number at the (n//2)th index.
"""
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        return nums[(len(nums)//2)]
"""
# Time complexity: O(nlogn). Explanation: for the sorting.
# Space complexity: 0(1).


# Approach4: We'll use hashmap to store count of all items from given array, as we traverse through that array. As we encounter the count being more than n//2, we'll return it.
"""class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashmap=[0]*(max(nums)+1) #Constraints has it that nums[i] could be between -10^9 to +10^9. So, we can not here, have len(nums) but max. If max element in array is 7, and arr length is 2, to store 7's value at that index number we'll require to have an index 7 in hashmap. Now, as even for len(7), as array starts from 0, we'll have last index as 6, so here we did n+1. Using dictionary hashmap at times like this would be much better.
        for i in range(len(nums)):            
            hashmap[nums[i]] += 1
            if hashmap[nums[i]] > len(nums)//2:
                return nums[i]
        return "Not Found"
"""
# Time complexity: O(n). Explanation: To traverse through the array, in worst case we'll find count>n//2 only at the last index of given array, hence in worst case O(n) time is required, given the array is represented as n.
# Space complexity: O(max(n)).


# Approach5: Better Space Complexity. We'll use a dictionary hashmap to store count of all items from given array. On encountering the count to be more than n//2, we'll return the current item.
"""
class Solution:
    def majorityElement(self, nums: List[int]) -> int:        
        hashDict = {} #By using dictionary, instead of indexes, we're storing the item's value as key, and hence we'll not need to have those many indexes beforehand declared in our data structure.
        for i in range(len(nums)):
            if nums[i] not in hashDict: #Note: In List although the 'in', 'not in' operator takes O(n) time complexity. But in case of dictionary and set if the keys are simple like numbers and not a string then the TC of in, not in is O(1)
                hashDict[nums[i]] = 1
            else:
                hashDict[nums[i]] += 1
            if hashDict[nums[i]] > len(nums) // 2:
                return nums[i]
                
S = Solution()
# print(S.majorityElement([2, 2, 1, 1, 1, 2, 2]))
print(S.majorityElement([1]))"""
# Time Complexity: O(n).
# Space Complexity: O(n). Explanation: max n-(n//2) different items will be there, which would be size of the dictionary. We generalize that to O(n).


# Approach6: Better Space Complexity. As we know that regardless of the length of the array being odd or even, we'll always've the repeating number for more than half times in the array. So we can do the cancellation of dislike numbers and the last left number would be majority repeating number. We can start with first item and traverse the array further on. While traversing, as the same item is witnessed, we increase the counter by one, and if a different item is witnessed then we'll decrease the counter by one. If counter is detected to have become zero, we'll change the item and will again start keeping count. At the end, we should have found an item with count!=0, we'll return that. This is called Moore Voting Algorithm.
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        ct1, pt1 = 1, nums[0]
        for i in range(1, len(nums)):
            if nums[i] == pt1:
                ct1 += 1
            else:
                ct1 -= 1
            if ct1 == 0:
                pt1 = nums[i]
                ct1 = 1
        return pt1

S = Solution()
print(S.majorityElement([2, 2, 1, 1, 1, 2, 2]))
# Time Complexity: O(n). Explanation: Only one iteration through the given array would be required.
# Space Complexity: O(1). Explanation: We only use 2 extra variables which are counter and item. Both uses constant space.
