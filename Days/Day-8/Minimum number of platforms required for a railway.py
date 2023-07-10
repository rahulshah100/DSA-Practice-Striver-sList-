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

# Expected Time Complexity: O(nLogn)
# Expected Auxiliary Space: O(n)

# Constraints:
# 1 ≤ n ≤ 50000
# 0000 ≤ A[i] ≤ D[i] ≤ 2359
# ---------------------------------------------------------------------------------------------------------
# Approach1: In constraints the departure is mentioned to possibly be equal or later, but never before corresponding arrival. We'll sort departure and arrival time and will traverse through arrival times. We'll use an l variable to mark the last departure which we'll keep comparing while traversing the sorted arrival times. If departure pointed by l is before/lesser than current iteration's arrival then that will mean that platform has become vacant, in which case from an initially declared ct variable which is used to keep count of platforms-required-at-any-time the value will be decremented by 1. Further we'll continue comparing the further departures with same arrival time by incrementing l pointer by 1, uptill l is lesser than or equal to the index of current arrival time and uptill updated departures are also before the current arrival. Contradictingly if arrival time is before/lesser than departure pointed by l, it also has to be before the later departures as departure array is sorted and hence we'll increment ct by 1 indicating requirement of 1 more platform. In each iteration of arrival time we'll increment ct by 1 and compare the updated ct with a maxCt variable which keeps a track of max ct found. At the end maxCt will be returned.
class Solution:
    def minimumPlatform(self, n, arr, dep):
        arr.sort()
        dep.sort()
        l = ct = maxCt = 0
        for i in range(n):
            while arr[i] > dep[l] and l<=i: #in question it is specified if at same time a train has departed if an another comes, we have to provide seperate platform. Or here we would've used 'arr[i] >= arr[l]'. Also as by constraint: arrival and departure could be the same so we have to seek l uptill same value as i.
                ct -= 1
                l += 1
            ct += 1
            maxCt = max(maxCt, ct)
        return maxCt
S=Solution()
print(S.minimumPlatform(6,[1, 3, 0, 5, 8, 5],[2, 4, 6, 7, 9, 9]))
# TC: O(n+m) given arr and dep are of size n and m respectively.
# SC: O(1)