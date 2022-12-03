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
# Approach1: Basically this question is a find max intersection happening for any range, given n ranges. For a train if it's times are given in format: (start,end) and if at the station, the entire schedule for the day is like [(1,5),(3,4),(4,5),(6,8),(7,9)] then in this case we can say for 1,5's range we have 4,5 as conflicting. For 3,4 we have 4,5 conflicting and for 4,5 we have 1,5 and 3,4 conflicting making it an intersection of total 3 items. For 6,7 and 7,9 there are no intersections. So here max intersection is the platform we need to have i.e.3. We'll sort the given train arrival times and will reflect that sorting in the train's departure time. Further we'll create an array of size 2361 filled with 0's. Now for each train time, for the arrival time of that train we'll increase the count in that index of our newly created array by 1, which will show now it has gotten occupied i.e. from 0 train there initially to now there being +1 train. For the same train's departure time, as it is given 'same platform can not be used for both departure of a train and arrival of another train' hence we'll decrease the count stored at the index=departureTime+1 meaning that from this time one less train is there. After the entire schedule is jotted in array like this, we'll just do prefixSum of all the items in an array, which will show for each index i.e.time how many trains are using it. We'll return max value from this array now.

class Solution:
    # Function to find the minimum number of platforms required at the
    # railway station such that no train waits.
    def minimumPlatform(self, n, arr, dep):
        times = []
        for i in range(len(arr)):
            times.append([arr[i], dep[i]])

        times.sort(key=lambda x: x[0])

        day = [0 for _ in range(2361)]  # we are taking 2361 as for hashmap or prefixList to store item at nth index there should be n+1 items only then we'll have nth index,as indexing is not from 1 to n but 0,n. Hence here given constraint is max time could be 2359 to store which we'll need 2360 size in prefixSumList. Further #--1 could have us checking for 2360th index, to check which our day array must have 2361 items.

        for i in range(len(times)):
            day[times[i][0]] += 1
            day[times[i][1] + 1] -= 1 #--1

        max = -1
        for i in range(1, 2361):
            day[i] += day[i - 1]
            if day[i] > max:
                max = day[i]
        return max
# TC: O(n+nlogn+2361+n+2360) Explanation: n time for putting arr and dep items in times. nlogn times for sorting times. 2361 Constant Time for creating day with 2361 prefilled 0s. for filling day according to times array, n time is taken. 2360 Constant Time for loop from 1,2361 range in the last for loop. This total TC can be generalized as O(nlogn)
# SC: O(2n+2361) Explanation: times will store n arr-items and n dep-items making it 2n. Plus day will store 2361 items. Ignoring constants, Space Complexity is 2n