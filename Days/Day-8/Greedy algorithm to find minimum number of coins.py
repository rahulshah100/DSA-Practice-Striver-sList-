# https://www.codingninjas.com/codestudio/problems/975277?topList=striver-sde-sheet-problems&utm_source=striver&utm_medium=website

# Find Minimum Number Of Coins
# Dora, the explorer, visits India and decides to try the famous Indian food. However, the restaurant accepts only Indian currency i.e. [1, 2, 5, 10, 20, 50, 100, 500, 1000] valued coins. So, Dora goes to a bank that has an infinite supply of each of the denominations to make a change for a given ‘Amount’ of money. As a cashier at the bank, your task is to provide Dora the minimum number of coins that add up to the given ‘Amount’.

# Examples:For Amount = 70, the minimum number of coins required is 2 i.e an Rs. 50 coin and a Rs. 20 coin.

# Input Format: The first line of input contains an integer 'T' representing the number of test cases or queries to be processed. Then the test case follows. The only line of each test case contains a single integer ‘Amount’ representing the amount Dora wishes to change to Indian currency.
# Output Format: For each test case, print the minimum number of coins needed to make the change. Print the output of each test case in a separate line.

# Constraints:
# 1 <= T <= 100
# 1 <= Amount <= 10^5
# Where 'T' is the number of test-cases
# Time Limit: 1sec

# Sample Input1:
#                 2
#                 13
#                 20
# Sample Output1:
#                 3
#                 1
# Explanation: For the First Test Case ,the minimum number of coins to make the change are 3 {1, 2, 10}. For the second Test Case, only one coin {20} is required.
# ------------------------------------------------------------------------
# Approach1:
denominations = [1, 2, 5, 10, 20, 50, 100, 500, 1000]

def findMinimumCoins(amount):
    count=0
    for i in range(len(denominations)-1,-1,-1):
        while amount-denominations[i]>=0:
            amount=amount-denominations[i]
            count+=1
    print(count)
    return count
findMinimumCoins(3,13,50,96)

# TC: O(amount) Explanation: If 50003 was to be given as input, then 1000 would be used 50 times and then we'll go from 500 to 100 to 50... uptill 2 and use 2 denomination once and then take a one. So it is clear, we'll do 50+8 iterations in this case. This can be for worst case generalized by O(amount)
# SC: O(1)