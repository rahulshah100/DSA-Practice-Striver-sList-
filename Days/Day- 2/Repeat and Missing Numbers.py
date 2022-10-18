# https://www.interviewbit.com/problems/repeat-and-missing-number-array/
# You are given a read only array of n integers from 1 to n.
# Each integer appears exactly once except A which appears twice and B which is missing.
# Return A and B.
# Note: Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
# Note that in your output A should precede B.
# Example: Input:[3 1 2 5 3]  Output:[3, 4]
# ------------------------------------------------------------------------------------
# Approach 1: Using hashmap to store count.
class Solution:
    # @param A : tuple of integers
    # @return a list of integers
    def repeatedNumber(self, A):
        hashmap = [0] * (len(A) + 1)
        for i in A:
            hashmap[i] += 1
        for j in range(len(hashmap)):
            if hashmap[j] == 0:
                missing = j
            if hashmap[j] == 2:
                repeat = j
        return ([repeat, missing])


S = Solution()
print(S.repeatedNumber([3, 1, 2, 5, 3]))
# Time Complexity: O(2n). Explanation: n time for storing items in the hashmap. Important: len(hashmap) takes O(1) time as array object has a property called __len__ and hence that directly gives out the length. That is why in the 2nd for loop j in range(len(hashmap)) would take n time, reponsible for only getting j traversed through len(hashmap), or else if len(hashmap) had time complexity O(n), here our j loop would have O(n^2) time complexity. Thus, summing up the time complexities of two for loops we have final Time Complexity as O(n).
# Space Complexity:O(n). Explanation: Space taken by hashmap.


# Approach2: Better Space, compromised Time Complexity.
# Use merge sort to sort array. Traverse the sorted array from range(0, n-1). In every iteration compare if array[i+1]==array[i]+1. If not then if array[i+1]==array[i+1] or if array[i+1]==array[i]+2, then we can respectively say to have found the repeating and missing elements which are array[i+1] and array[i]+1 respectively.
# Time Complexity: O(nlogn + n). Explanation: mergesort taking nlogn and then n time to traverse the array to compare the adjacent element, which ultimately helps finding repeating and missing item.
# Space Complexity: O(1).


# Approach3: Reduced time and space complexity. As we are given that the array of size n has numbers from 1 to n, with just one repeating and one missing number, we can find sum of numbers from 1 to n for eg:For A=[3,1,2,5,3] size is 5, we'll do summation of all numbers from 1 to n i.e.[1,2,3,4,5] and subtract given array from this one i.e.[1,2,3,4,5]-[3,1,2,5,3]; If we sort out the equation by cancelling the number from left array with the right array we have 4-3. Here 4 is the missing in given array and 3 is recurring one. But cancelling the same numbers would require a for loop traversing through both the arrays and comparing the elements, we might even have to sort the given array for easier comparision, which will all increase the time complexity, hence we'll generalize the above equation and will directly evaluate without having to check for cancelling the same elements i.e. how here X-Y=1. Further we can do X^2-Y^2 and evaluate that, and from there on we can do substitution and cancellation amongst given equation to reach the value of X & Y.
class Solution:
    # @param A : tuple of integers
    # @return a list of integers
    def repeatedNumber(self, A):
        sumOfA = 0
        sumOfA2 = 0
        n = 0
        # In one loop finding the linear sum and squared sum of all elems of given array.
        for a in A:
            sumOfA2 += a * a
            sumOfA += a
            n += 1
        # Note: here we are not using a for loop but a formula to find the sum of 1 to n items or else this would have increased the total time complexity by O(n).
        sumOfN = n * (n + 1) / 2
        sumOfN2 = n * (n+1) * ((2*n)+1)/2

        XminY=sumOfN - sumOfA

        # X2minY2 could be written as (XplusY)(XminY). Which further leads to below written equation.
        XplusY=(sumOfN2-sumOfA2)/XminY

        # Now XminY + XplusY will give 2X, hence we get X as
        X=(XminY+XplusY)/2

        # X-Y=XminY. So Y=X-XminY
        Y=X-XminY
        return([X, Y])


S = Solution()
print(S.repeatedNumber([3, 1, 2, 5, 3]))
# Time Complexity: O(n) given that the size of A is n. Only one for loop traversal will contribute into time complexity,and it runs for n time.
# Space Complexity: O(1)