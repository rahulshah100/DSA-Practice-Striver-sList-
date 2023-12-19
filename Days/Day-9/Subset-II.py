# https://leetcode.com/problems/subsets-ii/

# Subsets II
#  Given an integer array nums that may contain duplicates, return all possible subsets (the power set). The solution set must not contain duplicate subsets.Return the solution in any order.

# Example1:
# Input: nums = [1, 2, 2]
# Output: [[], [1], [1, 2], [1, 2, 2], [2], [2, 2]]

# Example2:
# Input: nums = [0]
# Output: [[], [0]]

# Constraints:
# 1 <= nums.length <= 10
# -10 <= nums[i] <= 10
# --------------------------------------------------------------------------------------------------------------------------------------------
# Approach1: In power method to avoid duplicates we'll first do sorting of given array and use a set() to append new subArrays, later to convert the whole set into array for returning. We'll use 2 for loops, first one representing the numbers/possibility of 2^n subsets and second for-loop to pick items from given array in accordance with binary representation of 2^n numbers. (Better explained in Subset Sums.py under the same Day).
"""
from typing import List

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n,resSet=len(nums),set()
        for i in range(2**n):
            temp=[]
            for j in range(n):
                if i&(1<<j)!=0:
                    temp.append(nums[j])
            resSet.add(tuple(temp))
        resArr=[list(i) for i in resSet]
        return resArr

S=Solution()
print(S.subsetsWithDup([1,2,2])) #[[],[1],[1,2],[1,2,2],[2],[2,2]]
"""
# TC: O(nlogn+ n(2^n) + 2^n) Explanation: for sorting n item array nlogn. For an n time traversal using for loop inside a 2^n time traversing for-loop we'll have n(2^n) TC. Converting 2^n items (in worst case) from set() into list another 2^n Time.
# SC: O(n(2^n)) Explanation: Although we are returning resArr (whose space could be forgiven as it's inevitable and asked to be returned), we had to utilize resSet which will hold 2^n possible subsets each of which at max can have n length.


# Approach2: Better Space worst Time Complexity. In approach one instead of going over an intermediary step of converting set in list here we'll directly use list itself wherein while appending temp into resArr we'll check once if temp is not present and only if so we'll append:
"""
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n,resArr=len(nums),[]
        for i in range(2**n):
            temp=[]
            for j in range(n):
                if i&(1<<j)!=0:
                    temp.append(nums[j])
            if temp not in resArr:
                resArr.append(temp)
        return resArr
"""
# TC: O(nlogn+ n(2^n) + 2^n + (2^n)(2^n)) In Approach 1's TC an additional (2^n)(2^n) time is added because for 2^n times while appending temp we'll check resArr which at max could have 2^n subArrays, to figure whether temp already exists. So this yields (2^n)(2^n) addition time
# SC: O(1) apart from necessary resArr's space nothing more is used


# Approach3: Using a nested for loops and a resultantArr which will have an empty array, we'll iterate through given array using outer for loop. For each iteration of outer for loop the item pointed by current iteration from given Array would be clubbed with the all the items of resArr, one after the other as they'll be pointed by  inner for loop. The clubbed items will be appended in resulatnArr as new subArrays. To avoid duplicates, in this much code we'll additionaly have the given array sorted and while appending a new item in resultantArr we'll check and make sure it doesn't already exist
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        resArr=[[]]
        for i in range(len(nums)):
            for j in range(len(resArr)):
                    temp=resArr[j][:] #As seen here a shallow copy is needed of resArr's j-th index coz otherwise altering temp ended altering the already stored at item in resArr at j-th index
                    temp.append(nums[i])
                    if temp not in resArr:
                        resArr.append(temp)
        return resArr
# TC: O(nlogn + n(2^n)(2^n)) Explanation: nlogn for sort and then n(2^n) for coming inside the inner for-loop where in we further check in worst case for 2^n items if temp is not present. So that becomes n(2^n)(2^n).
# SC: O(n) as temp could at max be making a subArray's copy of n items.


# Approach4: Using recursion's pick and not pickup approach. We will use an ansArr, tempArr, and given nums arr as arguments to helper-function and do recursive calls. Each time not picking and picking and resultantly eliminating the last item from nums in every iteration. When nums become empty we check if tempArr doesn't exist in ansArr and if so, we append it.
from typing import List

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        return self.helperfunc([], [], nums)

    def helperfunc(self, tempArr, ansArr, nums):
        if len(nums) > 0:
            self.helperfunc(tempArr, ansArr, nums[:-1])
            tempArr=tempArr[:]
            tempArr.append(nums[-1])
            self.helperfunc(tempArr, ansArr, nums[:-1])
        elif tempArr not in ansArr:
            ansArr.append(tempArr)
        return ansArr

S = Solution()
print(S.subsetsWithDup([1, 2, 2]))  # O/P: [[], [1], [1, 2], [1, 2, 2], [2], [2, 2]]
# TC:O(2^2n + 2^n + nlogn) Explanation: nlogn for sorting at beginning. 2^n for forming recursive tree i.e. for all the recursive calls. 2^n will be end points in which for each time we'll check if tempArr is present in ansArr which will take additional 2^n * (size of ansArr). Given the size of ansArr in worst case can be 2^n, we get (2^n)^2 i.e 2^2n.
# SC:O(2n+ 2^n) Explanation: Stack space of n will be required alongside using n space (in worst case) to hold the temporary array:temp in any given call, plus ansArr will hold a 2^n items. Note: here we're going with the understanding that for recursion current space and the stack space is occupied only for ongoing/present call that is running at any moment as all the other ones are not simultaneously happening, so in that way at worst for a given call it'll have a depth of n. From there only once call returns encountering the base case the second parent call i.e. right branch of tree will start to be executed.


# Approach5: Improved SC and TC than Approach4. In approach4 to avoid checking if tempArr is present in ansArr the approach we can take is we can generate all equal sized sub-arrays for doing which we'll iterate over the nums and when we find the current number to be same as last number we skip the iteration. Further, as this type of sub-arrays are being created we'll put a recursive call with the index after the one from where the item has been picked for creating that particular subarray. So what we can do is a for-loop in which we'll append single items at first, where we check if current item is not equal to it's prev which if so we skip this iteration. If not skipped then this item would be appended in an ansArr. Then we'll make a recursive call made with the next then current index passed. Again as function is ran we know we are building array of a bigger length and for which we need to have access to the existing array, for this we'll fetch last item from ansArr, and as from there only this recursive call is made that is the item we need; we'll make this as temp. Further we know even if current item is equal to last item we still want it once because here including it will result in an array of different length i.e. [2] and [2] we dont want but [2,2] we want, so we know the checking condition in for-loop has to be altered, and we cut ourselves an exception to not check for the iteration where i is same as index passed, because for-loop runs with i pointer incremented from index to totalArrLength and thus for building a longer array as a recursive call is made we know i==index is where even if a duplicate is there we want it.
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        return self.helperfunc(0, [[]], nums)

    def helperfunc(self, index, ansArr, nums):
        temp = ansArr[-1][:]
        for i in range(index, len(nums)):
            if i != index and nums[i] == nums[i - 1]:
                continue
            temp.append(nums[i])
            ansArr.append(temp[:])
            self.helperfunc(i + 1, ansArr, nums)
            temp.pop()
        return ansArr
# TC: O(nlogn + 2^n). Explanation: nlogn to sort the givenArray at starting and further the algorithm explores all the combinations of subArray which are 2^n hence that's the rate at which algorithm grows or the time algo takes.
# SC: O(2n) Explanation: At worst the executing function will make a copy of temp equal to size of n. Now the execution is such that only one chain of recursion is in execution at once. At max the recursion chain will be on length n. And it's from here i.e. (n) max depth of recursive chain, that execution hits the base condition and further backtracks to culminate into a new branch of recursive calls will could further keep going on till base condition is again hit. But point is to say at worst n would be stack space to store recursive call lineage and only one current execution will be happening wherein temp's would be an only additional space. Taking worst of both i.e. n+n space is consumed.