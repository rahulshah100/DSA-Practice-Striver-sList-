# https://leetcode.com/problems/remove-duplicates-from-sorted-array/

# Remove Duplicate from Sorted array
# Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same.Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array nums. More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result. It does not matter what you leave beyond the first k elements. Return k after placing the final result in the first k slots of nums. Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.

# Custom Judge:
# The judge will test your solution with the following code:
# int[] nums = [...]; // Input array
# int[] expectedNums = [...]; // The expected answer with correct length
# int k = removeDuplicates(nums); // Calls your implementation
# assert k == expectedNums.length;
# for (int i = 0; i < k; i++) {
#     assert nums[i] == expectedNums[i];
# }
# If all assertions pass, then your solution will be accepted.

# Example 1:
# Input: nums = [1,1,2]
# Output: 2, nums = [1,2,_]
# Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively. It does not matter what you leave beyond the returned k (hence they are underscores).

# Example 2:
# Input: nums = [0,0,1,1,1,2,2,3,3,4]
# Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
# Explanation: Your function should return k = 5, with the first five elements of nums being 0, 1, 2, 3, and 4 respectively. It does not matter what you leave beyond the returned k (hence they are underscores).

# Constraints:
# 1 <= nums.length <= 3 * 104
# -100 <= nums[i] <= 100
# nums is sorted in non-decreasing order.
# ----------------------------------------------------------------------------------------------------------
# Approach1: Brute Force. Use a hashSet to store all items from given list in questio; this will give us all unique items. Further for our output we need the list passed in function to have all unique items arranged in it, in the order they appear. As it's said that given array would always have items in ascending order, we'll convert set to list as we can only then push all the unique items from set in given list, coz otherwise in set items can not be accessed through the index. Also as within set the order of item isnt maintained, we'll sort list which is converted from set, before we use it to do insertion in list passed in the function.
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        S=set()
        for i in range(len(nums)): #n time
            S.add(nums[i])
        newS=list(S) #Conversion from set to list takes n time in python.
        newS.sort()  #takes nlogn time
        for i in range(len(newS)):#n time
            nums[i]=newS[i]
        return len(newS)
# TC: O(3n+nlogn) Explanation: as comment in the code explains
# SC: O(n) Explanation: for storing n items in hashSet

# Approach2: Using 2 pointers. Using i to track unique items and j to traverse all the items in given array. Starting from item at 1st index, we'll compare it with item right beofre it, which if found different then we'll store it at ith index and make i and j move forward. If repeated item is found, then i will stay unchanged and j will go to next item.
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i,j=1,1
        while j<len(nums): #See how when only one items list is given, we'll not get in here and so Overflow error at #--1 is avoided
            if nums[j]!=nums[j-1]: #--1
                nums[i]=nums[j]
                i+=1
            j+=1
        print(nums,i)
        return i
# TC: O(n)
# SC: O(1)