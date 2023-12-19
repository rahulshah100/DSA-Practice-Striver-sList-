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
# 1 <= haystack.length, needle.length <= 10^4
# haystack and needle consist of only lowercase English characters.
# -------------------------------------------------------------------------------------------------------------------------------------------
# Approach1: Using KMP Algo - The KMP algorithm improves the brute force algorithm's TC from O(m*n) to O(m+n) by using an extra LPS array (Longest prefix which is also suffix) of size m (denoting b/pattern/smaller-string). So if we think of brute force algorithm for String Matching then what happens is... Consider a-string to be "abcbcglx" and b-string being "bcgll" and that we've pointers i, and j which traverses in 'a' and 'b' strings respectively. Then starting with i=0, j=0 the corresponding items don't match, and so we increment i. Now for i=1, j=0 items match and so we increment both of them, and further for i=2, j=1 items match again so we make i=3, j=2 where items which are 'b' and 'g' dont match. In that case what we're gonna do is that, because for the substring starting from index i=1 the complete match couldnt be found, we'll go over the whole thing again starting with next index from i=1, that is i=2 and j=0.
# So this is where KMP does its optimisation where it ensures i never has to go back like how in brute force it did from i=3 to i=2. To achieve this, KMP uses the insight of Longest Prefix Suffix match. To explain this let's consider a-string as 'abcxabcxabcxabcd' and b-string to be 'abcxabcd'. Say as we can see we can reach without a hiccup till i=7, and j=7 but that's where the items dont match. Now because j has already matched for index upto and including 6, coz only that's how currently we can possible be at j=7; then now instead of making j=0 and i=1, we'll check in b-string if upto and including index 6 whether we can find a LPS, which in this case we can see is 'abc' that matches from index-0-to-2 being the prefix and index-4-to-6 being our suffix. Because of this we know if j=7 didnt match still instead of making j=0 directly we can try reducing it to index-3 which is because index 0-to-2 matches with that of 4-to-6 and so at this point when we're at j=7 we can safely assume if the items 4-to-6 matched with a-string then so will items from index 2-to-3. This let's us make j=3=>x which matches with i=7=>x. Thus after only changing j value once, we kept i going further ahead. In case where even for j=3 the item hadnt matched then because upto index 2 we have no LPS, we'd have to make j=0 and when that doesnt match with i=7, we increment i. In practice how we here figured index-3 is where we need to shift j, that part would be handled by LPS array. At each index LPS array will store length of longest matching LPS. So in this case we'd have looked at index-6 and must have found 4 stored there because 'abc' is LPS and it's length=3. So to equate this out, for j=7 not matching with i=7, we did j=LPS[6].
# This gives the complete jist of algo and also shows that it is a 3 case stuff where case1: a[i] matches b[j] where we increment both i and j to try finding extending the longest match; case2: a[i] doesnt match b[j] but j is not 0 in which case we can have an earlier j index where we can possibly shift it to by looking in LPS array, so we do j=LPS[j-1]; case3: a[i] and b[j] dont match and j is 0 where we'll simply increment i.
# Watch the video on this link to exactly understand this algo: https://www.youtube.com/watch?v=GTJr8OvyEVQ&ab_channel=TusharRoy-CodingMadeSimple
# To make this string matching algorithm called KMP functional we divide it in 2 parts each constituting of above 3 steps, where the first part is the creating LPS where we match the same string (b-string) with itself by making i=1 and j=0 at start and iterate over the given b-string. The second part is the where we compare given 2 strings a-string and b-string and take in use prior generated LPS for reference in case items dont match.
class Solution:
    def strStr(self, a: str, b: str) -> int:
        f = self.kmp(b)
        n, m = len(a), len(b)
        i = j = 0
        while i < n:
            if b[j] == a[i]: #While comparing 2 strings if items are matching we're incrementing both pointers uptill the whole b string is not matched after which we return the index where the starting of b-string is found in a-string
                if j == m - 1:
                    return i - m + 1
                i += 1
                j += 1
            elif j > 0:  #If
                j = f[j - 1]
            else:
                i += 1
        return -1

    def kmp(self, pattern):  #Create LPS array -  it shows for each index of the string called pattern, the length of common prefix that is also a suffix
        f = [0] * len(pattern) #Fill LPS array with 0s initially
        i = 1 #For index 0, as substring cant be proper prefix because it just has a single character and so there is no suffix that can be separated from prefix, so common prefix suffix length is staying 0 and and hence i is directly assigned to 1
        j = 0
        while i < len(f):
            if pattern[j] == pattern[i]:
                f[i] = j + 1
                i += 1
                j += 1
            elif j > 0: #when the current item doesnt match but also j is not 0, meaning a possible LPS instance and so we try going there
                j = f[j - 1]
            else: #If items dont match, neither do they have before i.e.j==0; then we'll just increment i and move-on
                i += 1
        return f

S = Solution()
print(S.strStr("cdabcdab","ababacad"))
# print(S.strStr("cdabcdab","abcd"))
# print(S.strStr("cabcabca", "abc"))
# print(S.strStr("aa", "a"))
# print(S.strStr("aaaaaaaaaaaaaaaaaaaaaab", "ba"))
# TC: O(n+m) where n is the length of string a and m is the length of string b  Explanation: kmp function takes m time to compute LPS array i.e.f and then we iterate over haystack which is length of n.
# SC: O(m) Explanation: for creating an LPS array of m items