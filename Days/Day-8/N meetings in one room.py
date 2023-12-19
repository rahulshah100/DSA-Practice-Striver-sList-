# https://practice.geeksforgeeks.org/problems/n-meetings-in-one-room-1587115620/1

# N meetings in one room
# There is one meeting room in a firm. There are N meetings in the form of (start[i], end[i]) where start[i] is start time of meeting i and end[i] is finish time of meeting i.
# What is the maximum number of meetings that can be accommodated in the meeting room when only one meeting can be held in the meeting room at a particular time?

# Note: Start time of one chosen meeting can't be equal to the end time of the other chosen meeting.


# Example 1:
# Input:
# N = 6
# start[] = {1,3,0,5,8,5}
# end[] =  {2,4,6,7,9,9}
# Output: 4
# Explanation: Maximum four meetings can be held with given start and end timings. The meetings are - (1, 2),(3, 4), (5,7) and (8,9)

# Example 2:
# Input:
# N = 3
# start[] = {10, 12, 20}
# end[] = {20, 25, 30}
# Output: 1
# Explanation: Only one meeting can be held with given start and end timings.

# Your Task :
# You don't need to read inputs or print anything. Complete the function maxMeetings() that takes two arrays start[] and end[] along with their size N as input parameters and returns the maximum number of meetings that can be held in the meeting room.

# Expected Time Complexity : O(N*LogN)
# Expected Auxiliary Space : O(N)

# Constraints:
# 1 ≤ N ≤ 105
# 0 ≤ start[i] < end[i] ≤ 105
# ------------------------------------------------------------------------------------------------------------------------------------------------------------
# Note: a greedy approach involves making locally optimal choices based on initial reasoning, while dynamic programming explores all possibilities to identify the most favorable solution. Like to solve this question we could've chosen approach of either sorting meetings with smallest operating time or in the order of their finish times. Greedy thinks only about first iteration which here will make it say if first one ends very soon there is scope for other more meetings to start later, while with sorting-based-on-operating-time approach the first go of selecting meeting with smallest operating time doesn't make much sense. So greedy will only think up-till first go and in this case it'll say sorting based on finishing time is the way to go. However, either of the approaches might not be optimal always. In such cases, where we don't have a straightforward optimal approach, we use Dynamic Programming which computes all the possibilities and acts accordingly. So this is what is meant by solving these questions by Greedy Approach.

# Approach1: Using an timeArr we'll store all the pairs of starting and ending times, each as one item. Further we'll sort the timeArr according to the ending times. Making 1st item of sorted timeArr as the one by default conducted, we'll now create a ct variable initialized to 1 and a lastMeetInd set to 0 which will keep record of index of timeArr from where the last included meeting has been taken. Now while traversing the sorted timeArr we'll start from 2nd item and compare if it's starting time of this item is after the ending time of item at lastMeetInd index which if so ct is incremented by 1 and we update lastMeetInd as the current index. We return ct at the end.
class Solution:
        def maximumMeetings(self, n, start, end):
            timeArr = []
            for i in range(n):
                timeArr.append([start[i], end[i]])
            timeArr.sort(key=lambda x: x[1])

            ct = 1
            lastMeetInd = 0
            for i in range(1, n):
                if timeArr[i][0] > timeArr[lastMeetInd][1]:
                    ct += 1
                    lastMeetInd = i
            return ct
# TC: O(n+nlogn+n) Explanation: n for traversing given list to store the items in timeArr, nlogn to sort timeArr, n for traversing the sorted timeArr to count meetings
# SC: O(n) Explanation: timeArr taking n space.