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
# Approach1: Median meaning finding the center most number in range of number which are sorted.
class Solution:
    def findMedian(self, A):
        OneDArr=[]
        for i in range(len(A)):
            for j in range(len(A[0])):
                OneDArr.append(A[i][j])
        OneDArr.sort()
        mid=len(OneDArr)//2
        return OneDArr[mid] #N*M is odd as mentioned in constraint, spares us from otherwise having to think what to show as median for say Arr=[1,3,7,9]

S = Solution()
print(S.findMedian([[1, 3, 5],
                    [2, 6, 9],
                    [3, 6, 9]]))
# TC: O(MN + MNlogMN) Explanation: Iterating through N numbers for M Times yields MN. Plus sorting the array takes MNlogMN
# SC: O(MN) Explanation: OneDArr stores MN items


# Approach2: In an n*m array i.e. [[1, 3, 7],[2, 7, 9],[3, 7, 9]] median could only be a number which has more than (n*m)//2 count of items from the given Array which are less than or equal to the current number. For eg: from 2D array consider 2 to be median. As there are only (n*m)//2=> 9//2=> 4 and 2 has only 2 instances where it items are equal or lesser than it, 2 cant be median. Similarly, 3 has 4 number satisfying this condition which as is not greater than (n*m)//2 i.e.4, 3 also cant be median. With this condition 7,8,9 could all be medians, as in the given array the number of items less than or equal to them are greater than (n*m)//2. Intuition is to find the first number, if we were checking in a sorted given array, which will satisfy the median condition and is present in the given Array too which for the given example will be 7. For achieving this we can find highest and lowest number from given array and for all the numbers in between including highest and lowest, check count of items satisfying median condition. The first number where condition is met we'll start checking if this number is present in givenArray. Given that 1<= A[i] <=10^9 for 10^9 which is constant we can run for loop wherein each time nm items would be traversed yielding nm TC. Or this is where we could kick in Binary Search to identify the exact spots where the condition is met. Finding mid-point of high and low which is highest and lowest number by default, we'll see if that number satisfies condition of median. If so we'll move the high to mid-1 to see if new mid will also satisfy median condition. If it does not we'll shift low to mid+1. At the point low becomes greater than high we return the number pointed by low. Guarantee for the returned low to have been existing in the given Array comes from the fact how in above example for 3 if median condition wasn't met, so won't it if mid was 4,5, and 6. As these number are not present and hence no difference would be created in count of items for them satisfying the median condition, their counts will stay same as count of last present number before them. In such case low would kept being increased then mid. Eventually high and low will catch up. And as they do, as high always ensures the items above it are the ones that meet median condition and low ensures items below it don't satisfy condition, we know from there the next item i.e.above high is first item to satisfy median condition and it is returned.
class Solution:
    def findMedian(self, A):
        rows, cols = len(A), len(A[0])
        l = u = A[0][0]
        for i in range(rows):
            for j in range(cols):
                if l > A[i][j]: l = A[i][j]
                if u < A[i][j]: u = A[i][j]

        while l <= u:
            mid = (l + u) // 2  # Binary search on range of all numbers from lowest to highest items in given Arr
            if countInstances(A, mid, cols, rows) <= (rows * cols) // 2:
                l = mid + 1
            else:
                u = mid - 1
        return l


def countInstances(Arr, number, totcolS, totRows): #As rows are sorted, we'll use Bin search, where we'll identify spot from where numbers are higher than given number.
    totCt=0
    for i in range(totRows):
        low, high = 0, totcolS - 1
        while low <= high:
            mid = (low + high) // 2
            if Arr[i][mid] <= number:
                low = mid+1
            else:
                high = mid-1
        totCt += low
    return totCt


S = Solution()
print(S.findMedian([[1, 3, 5],
                    [2, 6, 9],
                    [3, 6, 9]]))
print(S.findMedian([
  [1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3]
]))
# TC: O(nlog(m)) given n rows and m columns Explanation: for range of numbers equivalent to difference between the highest and lowest variables, we'll call countInstances which will run binary search on subArr of length m for n times. Given constraints minimum could be an item 1 in given array and max could be 10^9. So that makes worst case TC for us as O(10^9 * nlogm) but as 10^9 is constant and Time Complexity is used to see how algorithm grows to take more time as array size increases, here that makes 10^9 irrelevant to be included. Hence TC=nlongm
# SC: O(1)