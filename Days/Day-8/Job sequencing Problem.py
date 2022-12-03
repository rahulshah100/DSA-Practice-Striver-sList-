# https://practice.geeksforgeeks.org/problems/job-sequencing-problem-1587115620/1

# Job Sequencing Problem: Given a set of N jobs where each jobi has a deadline and profit associated with it.

# Each job takes 1 unit of time to complete and only one job can be scheduled at a time. We earn the profit associated with job if and only if the job is completed by its deadline. Find the number of jobs done and the maximum profit. Note: Jobs will be given in the form (Jobid, Deadline, Profit) associated with that Job.

# Example 1:
# Input:
# N = 4
# Jobs = {(1,4,20),(2,1,10),(3,1,40),(4,1,30)}
# Output: 2 60
# Explanation: Job1 and Job3 can be done with maximum profit of 60 (20+40).

# Example 2:
# Input:
# N = 5
# Jobs = {(1,2,100),(2,1,19),(3,2,27),(4,1,25),(5,1,15)}
# Output: 2 127
# Explanation: 2 jobs can be done with maximum profit of 127 (100+27).

# Your Task: You don't need to read input or print anything. Your task is to complete the function JobScheduling() which takes an integer N and an array of Jobs(Job id, Deadline, Profit) as input and returns the count of jobs and maximum profit as a list or vector of 2 elements.

# Expected Time Complexity: O(NlogN)
# Expected Auxilliary Space: O(N)

# Constraints:
# 1 <= N <= 10^5
# 1 <= Deadline <= 100
# 1 <= Profit <= 500
# -----------------------------------------------------------------------------------------------------------------------------------------------------------
# Approach1: We'll sort all the jobs in order of Profit from highest to lowest. We'll make a temp Array of Size of maximum deadline+1 amongst all given jobs, where in we'll mark days which are booked for performing a Job. We'll traverse sorted Jobs List and will place the jobs at the deadline, which if is occupied we'll move to a day prior to that, if that is also occupied, we'll check till the first item of temp Array created. As jobs are marked in tempArray we'll keep summing their profits, which at the ending we'll return.
class Solution:
    def JobScheduling(self, Jobs, n):
        jobsArr = []
        maxDeadline = 0
        for i in Jobs:
            jobsArr.append([i.id, i.deadline, i.profit])  # Jobs is given as an object, we are converting it into arr here so further it could be sorted easily.
            maxDeadline = max(maxDeadline, i.deadline)

        jobsArr.sort(key=lambda x: x[2], reverse=True)
        tempArr = [0 for _ in range(maxDeadline + 1)]
        count = 0
        totalProfit = 0

        for i in range(len(jobsArr)):
            for j in range(jobsArr[i][1] - 1, -1, -1): #Starting from the deadline of ith item in jobsArr, we'll check till the first item item in tempArr if we've vacant days. But if deadline is 1, and before 1 there should not be any more days like no 0th day; to get what here we wrote range(jobsArr[i][1] - 1, -1, -1). An alternate could have been range(jobsArr[i][1], 0, -1).
                if tempArr[j] == 0:
                    tempArr[j] += 1
                    count += 1
                    totalProfit += jobsArr[i][2]
                    break
        return [count, totalProfit]
# TC: O(n+nlogn + n*m) where n is number of jobs in the given array and m is longest deadline. Explanation: n to fill jobsArr and counting maxDeadline. nlogn to sort the given Jobs array, and n*m to check for n items, in tempArray from m to 0th index if an index is vacant.
# SC: O(m+1+n) Explanation: m+1 for tempArr and n for jobsArr