# https://leetcode.com/problems/string-to-integer-atoi/

# Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer (similar to C/C++'s atoi function).

# The algorithm for myAtoi(string s) is as follows:
# 1. Read in and ignore any leading whitespace.
# 2. Check if the next character (if not already at the end of the string) is '-' or '+'. Read this character in if it is either. This determines if the final result is negative or positive respectively. Assume the result is positive if neither is present.
# 3. Read in next the characters until the next non-digit character or the end of the input is reached. The rest of the string is ignored.
# 4. Convert these digits into an integer (i.e. "123" -> 123, "0032" -> 32). If no digits were read, then the integer is 0. Change the sign as necessary (from step 2).
# 5. If the integer is out of the 32-bit signed integer range [-231, 231 - 1], then clamp the integer so that it remains in the range. Specifically, integers less than -231 should be clamped to -231, and integers greater than 231 - 1 should be clamped to 231 - 1.
# 6. Return the integer as the final result.

# Note:
# Only the space character ' ' is considered a whitespace character.
# Do not ignore any characters other than the leading whitespace or the rest of the string after the digits.

# Example 1:
# Input: s = "42"
# Output: 42
# Explanation: The underlined characters are what is read in, the caret is the current reader position.
# Step 1: "42" (no characters read because there is no leading whitespace)
#          ^
# Step 2: "42" (no characters read because there is neither a '-' nor '+')
#          ^
# Step 3: "42" ("42" is read in)
#            ^
# The parsed integer is 42.
# Since 42 is in the range [-231, 231 - 1], the final result is 42.

# Example 2:
# Input: s = "   -42"
# Output: -42
# Explanation:
# Step 1: "   -42" (leading whitespace is read and ignored)
#             ^
# Step 2: "   -42" ('-' is read, so the result should be negative)
#              ^
# Step 3: "   -42" ("42" is read in)
#                ^
# The parsed integer is -42.
# Since -42 is in the range [-231, 231 - 1], the final result is -42.

# Example 3:
# Input: s = "4193 with words"
# Output: 4193
# Explanation:
# Step 1: "4193 with words" (no characters read because there is no leading whitespace)
#          ^
# Step 2: "4193 with words" (no characters read because there is neither a '-' nor '+')
#          ^
# Step 3: "4193 with words" ("4193" is read in; reading stops because the next character is a non-digit)
#              ^
# The parsed integer is 4193.
# Since 4193 is in the range [-231, 231 - 1], the final result is 4193.

# Constraints:
# 0 <= s.length <= 200
# s consists of English letters (lower-case and upper-case), digits (0-9), ' ', '+', '-', and '.'.
# ------------------------------------------------------------------------------------------------------------------------------
# Approach1: We'll simply follow steps mentioned in question where step 1 and 2 are rather simple to follow where for step 1 we keep incrementing pointer i up-till either the string is run out upon or if we don't find empty space i.e. " " on this index. Thus, after clearing leading spaces, for step 2 we'll now see if we've either "-" or "+" at this i-th index of the string which if true we'll check if it is "+" we define a sign variable equal to +1 or -1 on identifying s[i] to be "-". If this index doesn't hold either of "-" or "+" we'll by default have sign variable defined as +1, this is at the end multiplied with the number found from given string and multiplied with it to ensure the actual sign in string stays the same in converted number. For Step 3 we'll now iterate i from its current value up-till end of string or if we find a non-digit item in string whichever happens first. Till then, we'll keep converting the string items thus found into int and before summing them into say a variable num (which'll hold converted number) we'll multiply num with 10 so "123" string can be made into like 1*10 + 2 =>10+2 => 12 and then before adding 3 in num we'll have 12*10 + 3 => 120+3 => 123. To incorporate 5th step, here itself after every iteration in while at the end we'll keep checking if num crossed either variable INT_MAX i.e. 2**31 - 1 while sign being +1 or INT_MIN i.e. 2**31 with sign being -1. In either cases the corresponding variables are returned just that in case INT_MIN is violated, because num actually doesn't have the sign on it, we made INT_MIN as 2**31 instead of -2**31, so it could be compared; hence in use case where INT_MIN condition is violated we return -INT_MIN instead of INT_MIN. In case step 5 never got triggered and step3 ends, we'll return num multiplied with the sign
class Solution:
    def myAtoi(self, s: str) -> int:
        # Step 1: Read and ignore leading whitespace
        i = 0
        while i < len(s) and s[i] == ' ':
            i += 1

        # Step 2: Check for '+' or '-'
        sign = 1
        if i < len(s) and (s[i] == '-' or s[i] == '+'):
            sign = -1 if s[i] == '-' else 1
            i += 1

        # Step 3 & 5: Read in the characters until the next non-digit character or end of input
        INT_MAX = 2 ** 31 - 1
        INT_MIN = 2 ** 31
        num = 0
        while i < len(s) and s[i].isdigit():
            digit = int(s[i])

            num = num * 10 + digit

            i += 1

            # Step 5: Check for integer overflow
            if num >= INT_MAX and sign == 1:
                return INT_MAX
            elif num >= INT_MIN and sign == -1:
                return -INT_MIN

        # Step 4: Apply sign and return the result
        return sign * num

S = Solution()
print(S.myAtoi("42"))  # Output: 42
print(S.myAtoi("   -42"))  # Output: -42
print(S.myAtoi("4193 with words"))  # Output: 4193
# TC: O(n)
# SC: O(1)
