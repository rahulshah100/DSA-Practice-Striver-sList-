# https://www.interviewbit.com/problems/repeat-and-missing-number-array/
# You are given a read only array of n integers from 1 to n.
# Each integer appears exactly once except A which appears twice and B which is missing.
# Return A and B.
# Note: Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
# Note that in your output A should precede B.
# Example: Input:[3 1 2 5 3]  Output:[3, 4]
# ------------------------------------------------------------------------------------
# Approach 1: Using 2 for loop: Outer one to point to all items from 1 to n. For each of this iteration we'll check using inner for loop which will be iterating through given array, if item is found twice or missing
class Solution:
    def repeatedNumber(self, A):
        missing = twice = None
        for i in range(1, len(A)+1):
            hashDict, notFound = {}, True
            for j in range(len(A)):
                if i == A[j] and i not in hashDict:
                    hashDict[i] = 1
                    notFound = False
                elif i == A[j] and i in hashDict:
                    twice = i
            if notFound:
                missing = i
        return [twice, missing]
# TC: O(n^2)
# SC: O(n)


# Approach 2: Using Array hashmap to store count.
class Solution:
    # @param A : tuple of integers
    # @return a list of integers
    def repeatedNumber(self, A):
        hashmap = [0] * (len(A) + 1) #We can also use [0 for i in range(len(A) + 1)] to make a list of n size
        for i in A:
            hashmap[i] += 1
        for j in range(len(hashmap)):  # Important: len(hashmap) takes O(1) time as array object has a property called __len__ which directly gives out the length
            if hashmap[j] == 0:
                missing = j
            if hashmap[j] == 2:
                repeat = j
        return ([repeat, missing])

S = Solution()
print(S.repeatedNumber([3, 1, 2, 5, 3]))
# Time Complexity: O(3n). Explanation: n time for creating the hashmap filled with 0s. n time for storing items in the hashmap. n more time for the second for loop. We have final Time Complexity as O(3n).
# Space Complexity:O(n). Explanation: Space taken by hashmap.


# Approach3: Storing in Dictionary HashMap and then Looping. Improved TC
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


# Approach4: Improved SC, decremented TC
# Sort the array and traverse up-to last second item of array. Each time compare whether the next item is an increment to current item. If next is not an increment to current then is it a duplicate to the current? to check which we see if next item is equal to current even. If it is not even a duplicate we mark the not found item that is the incremented item: current + 1 to be missing. There are two edge cases here  where either the very first item of array is missing or it is the last one. 1) if very first item is missing the next we'll check could be an increment or duplicate and from there on we could have a proper incremental order, resulting in not finding the missing item at all. To overcome this we check for first iteration of for-loop when i=0 if first item in our sorted array is 1, which if not we mark 1 to be missing. 2)For case like ([1,2,2,3] or) [1,2,2] for first iteration 2 is an increment to 1 and we move to iteration 2, the next 2 is not an increment but is equal to this 2 hence a duplicate and then the loop ends as we take only uptill second last, coz for last item we cant compare it with it's next as there is no next. In such case missing stays None, so after for loop when we detect missing as None we make missing as last item+1
class Solution:
    def repeatedNumber(self, A):
        A = [i for i in A] #As what's given in question turns out to be a tuple which is immutable and hence to sort which we convert it to array
        A.sort()
        missing = twice = None
        for i in range(len(A) - 1):
            if i == 0 and A[i] != 1:
                missing = 1
            elif A[i + 1] != A[i] + 1 and A[i + 1] != A[i]:
                missing = A[i] + 1
            if A[i+1]==A[i]:
                twice=A[i]
        if missing == None:
            missing = A[-1] + 1
        return (twice, missing)
# Time Complexity: O(nlogn + n). Explanation: mergesort taking nlogn and then n time to loop over the array
# Space Complexity: O(1).


# Approach5: Reduced time and space complexity. As we are given that the array of size n has numbers from 1 to n, with just one repeating and one missing number, we can find sum of numbers from 1 to n for eg:For A=[3,1,2,5,3] size is 5, we'll do summation of all numbers from 1 to n i.e.[1,2,3,4,5] and subtract given array from this one i.e.[1,2,3,4,5]-[3,1,2,5,3]; If we sort out the equation by cancelling the number from left array with the right array we have 4-3. Here 4 is the missing in given array and 3 is recurring one. But cancelling the same numbers would require a for loop traversing through both the arrays and comparing the elements, we might even have to sort the given array for easier comparison, which will all increase the time complexity. Hence, we'll generalize the above equation and will directly evaluate without having to check for cancelling the same elements i.e. how here X-Y=1. Further we can do X^2-Y^2 and evaluate that, and from there on we can do substitution and cancellation amongst given equation to find the individual value of X & Y.
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
        XPlusY = XSqminYSq // XminY  # --(2) #NOTE: We couldn't have directly done addition of SumA and SumIdealA to get XPlusY because X and Y denotes the repeating and  missing number respectively and not simply addition/operation performed on any 2 Arrays. It just so happens to be that in case of XminY and XSqminYSq we'll be getting the left numbers as X and Y, X^2 and Y^2 respectively as during difference the rest of the numbers are cancelled out

        X = (XminY + XPlusY) // 2
        Y = XPlusY - X

        return [Y, X]


S = Solution()
print(S.repeatedNumber([3, 1, 2, 5, 3]))
# Time Complexity: O(n) given that the size of A is n. Only one for loop traversal will contribute into time complexity,and it runs for n time.
# Space Complexity: O(1)
