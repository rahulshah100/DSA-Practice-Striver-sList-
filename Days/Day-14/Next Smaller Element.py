# https://www.interviewbit.com/problems/nearest-smaller-element/

# Given an array, find the nearest smaller element G[i] for every element A[i] in the array such that the element has an index smaller than i.

# More formally,
# G[i] for an element A[i] = an element A[j] such that
# j is maximum possible AND
# j < i AND A[j] < A[i]
# Elements for which no smaller element exist, consider next smaller element as -1.

# Input Format
# The only argument given is integer array A.
# Output Format
# Return the integar array G such that G[i] contains nearest smaller number than A[i].If no such element occurs G[i] should be - 1.

# For Example
# Input1:
# A = [4, 5, 2, 10, 8]
# Output1:
# G = [-1, 4, -1, 2, 2]
# Explaination1:
# index1: No element less than 4 in left of 4, G[1] = -1
# index 2: A[1] is only element less than A[2], G[2] = A[1]
# index 3: No element less than 2 in left of 2, G[3] = -1
# index 4: A[3] is nearest element which is less than A[4], G[4] = A[3]
# index 4: A[3] is nearest element which is less than A[5], G[5] = A[3]

# Input2:
# A = [3, 2, 1]
# Output2:
# [-1, -1, -1]
# Explaination2:
# index 1: No element less than 3 in left of 3, G[1] = -1
# index 2: No element less than 2 in left of 2, G[2] = -1
# index 3: No element less than 1 in left of 1, G[3] = -1
# -------------------------------------------------------------------------------------------------------------------------------------------
# Approach1: Use nested for loops where outer one traverses the givenArray left to right and inner one traverses for the selected item, all the items on its left up-till first smaller item is encountered in which case the smaller item is stored in an ansArr. If we exhaust the array while inner for-loop looks for smaller-item we identify this with our j-pointer having became 0 and in addition when even at 0th index in givenArr the item available is smaller than the one pointed by outer for-loop; in such case we append -1.
class Solution:
    def prevSmaller(self, A):
        ansArr = [-1] #So down below in for-loop we can skip i=0th iteration coz for it j=i-1 became -1 and gave error
        for i in range(1,len(A)):
            for j in range(i - 1, -1, -1):
                if A[j] < A[i]:
                    ansArr.append(A[j])
                    break
            if j == 0 and A[j] >= A[i]:
                ansArr.append(-1)
        return ansArr

S = Solution()
print(S.prevSmaller([4, 5, 2, 10, 8]))
# TC: O(n^2)
# SC: O(1)

# Approach2: Improved Time but compromised SC - Because we see for an item the last smaller item before it is the one preferred over any farther smaller item, this is a LIFO problem where we can use a stack. We traverse given array from left to right and maintain a stack sorted from starting to end in ascending order. New item is compared with top of stack and stack is popped till we find an item smaller than current one or if stack becomes empty. Accordingly, we fill answer in ansArr and append in the stack the current item
class Solution:
    def prevSmaller(self, A):
        stack, ansArr = [], []
        for i in range(len(A)):
            while stack and stack[-1] >= A[i]:
                stack.pop()

            if not stack:
                ansArr.append(-1)
            else:
                ansArr.append(stack[-1])

            stack.append(A[i])
        return ansArr

S = Solution()
print(S.prevSmaller([34, 35, 27, 42, 5, 28, 39, 20, 28]))
# TC: O(2n) Explanation: for-loop takes n time inside which the while loop that runs could at worst for all collective iterations could run for n more times
# SC: O(n) Explanation: stack occupies n space in worst case