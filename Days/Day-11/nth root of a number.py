# https://www.codingninjas.com/studio/problems/1062679?topList=striver-sde-sheet-problems&utm_source=striver&utm_medium=website

# You are given two positive integers. You have to return the 'nth' root of 'm'. If the 'nth root is not an integer, return -1.

# Example1:
# Input: ‘n’ = 3, ‘m’ = 27
# Output: 3
# Explanation:
# 3rd Root of 27 is 3, as (3)^3 equals 27.

# Example2:
# Input:4 69
# Output:-1
# Explanation: 4th Root of 69 is not an integer, hence -1.

# Constraints:
# 1 <= n <= 30
# 1 <= m <= 10^9
# Time Limit: 1 sec.
# ------------------------------------------------------------------------------------------------------------------------
# Approach1: Run a for loop to check for all numbers from 1 to m if they're multiplied by themselves for n times, and if either of them equals to m, we return this number as answer. Outside this for loop we return -1.
def NthRoot(n: int, m: int) -> int:
    for i in range(1, m + 1):
        tot = 1
        for j in range(n):
            tot *= i
        if tot == m:
            return i
    return -1

print(NthRoot(3, 27))  # O/P: 3
# TC: O(mn)
# SC: O(1)


# Approach2: Binary Search- We'll run Binary search with an upper as the givenNumer- m and lower as 1, coz not 1 and anything less than 1 i.e. say 0 will mean taking into account the answer to be in decimals too but question states only if whole number is answer then to return it or else to return -1, so no need to start from 0. Further we'll find mid for lower, upper using an integer division, and if n times mid is equal to m then we return mid, if m times m is greater than m then we reduce upper to mid-1. Or else we bump lower to mid+1. The process of finding mid and updating lower, upper will go on till lower is less than or equal to upper as when they're equal that might be the mid, so we do take into account for lower to be upto higher as well. Outside while we'll return -1.
def NthRoot(n: int, m: int) -> int:
    l, u = 1, m
    while u >= l:
        mid = (l + u) // 2
        nTimesMid = 1
        for i in range(n):
            nTimesMid *= mid
            if nTimesMid>m: #If we've discovered that u would have to be modified than let's limit the effort here mow.
                break
        if nTimesMid == m:
            return mid
        elif nTimesMid > m:
            u = mid - 1
        else:
            l = mid + 1
    return -1


print(NthRoot(4, 69))
print(NthRoot(3, 27))

# TC: O(nlogm) Explanation: for array with of size m in max logm time l will cross u, so logm time for binary search wherein for each iteration, a for loop runs for n times.
# SC: O(1) Explanation: Apart from constant space used by mid and tot variable, no extra space is utilised
