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
# Approach1: Brute Force: Not in-place as we're using external space for S and newS. Add the items of a given array into a Set to remove Duplicates. Turn Set back into a different array. Sort this array and then traverse it, while doing that copy the items from the new array into the given array so it seems given array has directly been modified.
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        S=set()
        for i in range(len(nums)): #n time
            S.add(nums[i])
        newS=list(S) #Conversion from set to list takes n time in python.
        newS.sort()  #takes nlogn time
        for i in range(len(newS)):#n time
            nums[i]=newS[i]     #See this is still in bounds of in-place as directly at index changes are happening
        return len(newS)        #but if we made nums=[] before this for-loop and then we did nums.append[], that violates the in-place and the answer did not match
# TC: O(3n+nlogn) Explanation: as comment in the code explains
# SC: O(n) Explanation: for storing n items in hashSet


# Approach2: Using 2 pointers. We'll use i to band-together all the unique elems before it, and j to keep comparing elems further in the list. Starting from index 1 if item at j is same as the one at j-1th index, we'll simply keep incrementing j uptill that's not true. When jth item differs than j-1's, we'll store the jth item at ith index too and increment both i and j. In this way all elems before index i are unique ones.
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        for k in range(1, len(nums)):
            if nums[k] != nums[k - 1]:
                nums[i + 1] = nums[k]
                i += 1
        return i + 1
# TC: O(n)
# SC: O(1)