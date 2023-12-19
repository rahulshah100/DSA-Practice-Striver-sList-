# https://www.interviewbit.com/problems/maximum-sum-combinations/

# Given two equally sized 1-D arrays A, B containing N integers each. A sum combination is made by adding one element from array A and another element of array B. Return the maximum C valid sum combinations from all the possible sum combinations.

# Constraint:
# 1 <= N <= 10^5
# 1 <= A[i] <= 10^5
# 1 <= C <= N

# Input Format
# First argument is an one-dimensional integer array A of size N.
# Second argument is an one-dimensional integer array B of size N.
# Third argument is an integer C.

# Output Format: Return a one-dimensional integer array of size C denoting the top C maximum sum combinations.

# NOTE:The returned array must be sorted in non-increasing order.

# Example Input
# Input 1:
#  A = [3, 2]
#  B = [1, 4]
#  C = 2

# Input 2:
#  A = [1, 4, 2, 3]
#  B = [2, 5, 1, 6]
#  C = 4

# Example Output
# Output 1: [7, 6]
# Output 1:[10, 9, 9, 8]

# Example Explanation
# Explanation 1:
#  7     (A : 3) + (B : 4)
#  6     (A : 2) + (B : 4)

# Explanation 2:
#  10   (A : 4) + (B : 6)
#  9   (A : 4) + (B : 5)
#  9   (A : 3) + (B : 6)
#  8   (A : 3) + (B : 5)
# -------------------------------------------------------------------------------------------------------------------------------------------
# Approach1: Brute Force - we'll find summations for all corresponding elements of both arrays with each other, and store them in a maxHeap. Now for C times, we'll pop the maximum item out of it and store them in a list that is returned as the answer
import heapq

class Solution:
    def solve(self, A, B, C):
        maxHeap=[]
        resArr = []
        for i in range(len(A)):
            for j in range(len(B)):
                heapq.heappush(maxHeap,-(A[i]+B[j]))

        for i in range(C):
            resArr.append(-heapq.heappop(maxHeap))
        return resArr

S = Solution()
print(S.solve([1, 4, 2, 3], [2, 5, 1, 6], 4))
print(S.solve([3,2], [1,4], 2))
# TC: O((n^2+n)logn) Explanation: for n^2  times heappush will be ran where each time it'll take logn time. At worst C could be N, as given in constraints and so heap-pop will be ran for n times where each time it'll take logn time
# SC: O(n^2+n) Explanation: resArr can store n extra elements at worst and heapq will store n^2 additional elements


# Approach 2: Instead of storing all the possible combinations, we think of optimizing the algo to compute only necessary sums. For this we sort both the given arrays in Descending order. Now if we think of finding the top k combinations we know first is where from both arrays their 0th index is chosen. After this we can have 0th index of 1st array and 1st index of 2nd array giving the new highest, or it might as well be given by 1st index of 1st array and 0th index of 2nd array. If we understand this by an example:
# A = [6,3,2,1]
# B = [9,8,7,2]
# k = 4
# we picked i=0 and j=0 index from A and B arrays respectively i.e. items 6 and 9 giving a sum 15; thus we have 3 more greatest sums to find yet
# now we can get the highest sum by 1) i, j+1 i.e. 6 & 8 => 14 or 2) i+1, j i.e. 3 and 9 => 12   #------1
# Here we know 14 is highest; and now we have 2 more greatest sums to find; yet our i and j are updated here to reflect the picked pair i.e. i=0, j=1
# Further we have 1) i, j+1 i.e. 3 and 7 => 10 or 2) i+1, j i.e. 6 & 7 => 13; alongside from prev #----1 the unused possible pair giving us one more option 3) 3 and 9 => 12; to select max from amongst  #---2
# Thus we can see a pattern forming.
# TO implement this we can see we can use maxHeap to keep inserting new pairs which will -(A[i],B[j+1]) or -(A[i+1),B[j]) each time we can update the i and j from popped maxHeap item if we had i, and j index stored there too. This makes us think we could better store -( (A[i],B[j+1]), i, j+1 ) in maxHeap (YES, it is an allowed syntax for heappush where mainly based on 1st param, the items are arranged and in case two items have same value for 1st param then 2nd and later 3rd and so on other params are checked) and while retrieving the popped item we can use python's unpacking syntax i.e. sum, i, j = heap.pop(). Thus obtained sum would be stored in an ansArr that will be returned. We will do this in a for-loop that runs k times.
# Plus we can have one more issue which is that suppose we come across a case like #--2 where option 3 gets selected i.e. 3 and 9 are picked and i and j becomes 1, and 0 then although we'd have traversed i+1, j i.e. 2 and 0th index or i, j+1 i.e. 1, 1 index we will re-travel them and duplicate entries would be found in ansArr. To avoid this we'll store a pair of i and j in a set and every time check while storing i+1, j or i, j+1 that whether that combination is not already in the set.
import heapq

class Solution:
    def solve(self, A, B, C):
        A.sort(reverse=True)
        B.sort(reverse=True)
        maxHeap, ansArr = [], []
        visitedInd = set()

        heapq.heappush(
            maxHeap,
            (
                -(A[0] + B[0]),
                0,
                0
            )
        )
        visitedInd.add(tuple([0, 0]))

        for i in range(C):
            currMax, i, j = heapq.heappop(maxHeap)
            ansArr.append(-currMax)

            if i + 1 < len(A) and (i + 1, j) not in visitedInd:
                heapq.heappush(
                    maxHeap,
                    (
                        -(A[i + 1] + B[j]),
                        i + 1,
                        j
                    )
                )
                visitedInd.add(tuple([i + 1, j]))

            if j + 1 < len(B) and (i, j + 1) not in visitedInd: #Set lookup will take O(1) time
                heapq.heappush(
                    maxHeap,
                    (
                        -(A[i] + B[j + 1]),
                        i,
                        j + 1
                    )
                )
                visitedInd.add(tuple([i, j + 1]))

        return ansArr


S = Solution()
print(S.solve([1, 4, 2, 3], [2, 5, 1, 6], 4))
print(S.solve([3, 2], [1, 4], 2))

# TC: O(nlogn) Explanation: n+n i.e. 2n to sort array A and B. for loop runs C times which can at worst be n (as given in constraint), each time where we are doing 1 heapPop and 2 heapPush adding 3logn complexity and thus this part gives 3nlogn TC. Thus summing up we have 2n + 3nlogn i.e. generalized as nlogn
# SC: O(n) Explanation: We store 2 items in maxHeap per 1 for-loop iteration, and at worst where C is n we'll have such n iteration making maxHeap occupy 2n items. Similarly set Stores 2 coordinates per for-loop iteration and will have at max 2n items. Thus we can at max have 4n Space Complexity that is generalized as n.