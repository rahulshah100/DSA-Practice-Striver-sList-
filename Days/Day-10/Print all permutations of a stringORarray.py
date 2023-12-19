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
# Approach1: Backtracking - in a for loop inside a recursive function, which takes an index and subArr as it's params, we'll swap the item pointed by index-param with for-loop-pointer. For-loop iterates from index-param uptill length of given array. As a swap is done a further recursive call is made with an incremented index pointer and resultant of the swap as a subArr. As we meet the base case of index-param being equal to length of given array we append subArr into resArr and return out. Coming back to parent call, we restore the subArr by re-swapping the last swapped items, so it is yet again prepared for the next iteration in for-loop. Recursive Tree is shown below as Eg-
#                                                         i/p: [1,2,3]
#                                   [1,2,3]                    [2,1,3]                [3,2,1]
#                              [[1,2,3], [1,3,2]          [2,1,3]   [2,3,1]        [3,2,1] [3,1,2]]
from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        return self.helperfunc(nums, 0, [])

    def helperfunc(self, temp, index, ansArr):
        if index==len(temp):
            ansArr.append(temp[:])

        for i in range(index, len(temp)):
            temp[index], temp[i] = temp[i], temp[index]
            self.helperfunc(temp, index+1, ansArr)
            temp[index], temp[i] = temp[i], temp[index]
        return ansArr

S = Solution()
print(S.permute([1, 2, 3]))  # O/P: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
# TC: O(2(n!)(n)) Explanation: depth of tree is n and width is n!. Yes, for permutations possibilities are always n!. So that yields (n)(n!) TC. Also copying items in n! cases into resArrr will take n time each so that yield an additional n(n!) TC. Totalling these both 2(n)(n!) TC is consumed.
# SC: O(2n) Explanation: recursive stack space of n is used and so is additional n space used by temp.


# Approach2: Recursion - Worse than Approach1 for Time and Space Complexity. So in every iteration of for we'll make a new copy of temp which will be modified and sent further. Because of this we avoid having to restore original temp as we retrace back to that step while coming back from base condition, this is what seperates recursion from backtrack. Resultantly, we'll also not need to copy items into ansArr but could directly append subArr as it is the newly created temp List every time. As temp2 is always reassigned/recreated it's instances are not modified and new ones are always created due to which we dont see any troubles appending temp in ansArr without making it's shallow copy unlike above approach.
"""
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        return self.helperfunc(nums, 0, [])

    def helperfunc(self, temp, index, ansArr):
        if index==len(temp):
            ansArr.append(temp)

        for i in range(index, len(temp)):
            temp2=temp[:]
            temp2[index], temp2[i] = temp2[i], temp2[index]
            self.helperfunc(temp2, index+1, ansArr)
        return ansArr

S = Solution()
print(S.permute([1, 2, 3]))
"""
# TC: O(n!(n)(n)) Explanation: n!n time for recursive calls. In each call we are creating temp which will take n TC every time.
# SC: O(3n) Explanation: recursive stack space n, plus temp and temp2 using n space each, for the current execution. Hence total 3n Space.