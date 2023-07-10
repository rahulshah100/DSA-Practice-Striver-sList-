# https://leetcode.com/problems/longest-substring-without-repeating-characters/
# Longest Substring Without Repeating Characters

# Given a string s, find the length of the longest substring without repeating characters.

# Example 1:
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.

# Example 2:
# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.

# Example 3:
# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3. Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

# Constraints:
# 0 <= s.length <= 5 * 10^4
# s consists of English letters, digits, symbols and spaces.
# --------------------------------------------------------------------------------
# Note: It being unfair, due to language benefits, otherwise we can run a for loop and input all string chars into a set and further just return length of set.

# Approach1: Using 2 for loops compute all possible substrings. Count and return maxlength amongst non repeat sub-strings.
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLen=0
        for i in range(len(s)):
            temp = ""
            for j in range(i,len(s)):
                if s[j] in temp: # This will take O(n), due to implementation of strings in python being like that.
                    break
                else:
                    temp+=s[j]
                    maxLen = max(maxLen, len(temp))
        return maxLen

# S=Solution()
# S.lengthOfLongestSubstring("pwwkew")
# S.lengthOfLongestSubstring("abcabcbb")
# S.lengthOfLongestSubstring("bbb")
# TC: O(n^3) Explanation: inside 2 for loops, we're running an if statement which'll take n time too, everytime.
# SC: O(n) Explanation: using currStr in worst case will take n space.

# Approach2: Using 2 Pointers. We will use a for loop to provide an increasing right pointer, and an explicit l pointer starting from 0th index. right pointer will keep increasing storing all the unique elems in a temporary array. With every right pointer increment we will keep checking for updated length of this unique substring by differnce b/n right and left pointer, and incase it exceeds maxLen we'll update maxLen. If an elem is found repeating, we will keep incrementing l in temporary array making elems at all those indices None untill we remove the elem that got repeated. Now we are again all set to increment right pointer and start underaking counting of a new string. Idea here is to constrain a unique substring between l and increasing right pointer.
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLen = 0
        l = 0
        tempArr = []
        for i in range(len(s)):
            if s[i] in tempArr:
                while s[i] in tempArr:
                    tempArr[l]=None
                    l += 1
                tempArr.append(s[i]) #So that s[i] from current iteration doesnt get lapsed or temparray's size and indexes will faulter
            else:
                tempArr.append(s[i])
                maxLen = max(maxLen, i - l + 1)
        return maxLen

# S=Solution()
# S.lengthOfLongestSubstring("pwwkew")
# S.lengthOfLongestSubstring("abcabcbb")
# S.lengthOfLongestSubstring("bbb")
# TC:O(2n) Explanation: collecively the for and it's inner while could take 2n time, as for could iterate over an elem and while will increment uptill for. For will again increment say 2 iterations and now while has to catch up with for and runs twice. Thus collectively for+while will take 2n time.
# SC:O(n) Explanation: An extra arr variable.


# Approach3: Improved time complexity, compromised space complexity than Approach2 - by replacing the array with a dictionary. Where in approach 2 we had to move left all the way till way find an item which is pointed by right, if we can store the indexes of occurence of items, we can then directly place left at an index after where the occurence of the item is shown. This will save the whole while loop inside for loop.
# from typing import
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ct = l = 0
        hash = {}
        for i in range(len(s)):
            if s[i] in hash:
                l = max(l,hash[s[i]] + 1) #Two things: 1).We did hash[s[i]]+1 as for ith iteration of for loop we discovered that s[i] elem is repeating/is present in hash. Hence we have to circumvent this item so to have a unique substring. Therefore we do hash[s[i]]+1. 2) For updating l, we're taking max of l and hash[s[i]]+1 to ensure the new substring doesnt start from a point where although the last encountered repeat is circumvent but we're ending with some other repeating elems in between. Eg: abba for i at 2nd index we will find b already present at 1st index. Hence here, l would be updated to index 2. Furtehr when i is at index 3, we'll encounter 'a' to find it having repeated at index 0. Here we wont want l to be updated to 1st index just to circumvent 'a' in which case bba would become our string from l to i, which now has bb repeating. But in this case the already updated l's value i.e index 2 is optimal already as it doesnt involve a repeating.
            hash[s[i]] = i
            ct = max(ct, i - l + 1)
        return ct

S = Solution()
print(S.lengthOfLongestSubstring("abba"))
# TC:O(n) Explanation: n time for right to traverse n elements.
# SC:O(n) Explanation: Dict variable taking n extra space.
