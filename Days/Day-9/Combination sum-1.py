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
# Approach 1: Recursion- pick and not pick technique we'll use. So idea is from candidates array in every iteration we'll either pick or not pick the last item. The picked item will add onto the sum (maintained as a param) and will be stored in a temp array (maintained as param). Now uptill sum is lesser than target and the length of candidates arr is not 0, we'll keep placing the pick and non-pick calls. In pick as we're allowed to keep picking the same item we'll not shrink the size of candidates arr, while in non-pick we exclude last item from candidates arr before passing it to child recursive calls. As we find sum == target we store temp's copy in an ansArr. Further as this call returns so that temp can be brought into it's original state we pop last item.
from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        return self.helperFunc([], [], 0, candidates, target)

    def helperFunc(self, temp, ansArr, sum, candidates, target):
        if sum<target and len(candidates)!=0:
            self.helperFunc(temp, ansArr, sum, candidates[:-1], target)
            temp.append(candidates[-1])
            self.helperFunc(temp, ansArr, sum+candidates[-1], candidates, target) #Here we didnt send temp[:] because at #--1 we are storing a copy only, hence the temp can change here and it wont affect the stored value which is a copy
            temp.pop()
        elif sum==target:
            ansArr.append(temp[:]) #--1
        return ansArr

S = Solution()
print(S.combinationSum([2, 3, 6, 7], 7))
# TC: O((2^n)k) given length of array is n and target is k. Explanation: For pick and non-pick we'd have 2^n TC. But here as we can also keep picking the same item as many times as we want uptill it exceeds target, and given the constraint our smallest value can be 2. If we keep taking 2 at worst we'll take target/2 times i.e. k/2 times we can run 2^n calls at worst. Generalize k/2 as k and we get (2^n)*k as our TC.
# SC: O(2n) Explanation: recursive stack space of n/2 as at max the smallest number will be 2, so for 3 2s if target=6 we'll achieve its base condition. Hence a recursive chain will only grow an n/2 length- showing the recursive space occupied. Further temp might hold n elems at max, for a recursion. So (n/2)+n=>2n is SC. resArr is excluded from counting in SC as it is the required space, for returning the output.
