# https://leetcode.com/problems/valid-anagram/

# Given two strings s and t, return true if t is an anagram of s, and false otherwise.
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

# Example 1:
# Input: s = "anagram", t = "nagaram"
# Output: true
# Example 2:
# Input: s = "rat", t = "car"
# Output: false

# Constraints:
# 1 <= s.length, t.length <= 5 * 104
# s and t consist of lowercase English letters.

# Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?
# ---------------------------------------------------------------------------------------------------------------------------------------
# Approach1: Use a HashDictionary to first mark all the items and their counts while traversing s string and later decrement these counts while traversing t string. When trying to decrement, we check whether the item is present in key of dictionary and if it is not we return False. At the end we check the dictionary's counts and if any of them is not 0 we return False. At the end True is returned
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        tempDict = {}
        for i in range(len(s)):
            if s[i] not in tempDict:
                tempDict[s[i]] = 1
            else:
                tempDict[s[i]] += 1

        for j in range(len(t)):
            if t[j] not in tempDict:
                return False
            else:
                tempDict[t[j]] -= 1

        for key in tempDict:
            if tempDict[key]!=0:
                return False
        return True

S = Solution()
print(S.isAnagram("anagram", "nagaram"))
# TC: O(3n)
# SC: O(2n) #Explanation: Dictionary will take 2n space to store n items


# Approach2: Optimising approach1 for space at a time cost, and answering the follow-up question that if input was array of unicode chars instead of alphabet letters, what we;lll do. As we see from constraint in question only lowercase alphabets are given to us. Thus possible unicodes can come in the range of 26 values. As unicode for a, b, c i.e. small-a, small-b, small-c are gonna be 1 value afar if we subtract unicode of 'a' from all these letters we can be assured our range of items will be from 0 to 25. For this we create an array of size 26 pre-filled with 0s. And repeat the similar process as approach1 where we used hashDict, but instead here we use the pre-filled array as mentioned earlier
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        unicodeArr = [0 for i in range(26)]
        for i in s:
            unicodeArr[ord(i) - ord('a')] += 1

        for j in t:
            unicodeArr[ord(j) - ord('a')] -= 1

        for item in unicodeArr:
            if item != 0:
                return False
        return True

S = Solution()
print(S.isAnagram("rat", "car"))
# TC: O(4n) #Explanation: n for defining a pre-filled unicodeArr and 3n for 3 for-loops
# SC: O(1)  #Explanation: because a fixed array is use there is no growth of space as algo expands