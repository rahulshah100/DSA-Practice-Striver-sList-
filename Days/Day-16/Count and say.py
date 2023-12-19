# https://leetcode.com/problems/count-and-say/

# The count-and-say sequence is a sequence of digit strings defined by the recursive formula:
# countAndSay(1) = "1"
# countAndSay(n) is the way you would "say" the digit string from countAndSay(n-1), which is then converted into a different digit string.
# To determine how you "say" a digit string, split it into the minimal number of substrings such that each substring contains exactly one unique digit. Then for each substring, say the number of digits, then say the digit. Finally, concatenate every said digit.
# For example, the saying and conversion for digit string "3322251":
# Given a positive integer n, return the nth term of the count-and-say sequence.

# Example 1:
# Input: n = 1
# Output: "1"
# Explanation: This is the base case.
# Example 2:
# Input: n = 4
# Output: "1211"
# Explanation:
# countAndSay(1) = "1"
# countAndSay(2) = say "1" = one 1 = "11"
# countAndSay(3) = say "11" = two 1's = "21"
# countAndSay(4) = say "21" = one 2 + one 1 = "12" + "11" = "1211"

# Constraints:
# 1 <= n <= 30
# ----------------------------------------------------------------------------------------------------------------------------------------
# Approach1: Iterative approach - where for given n we'll create 1,2,...n type of strings on top of earlier one. Call these as resStr. For each time to create resStr of higher n we'll use an empty string say temp, and traverse the existing resStr where we compare current item with next and if they match a counter is incremented. As soon as they don't match the counter and current item of resStr that's being traversed gets stored in temp. Counter is then reassigned to 1 for counting the next different item of resStr. An exception to this traversal is when we encounter the last item where to compare we won't have any next item, and we directly store the existing counter and the current Item in temp. At the end of this traversal temp holds the new resStr and hence resStr gets re-assigned to temp
class Solution:
    def countAndSay(self, n: int) -> str:
        resStr = "1"
        for i in range(n - 1):
            temp = ""
            ct = 1
            for j in range(len(resStr)):
                if j != len(resStr) - 1:
                    if resStr[j] == resStr[j + 1]:
                        ct += 1
                    else:
                        temp += str(ct) + resStr[j]
                        ct = 1
                else:
                    temp += str(ct) + resStr[j]
            resStr = temp
        return resStr


S = Solution()
print(S.countAndSay(1))
print(S.countAndSay(2))
print(S.countAndSay(3))
print(S.countAndSay(4))
print(S.countAndSay(5))
# TC: O(m*n) considering n to be the input parameter and m to be average length of string at each iteration
# SC: O(2m) Explanation: m is average length of string and is the space consumed by temp and resStr. As resStr is not direcly returned it cant be exempted from being counted as used space with an excuse that it's the space required to store answer.