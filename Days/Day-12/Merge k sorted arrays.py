# https://www.codingninjas.com/studio/problems/merge-k-sorted-arrays_975379

# You have been given ‘K’ different arrays/lists, which are sorted individually (in ascending order). You need to merge all the given arrays/list such that the output array/list should be sorted in ascending order.

# Detailed explanation
# Input Format:
# The first line of input contains an integer T, the number of test cases.
# The first line of each test case contains an integer that denotes the value of K.
# The next 2*K lines of each test case follow:
# The first line contains an integer ‘N’ denoting the size of the array.
# The second line contains N space-separated integers.
# Output Format:
# The first and only line of output contains space-separated elements of the merged and sorted array, as described in the task.

# Note: You don’t have to print anything; it has already been taken care of. Just implement the function.

# Constraints:
# 1 <= T <= 5
# 1 <= K <= 5
# 1 <= N <= 20
# -10^5 <= DATA <= 10^5
# Time Limit: 1 sec

# Sample Input 1:
# 1
# 2
# 3
# 3 5 9
# 4
# 1 2 3 8
# Sample Output 1: 1 2 3 3 5 8 9
# Explanation of Sample Input 1:
# After merging the two given arrays/lists [3, 5, 9] and [ 1, 2, 3, 8], the output sorted array will be [1, 2, 3, 3, 5, 8, 9].

# Sample Input 2:
# 1
# 4
# 3
# 1 5 9
# 2
# 45 90
# 5
# 2 6 78 100 234
# 1
# 0
# Sample Output 2: 0 1 2 5 6 9 45 78 90 100 234
# Explanation of Sample Input 2:
# After merging the given arrays/lists [1, 5, 9], [45, 90], [2, 6, 78, 100, 234] and [0], the output sorted array will be [0, 1, 2, 5, 6, 9, 45, 78, 90, 100, 234].
# -------------------------------------------------------------------------------------------------------------------------------------------
# Approach1: merge all items of all arrays into one and then sort this one
def mergeKSortedArrays(kArrays, k:int):
    resArr=[]
    for i in range(k):
        for j in range(len(kArrays[i])):
            resArr.append(kArrays[i][j])
    resArr.sort()
    return resArr

print(mergeKSortedArrays([[3, 5, 9],[ 1, 2, 3, 8]], 2))
# TC: O(k*n + (k*n)log(k*n)) given k is number of subArrays within kArrays and n is average elements in each of that subarray  Explanation: k*n time taken in total, to traverse in the nested for-loops to append all the items in resArr and then to sort the array of k*n sized  k*nlog(k*n) Time utilized
# SC: O(n) Explanation: Creating a newArray resArr which is intermediate one as it is sorted upon, and not directly returned and hence it adds onto space complexity


# Approach2: Better Space and Time - As given arrays are sorted individually, we'll use minheap to store 1st element from each subArray, and pop the top into an ansArr which we later return. As an item is popped we add the next item from that very subArray. For achieving this i.e. knowing which subArray's what item to push next we keep track of these parameters by pushing a triplet in minHeap instead of single item. The triplet will have valueOfItem, subArrIndexFromWhichItWasPicked, arrIndexOfItemWithinThisSubArr. As all items are popped out of minHeap, we return the ansArr.
import heapq

def mergeKSortedArrays(kArrays, k: int):
    minHeap = []
    ansArr = []
    for i in range(k):
        heapq.heappush(minHeap, (kArrays[i][0], i, 0))
    while len(minHeap):
        item, arrInd, itemInd = heapq.heappop(minHeap)
        ansArr.append(item)
        if itemInd+1 < len(kArrays[arrInd]):
            heapq.heappush(minHeap, (kArrays[arrInd][itemInd + 1], arrInd, itemInd + 1))
    return ansArr

print(mergeKSortedArrays([[3, 5, 9], [1, 2, 3, 8]], 2))
# TC: O(2nklogk) given k is number of subArrays within kArrays and n is average elements in each of that subarray  Explanation: the while loop runs for n*k times as it will run for all the items of all the subArrays, within which we perform heappush and heappop on a size k minHeap, hence both of these operations will take logk i.e. n*k * 2logk which gives the mentioned TC.
# SC: O(k) Explanation: ansArr is directly used to be returned and hence is excluded from space, apart from which minHeap at anytime only stores 1 item from each subarray and given k subArrays minheap's size is k