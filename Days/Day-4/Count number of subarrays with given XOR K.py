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
# Return the total number of subarrays having bitwise XOR equals to B.

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
# The subarrays having XOR of their elements as 6 are:
# [4, 2], [4, 2, 2, 6, 4], [2, 2, 6], [6]
# Explanation 2:
# The subarrays having XOR of their elements as 5 are [5] and [5, 6, 7, 8, 9]
#-----------------------------------------------------------------------
# Approach1: Computing for all possible subarrays if XOR could result in the target value i.e.B. If so, we'll keep a track of count of items for that subarray. We'll output the highest count value
class Solution:
    def solve(self, A, B): #Note: & is bitwise and, | is bitwise or, ^ is bitwise XOR in python. In case of XOR, if a and b are not same in the value then like a=1 and b=0 or a=0 and b=1, then only we'll get the output as 1 otherwise we'll get 0.
        count=0
        for i in range(len(A)):
            XOR=A[i]
            for j in range(i+1,len(A)):
                if XOR==B:
                    count=max(count,j-i+1)
                XOR^=A[j]
        print(count)
        return count

# S = Solution()
# S.solve([4, 2, 2, 6, 4],6)
# print(S.solve([5, 6, 7, 8, 9],5))
# Time Complexity: O(n^2)
# Space Complexity:O(1)

# Approach2: Here we'll take advantage of fact that with xor, if a^b=c (i.e. a xor b is c) then c^b=a (c xor b will be equal to a), as 6^4==>0110^0100=>0010 i.e. 2 and 2^4=>0010^0100=>0110 i.e. 6. We'll create a prefix XOR array (i.e. at each index of the list, we'll store a cumulative xor of all items before and the one present on that index). Now for each iteration in the prefixArray, if we assume that item:b (target item to be found) is always present somewhere prior to index we're checking for, then we can say that a^b=c will hold true with b as given in question. In th a^b=c we can get c for each index from the prior created prefix array. Hence as we have item:b and c, if we are just able to find the existence of item:a in prefix array, prior to the index we're checking for in the given array, we can say the equation is satisfied and our presumption of b item being there is true for that iteration. In that case we'll sum up in a count variable, all the total occurences of item:a as for those many times item:b will be also there. On the other hand if while traversing, if the item we're looking for is present as it is in prefix Array, then we'll directly add one to count variable; if not, we will store it in a seperate lookupTable. To maintain this lookUp Table we'll use a dictionary with key as items and it's values as item's count. We'll return the count variable as output.
class Solution:
    def solve(self, A, B):
        prefixXOR = []
        prefixXOR.insert(0, A[0])
        for i in range(1, len(A)):
            prefixXOR.insert(i, A[i] ^ prefixXOR[i - 1])

        loopupTable = {}
        count = 0
        for i in range(len(prefixXOR)):
            if prefixXOR[i] == B:
                count += 1

            if prefixXOR[i] ^ B in loopupTable:
                count += loopupTable[prefixXOR[i] ^ B]

            if prefixXOR[i] in loopupTable: #Dictionary lookup in general case should be of a O(1) Time Complexity.
                loopupTable[prefixXOR[i]] += 1
            else:
                loopupTable[prefixXOR[i]] = 1
        print(loopupTable,prefixXOR)
        return count

S = Solution()
print(S.solve([4, 2, 2, 6, 4], 6))
print(S.solve([5, 6, 7, 8, 9], 5))
# Time Complexity: O(2n) Explanation: two for loops
# Space Complexity: O(3n) Explanation: 2n space for dictionary and n space for prefix Array

# Approach2 Improved implementation:
class Solution:
    def solve(self, A, B):
        lookupTable={}
        xor=0
        count=0
        for i in range(len(A)):
            xor ^= A[i]

            if xor ^ B in lookupTable:
                count += lookupTable[xor ^ B]

            if xor == B:
                count += 1

            if xor in lookupTable:
                lookupTable[xor] += 1
            else:
                lookupTable[xor] = 1
        return count
S = Solution()
print(S.solve([4, 2, 2, 6, 4],6))
print(S.solve([5, 6, 7, 8, 9],5))
# Time Complexity: O(n) Explanation:one for loop
# Space Complexity:O(2n) Explanation: Just a dictionary taking O(2n) space.