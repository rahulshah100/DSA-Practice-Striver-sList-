# https://leetcode.com/problems/roman-to-integer/

# Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
# For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

# Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:
# I can be placed before V (5) and X (10) to make 4 and 9.
# X can be placed before L (50) and C (100) to make 40 and 90.
# C can be placed before D (500) and M (1000) to make 400 and 900.
# Given a roman numeral, convert it to an integer.

# Example 1:
# Input: s = "III"
# Output: 3
# Explanation: III = 3.

# Example 2:
# Input: s = "LVIII"
# Output: 58
# Explanation: L = 50, V= 5, III = 3.

# Example 3:
# Input: s = "MCMXCIV"
# Output: 1994
# Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.

# Constraints:
# 1 <= s.length <= 15
# s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').
# It is guaranteed that s is a valid roman numeral in the range [1, 3999].
# ----------------------------------------------------------------------------------------------------------------------
# Approach1: We'll create 2 dictionaries first where keys are unconventional roman numbers such as IV, and IX where there values are corresponding conventional roman digits such as IIII and VIIII. Second dictionary holds translation of conventional roman digits as the key to simple digits as their values. In 2 for loops then we convert unconventional digits from given String to conventional ones, and conventional roman digits to simple digits which we keep summing up.
class Solution:
    def romanToInt(self, s: str) -> int:
        conversion = {
            "IV": "IIII",
            "IX": "VIIII",
            "XL": "XXXX",
            "XC": "LXXXX",
            "CD": "CCCC",
            "CM": "DCCCC"
        }

        romanToDigits = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        newStr, i = "", 0
        while i < len(s):
            if i < len(s) - 1 and s[i:i + 2] in conversion: #Much like in for loop form for(1,4) how 4 is omitted similarly in string last mentioned index gets omitted
                newStr += conversion[s[i:i + 2]]
                i += 2
            else:
                newStr += s[i]
                i += 1

        digit = 0
        for i in newStr:
            digit += romanToDigits[i]
        return digit

S = Solution()
print(S.romanToInt("MCMXCIV"))
# TC: O(2n)
# SC: O(n) #Explanation both dictionaries are constant space,and digit stores answer to be returned while newStr takes up n extra space


# Approach2: Improved Time and Space Complexity - As explained in question that only I being a smaller number can come in front of V and X, but V cant come in front of X because it's smaller than X. So it's just the rules of Roman numerals that you can't use “smaller letter just before bigger letter” not even to mean subtraction for any case except where the smaller letter is I in front of V and X, or X in front of L and C and C in front of D and M. So CM is a thing but VM is not a thing. Also, as constraint in the question mentions only valid roman numbers will be given in input, we can safely consider that whenever we encounter a smaller number in front of a larger number, it is still a valid number, and then if we look at conversion dictionary in approach1 it becomes clear that in these cases we can directly go on to subtract the smaller one from a total variable which thus keeps summing all the items and is returned at the end.
class Solution:
    def romanToInt(self, s: str) -> int:
        romanToDigits = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        total = 0
        for i in range(len(s)):
            if i != len(s) - 1 and romanToDigits[s[i]] < romanToDigits[s[i + 1]]:
                total -= romanToDigits[s[i]]
            else:
                total += romanToDigits[s[i]]
        return total

S = Solution()
print(S.romanToInt("MCMXCIV"))
# TC: O(n)
# SC: O(1)