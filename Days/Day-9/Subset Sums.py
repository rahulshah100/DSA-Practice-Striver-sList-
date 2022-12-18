# https://practice.geeksforgeeks.org/problems/subset-sums2234/1

# Subset Sums: Given a list arr of N integers, print sums of all subsets in it.

# Example 1:
# Input: N = 2
#        arr[] = {2, 3}
# Output:0 2 3 5
# Explanation: When no elements is taken then Sum = 0. When only 2 is taken then Sum = 2. When only 3 is taken then Sum = 3. When element 2 and 3 are taken then. Sum = 2+3 = 5.

# Example 2:
# Input: N = 3
#        arr[] = {5, 2, 1}
# Output:0 1 2 3 5 6 7 8

# Your Task: You don't need to read input or print anything. Your task is to complete the function subsetSums() which takes a list/vector and an integer N as an input parameter and return the list/vector of all the subset sums.
# Expected Time Complexity: O(2^N)
# Expected Auxiliary Space: O(2^N)

# Constraints:
# 1 <= N <= 15
# 0 <= arr[i] <= 10^4
# ------------------------------------------------------------------------------------------------------------------------------------------------------------
# Approach1: Brute Force- Power Set Method. For a given array of n length, the total subsets which could be generated is always 2^n. Now to find all the unique 2^n subsets we can refer the binary representations of (2^n)-1 numbers, starting from 0. For example for arr=[1,2,3] the total possible subsets will be 2^3=4. The subset sums for 2^n items can be derived off of numbers from 0 to 7, where-in 0 integer in binary will be 000 and 1 will be 001 whereas 5 will be 101. Now, for all the bits, we can assign them an index number and associate that with index in array. So number 1 in bits will be 001 which shows 0th, 1st and 2nd index of the given array. Referring to this index, 001 can be interpreted as choosing 1 from the given array, 010 as 2, 001 as 3; 000 will be choosing no numbers from array and 101 will be 1+3. Thus we can find 2^n subset sums.
class Solution:
    def subsetSums(self, arr, N):
        n, answer = len(arr), []
        for i in range(2 ** n): #Goes from 0 to 2^n - 1, inferring to that number.
            sum = 0
            for j in range(n): #Signifies bits equivalent in numbers as to the index of the given array i.e. we can have 00 representation for i=0 or it could be 0000, which will depend of whether arr=[3,5] or arr=[3,5,6,7] i.e. where n=2 or n=4
                if 0 != (i & 1 << j): #Given that n=3, for i=3 we'll have 3's bit form as 011. In this step we're checking one after the other for all n=3 bits if they're 1. For j=0, 1<<j i.e.1BitwiseLeftShift0 is 1 i.e. 001. We'll here do 3BitwiseAnd001 i.e. 011BitwiseAnd001 which will give 001 which is not 0 and hence we'll pick the item at the zeroth index in given array and make it a part of the sum. For j=1 and 2, we'll check if 0!=011BitwiseAnd010 and 0!=011BitwiseAnd100 respectively.
                    sum += arr[j]
            answer.append(sum)
        return answer

S = Solution()
print(S.subsetSums([5, 2, 1],3))
# TC: O(n * 2^n) Explanation: The outer for loop runs for 2^n times wherein for each iteration, the inner for loop runs for n times.
# SC: O(1) Explanation: No extra space apart from the inevitable one which is used for storing the output arr is stored.

# Approach2: Using recursion. For the given array we'll prepare a recursive tree wherein starting from left, for once, that item would be made the part of the sum and for once it wont be. We'll move forward in both the cases making the same choice where in from here on i.e.once having the number selected once and once not, we'll select the next item for once and we'll not for once. When in doing this we reach the last item, we get out of the recursive function storing the final sum in an output array. For eg: for [4,1,7] tree will be like
#                                               4,1,7
#     items=                  4                              Nothing picked
#                    41             4                       N.P         1
#                417   41        47     4                   N.P      17     1
#     sum=       12     5        11     4                   0        8      1
class Solution:
    def subsetSums(self, arr, N):
        output=[]
        def func(index, sum):
            if index==N:
                output.append(sum)
                return
            # Pick ith item
            func(index+1, sum)
            # Dont Pick ith item
            func(index + 1, sum+arr[index])
        func(0,0)
        output.sort()
        return output

S = Solution()
# print(S.subsetSums([5, 2, 1], 3))
print(S.subsetSums([4,1,7], 3))
# TC: O(2^n + (2^n)log(2^n)) Explanation: As every item is considered picked once and not picked once, for n items 2^n times the recursive calls will happen. In each of the 2^n calls, one item would be made the part of output array, hence we'll have 2^n items in output, to sort which (2^n)log(2^n) time is required.
# SC: O(n) Explanation: Stack Space. As the implementation is such that at any given worst case, only all the n levels would be getting executed and out of them n-1 level will be holding recursive stack space making the total space required in stack as O(n-1). For eg: For 4,1,7 the function calls will be in following order for the first chain of recursion 4->4,1->4,1,7 for when 4,1,7 is executed only 4->4,1 i.e.2 function calls are taking stack space. From 4,1,7 we will trace back to 4->4,1 and will execute 4,1 where only 4 will be held in recursive space.