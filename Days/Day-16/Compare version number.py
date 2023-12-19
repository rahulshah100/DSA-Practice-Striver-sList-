# https://leetcode.com/problems/compare-version-numbers/

# Given two version numbers, version1 and version2, compare them.
# Version numbers consist of one or more revisions joined by a dot '.'. Each revision consists of digits and may contain leading zeros. Every revision contains at least one character. Revisions are 0-indexed from left to right, with the leftmost revision being revision 0, the next revision being revision 1, and so on. For example 2.5.33 and 0.1 are valid version numbers.
# To compare version numbers, compare their revisions in left-to-right order. Revisions are compared using their integer value ignoring any leading zeros. This means that revisions 1 and 001 are considered equal. If a version number does not specify a revision at an index, then treat the revision as 0. For example, version 1.0 is less than version 1.1 because their revision 0s are the same, but their revision 1s are 0 and 1 respectively, and 0 < 1.

# Return the following:
# If version1 < version2, return -1.
# If version1 > version2, return 1.
# Otherwise, return 0.

# Example 1:
# Input: version1 = "1.01", version2 = "1.001"
# Output: 0
# Explanation: Ignoring leading zeroes, both "01" and "001" represent the same integer "1".
# Example 2:
# Input: version1 = "1.0", version2 = "1.0.0"
# Output: 0
# Explanation: version1 does not specify revision 2, which means it is treated as "0".
# Example 3:
# Input: version1 = "0.1", version2 = "1.1"
# Output: -1
# Explanation: version1's revision 0 is "0", while version2's revision 0 is "1". 0 < 1, so version1 < version2.

# Constraints:
# 1 <= version1.length, version2.length <= 500
# version1 and version2 only contain digits and '.'.
# version1 and version2 are valid version numbers.
# All the given revisions in version1 and version2 can be stored in a 32-bit integer.
# -------------------------------------------------------------------------------------------------------------------------------------------
# Approach1: Approach is to initially separate the item before first "." is encountered in both the strings i.e. version1, and version2 and convert this part into integers. We store them in num1 and num2 for respective strings. For this conversion for example '0293' had to be converted, then we loop over this part everytime multiplying num1 with 10 and adding the new one item (2*10 + 9)*10 + 3. Observe how this way all the leading 0s are automatically made futile. Once thus changed into integer, we compare num1 and num2 and return -1 if num1 is smaller, or return 1 if num1 is bigger, and if neither condition satisfies then it means this much portion of both strings have been the same, and we need to compare them further now. So further we skip the first item which is going to be a '.' where we earlier stopped and again loop the upcoming part of version1 and version2 till another '.' is encountered. This goes on till both the strings are not exhausted. If one string is exhausted as we'll initialise num1 and num2 with 0, that part is taken care of. As both strings are exhausted and for none of the revision (parts in between '.') we found any deviation in values it means the version are same, and so we return 0.
class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        i = j = 0
        while i < len(version1) or j < len(version2):
            num1 = num2 = 0
            while i < len(version1) and version1[i] != ".":
                num1 = num1 * 10 + int(version1[i])
                i += 1
            i += 1

            while j < len(version2) and version2[j] != ".":
                num2 = num2 * 10 + int(version2[j])
                j += 1
            j += 1

            if num1 > num2:
                return 1
            elif num2 > num1:
                return -1
        return 0

S = Solution()
print(S.compareVersion("2.5.33", "2.05.36"))
# TC: O(max(n,m)) where n is length of version1 and m is length of version2
# SC: O(1)