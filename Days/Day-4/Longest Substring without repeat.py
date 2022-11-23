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

# Approach1: Using 2 for loops to compute all possible substrings and in doing so as soon as some character that is already encounterd comes, we'll keep break the loop and will Count length of string uptill then. We'll output the highest count.
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        currStr=""
        Len=0
        for i in range(len(s)):
            currStr=""
            for j in range(i,len(s)):
                if s[j] not in currStr: #This will take O(n), due to implementation of strings in python being like that.
                    currStr+=s[j]
                    Len=max(Len,len(currStr))
                else:
                    break
        print(Len)

# S=Solution()
# S.lengthOfLongestSubstring("pwwkew")
# S.lengthOfLongestSubstring("abcabcbb")
# S.lengthOfLongestSubstring("bbb")
# TC: O(n^3) Explanation: inside 2 for loops, we're running an if statement which'll take n time too, everytime.
# SC: O(n) Explanation: using currStr in worst case will take n space.

# Approach2: Using 2 Pointers. We will keep left and right at 0th index and will keep moving right to higher indexes. All items that right points will go in an array but every time as right moves, we'll check if new item pointed by right is already in the array. If so we'll start moving left pointer uptill the first occurence of item pointed by right is crossed; in doing this all what left points will be deleted from array. We'll register the difference b/n right and left pointer to know the length of unique consequtive Substring. We'll output highest length.
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left,right=0,0
        arr=[]
        lenOfSubstring=0
        while right<len(s):
            while s[right] in arr:
                arr.remove(s[left])
                left+=1
            arr.insert(-1,s[right])
            lenOfSubstring=max(lenOfSubstring, right-left+1)
            right+=1
        print(lenOfSubstring)

# S=Solution()
# S.lengthOfLongestSubstring("pwwkew")
# S.lengthOfLongestSubstring("abcabcbb")
# S.lengthOfLongestSubstring("bbb")
# TC:O(2n) Explanation:n time for right to traverse n elements, and n time for total traversal left could go by in worst case.
# SC:O(n) Explanation: An extra arr variable.


# Approach3: Improved time complexity, compromised space complexity than Approach2, by replacing the array with a dictionary. Where in approach 2 we had to move left all the way till way find an item which is pointed by right, if we can store the indexes of occurence of items, and directly place left at an index after where the occurence of the item is shown, then that will save the left pointer's motion.
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left,right=0,0
        dict={}
        lenOfSubstring=0
        while right<len(s):
            if s[right] in dict:
                left=max(dict[s[right]]+1,left) #just like how .remove was removing the elems from arr in approach2, here we are not removing the items from dict but, restricting access of any index in dictionary which is lesser than the present value of left. For eg: in abba when at index:2 item:a will appear again, left would be on index:2 and our dictionary would have an item:a at index:0. So here we wont let left decrease and so when at #--1 the length is counted, it'll be for not repeating items only.
            dict[s[right]]=right
            lenOfSubstring=max(lenOfSubstring, right-left+1) #--1
            right+=1
        print(lenOfSubstring)

S=Solution()
# S.lengthOfLongestSubstring("pwwkew")
# S.lengthOfLongestSubstring("abcabcbb")
S.lengthOfLongestSubstring("abba")
# TC:O(n) Explanation: n time for right to traverse n elements.
# SC:O(2n) Explanation: Dict variable taking 2n space for storing n keys and n values.