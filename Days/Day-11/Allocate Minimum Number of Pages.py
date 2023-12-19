# https://www.interviewbit.com/problems/allocate-books/

# Problem Description
# Given an array of integers A of size N and an integer B. The College library has N books.The ith book has A[i] number of pages. You have to allocate books to B number of students so that the maximum number of pages allocated to a student is minimum.
# A book will be allocated to exactly one student. Each student has to be allocated at least one book. Allotment should be in contiguous order, for example: A student cannot be allocated book 1 and book 3, skipping book 2. Calculate and return that minimum possible number.
# NOTE: Return - 1 if a valid assignment is not possible.

# Problem Constraints
# 1 <= N <= 105
# 1 <= A[i], B <= 105

# Input Format The first argument given is the integer array A. The second argument given is the integer B.
# Output Format Return that minimum possible number.

# Example Input Input 1: A = [12, 34, 67, 90] B = 2
# Example Output Output 1: 113

# Input 2: A = [5, 17, 100, 11] B = 4
# Output 2: 100 Example Explanation

# Explanation 1: There are two students.Books can be distributed in following fashion: 1)  [12] and [34, 67, 90] Max number of pages is allocated to student 2 with 34 + 67 + 90 = 191 pages 2)[12, 34] and[67, 90] Max number of pages is allocated to student 2 with 67 + 90 = 157 pages 3)[12, 34, 67] and[90] Max number of pages is allocated to student 1 with 12 + 34 + 67 = 113 pages Of the 3 cases, Option 3 has the minimum pages = 113.
# --------------------------------------------------------------------------------------------------------------------------------------------
# Approach1: Problem is minimizing the maximum pages alloted to a student given B number of students. So for [12, 34, 67, 90] the case where we are given 4 students we can minimze our maximum allocation as 90 pages. In case there are more than 4 students we return -1. In case we have less than 4 students say only 1 student, we have to allot all the pages 12+34+67+90 i.e. 203 to him. Thus, we can see range of allotment falling between max(arr) to sum(arr). In this case range is 90-203, and assuming each value could be possible answer, we run a for-loop over range(90,204) and verify if the value is correct. To verify current value say i in this for loop, we run a nested for-loop which counts number of students required if at max i pages can be alloted to 1 student. So continuing the above used example as we iterate from 12 to 34 our total pages are less than 90 and totStudentCt is 1. As we encounter 67 it can't be added to 12,34 or else 90 is crossed, and so we allot 67 to new student making totStudentCt as 2. Further for 90, 67+90 crosses 90 and so we need one more student making totStudentCt as 3. The process of using a for-loop over range(90-203) can be replaced with Binary Search as an optimization coz 90-203 is in a sorted way how we're gonna traverse it.
class Solution:
    def books(self, A, B):
        if B > len(A):
            return -1

        u = l = 0
        for i in range(len(A)):
            if A[i] > l: l = A[i]
            u += A[i]

        while l <= u:
            mid = (l + u) // 2
            ct = 1
            sum = 0
            for i in range(len(A)):
                if sum + A[i] > mid:
                    sum = A[i]
                    ct += 1
                else:
                    sum += A[i]
            if ct <= B: #As we want to minimize pages so in case a page threshold satisfies number of student criteria, we still try checking for a lesser total of pageNumbers. Thus when failed we know we have came down from a threshold and the current one failed so the next one must satisfy, and hence as l is incremented at the end as case will fail, l will always have answer and thus we return it in end
                u = mid - 1
            else:
                l = mid + 1
        return l


S = Solution()
print(S.books([73, 58, 30, 72, 44, 78, 23, 9], 5)) #110
print(S.books([12, 34, 67, 90], 2)) #113
print(S.books([ 97, 26, 12, 67, 10, 33, 79, 49, 79, 21, 67, 72, 93, 36, 85, 45, 28, 91, 94, 57, 1, 53, 8, 44, 68, 90, 24 ], 26)) #97
print(S.books([ 87, 3, 27, 29, 40, 12, 3, 69, 9, 57, 60, 33, 99 ], 3)) #192
# TC: O(nlog(sum(A)-max(A))) where n is book is length of A
# SC: O(1)
