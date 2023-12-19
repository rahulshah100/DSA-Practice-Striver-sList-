# https://www.codingninjas.com/studio/problems/aggressive-cows_1082559?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf

# Problem Statement
# Detailed explanation ( Input/output format, Notes, Images )
# Sample Input 1 :
# 6 4
# 0 3 4 7 10 9
# Sample Output 1 :
# 3
# Explanation To Sample Input 1 : The maximum possible minimum distance between any two cows will be 3 when 4 cows are placed at positions {0, 3, 7, 10}. Here distance between cows are 3, 4 and 3 respectively.

# Sample Input 2 :
# 5 2
# 4 2 1 3 6
# Sample Output 2 :5

# Expected Time Complexity: Can you solve this in O(n * log(n)) time complexity?

# Constraints :
# 2 <= 'n' <= 10 ^ 5
# 2 <= 'k' <= n
# 0 <= 'arr[i]' <= 10 ^ 9
# Time Limit: 1 sec.
# -------------------------------------------------------------------------------------------------------------------------------------------
# Approach1: The question is to maximize the minimum distance between cows. Our range of distance possible between cows can be from (SecondMinOfStalls - MinOfStalls, to MaxOfStalls). So we run a binary search on this range, and for the mid of which we keep checking in a nested for-loop whether mid i.e. the distance, is a possible one between 2 stalls. For this we assume that 1).the givenArr is sorted which in our case isn't and so we sort, 2)that first cow is placed on very 1st stall, and so we already keep a count variable with value 1 showing how many cows have been place along with lastStallInd variable as 0 showing the last index from where Stall has been picked. Thus now to make this work we in nested for-loop we exclude 0th index and check for rest of stalls item, checking that difference between current index and lastStallInd is greater or equal to mid, which if so we update lastStall as current item and increase count by 1. Thus when ct gets calculated, it is compared with given k and if ct is greater or equal to k then it means, we could accommodate the required cows with mid distance. As we want to maximize distance we increase mid by making l as mid+1. Thus, we always know l has excluded the answer and that at the end u will decrease by 1 and therefore keep the answer and so we return u at the end.
def aggressiveCows(stalls, k):
    if k > len(stalls):
        return -1

    stalls.sort()
    l, u = stalls[1]-stalls[0], stalls[-1] - stalls[0]
    while l <= u:
        mid = (l + u) // 2
        lastStallInd = 0
        ct = 1
        for i in range(1, len(stalls)):
            if stalls[i] - stalls[lastStallInd] >= mid:
                ct, lastStallInd = ct + 1, i
        if ct >= k:
            l = mid + 1
        else:
            u = mid - 1
    return u


print(aggressiveCows([0, 3, 4, 7, 10, 9], 4))
# TC: O(nlogn + nlog(max(stalls)-min(stalls))) given that n is length of given array
# SC: O(1)