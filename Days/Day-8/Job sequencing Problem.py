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
# Expected Auxiliary Space: O(N)

# Constraints:
# 1 <= N <= 10^5
# 1 <= Deadline <= 100
# 1 <= Profit <= 500
# -----------------------------------------------------------------------------------------------------------------------------------------------------------
# Approach1: sort the given Array in descending order of Profit. Iterate through the sorted array marking the deadline of the Job true in hashDictionary. If a deadline is already occupied i.e. a job is already scheduled, in which case we'll keep decrement the deadline by 1 and check if that day is vacant in hashDictionary. If a Job is being marked in hashDictionary then using an initially declared totProf and ct variable, we'll keep track of total Profit and count of Jobs we've executed. Return ct, totProf.
class Solution:
    def JobScheduling(self,Jobs,n):
        print(type(Jobs),type(Jobs[1])) #<class 'list'> <class '__main__.Job'>
        # Jobs = list(Jobs) #This wont work!! as Jobs is a list already but not it's sub items. They're a class/object
        # jobsArr=[] #We could either use this or #--1
        # for i in Jobs:
        #     jobsArr.append([i.id, i.deadline, i.profit])
        jobsArr=[[i.id,i.deadline,i.profit] for i in Jobs] #--1
        print('jobsArr',jobsArr)
        jobsArr.sort(key=lambda x: x[2], reverse=True)
        ct = totProf = 0
        hash = {}
        for i in range(len(jobsArr)):
            deadline = jobsArr[i][1]
            while deadline:
                if deadline not in hash:
                    hash[deadline] = True
                    ct += 1
                    totProf += jobsArr[i][2]
                    break
                elif deadline > 0:
                    deadline -= 1
        return ct, totProf

S = Solution()
print(S.JobScheduling({(1, 4, 20), (2, 1, 10), (3, 1, 40), (4, 1, 30)}, 4))
# TC: O(n+nlogn+n^2) Explanation: n for making jobArr. nlogn to sort jobArr. A for loop with inner while will consume a further n^2. This could be generalized to O(n^2)
# SC: O(2n) Explanation: n for each- jobArr and hash
