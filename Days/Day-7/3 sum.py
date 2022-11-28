# https://leetcode.com/problems/3sum/

# 3Sum
# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
# Notice that the solution set must not contain duplicate triplets.

# Example 1:
# Input: nums = [-1, 0, 1, 2, -1, -4]
# Output: [[-1, -1, 2], [-1, 0, 1]]
# Explanation:
# nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
# nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
# nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
# The distinct triplets are[-1, 0, 1] and [-1, -1, 2]. Notice that the order of the output and the order of the triplets does not matter.

# Example 2:
# Input: nums = [0, 1, 1]
# Output: []
# Explanation: The only possible triplet does not sum up to 0.

# Example 3:
# Input: nums = [0, 0, 0]
# Output: [[0, 0, 0]]
# Explanation: The only possible triplet sums up to 0.

# Constraints:
# 3 <= nums.length <= 3000
# -105 <= nums[i] <= 105
# -----------------------------------------------------------------------------------------------------------------------------------------------------------------
# Approach1: Using 3 for loops, check all combinations of three elements and add all the trios where sum==0 in a set, to avoid duplicate entries. Output the set.
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        trios = set()
        nums.sort() #--1 Why needed? explained inside the if-statement below.
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                for k in range(j+1, len(nums)):
                    if nums[i]+nums[j]+nums[k]==0:
                        # resultantSet.add([nums[i],nums[j],nums[k]]) #This can not be done i.e. adding list into a set, as lists are mutable and sets are not. So it is not allowed to add a mutable in immutable datastructure.
                        trios.add(tuple([nums[i], nums[j], nums[k]])) #This can be done. Without #--1, in output we saw [-1,2,-1] is considered different from [2,-1,-1] as set was not eliminating them, and hence point of using set was lost as we didn't want trios with repeating combination of numbers, regardless of their order. So by #--1 we are ensuring the duplicates in terms of same numbers in a trio is avoided. If this was input: [-1,0,1,2,-1,-4], without sorting we were getting O/P: [[0,1,-1],[-1,0,1],[-1,2,-1]]. With sorting we had input as: [-4, -1, -1, 0, 1, 2] and output as [[-1,0,1],[-1,-1,2]].
        print(nums)
        return trios
# TC: O(n^3) Explanation: Despite sorting, the time is dominated by n^3, so nlogn + n^3 is shown as n^3 here.
# SC: O(n) Explanation: as only unique trio are allowed, at max in even [0,0,0] we'll answer with only one trio, and hence space should stay linear.


# Approach2: Reducing a for loop by hash map. We'll go through given array once to store items and their counts in a hash dict. Using 2 for loops to fixate 2 items of a trio and going through all the rest of the items to see if a fitting 3rd item in accordance to first two items i.e. -(item1+item2) could be found, where item1 and item2 are item pointed by 2 for loops. If such item exist, we can have trio possible and will add it in our set. We'll return set after completing all the traversals.
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        Hashmap = {}
        s = set()
        # Filling hashmap from nums, with items as keys and the number of their occurences as value
        for i in nums:
            Hashmap[i] = Hashmap.get(i, 0) + 1

        for i in range(len(nums)):
            Hashmap[nums[i]] -= 1  # Decrease the count of ith elem in Hashmap, as it is once already picked out of hashmap by selecting it as i, and hence making a trio item.
            for j in range(i + 1, len(nums) - 1):
                Hashmap[nums[j]] -= 1  # Like i we'll also have to reduce j
                c = -(nums[i] + nums[j])  # Number we have to find
                if c in Hashmap and Hashmap[c] >= 1:  # If the 3rd elem is present in hashmap and atleast if it's count is once
                    k = [nums[i], nums[j], c]
                    k.sort()  # sorting this so -1,0,1 and 1,-1,0 would both become -1,1,0 and would now not be repeated in set
                    s.add(tuple(k))
                Hashmap[nums[j]] += 1  # From next iteration, we'll want original counts of items to be there in hashmap, so we'll here increase the count which was beforehand decreased by one.
            Hashmap[nums[i]] += 1
        return s
# TC: O(n^2) Explanation: n time to populate the hashmap + (n^2)(3log3) time to traverse through entire given list with sorting 3 items each time.
# SC: O(n) Explanation: set taking n space and dict taking 2n space for keys and values of n items. Total: 3n


# Approach3: To avoid the use of extra space from Approach2, instead of a hashmap we will use a two pointer method, in a for loop, on a sorted array. The for-loop will work to show us a total (in negative) that we'll try to achieve from the sum of two pointers: low and high (in positive). The low+high should balance out item pointed by for-loop such that sum of all three (item pointed by for-loop and the two pointers) should be Zero. Low pointer selects the item which is just after the item selected by for-loop, while the high pointer will always start from last item in array. As array is sorted from left to right in ascending order, if we find an item pointed by for-loop to be greater than low+high, we'll move low to the right side keeping high as it is. If we find low+high>itemPointedByFor-loop then we'll move high to left keeping low as it is. In such was when we find low+high=-itemPointedByFor-loop we have a triplet. To ensure, items dont get repeated from this point, in for and low, high we'll seek their value directly to the point where the item isnt matching it's previous item's value, and as array is sorted, all same items are put together and if an item is encountered not matching it's previous one then we can safely say we dont need to check further as items repeated before wont be coming further on.
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()  # We sort the given array, so then in an array like [-2,-2,0,1,2,2,2,3,3] to skip the same elements, we would just look to the consecutive rights and skip items till they stops matching.
        result = []

        for i in range(len(nums) - 2):  # we loop only till 3rd last item, as last 2 items are left for low and high pointers, which can all together make the triplet.
            if i == 0 or (i > 0 and nums[i] != nums[i - 1]):  # we are skipping similar items by comparing the current item with item before i.e. to the left. So for 1st item i.e. 0th index we will not have an item to the left, and hence this condition is like this.
                low = i + 1
                high = len(nums) - 1

                while low < high:
                    if nums[low] + nums[high] == -nums[i]:
                        result.append([nums[i], nums[low], nums[high]])

                        while low < high and nums[low] == nums[low + 1]:  # low has become part of a triplet in result array, so now the same low cant be chosen again, so we skip all lows with this same value.
                            low += 1
                        while low < high and nums[high] == nums[high - 1]:
                            high -= 1
                        # final and diff pos from the last values
                        low += 1
                        high -= 1
                    elif (nums[low] + nums[high] < -nums[i]):
                        low += 1
                    else:
                        high -= 1
        return result
# TC: O(n^2) Explanation: Sorting takes nlogn + for loop takes n time, inside which both the pointers keep moving (both put together) for at most n times. So total of nlogn+n^2 time is taken
# SC: O(1) Explanation: Although we are storing answers in result Array but that's for returning the answer directly, so that could not be counted as extra space, apart from which nothing occupies anymore space, making the total SC as O(1).