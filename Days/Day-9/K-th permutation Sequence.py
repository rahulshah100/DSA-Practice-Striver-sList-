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
# Approach1: Recursion- Find all the possible permutations (Day10/Print all permutations of a stringORarray.py). While storing all the permutations, we'll store them as string in ansArr array. Thus generated array of strings is yet still unsorted and so we'll sort it once.Finally, we return the string from k-1th index of ansArr.
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        subStr=self.helperfunc([i for i in range(1, n + 1)], 0, [])
        subStr.sort() #apparently even on an array of string, sort() works
        return subStr[k-1]

    def helperfunc(self, temp, index, ansArr):
        if index == len(temp):
            resStr = ''.join(str(i) for i in temp)
            ansArr.append(resStr)

        for i in range(index, len(temp)):
            temp[index], temp[i] = temp[i], temp[index]
            self.helperfunc(temp, index + 1, ansArr)
            temp[index], temp[i] = temp[i], temp[index]
        return ansArr

S = Solution()
print(S.getPermutation(3, 5))
# TC: O(3n + 3n!n) Explanation: At starting to generate nums, for-loop takes n time. n!n for all recursions. For n! cases resStr would be appended with n elements from temp which adds n!n more TC. At the end to join n items from resArr[k-1], n more TC. Finally subStr has to be sorted too utilizing n!n more time as there are n! strings each n chars long.
# SC: O(2n + 2n!n) Explanation: n for recursive stack space and n to hold nums, plus resArr holding n! extra space as only one string which is asked for is justified to be stored and not all the n! strings, each with n length. Also subStr will take n!n space.


# Approach2: Maths - Improved Space and Time Complexity. Idea: for an n item the permutation i.e.ways possible to arrange them is always n!. So consider that for n=4, k=9 (generated array is [1,2,3,4]) we'll have total 4! i.e.24 possible arrangements. Out of them if we take 1 out, the array is [2,3,4] i.e. length = 3 and their possible permutation will be 3!. This is where we get an insight that out of 24 possibilities all 4 digits would be leading in n-1! cases. Like if we stored 24 possibilities in an array then from 0-5th index we'll have 1 as leading number i.e. 1 _ _ _ then for 6-11 index we'll have 2 _ _ _ and so on... Here the given k which is 9 but as in array we're talking i.e. we'll check for k-1 i.e. 8 will fall in range of 6-11 index. Thus we know 2 is gonna be leading and rest we have to think for [1,3,4] that which will be next number. Also with 2 leading the 6 possibilities we have for initial k i.e. 8, we can say it'll be 8-6 => 2nd i.e. (in array terms starting from 0) the 3rd possible arrangement. So our array has been changed here now and so has the k been i.e.k=(givenFactorialofN-1)%k
# For a dry run consider below example where n = 4 and k=9
# Given array will be [1,2,3,4]
# Here 1 will hold 0-5 arrangement, 2 will hold from 6-11 and so on... and as we have zero counted as index we reduce k to k-1 i.e.8
# factorial in this case we're checking for is n-1! i.e. 3! i.e. 6 is how got above gap 0-5 and stuff
# So k//factorial = 8//6 = 1 shows that k falls in index 6-11 and hence 2 which held that index is gonna be picked and so out if it's 6 possibilities if we reduce k the new k becomes k%fact => 8%6 => 2
# Thus new array = [1,3,4] and k=2 whereas developedString = '2'
# Further factorial = n-1!=> 2!=>2
# Shows that 0-1 are possible arrangements held by 1, then 2-3 held by 3 and 4-5 are held by 4
# Given that k=2 falls in 2-3 developedString='23' and k=k%fact => 2%2 => 0
# Thus new array = [1,4] and developedString='23' and k=0
# factorial = n-1! = 1! = 1
# So 0th order of arrangement is held by 1 and 1st is held by 4. As k==0 developedString='231' and k=k%fact = 0%1 = 0
# Thus new array = [4] developedString='231' and k=0
# fact = n-1 = 0! = 1
# Thus 0th order of arrangement is held by 4
# k=k%fact = 0%1 = 0th order of arrangement and so we pick 4 and developedString='2314'

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        return self.helperfunc([i for i in range(1,n+1)], k-1, '', n)

    def helperfunc(self, givenArr, k, temp, n):
        if n==1:
            temp+=str(givenArr[0])
            return temp
        currFact = self.factorial(n - 1)
        temp += str(givenArr[k // currFact])
        givenArr.pop(k // currFact)
        return self.helperfunc(givenArr, (k%currFact), temp, n-1)

    def factorial(self, num):
        for i in range(num - 1, 0, -1):
            num *= i
        return num


S = Solution()
print(S.getPermutation(4, 9))
# TC:O(n + 2n(n)) Explanation: n time to first time make givenArr. Further recursion will run for n times, each time calling factorial function which will take n time in addition to which n time will be taken by resArr.pop (it has to traverse till that array before deleting). So that makes up for seperate 2n(n) TC.
# SC: O(2n) Explanation: resArr holding n unnecessary space and n space for recursive stack of factorial for any given execution.