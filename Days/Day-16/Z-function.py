# https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/

# Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

# Example 1:
# Input: haystack = "sadbutsad", needle = "sad"
# Output: 0
# Explanation: "sad" occurs at index 0 and 6.
# The first occurrence is at index 0, so we return 0.

# Example 2:
# Input: haystack = "leetcode", needle = "leeto"
# Output: -1
# Explanation: "leeto" did not occur in "leetcode", so we return -1.

# Constraints:
# 1 <= haystack.length, needle.length <= 104
# haystack and needle consist of only lowercase English characters.
# ------------------------------------------------------------------------------------------------------------------------------------
# Approach1:
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(len(haystack)-len(needle)+1):
            match = True
            for j in range(len(needle)):
                if haystack[i + j] != needle[j]:
                    match = False
                    break
            if match:
                return i
            """ #These 2 line below is same as above written inner for-loop and the `if match` condition
            if haystack[i:i+len(needle)]==needle:
                return i
            """
        return -1
S = Solution()
S.strStr("hello", "ll")
# TC: O(n*m) where n is length of haystack and m is length of needle  Explanation: for loop runs for n times roughly inside which each time at worst we match m characters to verify needle matches there
# SC: O(1)


# Approach2: For much detailed explanation visit Day15-RobinKarp.py file. Using rabin-karp algo we assign a hash to each character and sum them up to find needle's hash. Using the same hash equation, we first find hash of n (where n is length of needle) items of haystack as their summation which if matches the needle's hash, we return index 0. If not, we start removing/subtracting individual hash of first item in the summation of haystack and add hash of n+1 th item's hash. Thus, on a rolling window basis we keep finding hash from haystack for each possible length of items equal to needle's length and as hash matches we return the current iteration. If no hash matches thus, we return -1
import sys

class Solution:
    def strStr(self, haystack, needle):
        # Initiating variables
        N = len(needle)
        H = len(haystack)
        mul = ord('z') - ord('a')
        over = sys.maxsize
        if N > H:
            return -1

        # Calculating hash_needle, and first n item's hash for hash_haystack
        hash_needle = 0
        hash_haystack = 0
        for i in range(N):
            hash_needle = (mul * hash_needle + ord(needle[i])) % over
            hash_haystack = (mul * hash_haystack + ord(haystack[i])) % over
        if hash_needle == hash_haystack:
            return 0

        # Rolling window to remove items from 1 up-to H-N+1, where in each iteration a new/next starting from index N would be added in hash_haystack
        idx_mul = mul ** (N - 1)
        for i in range(1, H - N + 1):
            hash_haystack = ( mul
                              *  ( hash_haystack - (ord(haystack[i - 1]) * idx_mul) )
                              +  ord(haystack[i + N - 1])
                            ) % over
            if hash_needle == hash_haystack:
                return i
        return -1

S = Solution()
print(S.strStr("hello", "ell"))
# TC: O(m) given length of needle is n and haystack is m  Explanation: If n is bigger than m we return -1 at the start, hence it's safe to assume m is bigger than n as we progress the algorithm. Further, for length n out of m we traverse in first for loop and the remaining ones we traverse in second for-loop. So in total we only traversed m items.
# SC: O(1)