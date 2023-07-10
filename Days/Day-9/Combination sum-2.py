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
# ----------------------------------------------------------------------------------------------------------------------
# Approach1: Here, while using pick and non-pick approach as it is specified that same number from array cant be repeated within same subArray, we'll always increment the current index. So function params of recursive function will be index, sum, subArray. Out of which index always increments while sum and subArray increment by given array's current index item, in case of pick and stays as it is in not pick case. Also unlike Combination sum-1, here constraint doesnt say there will be all distinct items in given Array. So we stick to using a resSet instead of resArr and also sort the given Array to avoid duplicate subArrays. Base condition is to return out of the function in case index is equal to length of array or sum exceeds the target. Contrarily if sum is found equal to target, we append subArray into resSet and then return out of the function. One thing to note is unlike in Combination sum-1, here order of base conditions matters and in fact here #--1 has to be mentioned compulsorily before #--2. This is for case where target=7 and givenArr=[1,2,7] where for non-pick call when subArr=[7] and index=2, and further a call to index+1 i.e. 3 index is made if #--2 is met first then without appending the subArr where sum=7, we'll terminate the function. In Combination sum-1 as there was a keep picking call, it took care of creating a subArr=[7] while not incrementing the index to 3.
"""
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        resSet = set()

        def helperFunc(index, sum, subArr):
            if sum == target:                    #--1
                resSet.add(tuple(subArr))
                return
            elif index == len(candidates) or sum > target: #--2
                return
            # keeps picking current
            temp = subArr[:]
            temp.append(candidates[index])
            helperFunc(index+1, sum + candidates[index], temp)
            # not-pick current
            helperFunc(index + 1, sum, subArr)

        helperFunc(0, 0, [])
        return resSet

S = Solution()
print(S.combinationSum2([2,5,2,1,2], 5))
"""
# TC: O(n(2^n)+nlogn) Explanation: temp creation takes n time, for 2^n recursive calls. Along with sorting the given array at begining for once.
# SC: O(2n) Explanation: Recursive stack space- n. temp contributing n more space in addition to recursive stack space.


# Approach2: Improved SC and marginal improvement in TC. We'll avoid using set() by incorporating the method of using a for loop with a condition to create all possible subArrays of the same length yet avoiding duplicates. This will save us of from list into tuple so to store it into set(). Also when a new item is stored in set() it runs a duplicate/collision detection check which under the hood makes using set() more expensive than lists in terms of time. So, inside a for loop, we'll append the current index's item from given array into subArray param and further recursively call the same function on updated subArr and updated index-params so that on top of them subArrays of further length could be generated. For base condition as last sublength would already have it's index at n-1, it wont enter into for loop and thus function ends by default with a return None.
from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        resArr = []

        def helperFunc(index, sum, subArr):
            if sum == target:
                resArr.append(subArr)
            elif sum > target: #To avoid keep checking for all the numbers even further ahead uptill last elem if we already have exceeded sum
                return

            for i in range(index, len(candidates)):
                if i != index and candidates[i] == candidates[i - 1]: continue
                helperFunc(i + 1, sum + candidates[i], subArr + [candidates[i]]) #Difference between concate and append for an array is that concate doesnt change original array but rather returns a new array that has copied all items from old array and at end adds the appended item. That also explains second difference which is that while append takes O(1) TC concate takes O(n) TC. So ovreall subArr + [candidates[i]] takes same time as temp=subArr[:]; temp.append(candidates[i])

        helperFunc(0, 0, [])
        return resArr


S = Solution()
print(S.combinationSum2([2, 5, 2, 1, 2], 5))
# TC:O(nlogn + n(2^n)) Explanation: sorting array at the starting- n and later generating all the arrays of same length and increasing the length then for generating all possible subArrays which are 2^n inside which every time at worst n TC would be taken for concate operation- hence n(2^n) TC.
# SC:O(n) Explanation: We're not creating a temp, so only for recursive calls stack space of n will be occupied.
