# https://leetcode.com/problems/longest-palindromic-substring/

# Given a string s, return the longest palindromic substring in s.

# Example 1:
# Input: s = "babad"
# Output: "bab"
# Explanation: "aba" is also a valid answer.

# Example 2:
# Input: s = "cbbd"
# Output: "bb"

# Constraints:
# 1 <= s.length <= 1000
# s consist of only digits and English letters.
# -----------------------------------------------------------------------------------------------------------------------------------
# Approach1: Compute all the substrings starting from the one of biggest length possible and check if they are palindrome, in which case we return them. To achieve computations of all the substring starting from the ones of biggest length possible we use nested for-loops where outer loop denoted substring length and iterates from len(s) to 0 (both inclusive). Inner loop will start with an empty tempStr and iterate over the given string, appending an item after the other in tempStr. As soon as len(tempStr) equals to that of the current substring size, that we are checking palindrome for which is the value of outer for-loop, we send the tempStr to a isPalindrome(). In isPalindrome() using front and back pointers that are incremented and decremented respectively in every iteration, we keep checking if items are same pointed by both pointers; this we keep checking up-till the front pointer crosses the back pointer which if any time violates the condition we return False or at end we return True. Thus having checked a palindrome, we return it as the biggest substring possible, or if not palindrome we remove the first item of tempStr so to maintain the size of subString, and thus go on to compute more substrings of the same length
class Solution:
    def longestPalindrome(self, s: str) -> str:
        for i in range(len(s), 0, -1):
            tempStr = ""
            for j in range(len(s)):
                tempStr += s[j]
                if len(tempStr) == i:
                    if self.isPalindrome(tempStr):
                        return tempStr
                    tempStr = tempStr[1:]

    def isPalindrome(self, givenStr):
        i, j = 0, len(givenStr) - 1
        while i <= j:
            if givenStr[i] != givenStr[j]:
                return False
            i+=1
            j-=1
        return True
# TC: O(n^3) Explanation: Outer for runs for n times inside which each time inner for runs for n times. TC of this much is n^2. Each time these two things i.e.loops runs, we check isPalindrome that takes n time, and so does the operation `tempStr = tempStr[1:]` takes n more time. Hence, each time for n^2 times 2n TC worth operations are performed => TC as n^2(2n) i.e. 2(n^3)
# SC: O(n) Explanation: only in worst case when tempStr is equal to the given string we occupy n space, or it'll always be lesser


# Approach2: We'll traverse the given string where for each item we'll assume them to be center of a palindrome substring. Now we'll try finding the longest palindrome around them. For this we keep expanding outside from the currInd say using l and r pointers and keep checking if items pointed by them are the same ones. Thus, in the inner loop itself as we expand and thus generate the possible substring we end up checking for palindrome which helps in reducing the TC that in approach2 was used to separately call isPalindrome(). But further here, there is a catch. It's that there could be 2 possibilities for palindrome length i.e. it can either be odd or even. If longest palindrome with the currentItem at center is odd like aabaa and say we're at currInd=2 then we can start with l=r=currInd and then decrement and increment the l & r pointers simultaneously till they are in the bounds of array length and are pointing to matching items i.e. givenStr[l]==givenStr[r]. As soon as any of these conditions violate we've recorded the longestPalindrome thus possible, and now we shift to checking for currInd=3 and so on... which is all fine. But for even length of palindrome like aab say we are at currInd = 0 and so l=r=currInd => l=r=0. Now if we simultaneously alter the l & r, we'll never get aa because from l=r=0 l will become -1 and go out of array bounds; and similarly for currInd=1, l will decrement to become 0 and r will increment to become 2 and string thus obtained is the whole aab. Thus, to get a possible even substring we need to start expand from currentItem considering l,r=i,i+1. Including both of these checks for every item in given substring we'll find longestSubstr and return it at end.
class Solution:
    def longestPalindrome(self, s: str) -> str:
        largestStr = ""

        for i in range(len(s)):
            r = l = i
            while r < len(s) and l >= 0 and s[r] == s[l]:
                if (r - l + 1) > len(largestStr):
                    largestStr = s[l:r + 1]
                r += 1
                l -= 1

            l, r = i, i + 1
            while r < len(s) and l >= 0 and s[r] == s[l]:
                if (r - l + 1) > len(largestStr):
                    largestStr = s[l:r + 1]
                r += 1
                l -= 1

        return largestStr

S = Solution()
print(S.longestPalindrome("abb"))
# TC: O(2n^2)
# SC: O(1)