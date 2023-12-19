# https://practice.geeksforgeeks.org/problems/largest-subarray-with-0-sum/1

# Given an array having both positive and negative integers. The task is to compute the length of the largest subarray with sum 0.

# Example 1: Input:
# N = 8
# A[] = {15,-2,2,-8,1,7,10,23}
# Output: 5
# Explanation: The largest subarray with sum 0 will be -2 2 -8 1 7.

# Your Task: You just have to complete the function maxLen() which takes two arguments an array A and n, where n is the size of the array A and returns the length of the largest subarray with 0 sum.

# Expected Time Complexity: O(N).
# Expected Auxiliary Space: O(N).

# Constraints:
# 1 <= N <= 10^5
# -1000 <= A[i] <= 1000, for each valid i
# ----------------------------------------------------------------------------------------------------------------------------------------------------------
# NOTE: SUBARRAY WORD WITHOUT EXPLICIT SPECIFICATION IMPLY CONSECUTIVE ELEMS ONLY, FROM PARENT ARRAY
# Approach1: Compute for all possible sub-arrays and if their total is 0, keep a note of their count of items. From all such counts, output the highest.
class Solution:
    def maxLen(self, n, arr):
        maxCt = 0
        for i in range(len(arr)):
            tot = currCt = 0
            for j in range(i, len(arr)): #Above we could've made tot=arr[i] and here taken j from i+1 but then in case like [0] where ans should be len=1 as 0 is an elem which could be a solo-subarray giving a total of 0. Because i+1 will make j=1 our inner loop will never run and maxCt is never updated. Thus we had an edge case.
                tot += arr[j]
                currCt += 1
                if tot == 0:
                    maxCt = max(maxCt, currCt)
        return maxCt

S=Solution()
S.maxLen(8,[15,-2,2,-8,1,7,10,23])
# Time Complexity: O(n^2) Explanation: 2 nested for loops
# Space Complexity: O(1)


# Approach2: Creating a Prefix Sum Table. Trick: By this point we should have noticed that in array question whenever we've had 2 for loops, we could use a hashmap to replace a for-loop. So instead of an inner for-loop helping the outer-for loop refer all the upcoming items. We can refer a hashmap for past item by creating a prefix table.
# Under 2 scenario we can find new maxLen 1) where at some point the whole array sums upto 0. 2) In between the array or some part of array sums upto 0. Here we'll iterate over the given array in one for loop adding all items to total. Thus, as we are constantly getting total of whole array 1) is taken care of. For 2) what we're using is an idea that say uptill index 3 i.e. 3rd iteration of for loop we had total of x and moving forward with iterations if total at 7th iteration again comes upto be exactly x then it must mean that all items between 7th and 3rd index cancells each other out. So when that happens we get some part of array or in-between array which handles 2). To handle this 2) as we iterate, we'll store new total and index at which we found the total in a dictionary hashmap. Every new iteration we check if that total has been stored in hashmap, in which case we'll find diff. between the then index and current index where same total is fetched, to give us length of 0 sum subarray.
class Solution:
    def maxLen(self, n, arr):
        hashDict = {}
        globalCt = sum = 0
        for i in range(n):
            sum += arr[i]
            if sum == 0:
                globalCt = i + 1
            elif sum not in hashDict:
                hashDict[sum] = i
            else:
                globalCt = max(globalCt, i - hashDict[sum])
        return globalCt

S=Solution()
S.maxLen(8,[15,-2,2,-8,1,7,10,23])
# Time Complexity: O(n) Explanation: n time for traversal through the given array
# Space Complexity: O(n) Explanation: We are using an extra space for storing a diction hash map that will at worst store n keys and values.