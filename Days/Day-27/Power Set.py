# https://practice.geeksforgeeks.org/problems/power-set4302/1

# Power Set: Given a string S, Find all the possible subsequences of the String in lexicographically-sorted order.

# Example 1:
# Input : str = "abc"
# Output: a ab abc ac b bc c
# Explanation : There are 7 subsequences that can be formed from abc.

# Example 2:
# Input: str = "aa"
# Output: a a aa
# Explanation : There are 3 subsequences that can be formed from aa.

# Your Task:
# You don't need to read input or print anything. Your task is to complete the function AllPossibleStrings() which takes S as the input parameter and returns a list of all possible subsequences (non-empty) that can be formed from S in lexicographically-sorted order.
# Expected Time Complexity: O(2n) where n is the length of the String
# Expected Space Complexity: O(n * 2n)

# Constraints:
# 1 <= Length of String <= 16
# --------------------------------------------------------------------------------------------------------
# Approach1: Brute Force- Power Set Method. For any given string of n length, the total substrings which could be obtained from combination of characters present in this given string is always 2^n. Now to find all the unique 2^n substrings we can refer the binary representations of 2^n-1 numbers starting from 0. For example for string=abc the total possible substrings will be 2^3=8. These strings can be derived off of numbers from 0 to 7, where in 0 integer in binary will be 000 and 1 will be 001 whereas 5 will be 101. Now, for all the bits, we can assign them an index number and associate that with index in string. 001 will be 0th 1st and 2nd index in given string i.e. abc. Hence 001 will be an a, 010 as b, 001 as c; 000 will be empty string and 101 will be ca.
class Solution:
    def AllPossibleStrings(self, s):
        n = len(s)
        arr=[]
        for i in range(1,2 ** n): #go from 0 to (2^n - 1) numbers. We skip 0 here as it gives empty string which is not matching in answer.
            substr = ""
            for j in range(n): #for each number, traverse all the index in that number's bitwise representation.
                if 0!=(i & 1 << j): #Checking if that particular index in the current number is set with bit 1. If so, we'll make the corresponding character from the given string as a part of answer. Note:'<<' is bitwise Left Shift Operator. Here we're checking for example for n=3 and i=5, we'll check for 5&InBinary(001) then in next iteration of this inner for-loop we'll check 5&010 and in last 5&100. 5 is 101 in binary hence 101&001 will be 001 which will be 2 which is non zero and hence we'll include 'a' in answer then 101&010 which is 000 so we dont do any temperament with answer and lastly 101&100 is 100 which is nonzero and so we include c in answer.
                    substr += s[j]
            arr.append(substr)
            arr.sort()
        return arr

S = Solution()
print(S.AllPossibleStrings('abc'))
# TC: O((n * 2^n) +nlogn) Explanation: The outer for loop runs for 2^n times wherein for each iteration, the inner for loop runs for n times. On top of that we'll for once sort the array which will take nlogn time.
# SC: O(1) Explanation: Only array which is used for storing purely output value is used, which just is inevitable to save up on. Hence we can say no extra space is used