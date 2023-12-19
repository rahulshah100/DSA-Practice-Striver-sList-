# https://www.interviewbit.com/problems/subarray-with-given-xor/

# Subarray with given XOR
# Given an array of integers A and an integer B. Find the total number of subarrays having bitwise XOR of all elements equals to B.

# Problem Constraints
# 1 <= length of the array <= 10^5
# 1 <= A[i], B <= 10^9

# Input Format:
# The first argument given is the integer array A.
# The second argument given is integer B.
# Output Format:
# Return the total number of sub-arrays having bitwise XOR equals to B.

# Example Input
# Input 1:
#  A = [4, 2, 2, 6, 4]
#  B = 6
# Input 2:
#  A = [5, 6, 7, 8, 9]
#  B = 5

# Example Output
# Output 1:
# 4
# Output 2:
# 2

# Example Explanation
# Explanation 1:
# The sub-arrays having XOR of their elements as 6 are:
# [4, 2], [4, 2, 2, 6, 4], [2, 2, 6], [6]
# Explanation 2:
# The sub-arrays having XOR of their elements as 5 are [5] and [5, 6, 7, 8, 9]
#-----------------------------------------------------------------------
# In XOR operation integers are first off reduced into bit format i.e.4 => 0100 and 6=>0110, after which the same bits yield 0 and different bits yield 1.
#                               So, 0100                NOTE: XOR OF NUMBER WITH ZERO ALWAYS RETURNS THE SAME NUMBER: 0100
#                               XOR 0110                                                                         XOR  0000
#                             Gives ----                                                                              ----
#                                   0010 => 2                                                                         0100

# Approach1: Computing all possible subarrays and check for XOR of all them if it is target value i.e. B. In case of which, we'll keep a track of count.
class Solution:
    def solve(self, A, B):
        ct = 0
        for i in range(len(A)):
            xor = 0
            for j in range(i,len(A)):  # starting from i so we'll not miss first number in arr A if it is a solo XOR's answer
                xor ^= A[j]
                if xor == B:
                    ct += 1
        return ct

# S = Solution()
# print(S.solve([5, 6, 7, 8, 9],5))
# Time Complexity: O(n^2)
# Space Complexity:O(1)


# Approach2: Prefix XOR Method - Here we'll take advantage of how operators work. Consider Eg: if 9-6=3 then 6+3=9. So if question was where we were given a table of prefix sum count that stored total of all the elem of array uptill each index and say it shows total=9 at index=4, and if we're asked whether we had any subarray that will sum upto 6, what will we do? We'll check the prefix sum table to see if there is 3 at any point. If so from as many 3's we'll have, from those indexes uptill index=4 we can say we have a subarray that totals upto 6. Similarly with xor, if a^b=c we can also say c^b=a i.e if 6^4==>0110^0100=>0010=>2 then 2^4=>0010^0100=>0110=> 6. Using this idea, we'll here create a prefix XOR array i.e. for each elem in given array, we'll compute XOR of all the elems of and uptill that point and store these prefix xor's in a lookup table i.e. hashmap. Now while computing prefix array, at each iteration we'll the do prefix XOR's xor-operation with the target and will check if it's output is present in lookup table. If so, we will increment a counter variable by number of times the output is shown to have repeated as those many XORs are found too. We'll further update our prefix table with new xor value checking whether the value was already present, in which case we'll increment it's current count. If value wasnt present we'll now include it in lookup table, setting it to 1.
class Solution:
    def solve(self, A, B):
        dict = {0: 1} #This is base condition or prerequisite, or we'd have to include a one more if (not elif, but if) condition where xor==B as in #--1. It's like saying 9-0==9 that 9 is sum uptill 4th index and we are asked as target total of 9, and we start looking in lookup table if we had a 0 totalling entry.
        xor = ct = 0
        for i in range(len(A)):
            xor ^= A[i]
            # if xor==B: #--1
            #   ct+=1    #With this if, the below if-statement has to be an if only and not an elif coz of cases like [0, 5] target=5 where for second iteration i.e.index 1 the xor=5, so we do satisfy xor==B signifying [0,5] is an appropriate array but then so is the subarray [5] too i.e. xor ^ B i.e. 5^5 = 0 => is present in dict coz of 1st iteration, but we wont have checked this second condition itself should we not have both if-statements and not an if,elif statements.
            if xor ^ B in dict:
                ct += dict[xor ^ B]

            if xor in dict: #This is not in an else condition in conjunction to above because even when we find xor^B in dict, we'll want to store xor found at this point in our lookup table
                dict[xor] += 1
            else:
                dict[xor] = 1
        return ct
S = Solution()
print(S.solve([4, 2, 2, 6, 4],6))
# Time Complexity: O(n) Explanation: one for loop
# Space Complexity:O(n) Explanation: Just a dictionary taking O(n) space.