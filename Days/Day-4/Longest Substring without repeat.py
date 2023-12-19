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

# Approach1: Using 2 for loops and a string hashMap to compute all possible substrings. Count and return maxlength amongst non repeat sub-strings.
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
# S.lengthOfLongestSubstring("bbb")
# TC: O(n^3) Explanation: inside 2 for loops, we're running an if statement which'll take n time too, everytime.
# SC: O(n) Explanation: using currStr in worst case will take n space.


# Approach2: Computing all possible substrings using 2 for-loop and a set hashMap.
"""
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        globMax = 0
        for i in range(len(s)):
            hashSet = set()
            for j in range(i, len(s)):
                if s[j] not in hashSet:  #Set lookup takes O(1) in python
                    hashSet.add(s[j])
                    globMax = max(globMax, j + 1 - i)
                else:
                    break
        return globMax
"""
# TC: O(n^2)
# SC: O(n)


# Approach3: Using a Pointers with a hashMap. Trick: If we're using 2 for loops, one way to reduce one for loop is very intuitive which is to use a hashmap.
# Here we can think of making a prefix hashDict where we store an elem and across it the index at which it is found as a pair, as we traverse in single for-loop through entire array. Each time we'll check if the current item is found in hashDict, which if the case we can update a pointer say l to the specified location across this item in hashDict+1. Otherwise, we'll simply keep incrementing ct to keep counting unique chars as ct=max(currentIndex+1-l,ct).
"""class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashMap = {}
        globMax = 0
        l = 0
        for i in range(len(s)):
            if s[i] in hashMap and hashMap[s[i]] >= l: #hashMap[s[i]] >= l makes sure for examples like 'tmmzuxt' where when we encounter second m, l is shifted to index 2 that when we're at last t and find a repeating item t in our hashDict at 0th index, we're not shifting l to 2.
                l = hashMap[s[i]]+1
            hashMap[s[i]]=i
            globMax = max(globMax, i + 1 - l)
        return globMax"""
# TC: O(n)
# SC: O(n)


# Approach 4: Same as Approach3 but using hashArr. Just for understanding concepts better.
# We will use a for loop to provide an increasing right pointer, and an explicit l pointer starting from 0th index. Right pointer will keep increasing and storing all the unique elems in  array. With every right pointer increment we will keep checking for updated length of the current unique substring by difference b/n right and left pointer, and incase it exceeds maxLen we'll update maxLen. If an elem is found repeating, we will keep incrementing l in temporary array making elems at all those indices None untill we remove the elem that got repeated. Now we are again all set to increment right pointer and start undertaking counting of a new string. Idea here is to constrain a unique substring between l and increasing right pointer.
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashMap = []
        maxLen = 0
        l = 0
        for i in range(len(s)):
            if s[i] not in hashMap:
                maxLen = max(maxLen, i + 1 - l)
            else:
                while s[i] in hashMap: #Array lookup takes O(n)
                    hashMap[l] = None
                    l += 1
            hashMap.append(s[i])
        return maxLen

# S=Solution()
# S.lengthOfLongestSubstring("bbb")
# TC:O(2n) Explanation: collectively the for and it's inner while could take 2n time, as for could iterate over an elem and while will increment uptill for. For will again increment say 2 iterations and now while has to catch up with for and runs twice. Thus, collectively for+while will take 2n time.
# SC:O(n) Explanation: An extra arr variable.