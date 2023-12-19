# https://leetcode.com/problems/longest-common-prefix/

# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".

# Example 1:
# Input: strs = ["flower","flow","flight"]
# Output: "fl"

# Example 2:
# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.

# Constraints:
# 1 <= strs.length <= 200
# 0 <= strs[i].length <= 200
# strs[i] consists of only lowercase English letters.
# ------------------------------------------------------------------------------------------------------------------------------
# Approach1: Using nested for-loops we traverse over the subItems in given array matching their subStrings. For this first for-loop traverses over the length of 1st string item in given array so it'll point the index and second for-loop will check through all the string items in given array for up-till this current index whether there subStrings matched. If so after the second for-loop yet still inside the first for-loop we mark a commonPrefix variable to be equal to this subString. Further we continue with further for-loop traversals to find possibly a longer subString match. On the contrary, if in 2nd for-loop subItem doesnt matching uptill the current index then we know it wont even match further and so we return commonPrefix variable at this point. In case the whole string items match we have to return the commonPrefix even at the end of nested for-loop.
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        commonPrefix = ""
        for i in range(len(strs[0])):
            item = strs[0][0:i + 1]
            for j in range(1, len(strs)):
                if strs[j][0:i + 1] != item:
                    return commonPrefix
            commonPrefix = item
        return commonPrefix
# TC: O(nm) Given there are n strings each of m length
# SC: O(1)


# Approach2: Using binary search instead of the outer for-loop to iterate through first item in given Array, and further matching in all the array items if it matches for their starting.
from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        l, u = 0, len(strs[0]) - 1
        longestCommon = ""
        while l <= u:
            mid = (l + u) // 2
            if self.isCommon(strs, strs[0][:mid + 1], mid + 1):
                longestCommon = strs[0][:mid + 1]
                l = mid + 1
            else:
                u = mid - 1
        return longestCommon

    def isCommon(self, arr, item, itemLen):
        for i in range(len(arr)):
            if len(arr[i])<itemLen or arr[i][:itemLen]!=item:
                return False
        return True

S = Solution()
print(S.longestCommonPrefix(["flower", "flow", "flight"]))
# TC: O(nlogm)
# SC: O(1)
