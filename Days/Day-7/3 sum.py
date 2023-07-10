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
        trios = set() #to avoid duplicate triplets
        nums.sort() #Needed as set considers 1,2,2 and 2,1,2 as different triplets. If in array they are sorted we'll only have 1,2,2 and 1,2,2
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                for k in range(j+1, len(nums)):
                    if nums[i]+nums[j]+nums[k]==0:
                        trios.add(tuple([nums[i], nums[j], nums[k]])) #In set, we cant add lists and set doesnt allow changing it's elem's values. So we convert array to tuple and save in set.
        return trios
# TC: O(n^3) Explanation: Despite sorting, the time is dominated by n^3, so nlogn + n^3 is shown as n^3 here.
# SC: O(n) Explanation: as only unique trio are allowed, at max in even [0,0,0] we'll answer with only one trio, and hence space should stay linear.


# Approach2: Reducing a for loop by hashmap. Using 2 for loops we'll traverse the given array where we'll check at each iteration we'll store item pointed by secondForLoop in hashmap and will keep checking if an item:itemsX such that forloops1'sItem+forloop2'sItem+itemX will sum upto 0 is present in hashmap in which case we'll include trio in our set.
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = set()
        nums.sort()
        for i in range(len(nums)):
            hashmap={}
            for j in range(i + 1, len(nums)):
                if -(nums[i] + nums[j]) in hashmap:
                    triplets.add(tuple([nums[i], nums[j], -(nums[i] + nums[j])]))
                hashmap[nums[j]] = True
        return triplets

# TC: O(n^2 + nlogn) Explanation: for sorting and running a for loop with an inner for loop
# SC: O(n) Explanation: set taking n space and dict taking 2n space for keys and values of n items. Total: 3n


# Approach3: To avoid the use of extra space from Approach2, instead of a hashmap we will use a two pointer method, in a for loop, on a sorted array. The for-loop will work to show us a total (in negative) that we'll try to achieve from the sum of two pointers: low and high (in positive). Low pointer is set to item just after the one selected by for-loop, while the high pointer will always start from last. As array is sorted from left to right in ascending order, if we find an item pointed by for-loop to be greater than low+high, we'll move low to the right side keeping high as it is. If we find low+high>itemPointedByFor-loop then we'll move high to left keeping low as it is. When we find low+high=-itemPointedByFor-loop we have a triplet which will be stored in an array to be returned. To ensure, items dont get repeated from this point, in for and low, high we'll seek their value directly to the point where the item isnt matching it's previous item's value, and as array is sorted, all same items are put together and if an item is encountered not matching it's previous one then we can safely say we dont need to check further as items repeated before wont be coming further on.
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()  # We sort the given array, so to be able to skip the same values.
        result = []

        for i in range(len(nums)): #Interesting catch: For last iteration where for array size:3 i will be 2, at #--1  high and low will be 2 and 3 yet due to condition at #--2 we'll not get error
            if i == 0 or (i > 0 and nums[i] != nums[i - 1]):  # we are skipping similar items
                high = len(nums) - 1 #--1
                low = i + 1

                while low < high: #--2
                    if nums[low] + nums[high] == -nums[i]:
                        result.append([nums[i], nums[low], nums[high]])
                        while low < high and nums[low] == nums[low + 1]:  #Once low and high has become part of triplet, to avoid duplicates (as we're using array to store them) as well as time/space complexties we'll skip repeating items
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
# TC: O(n^2 + nlogn) Explanation: Sorting takes nlogn + for loop takes n time, inside which both the pointers keep moving (both put together) for at most n times. So total of nlogn+n^2 time is taken
# SC: O(1) Explanation: Although we are storing answers in result Array but that's for returning the answer directly, so that could not be counted as extra space, apart from which nothing occupies anymore space, making the total SC as O(1).