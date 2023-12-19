# https://leetcode.com/problems/reverse-words-in-a-string/

# Given an input string s, reverse the order of the words.
# A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.
# Return a string of the words in reverse order concatenated by a single space.
# Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.

# Example 1:
# Input: s = "the sky is blue"
# Output: "blue is sky the"

# Example 2:
# Input: s = "  hello world  "
# Output: "world hello"
# Explanation: Your reversed string should not contain leading or trailing spaces.

# Example 3:
# Input: s = "a good   example"
# Output: "example good a"
# Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.

# Constraints:
# 1 <= s.length <= 104
# s contains English letters (upper-case and lower-case), digits, and spaces ' '.
# There is at least one word in s.

# Follow-up: If the string data type is mutable in your language, can you solve it in-place with O(1) extra space?
# ----------------------------------------------------------------------------------------------------------------------------------
# Approach1: Traverse the given string storing each item in a separate string tempStr up-till you find the current item being empty space " " in which case the existing tempStr is stored in tempArr and tempStr is made empty again i.e. tempStr="". At the end we might not have gotten chance to append the last tempStr as at last we might not encounter trailing empty spaces in given string, only when we appended the word in tempArr, and so after the for-loop if tempStr is not an empty string then we'll append it to tempArr and make it into an empty string in which we further store items from tempArr in reverse fashion. So we reverse traverse tempArr and we keep appending items in tempStr, with a catch that between two items of tempArr i.e. words we want to keep one space and so we detect that by filtering the first word i.e. len(tempStr)==0 and empty items in tempArr generated due to more than one continuous space in given string i.e. tempArr[i]=""; in those cases we dont and otherwise before appending item in tempStr we add " ".
class Solution:
    def reverseWords(self, s: str) -> str:
        tempArr = []
        tempStr = ""
        for i in s:  # In string we can iterate by string index as well as by item directly
            if i != " ":
                tempStr += i
            else:
                tempArr.append(tempStr)
                tempStr = ""

        if tempStr != "":
            tempArr.append(tempStr)
            tempStr = ""
        # tempArr = s.split(" ") #This is exactly identical to the whole above code


        for i in range(len(tempArr) - 1, -1, -1):
            if tempArr[i] != "" and len(tempStr) != 0:
                tempStr += " "
            tempStr += tempArr[i]
        return tempStr
        # return " ".join(tempArr[::-1]) #This is equivalent to the last for-loop with an exception that here we wont have a condition to not add " " i.e. space when tempArr's item is empty string i.e. ""

S = Solution()
print(S.reverseWords("dog        is good"))
# TC: O(2n)
# SC: O(2n) Explanation: for tempArr and tempStr