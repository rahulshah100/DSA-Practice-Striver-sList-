# https://leetcode.com/problems/permutations/

# Given an array nums of distinct integers, return all the possible permutations.You can return the answer in any order.

# Example1:
# Input: nums = [1, 2, 3]
# Output: [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]

# Example2:
# Input: nums = [0, 1]
# Output: [[0, 1], [1, 0]]

# Example3:
# Input: nums = [1]
# Output: [[1]]

# Constraints:
# 1 <= nums.length <= 6
# -10 <= nums[i] <= 10
# All the integers of nums are unique.
# ------------------------------------------------------------------------------------------------------------------------------
# Approach1: Backtracking- in a for loop inside a recursive function, which takes an index and subArr as it's params, we'll swap the item pointed by index-param with for-loop-pointer. For-loop iterates from index-param uptill length of given array. As a swap is done a further recursive call is made with an incremented index pointer and resultant of the swap as a subArr. As we meet the base case of index-param being equal to length of given array we append subArr into resArr and return out. Coming back to parent call, we restore the subArr by reswapping the last swapped items, so it is yet again prepared for the next iteration in for-loop. Recursive Tree is shown below as Eg-
#                                                          i/p: [1,2,3]
#                                   [1,2,3]                [2,1,3]                [3,2,1]
#                               [[1,2,3], [1,3,2]  ,     [2,1,3]   [2,3,1]     ,  [3,2,1] [3,1,2]]
#Return/Base Condition
from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        resArr = []

        def helperFunc(index, subArr):
            if index == len(nums)-1:
                resArr.append(subArr[:])
                return

            for i in range(index, len(nums)):
                subArr[index], subArr[i] = subArr[i], subArr[index]
                helperFunc(index + 1, subArr)
                subArr[index], subArr[i] = subArr[i], subArr[index]

        helperFunc(0, nums)
        return resArr


S = Solution()
print(S.permute([1, 2, 3]))  # O/P: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
# TC: O(2(n!)(n)) Explanation: depth of tree is n and width is n!. Yes, for permutations possibilities are always n!. So that yields (n)(n!) TC. Also copying items in n! cases into resArrr will take n time each so that yield an additional n(n!) TC. Totalling these both 2(n)(n!) TC is consumed.
# SC: O(n) Explanation: recursive stack space of n is only what's used here


# Approach2: Recursion- Worst than Approach1 for Time and Space Complexity. So in every iteration of for we'll make a new copy of subArr which will be modified and sent further. Because of this we avoid having to restore original subArr as we retrace back to that step once coming back from base condition, this is what seperates recursion from backtrack. Resultantly, we'll also not need to copy items into resArr but could directly append subArr as it is the newly created temp List every time. As temp is always reassigned/recreated it's instances are not modified and new ones are always created due to which we dont see any troubles appending subArr in resArr without making it's shallow copy unlike above approach.
"""
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        resArr = []

        def helperFunc(index, subArr):
            if index == len(nums)-1:
                resArr.append(subArr)
                return

            for i in range(index, len(nums)):
                temp=subArr[:]
                temp[index], temp[i] = temp[i], temp[index]
                helperFunc(index + 1, temp)

        helperFunc(0, nums)
        return resArr
"""
# TC: O(n!(n)(n)) Explanation: n!n time for recursive calls. In each call we are creating temp which will take n TC every time.
# SC: O(2n) Explanation: recursive stack space n, plus temp using n space for the current execution in worst case. Hence total 2n Space.