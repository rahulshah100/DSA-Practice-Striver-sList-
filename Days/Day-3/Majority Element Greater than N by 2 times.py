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
# Time Complexity: O(n^2). Explaination: This wouldnt exactly be 0(n^2) as we have the repeating number for more than n//2 i.e. almost half the array would alway be occupied by that element. So in worst case the first for loop should be able to discover that item on the (((n+1)//2)+1)th iteration. Eg: [7,1,12,23,2,6,6,6,6]. Hence even in worst case we'll have the first for loop run for n-(((n+1)//2)+1) iterations. For each of that iteration we'll be checking one one less number each time, with max being n items, so due to this pattern the total complexity will follow the pattern x(x+1)/2. Thus total complexity is (n-(((n+1)//2)+1))*(n+1)/2. Ofcourse generalized as n^2.
# Space Complexity: O(1)

# Approach2: Sort out the array using merge sort which will take nlogn time. In the sorted array we are given there are more than floor(n/2) occurences of the number we have to find. Here the n could be even or odd. If even 8/2=>4; so here, we will've atleast 5 occurences of target number in an array of size 8. If odd floor(9/2)=>4; here, we will've atleast 5 occurences in an array of size 9. Now as there are these many occurences, if we look in the sorted array, we should have the target number at the (n//2)th index.
from typing import List

"""class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        return nums[(len(nums)//2)]

S=Solution()
print(S.majorityElement([2,2,1,1,1,2,2]))
print(S.majorityElement([3,3,4]))"""
# Time complexity: O(nlogn). Explanation: for the sorting.
# Space complexity: 0(1).

# Approach3: We'll use hashmap to store count of all items from given array, as we traverse through that array. As we encounter the count being more than n//2, we'll return it.
"""class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        MinOccurences=len(nums)//2
        hashmap=[0]*(max(nums)+1) #Constraints has it that num[i] could be between -10^9 to +10^9. So, we can not here, have len(nums) but max. If max element in array is 7, and arr length is 2, to store 7's value at that index number we'll require to have an index 7 in hashmap. Now, as even for len(7), as array starts from 0,we'll have last index as 6, so here we did n+1. Using dictionary hashmap at times like this would be much better.
        for i in range(len(nums)):
            if hashmap[nums[i]]<=MinOccurences:
                hashmap[nums[i]]+=1
            if hashmap[nums[i]]>MinOccurences:
                return nums[i]
        return "Not Found"

S=Solution()
# print(S.majorityElement([2,2,1,1,1,2,2]))
print(S.majorityElement([3,2,2]))"""
# Time complexity: O(n). Explaination: To traverse through the array, in worst case we'll find count>n//2 only at the last index of given array, hence in worst case O(n) time is required, given the array is represented as n.
# Space complexity: O(max(n)).

# Approach4: Better Space Complexity. We'll use a dictionary hashmap to store count of all items from given array, as we traverse through that array. As we encounter the count being more than n//2, we'll return it.
"""
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashmap = {} #By using dictionary, instead of indexes, we're storing the item's value as key, and hence we'll not need to have those many indexes beforehand declared in our data structure.
        for i in range(len(nums)):
            if nums[i] in hashmap: #Note: In List although the 'in', 'not in' operator takes O(n) time complexity, in case of dictionary and set if the keys are simple like numbers and not a string then the time complexity of in, not in is O(1)
                hashmap[nums[i]] += 1
                if hashmap[nums[i]] > len(nums) // 2:
                    return nums[i]
            else:
                hashmap[nums[i]] = 1
        return nums[0] #In case where array is just having 1 elem like [18] then as it'll just go one iteration of for loop where in yet we just declared hashmap[nums[i]] = 1 and it didnt go into nums[i] in hashmap, we've to write this return

S = Solution()
# print(S.majorityElement([2, 2, 1, 1, 1, 2, 2]))
print(S.majorityElement([1]))"""
# Time Complexity: O(n).Explaination: To travers n elements. Suppose the n//2+1th instance only occurs at the last item of the array, so worst gives us an n iterations.
# Space Complexity: O(n). Explaination: max n-(n//2) different items will be there, which would be size of this array. We generalize that to O(n).

# Approach5: Better Space Complexity. As we know that regardless of the length of the array being odd or even, we'll always've the repeating number have for more than half times in the array. So we can do the cancellation of dislike numbers and the last left number would be majority repeating number. We can start with first item and traverse the array further on. While travsersing, as the same item is witnessed, we increase the counter by one, and if a different item is witnessed then we'll decrease the counter by one. If counter is detected to have become zero, we'll change the item and will again start keeping count. At the end, we should have found an item with count!=0, we'll return that. This is called Moore Voting Algorithm.
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter = 0
        item = None
        for i in range(len(nums)):
            if counter == 0:
                item = nums[i]
            if item == nums[i]:
                counter += 1
            else:
                counter -= 1
        return item


S = Solution()
print(S.majorityElement([2, 2, 1, 1, 1, 2, 2]))
# Time Complexity: O(n). Explanation: Only one iteration through the given array would be required.
# Space Complexity: O(1). Explanation: We only use 2 extra variables which are counter and item. Both uses constant space.
