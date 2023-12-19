# https://leetcode.com/problems/valid-parentheses/submissions/

# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.

# Example 1:
# Input: s = "()"
# Output: true

# Example 2:
# Input: s = "()[]{}"
# Output: true

# Example 3:
# Input: s = "(]"
# Output: false

# Constraints:
# 1 <= s.length <= 104
# s consists of parentheses only '()[]{}'.
# -------------------------------------------------------------------------------------------------------------------------------------
# Approach 1: Because brackets like ({)} are also not valid, initially I used the solution as
# class Solution:
#     def isValid(self, s: str) -> bool:
#         roundB = squareB = curlyB = 0
#         for i in range(len(s)):
#             if s[i] == "(":
#                 roundB += 1
#             elif s[i] == ")":
#                 if squareB >= 1 or curlyB >= 1: return False
#                 roundB -= 1
#             elif s[i] == "[":
#                 squareB += 1
#             elif s[i] == "]":
#                 if roundB >= 1 or curlyB >= 1: return False
#                 squareB -= 1
#             elif s[i] == "{":
#                 curlyB += 1
#             else:
#                 if roundB >= 1 or squareB >= 1: return False
#                 curlyB -= 1
#             if roundB < 0 or squareB < 0 or curlyB < 0:
#                 return False
#         return roundB == squareB == curlyB == 0
# But it failed cases like {[]} where when checking for "]", we hit off "if roundB >= 1 or curlyB >= 1: return False" so this sort-of a trivial approach didn't work. That is where we thought of stack because evey time while encountering a closing bracket of any type we had to only make sure that last that can be popped from an array storing all the opening brackets is of same type.
class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        for i in range(len(s)):
            if (s[i]==")" or s[i]=="]" or s[i]=="}") and len(stack)==0: #When first item of s is a closing paranthesis
                return False
            elif s[i]==")" and stack[-1]!="(" or s[i]=="]" and stack[-1]!="[" or s[i]=="}" and stack[-1]!="{":
                return False
            elif s[i]==")" or s[i]=="]" or s[i]=="}":
                stack.pop()
            else:
                stack.append(s[i])
        return len(stack)==0 #At end to filter out cases like (([{ we check and return a comparison of stack length to be 0

S = Solution()
print(S.isValid("()[]{}"))
print(S.isValid("{[]}"))
# TC: O(n) Explanation: In for loop it takes n time to traverse the given string
# SC: O(n) Explanation: stack is an extra variable which in worst case can be of size n
