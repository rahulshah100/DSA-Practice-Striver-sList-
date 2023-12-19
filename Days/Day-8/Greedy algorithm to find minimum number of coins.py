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
# Approach1: We will have a denominations array sorted descendingly, for our agenda to keep no. of coins minimum. Further from given amount we'll keep deducting the highest denomination if the subtraction is 0 or a number greater, alongside keeping a counter incremented for each time deduction happens. Once the sum is not bigger or equal to zero, we'll check for next denomination.
denominations = [1000, 500, 100, 50, 20, 10, 5, 2, 1]

def findMinimumCoins(amount):
    ct = i = 0
    while amount:
        if amount-denominations[i]>=0:
            ct += 1
            amount -= denominations[i]
        else:
            i += 1
    return ct

print(findMinimumCoins(70))
# TC: O(n)
# SC: O(1)