# https://leetcode.com/problems/permutation-sequence/

# The set [1, 2, 3, ..., n] contains a total of n! unique permutations.
# By listing and labeling all of the permutations in order, we get the following sequence for n = 3:
# "123"
# "132"
# "213"
# "231"
# "312"
# "321"
# Given n and k, return the kth permutation sequence.

# Example 1:
# Input: n = 3, k = 3
# Output: "213"

# Example 2:
# Input: n = 4, k = 9
# Output: "2314"

# Example 3:
# Input: n = 3, k = 1
# Output: "123"

# Constraints:
# 1 <= n <= 9
# 1 <= k <= n!
# ------------------------------------------------------------------------------------------------------------------------------------
# Approach1: Recursion- Find all the possible permutations and store them in an array (Day10/Print all permutations of a stringORarray.py). Further sort the array and return the asked index-1. For mentioned n first we'll generate an array which has those many items in incremental order starting from 1. At last from resArr, we select k-1th index subArray and convert that into a string which is returned.
from typing import List


class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        resArr = []
        nums = []
        for i in range(1, n + 1):
            nums.append(i)  # --1

        def helperFunc(index, subArr):
            if index == len(nums) - 1:
                resArr.append(subArr[:])
                return

            for i in range(index, len(nums)):
                subArr[index], subArr[i] = subArr[i], subArr[
                    index]  # Strings are immutable just like other basic DataTypes, so although a string item can be accessed by index, the items could not be swapped. Hence at #--1 we couldn't have alternatively chosen for a string instead of list, but we have to use all lists and later convert required one into string. Note: although immutable but string could be concatenated as concate returns a new string itself. So after declaring nums="", at #--1 we could've done nums+=str(i). But again then at swapping here, we wont have been able.
                helperFunc(index + 1, subArr)
                subArr[index], subArr[i] = subArr[i], subArr[index]

        helperFunc(0, nums)
        resArr.sort()
        resArr = resArr[k - 1]
        resStr = ''.join(str(i) for i in resArr)
        return resStr


S = Solution()
print(S.getPermutation(3, 3))


# TC: O(2n + 2n!n) Explanation: At starting to generate nums, for-loop takes n time. n!n for all recursions. For n! cases resArr would be appended with n elements from subArr which adds n!n more TC. At the end to join n items from resArr[k-1], n more TC.
# SC: O(2n + n!n) Explanation: n for recursive stack space and n to hold nums, plus resArr holding n!n extra space as only one string which is asked for is justified to be stored not all n! strings each with n length.


# Approach2: Maths- Improved Space and Time Complexity. Consider Eg: of n, k as 4, 9. Given array generated is [1,2,3,4]. Now we know n! are total permutations and given are n items, so we can say there are n!/n=> n(n-1!)/n => n-1! perms (permutations) where each of n items will be leading. This shows from 0 to n-1!=> 0 to 6 are those permutations wherein 1 will be leading number. As given k is raw number and does not account for fact that as array indices start from 0 and so will permutations, we have to deduct 1 from k and level it out at begining. There-after k//n-1! shows that of n groups of n-1! items (which is where the item would be leading), which group does k fall in further showing what will be leading character. In this case 9//6=>1st index and so we remove 2, to make our currStr="2" and givenArr=[1,3,4]. Before removal we'll also have to update k, as now k has to be capped to under (n-1)!. So we do k=k%(n-1)!=>9%6=>3. Thus we have givenArr=[1,3,4] currStr="2" and k=3. We again pick up item at index k//n-1!=> 3//2 => 1 and update k to 3%2=>1. So now givenArr=[1,4] currStr="23" k=1. Again to be picked index is k//n-1!=> 1/1=1 meaning givenArr=[1] and currStr="231", and updated k=k%(n-1!)=> 1%1=0. Uptill len(givenArr)==0, we'll keep doing this. This time picked item = 0//0!=> 0//1=> 1, meaning givenArr=[] and currStr="2314".
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        resArr, resStr = [], ""
        for i in range(1, n + 1):
            resArr.append(i)

        k -= 1
        while len(resArr) > 0:
            fact = factorial(len(resArr) - 1)
            resStr += str(resArr[k // fact])
            resArr.pop(k // fact)
            k = k % fact
        return resStr


def factorial(num):
    if num > 1:
        return num * factorial(num - 1)
    return 1


S = Solution()
print(S.getPermutation(4, 4))
# TC:O(n + 3n(n)) Explanation: n time to fill resArr. Further while loop will run for n times, each time remove 1 item from n item array, uptill array length==0. Inside each iteration of while factorial will take n time and so will resStr (concate will create a new string where added item is appended), and resArr.pop (it has to traverse till that array before deleting). So that makes up for 3n(n) TC.
# SC: O(2n) Explanation: resArr holding n unnecessary space and n space for recursive stack of factorial for any given execution.
