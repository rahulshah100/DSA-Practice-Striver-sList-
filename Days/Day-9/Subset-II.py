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
# TC: O(nlogn+ n(2^n) + 2^n) Explanation: for sorting n item array nlogn. For a n time traversing for loop inside a 2^n time traversing for-loop we'll have n(2^n) TC. Converting 2^n items (in worst case) from set() into list another 2^n Time.
# SC: O(n(2^n)) Explanation: Although we are returning resArr (whose space could be forgiveable as it's inevatible and asked to be returned), we had to utilize resSet which will hold 2^n possible subsets each of which at max can have n length.


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
            n=len(resArr)
            for j in range(n):
                    temp=resArr[j][:] #we need an intermediate data-structure, in this case temp, coz directly doing resArr[j].append(nums[i]) will modify original resArr's jth index. Whereas here we are trying to rather generate a new item for resArr and not modify it's existing item.
                    temp.append(nums[i])
                    if temp not in resArr:
                        resArr.append(temp)
        return resArr
# TC: O(nlogn + n(2^n)(2^n)) Explanation: nlogn for sort and then n(2^n) for coming inside the inner for-loop where in we further check in worst case for 2^n items if temp is not present. So that becomes n(2^n)(2^n).
# SC: O(n) as temp could at max be making a subArray's copy which'll have n items.


# Approach4: Using recursion's pick and not pickup approach. Starting from index 0 and an empty array as our function params, we call to a function which will keep making 2 recursive calls. In each of these calls, the index is incremented once. While only in either of the calls we'll append the array param with item from given array current index. In the other call array param will be passed as it is. This will go on till base case of index=len(givenArr) where as we're at end of recursion chain we'll append the array param in a resultantSet which will take care of not repeating subArrays in result. Also to avoid duplicate subArrays we take an additional step to sort the given array so all the repeating subArrays will have items arranged in same manner. At last to return a list, we convert resultantSet to a resultantArray
from typing import List

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        resSet = set()

        def helperFunc(index, subArr, n):
            if index == n:
                resSet.add(tuple(subArr))
                return
            # pick
            temp = subArr[:]
            temp.append(nums[index])
            helperFunc(index + 1, temp, n)
            # not pick
            helperFunc(index + 1, subArr, n)

        helperFunc(0, [], len(nums))
        resArr = [list(i) for i in resSet]
        return resArr


S = Solution()
print(S.subsetsWithDup([1, 2, 2]))  # O/P: [[], [1], [1, 2], [1, 2, 2], [2], [2, 2]]
# TC:O(2(2^n)+nlogn) Explanation: nlogn for sorting at begining. 2^n for recursive calls. 2^n items will be there in resSet which will be transfered into a making them 2^n items in worst case as resArr, this thing will take 2^n.
# SC:O(2n+ 2^n) Explanation: Stack space of n will be required alongside using n space (in worst case) to hold the temporary array:temp in any given call, plus resSet will hold a 2^n items. Note: here we're going with the understanding that for recursion current space and the stack space is occupied only for ongoing/present call that is running at any moment as all the other ones are not simultaneously happening, so in that way at worst for a given call it'll have a depth of n. From there only once call returns encountering the base case the second parent call i.e. right branch of tree will start to be executed.


# Approach5: Improved SC and TC than Approach4. We'll avoid conversion of set into a list by builiding a code which at first only wont let the duplicates in resultant Array. So the idea is to generate all subArrays of same size starting from size 1 within same iteration, and keep adding them in resultant Array. As they're added in resultant, further by recursion we'll can send the one sized subArrays along with the index from where it's number has been picked to same function call wherein now starting from after that number we add one-one more number, striving to generate all subArrays with size 2. In doing this when array is of size of given Array's length and recusion is called on it then now as the for-loop that iterates upto length of givenArrays is encountered, it wont execute and so after that as no more code is to be executed, that's from where return None will be by default called as base condition. In doing all this to avoid duplicates we'll take 2 steps. First is to sort the array so all same numbers are adjacent. Second is inside start of every iteration we'll check if this number is same as it's previous one, even which if so and if it's first number in the iteration then as it is contributing to an increased lenth of subArray which wont have prior happened, we let the number through otherwise skip this iteration. To explain duplicate condition in context of Eg: [1,2,2,2]. For 1 sized arrays we'll get [1] as 1 is not equal to it's prior number. We'll get the 2 right after 1 as 2 is not equal to one, but later 2s are ignored. Now when with [1] we go onto next recursion where we build subArrays of size 2 again the 2 right after 1 has no issue as 2 is not equal to one and it gets added and we get [1,2]; further for subArray [2] when size 2 subarray has to be built and the 2 after it is checked where 2 is equal to 2, we'll still wanna include it as [2,2] is a unique subArray which has not earlier been discovered. So if in for-loop we're at first iteration or if num[i]!=num[i-1] we'll let the number through or else it is duplicate and will be skipped.
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        resArr=[[]]
        def helperFunc(subArr, index):
            for i in range(index, len(nums)):
                if i!=index and nums[i]==nums[i-1]: continue
                temp=subArr[:]
                temp.append(nums[i])
                resArr.append(temp)
                helperFunc(temp, i+1)
        helperFunc([],0)
        return resArr
# TC: O(nlogn + n(2^n)). Explanation: depth is going to be of n and width will be 2^n, so n(2^n) recursive TC & nlogn to sort the givenArray at starting.
# SC: O(2n) Explanation: At worst the executing function will make a copy of temp equal to size of n. Now the execution is such that only one chain of recursion is in execution at once. At max the recursion chain will be on length n. And it's from here i.e. (n) max depth of recursive chain, that execution hits the base condition and further backtracks to culminate into a new branch of recursive calls will could further keep going on till base condition is again hit. But point is to say at worst n would be stack space to store recursive call lineage and only one current execution will be happening wherein temp's would be an only additional space. Taking worst of both i.e. n+n space is consumed.