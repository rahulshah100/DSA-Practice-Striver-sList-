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
# Approach1: Brute Force- Power Set Method. For a given array of n length, the total possible subsets are always 2^n. Now to find all these unique 2^n subsets we can refer to the binary representations of 2^n numbers, starting from 0. Referring to these binary representations, for each representation the positions of their one would be synonymous to picking up items from that spot in the given array to make one subset. For eg for arr=[12,31,6] we'll have 2^3=8 subarrays possible. Starting from 0 to 6, we have these 8 numbers there whose binary representation will suggest fashion to pick items from array. For eg: number 6 is 110. This says pick 1st and 2nd item from array. To satisfy this approach in code we'll use two for loops, outer one representing 2^n numbers and inner one selecting elems from array in accordance to current number. In inner for loop we'll use the left shift operator to shift 1 by those many indices, to get array indices in a comparable form with current number chosen. So for j=0, 1<<j will be 001, and j=1=> 1<<j=010 while j=2=> 1<<j=> 100. Further we'll compare these left-shifted values with current number using a bitwise '&-Operator' to see whether we a 1, in which case it means the number has to be picked. For eg: i=6=110 when subjected to '&' with 001, 010, and 100 will give 0,1,1 meaning 2nd and 3rd item are picked
class Solution:
    def subsetSums(self, arr, N):
        resultArr = []
        for i in range(2 ** N):
            sum = 0
            for j in range(N):
                if 0 != (i & (1 << j)): #Here '&' is bitwise AND and '<<' is left shift operator #For eg: for an arr=[12,31,6] at the 4th iteration of pointer-i, i=3 i.e. i=011 and j will be 0,1, and 2. So 1<<j will be 001, 010, and 100. Now i & 1<<j means 011&001, 011&010, 011&100 which will give 1,1,0 meaning array's 0th and 1st items could be selected
                    sum += arr[j]
            resultArr.append(sum)
        return resultArr

S = Solution()
print(S.subsetSums([5, 2, 1],3))
# TC: O(n * 2^n) Explanation: The outer for loop runs for 2^n times wherein for each iteration, the inner one runs for n times.
# SC: O(1) Explanation: No extra space apart from the inevitable one used for storing the output arr is consumed.


# Approach2: Improved TC. Starting with a resulant Array that has a 0 by default and iterating over the Given Array, wherein for each iteration we'll sum up all the items of resultant Array with item pointed by current iteration in Given Array and append these additional items in resultant Array.
"""class Solution:
    def subsetSums(self, arr, N):
        resltantArr=[0]
        for i in range(N):
            for j in range(len(resltantArr)):
                resltantArr.append(resltantArr[j]+arr[i])
        return resltantArr

S = Solution()
print(S.subsetSums([5, 2, 1], 3))"""
# TC: O(n^2)
# SC: O(1) Explanation as there is no extra space apart from the inevitable one used to store what's as a whole a data structure which is gonna be returned


# Approach3: Using recursion. Starting from N-1th index we'll run a recursive function call to a function which takes index and sum as it's params. Each recursive call will once include the array item at current index in sum and once it wont. Thus once picking and once not picking the the current index item, we'll decrement the index uptill it becomes -1 where the whole array has essentially been traversed and in terms of recursive call we're at the end of the call chain and so this is where we store the sum in a resultant Array and return out of function call. For eg: for [4,1,7] picked and not picked items tree will be like
#                                                4,1,7
#     items=                   7                                            NP
#                     1,7              7                         1                      NP
#                4,1,7    1,7       4,7  7                  4,1     1               4        NP
# ------------------------------------return 0 (Base/Termination Condition)---------------------------------
class Solution:
    def __init__(self):
        self.resArr = []

    def subsetSums(self, arr, N):
        def temp1(index, sum):
            if index==-1:
                self.resArr.append(sum)
                return
            # Pick
            temp1(index-1, sum+arr[index])
            # Dont Pick
            temp1(index-1, sum)
        temp1(N-1, 0)
        return self.resArr

S = Solution()
print(S.subsetSums([5, 2, 1], 3))
# TC: O(2^n) Explanation: Don't confuse this with merge sort where the tc is nlogn. In merge sort (n/2)logn were total number of recursive calls and nlogn was time for merging. Of essence here is number of recursive calls of merge sort which can be generalized as nlogn. So if we see recursive tree of merge sort we'll notice at each step we kept reducing total length by half uptill length once became 1, so there within logn levels we had our business done. Here we are not halving the work having to be done in every step uptill we reach index -1 but we are going one step after other that is a difference of 1 instead of half is inflicted in this case. So that's about depth of recursion. If we were to talk of width, we know in merge at max width is of n/2 recursive calls or generalizing it as n happens. But here will we have only n i.e.3 outcomes from above eg of  4,1,7?! No, we have 8 outcomes. So this is case where at each recursive call our task is getting doubled inside each one which will further be doubled. Hence this is case of depth n where in each recusive calls task gets doubled so a total of 2^n recursive calls are made. If in each recursive call task increased by n folds it'd be a case of n^n TC.
# SC: O(n) Explanation: Stack Space. At max the depth of recursive tree will be n. As stack space only gets counted towards the running function and rest function calls are said to minimized, at worst O(n) stack space will be consumed. Sparing the calculation of inevitable space to store 2^n item which will be returned, our total SC is O(n)