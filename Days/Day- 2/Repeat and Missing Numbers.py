# https://www.interviewbit.com/problems/repeat-and-missing-number-array/
# You are given a read only array of n integers from 1 to n.
# Each integer appears exactly once except A which appears twice and B which is missing.
# Return A and B.
# Note: Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
# Note that in your output A should precede B.
# Example: Input:[3 1 2 5 3]  Output:[3, 4]
# ------------------------------------------------------------------------------------
# Approach 1: Using Array hashmap to store count.
class Solution:
    # @param A : tuple of integers
    # @return a list of integers
    def repeatedNumber(self, A):
        hashmap = [0] * (len(A) + 1)
        for i in A:
            hashmap[i] += 1
        for j in range(
                len(hashmap)):  # Important: len(hashmap) takes O(1) time as array object has a property called __len__ which directly gives out the length
            if hashmap[j] == 0:
                missing = j
            if hashmap[j] == 2:
                repeat = j
        return ([repeat, missing])


S = Solution()
print(S.repeatedNumber([3, 1, 2, 5, 3]))
# Time Complexity: O(3n). Explanation: n time for creating the hashmap filled with 0s. n time for storing items in the hashmap. n more time for the second for loop. We have final Time Complexity as O(3n).
# Space Complexity:O(n). Explanation: Space taken by hashmap.


# Approach2: Storing in Dictionary HashMap and then Looping. Improved TC
"""
class Solution:
    def repeatedNumber(self, A):
        hashMap = {}
        repeat = notPresent = None
        for i in range(len(A)):
            if A[i] in hashMap: #NOTE: in python, hashmap lookup in such format takes O(1) TC while array lookup takes O(n) TC
                repeat = A[i]
                break
            hashMap[i] = True
        for i in range(1, len(A) + 1):
            if i not in hashMap:
                notPresent = i
                break
        return [repeat, notPresent]
"""


# TC: O(2n) #NOTE: How we didn't have to initialize dictionary hashmap with 0s like we had to with Array hashmap
# SC: O(n)


# Approach3: Improved SC, decremented TC- Sorting and then looping
# Use merge sort to sort array. Traverse the sorted array from range(0, n-1). In every iteration compare if array[i+1]==array[i]+1. If not then if array[i+1]==array[i+1] or if array[i+1]==array[i]+2, then we can respectively say to have found the repeating and missing elements which are array[i+1] and array[i]+1 respectively.
# Time Complexity: O(nlogn + n). Explanation: mergesort taking nlogn and then n time to traverse the array to compare the adjacent element, which ultimately helps finding repeating and missing item.
# Space Complexity: O(1).


# Approach4: Reduced time and space complexity. As we are given that the array of size n has numbers from 1 to n, with just one repeating and one missing number, we can find sum of numbers from 1 to n for eg:For A=[3,1,2,5,3] size is 5, we'll do summation of all numbers from 1 to n i.e.[1,2,3,4,5] and subtract given array from this one i.e.[1,2,3,4,5]-[3,1,2,5,3]; If we sort out the equation by cancelling the number from left array with the right array we have 4-3. Here 4 is the missing in given array and 3 is recurring one. But cancelling the same numbers would require a for loop traversing through both the arrays and comparing the elements, we might even have to sort the given array for easier comparison, which will all increase the time complexity. Hence we'll generalize the above equation and will directly evaluate without having to check for cancelling the same elements i.e. how here X-Y=1. Further we can do X^2-Y^2 and evaluate that, and from there on we can do substitution and cancellation amongst given equation to find the individual value of X & Y.
class Solution:
    def repeatedNumber(self, A):
        n = len(A)

        SumA = A[0]
        SumASq = A[0] * A[0]
        for i in range(1, len(A)):
            SumA += A[i]
            SumASq += A[i] * A[i]

        SumIdealA = (n * (n + 1)) // 2
        SumSqIdealA = (n * (n + 1) * ((2 * n) + 1)) // 6

        XminY = SumIdealA - SumA  # Where X denotes the missing and Y denotes the repeating number #---(1)
        XSqminYSq = SumSqIdealA - SumASq
        XPlusY = XSqminYSq // XminY  # --(2) #NOTE: We couldnt have directly done addition of SumA and SumIdealA to get XPlusY becasuse X and Y denotes the repeating and  missing number repsectively and not simply addition/operation performed on any 2 Arrays. It just so happens to be that in case of XminY and XSqminYSq we'll be getting the left numbers as X and Y, X^2 and Y^2 respectively as during difference the rest of the numbers are cancelled out

        X = (XminY + XPlusY) // 2
        Y = XPlusY - X

        return [Y, X]


S = Solution()
print(S.repeatedNumber([3, 1, 2, 5, 3]))
# Time Complexity: O(n) given that the size of A is n. Only one for loop traversal will contribute into time complexity,and it runs for n time.
# Space Complexity: O(1)
