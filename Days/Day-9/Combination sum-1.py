# https://leetcode.com/problems/combination-sum/

# Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order. The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the frequency of at least one of the chosen numbers is different. The test cases are generated such that the number of unique combinations that sum up to target is less than 150 combinations for the given input.

# Example 1:
# Input: candidates = [2, 3, 6, 7] target = 7
# Output:[[2, 2, 3], [7]]
# Explanation:
# 2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
# 7 is a candidate, and 7 = 7.
# These are the only two combinations.

# Example 2:
# Input: candidates = [2,3,5], target = 8
# Output: [[2,2,2,2],[2,3,3],[3,5]]

# Example 3:
# Input: candidates = [2], target = 1
# Output: []

# Constraints:
# 1 <= candidates.length <= 30
# 2 <= candidates[i] <= 40
# All elements of candidates are distinct.
# 1 <= target <= 40
# --------------------------------------------------------------------------------------------------------------------------
# Approach 1: Recursion- pick and not pick technique we'll use. Note we are given in constraint all elems of candidates are distinct so we'll simply use an resArr to return all subArrays here. We keep calling a recursive function with index, sum and subArr as function params. Inside this function if sum is found to have exceeded the target or if index has become equal to length of given array we simply return out of recursive loop. On the other hand if sum is found equal to target we'll append the subArr into resArr and the return out of the recursive loop. If none of this cases are true then we'll recusrively keep calling the function once with same index, but sum incremented by current index and it's subArr appended by given array's current index item- showing pick, while the second recursive call incrementing index while keeping sum and subArr as it is showing not pick.
from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        resArr = []

        def helperFunc(index, sum, subArr):
            if index == len(candidates) or sum > target:
                return
            elif sum == target:
                resArr.append(subArr)
                return
            # keeps picking current
            temp = subArr[:]    #This is an O(n) TC Operation, not O(1)
            temp.append(candidates[index])
            helperFunc(index, sum + candidates[index], temp)
            # not-pick current
            helperFunc(index + 1, sum, subArr)

        helperFunc(0, 0, [])
        return resArr

S = Solution()
# print(S.combinationSum([2, 3, 6, 7], 7))  #O/P:[[2,2,3],[7]]
print(S.combinationSum([3, 5, 8], 11))
# TC: O((2^n)n) Explanation: For given array of n length those are n option wherein we can determine pick and not pick. And that is within each option after once having picked/not-picked we are further deciding whether to pick or not-pick the same or the farther element. Of essence is to see each option opening to 2 new options. Further inside each of them temp has to be made from subArr which at max can take n time.
# SC: O(2n) Explanation: recursive stack space of n/2 as at max the smallest number will be 2, as given in constraints, so for 3 2s if target=6 we'll achieve it hit the base condition. Hence a recursive chain will only grow an n/2 length- showing the recursive space occupied. Further temp might hold n elems at max, for a recursion. So (n/2)(n)=>n^2 is SC. resArr is excluded from counting in SC as it's shows the required space for returning the output.
