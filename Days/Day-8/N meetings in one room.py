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
# Explanation: Only one meetings can be held with given start and end timings.

# Your Task :
# You don't need to read inputs or print anything. Complete the function maxMeetings() that takes two arrays start[] and end[] along with their size N as input parameters and returns the maximum number of meetings that can be held in the meeting room.

# Expected Time Complexity : O(N*LogN)
# Expected Auxilliary Space : O(N)

# Constraints:
# 1 ≤ N ≤ 105
# 0 ≤ start[i] < end[i] ≤ 105
# ------------------------------------------------------------------------------------------------------------------------------------------------------------
# Note: Greedy Approach means just going through one way of approaching which seems to be making sense for and upto the first go and then we'll repeat that for all following iterations. Like here we could choose the meetings with smallest operating time and finish meetings in that order, or in order of their finishing times. We'll dry both the ways. Here executing meetings in their finishing order is making looking more efficient. However that might not be a case always. In such cases, where we dont have a straightforward way which is most efficient, we use Dynamic Programming which computes all the possibilities and acts accordingly. So this is what is meant by solving these questions by Greedy Approach.
# Approach1: For value of start and end belonging to one meeting, we'll store all such pairs in a hashList as one item. Further we'll sort the hashList according to the finishing time of the activities. From hashList we'll by default include the first item in our answer. Now we'll traverse hashList comparing the starting time of an item with the last item chosen in answer. If starting time comes after finish time of last item included in answer then we are good to include this item in answer.
class Solution:
        def maximumMeetings(self, n, start, end):
            hashList = []
            for i in range(len(start)):
                hashList.append([start[i], end[i]])
            hashList.sort(key=lambda x: x[1])

            result = [hashList[0]]
            for i in range(1, len(hashList)):
                if hashList[i][0] > result[-1][1]:
                    result.append(hashList[i])
            return len(result)
# TC: O(n+nlogn+n) Explanation: n for traversing given list to store the items in hashList, nlogn to sort hashList, n for traversing the hashList to fill the result array
# SC: O(2n) Explanation: hashList and result array both taking equivalent to n space.