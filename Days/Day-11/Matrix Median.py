# https://www.interviewbit.com/problems/matrix-median/

# Problem Description
# Given a matrix of integers A of size N x M in which each row is sorted. Find and return the overall median of matrix A.
# NOTE: No extra memory is allowed.
# NOTE: Rows are numbered from top to bottom and columns are numbered from left to right.

# Problem Constraints
# 1 <= N, M <= 10 ^ 5
# 1 <= N * M <= 10 ^ 6
# 1 <= A[i] <= 10 ^ 9
# N * M is odd

# Input Format: The first and only argument given is the integer matrix A.
# Output Format: Return the overall median of matrix A.

# Example1:
# A = [[1, 3, 5],
#      [2, 6, 9],
#      [3, 6, 9]]
# Output: 5
# Example Explanation: A = [1, 2, 3, 3, 5, 6, 6, 9, 9] Median is 5. So, we return 5.

# Example2: A = [[5, 17, 100]]
# Output: 17
# Explanation: Median is 17.
# ------------------------------------------------------------------------------------------------------------------------------------
# Note: Median meaning finding the number before and after which we'll have equal items present

# Approach1: Make a 1D array from the given N*M dimensional array, and sort it to later return the middle item.
class Solution:
    def findMedian(self, A):
        OneDArr = []
        for i in range(len(A)):
            for j in range(len(A[0])):
                OneDArr.append(A[i][j])
        OneDArr.sort()
        mid = len(OneDArr) // 2
        return OneDArr[
            mid]  # N*M is odd as mentioned in constraint, spares us from otherwise having to think what to show as median for say Arr=[1,3,7,9]


S = Solution()
print(S.findMedian([[1, 3, 5],
                    [2, 6, 9],
                    [3, 6, 9]]))


# TC: O(MN + MNlogMN) Explanation: Iterating through N numbers for M Times yields MN. Plus sorting the array takes MNlogMN
# SC: O(MN) Explanation: OneDArr stores MN items


# Approach2: Intuition: If we discover highest and lowest item in the given matrix then using binary search we can keep searching for numbers for which the count of items in array which are either equal or lesser than this number are m*n//2 items. Now it could happen that for [[1, 3, 7],[2, 7, 9],[3, 7, 9]] lowest=1, highest=9 and mid==5. While checking for 5 we discover 1,3,2,3 i.e. 4 numbers are there lesser or equal to 5 which are present in array which is equal to row*col//2 => 3*3//2 => 4 and hence it meets median condition yet still we could have 4 which is the case here which could also satisfy median condition. Thus even after meeting median condition we'll let binary search play out up-till l<=u condition violates. If you notice 5 or 4 which condition satisfies is not even in array but eventually as we let binary search continue, we'll come to 3 from 4 and after which l<=u will violate. Thus, always we'll converge at an item present before l<=u violates. To keep track of lastMedian we found we use an extra variable and return this once binary search is over.
class Solution:
    def findMedian(self, A):
        lowest = highest = A[0][0]
        for i in range(len(A)):
            for j in range(len(A[0])):
                if A[i][j] < lowest: lowest = A[i][j]
                if A[i][j] > highest: highest = A[i][j]

        l, u = lowest, highest
        lastMedian = None
        while l <= u:
            mid = (l + u) // 2
            count = 0
            for i in range(len(A)):
                for j in range(len(A[0])):
                    if A[i][j] <= mid:
                        count += 1
            if count > (len(A) * len(A[0])) // 2:
                lastMedian = mid
                u = mid - 1
            else:
                l = mid + 1
        return lastMedian


A = [[1, 3, 5],
     [2, 6, 9],
     [3, 6, 13]]
S = Solution()
print(S.findMedian(A))
# TC: O(nm + mnlog(maxItemInArr-minItemInArr)) where n is row and m is columns. Explanation: nm to traverse and find highest and lowest. Further, for this range between highest and lowest we'll do binary search which takes log(maxItemInArr-minItemInArr) time. In each binary search iteration we're traversing whole array i.e. mn to find count, so it becomes mnlog(maxItemInArr-minItemInArr) for every binary search iteration.
# SC: O(1)


# Approach3: Improvement to Approach 2. We'll do 2 optimization 1) Avoid using lastMedian and instead return l 2) Taking advantage of fact that each row is sorted, we'll not use 2 for loops but binary search on it. To expand on point 1 we notice that l is incremented in case mid is not found to meet the median condition and u is decremented in case median is found. Thus, we're always making sure onto left of l-pointer we have all and only those numbers which passes the median condition, and starting l-pointer we have numbers with corresponding counts greater than (m*n)//2. Similarly with u-pointer we decrement it whenever nums[u] is meeting median, thus making sure u and onto its left no items meet median condition. Thus, here we return nums[l] as first number to meet median condition, and it's the same as to writing nums[u+1]. To expand on 2, we'll use a loop to traverse us in rows and in each row we'll use binary search to find the sweet spot below which items are lesser or equal to current item, and we'll add this count for each row.
class Solution:
    def findMedian(self, A):
        lowest = highest = A[0][0]
        for i in range(len(A)):
            for j in range(len(A[0])):
                if A[i][j] < lowest: lowest = A[i][j]
                if A[i][j] > highest: highest = A[i][j]

        l, u = lowest, highest
        while l <= u:
            mid = (l + u) // 2
            if self.count(mid, A) > (len(A) * len(A[0])) // 2:
                u = mid - 1
            else:
                l = mid + 1
        return l

    def count(self, num, A):
        totCt = 0
        for i in range(len(A)):
            l, u = 0, len(A[0]) - 1
            while l <= u:
                mid = (l + u) // 2
                if A[i][mid] > num:
                    u = mid - 1
                else:
                    l = mid + 1
            totCt += l  # Note: To discover why l is added, dry run a case or two Eg: where 14 is number lesser or equal to which we're looking for in [13, 15, 17, 19] we'll find l is always giving the answer. Alternatively, l is only how it works and not even mid+1. Coz for last time when mid is found and after which l increments and l<=u is violated; then mid+1 is fine as it is equal to l. But when mid is discovered & further u decrements to violate the condition, mid+1 will give wrong answer in that case as it'll be an index one more than l. Basically with l we're making sure to increment it in the case a smaller number is encountered and so it always ends up barring the smaller entries under it.
        return totCt

A = [[1, 3, 5],
     [2, 6, 9],
     [3, 6, 13]]
S = Solution()
print(S.findMedian(A))
# TC: O(nm + log(nm)log(maxItemInArr-minItemInArr)) Main difference than approach2 here is that instead of nm time in each BS iteration it'll be log(nm)
# SC: O(1)
