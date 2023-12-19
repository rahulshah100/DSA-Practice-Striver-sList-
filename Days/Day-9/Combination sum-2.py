# https://leetcode.com/problems/combination-sum-ii/

# Given candidates and target, find all unique combinations in candidates where the numbers sum to target, with each number used only once and no duplicate combinations in the solution set.

# Example 1:
# Input: candidates = [10,1,2,7,6,1,5], target = 8
# Output: [[1,1,6],[1,2,5],[1,7],[2,6]]

# Example 2:
# Input: candidates = [2,5,2,1,2], target = 5
# Output: [[1,2,2],[5]]

# Constraints:
# 1 <= candidates.length <= 100
# 1 <= candidates[i] <= 50
# 1 <= target <= 30
# --------------------------------------------------------------------------------------------------------------------------------
# Approach1: Using Combination sum-1.py's pick and non pick method with 3 changes we achieve this. First when picking unlike Combination sum-1.py here we can't chose the same number for more than one so we shrink candidates to items excluding the last one with each recursive call. Further at the start we sort the candidates so that for arr=[12,1,43,5,1,32] we wont get sub-arrays as [1,5] and [5,1] which will be considered seperate, but now we'll have both as [1,5]. Finally to exclude repeating subArrays, while appending we check if temp is not in ansArr.
"""from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        return self.helperFunc([], [], 0, candidates, target)

    def helperFunc(self, temp, ansArr, sum, candidates, target):
        if sum<target and len(candidates)!=0:
            self.helperFunc(temp, ansArr, sum, candidates[:-1], target)
            temp.append(candidates[-1])
            self.helperFunc(temp, ansArr, sum+candidates[-1], candidates[:-1], target)
            temp.pop()
        elif sum==target and temp not in ansArr:
            ansArr.append(temp[:])
        return ansArr

S = Solution()
print(S.combinationSum([2, 3, 6, 7], 7))
"""
# TC: O(nlogn + 2^n + 2^2n) Explanation: Sorting the given array at begining for once takes nlogn. Each call grows with 2 more, so 2^n time complexity for all recursive calls. Plus at the end for 2^n cases at worst i.e. all pick and non-pick combination we will have to check through ansArr of size 2^n if temp is not in ansArr.
# SC: O(2n) Explanation: Recursive stack space- n. temp contributing n more space in addition to recursive stack space.


# Approach2: In approach1 we'll avoid checking the condition of temp not in ansArr by devising a similar logic to Subset-ii.py, where in we create all possible subarrays of one length at a time in a for-loop and put recursive call for each for-loop iteration with an incremented index so that on top of existing length of array, more elements can be added and a bigger array could be built. In this for-loop we use continue-statement to skip iterations where when i!=index and still if the item at i in candidates is same as candidate's i-1th item. In each recursive function call we check first if sum is equal to target and if so, we append a copy of temp into ansArr. If otherwise sum>target or index==len(candidates) we return back from that function. Also note we use sorted candidates array here.
from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        return self.helperFunc([], [], 0, 0, candidates, target)

    def helperFunc(self, temp, ansArr, sum, index, candidates, target):
        if sum==target:
            ansArr.append(temp[:])
        elif sum>target or index==len(candidates):
            return
        for i in range(index, len(candidates)):
            if i != index and candidates[i] == candidates[i - 1]:
                continue
            temp.append(candidates[i])
            self.helperFunc(temp, ansArr, sum+candidates[i], i+1, candidates, target)
            temp.pop()
        return ansArr

S = Solution()
print(S.combinationSum2([2, 3, 6, 7], 7))
# TC:O(nlogn + 2^n) Explanation: sorting array at the starting takes nlogn and later exploring the cases of all the subarrays possible i.e. 2^n
# SC:O(n) Explanation: Only for recursive calls stack space of n will be occupied.
