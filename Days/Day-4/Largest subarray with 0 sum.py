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
# Approach1: Compute for all possible subarrays if their total is 0; if so, keep a note of their count of items. From all such counts, output the highest.
class Solution:
    def maxLen(self, n, arr):
        i=0
        Count=0
        while i<n:
            total=arr[i]
            j=i+1
            while j<n:
                total+=arr[j]
                if total==0:
                    Count = max(Count, j-i+1)
                j+=1
            i+=1
        print(Count)
        return Count

S=Solution()
S.maxLen(8,[15,-2,2,-8,1,7,10,23])
# Time Complexity: O(n^2) Explanation: 2 nested while loops
# Space Complexity: O(1)

# Approach2: Using a dictionary as a hashmap. While traversing the given list, we'll maintain a sum of all the items till that point. At each iteration we'll check if the sum is 0. If sum is 0 we'll see the iteration at which we are, to find the total items that'd have contributed in making sum come upto 0, at this point. We'll keep the count of items when sum is 0. If sum is not 0, we'll check if in our hashmap that sum already exists, by checking the key values. If sum does not exist, we'll store the sum as key and current index/iteration as the value. If the key/sum exists we'll subtract the value (which means array index) of key where previously same sum was found, from the current value/iteration; this will give us the count of in between numbers before and after which we got a same nonzero sum. This in between numbers must add upto zero to mainatin before and after sum value as 0. We'll store this number of in between items in our count variable. We'll output the highest count value.
class Solution:
    def maxLen(self, n, arr):
        hashMap={}
        sum=0
        count=0
        for i in range(n):
            sum+=arr[i]
            if sum==0:
                count=i+1
            else:
                if sum in hashMap: #Note: Dictionary look up if the key are not same/very complex, happens in O(1) Time.
                    count=max(count, i-hashMap[sum])
                else:
                    hashMap[sum]=i
        print(count)
        return count

S=Solution()
S.maxLen(8,[15,-2,2,-8,1,7,10,23])
# Time Complexity: O(n) Explanation: n time for traversal through the given array
# Space Complexity: O(n) Explanation: We are using an extra space for storing a diction hash map that will at worst store n keys and values. SO in total 2n space is used extra. Generalizing O(2n) we can represent it as O(n).