# https://practice.geeksforgeeks.org/problems/minimum-platforms-1587115620/1#

# Minimum Platforms
# Given arrival and departure times of all trains that reach a railway station. Find the minimum number of platforms required for the railway station so that no train is kept waiting.
# Consider that all the trains arrive on the same day and leave on the same day. Arrival and departure time can never be the same for a train but we can have arrival time of one train equal to departure time of the other. At any given instance of time, same platform can not be used for both departure of a train and arrival of another train. In such cases, we need different platforms.

# Example 1:
# Input: n = 6
# arr[] = {0900, 0940, 0950, 1100, 1500, 1800}
# dep[] = {0910, 1200, 1120, 1130, 1900, 2000}
# Output: 3
# Explanation: Minimum 3 platforms are required to safely arrive and depart all trains.

# Example 2:
# Input: n = 3
# arr[] = {0900, 1100, 1235}
# dep[] = {1000, 1200, 1240}
# Output: 1
# Explanation: Only 1 platform is required to safely manage the arrival and departure of all trains.

# Your Task: You don't need to read input or print anything. Your task is to complete the function findPlatform() which takes the array arr[] (denoting the arrival times), array dep[] (denoting the departure times) and the size of the array as inputs and returns the minimum number of platforms required at the railway station such that no train waits.

# Note: Time intervals are in the 24-hour format(HHMM) , where the first two characters represent hour (between 00 to 23 ) and the last two characters represent minutes (this may be > 59).

# Expected Time Complexity: O(nlogn)
# Expected Auxiliary Space: O(n)

# Constraints:
# 1 ≤ n ≤ 50000
# 0000 ≤ A[i] ≤ D[i] ≤ 2359
# -----------------------------------------------------------------------------------------------------------------------------------------
# Approach1: Sorting the arr, and corresponding entries of dep would follow. For this I am merging both arrays into multiple sub-arrays each with a pair of arr, dep time and storing whole thing into a new arr. The new arr is sorted based on key as first value of its items. Further I split back sorted sub-arrays into arr and dep arrays. After this we run a nested for loop to check for each entry if there are any prev entries which have their departure after or at time of current one's arrival which if so we keep a local counter and increment it by 1. To keep track of max local, we use a globCt which is returned at the end.
"""class Solution:
    def minimumPlatform(self, n, arr, dep):
        globCt = 1
        mixedDict=[]
        for i in range(n):
            mixedDict.append([arr[i],dep[i]])
        mixedDict.sort(key=lambda x: x[0])

        for i in range(n):
            arr[i],dep[i]=mixedDict[i][0],mixedDict[i][1]

        for i in range(n):
            locCt = 1
            for j in range(i):
                if arr[i] <= dep[j]:
                    locCt += 1
            globCt = max(globCt, locCt)
        return globCt

S = Solution()
print(S.minimumPlatform(10,[41,1616,297,2042,1013,987,2050,525,636,109], [2275,2076,1580,2144,1231,1672,2137,1016,2234,1043]))"""
# TC: O(2n + nlogn + n^2) Explanation: Total Tc is n + n + nlogn + n(1 + 2 +...n-1) i.e. 2n + n(n+1)/2 => giving worst TC as n^2
# SC: O(2n) Explanation: For using mixedDict to store n extra items each of which is 2 integers.


# Approach2: In constraints the departure is mentioned to possibly be equal or later, but never before corresponding arrival. We'll sort departure and arrival time seperately and will traverse through arrival times. After that we'll traverse both arrays using 'a' and 'd' pointer respectively, before either of the pointers run out on the entire length of it's corresponding array. In each iteration we'll compare dep of 'd' index to be equal to or greater than arr at 'a' index. If true, it means the train at d index has not departed as train at 'a' index arrived. So we'll increase a counter and check for next arr time by incrementing 'a' pointer. Conversely, in else-statement we'll free a platform by decrementing the counter, alongside increment 'd' pointer. To keep track of max value counter reaches, we'll use a globalCounter.
class Solution:
    def minimumPlatform(self, n, arr, dep):
        arr.sort()
        dep.sort()

        a, d = 0, 0
        ct = maxCt = 0
        while a < n and d < n:
            if dep[d] >= arr[a]:
                ct += 1
                a += 1
                maxCt = max(maxCt, ct)
            else:
                ct -= 1
                d += 1
        return maxCt
S=Solution()
# print(S.minimumPlatform(6,[1, 3, 0, 5, 8, 5],[2, 4, 6, 7, 9, 9]))
print(S.minimumPlatform(4,[900, 915, 945, 1015], [930,1000,1030,1045]))
# TC: O(2nlogn + 2n) Explanation: 2n is what while loop will take in worst case where 'd' is traversed full lenght and so is 'a', and 2nlogn is to sort the two arrays.
# SC: O(1)