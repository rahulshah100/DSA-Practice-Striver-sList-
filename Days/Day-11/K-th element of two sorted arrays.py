# https://practice.geeksforgeeks.org/problems/k-th-element-of-two-sorted-array1317/1

# Given two sorted arrays arr1 and arr2 of size N and M respectively and an element K. The task is to find the element that would be at the kth position of the final sorted array.

# Example 1:
# Input:
# arr1[] = {2, 3, 6, 7, 9}
# arr2[] = {1, 4, 8, 10}
# k = 5
# Output: 6
# Explanation:
# The final sorted array would be -
# 1, 2, 3, 4, 6, 7, 8, 9, 10
# The 5th element of this array is 6.

# Example 2:
# Input:
# arr1[] = {100, 112, 256, 349, 770}
# arr2[] = {72, 86, 113, 119, 265, 445, 892}
# k = 7
# Output: 256
# Explanation:
# Final sorted array is - 72, 86, 100, 112,
# 113, 119, 256, 265, 349, 445, 770, 892
# 7th element of this array is 256.

# Your Task:
# You don't need to read input or print anything. Your task is to complete the function kthElement() which takes the arrays arr1[], arr2[], its size N and M respectively and an integer K as inputs and returns the element at the Kth position.

# Expected Time Complexity: O(Log(N) + Log(M))
# Expected Auxiliary Space: O(Log (N))

# Constraints:
# 1 <= N, M <= 106
# 0 <= arr1i, arr2i < INT_MAX
# 1 <= K <= N+M
# --------------------------------------------------------------------------------------------------------------------------------------------
# Note in question it is not given in description but we do suppose arrays are sorted.
# Approach1: Combine 2 arrays into a new array and sort this new array. Return item at n-1th index
"""
class Solution:
    def kthElement(self,  arr1, arr2, n, m, k):
        newArr=[]
        for i in range(len(arr1)):
            newArr.append(arr1[i])
        for j in range(len(arr2)):
            newArr.append(arr2[j])

        newArr.sort()
        return newArr[k-1]
"""
# TC: O(m+n+mnlogmn)
# SC: O(m+n)


# Approach2: Same as approach1 but here we use a pointer lastPointed to keep track of last variable and thus avoid creating a new sorted array
class Solution:
    def kthElement(self, arr1, arr2, n, m, k):
        pt1 = pt2 = 0
        while k:
            if pt2 == len(arr2) or pt1 < len(arr1) and arr1[pt1] <= arr2[pt2]:
                lastPicked = arr1[pt1]
                pt1 += 1
            else:
                lastPicked = arr2[pt2]
                pt2 += 1
            k -= 1
        return lastPicked
# TC: O(k) given that k is order of item Explanation: Collectively as for k times we'll let pointers increment
# SC: O(1)


# Approach 3: In addition to Medianof2sortedarrays.py's Binary Sort Approach here we have to take care of 2 additional cases that 1) For n=8, m=2 and k=7 if we take n//2 items from n sized array, then despite taking the whole m sized array we'll not be able to count kth item. Hence, l in case of arr1 has to be max(0,k-m) 2) Say k=2 and n=8 and m=7 then taking n//2 items from n array will give us 4th item directly, before including any items from m array. Hence, u has to be capped at k at max;  so we'll do u=min(k,n). In addition to these 2 cases we have incorporate only 1 more change that cut2 is now made k - cut1.
import math

class Solution:
    def kthElement(self, arr1, arr2, n, m, k):
        if n > m: return self.kthElement(arr2, arr1, m, n, k)  # Additional optimisation to always run binary sort on smaller sized array
        lower, upper = max(0, k - m), min(k, n)
        while True:
            cut1 = (lower + upper) // 2
            cut2 = k - cut1

            l1 = -math.inf if cut1 == 0 else arr1[cut1 - 1]
            l2 = -math.inf if cut2 == 0 else arr2[cut2 - 1]
            r1 = math.inf if cut1 == n else arr1[cut1]
            r2 = math.inf if cut2 == m else arr2[cut2]

            if l1 <= r2 and l2 <= r1:
                return max(l1, l2)
            elif l1 > r2:
                upper = cut1 - 1
            else:
                lower = cut1 + 1


S = Solution()
print(S.kthElement([7, 10, 11, 28, 31, 49, 70], [6, 8, 9, 13, 14, 19, 20, 22], 7, 8, 9))
# print(S.kthElement([7, 10, 11, 28, 31, 49, 70], [6, 8, 9, 13], 7, 4, 9))
# TC: log(min(m,n))
# SC: O(1)