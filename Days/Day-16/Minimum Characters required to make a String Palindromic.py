# https://www.interviewbit.com/problems/minimum-characters-required-to-make-a-string-palindromic/

# Problem Description
# Given a string A. The only operation allowed is to insert characters at the beginning of the string.
# Find how many minimum characters are needed to be inserted to make the string a palindrome string.

# Problem Constraints
# 1 <= |A| <= 10^6

# Input Format
# The only argument given is string A.

# Output Format
# Return the minimum characters that are needed to be inserted to make the string a palindrome string.

# Example Input
# Input 1:
# A = "ABC"
# Input 2:
# A = "AACECAAAA"

# Example Output
# Output 1:
# 2
# Output 2:
# 2

# Example Explanation
# Explanation 1:
# Insert 'B' at beginning, string becomes: "BABC".
# Insert 'C' at beginning, string becomes: "CBABC".
# Explanation 2:
# Insert 'A' at beginning, string becomes: "AAACECAAAA".
# Insert 'A' at beginning, string becomes: "AAAACECAAAA".
# -------------------------------------------------------------------------------------------------------------------------------------------
# Approach1: Because we can only insert items from the beginning of string, from back we'll have to discover items which are not participating in the longest palindrome substring of the givenString; where substring is taken from the starting of the givenString. So like in "AACECAAAA" from front AACECAA is longest palindromic substring and at the end "AA" is not contributing into this, it also implies "AA" doesn't match at the front, and we'll have to add it, making min chars required to make the given string palindromic as 2. Consider one more example "DABCECBA" so here in terms of being a consecutive palindromic string right from the starting item, we can find is D, meaning all the rest of the items ABCECBA have to be inserted at the front. Hence we've to find longest palindromic substring from start here. To implement this in a while loop using i and j we'll start comparing the front and back of given string and if they match the pointers are incremented and decremented respectively. If they don't match that means from back we'll reduce an item and thus obtained substring is again tried across possibility of being a substring. We keep count of these reductions we make and return that at the end. Also, to keep track of where j started from for the substring where mismatch happened, we use an extra variable temp which will initially be equal to j, and whenever j and i's item don't match j is temp is decremented and this new value is reassigned to j.
"""class Solution:
    def solve(self, A):
        i, j = 0, len(A) - 1
        temp = j
        minChars=0
        while i < j:
            if A[i] == A[j]:
                j-=1
                i+=1
            else:
                minChars+=1
                temp-=1
                j=temp
                i=0
        return minChars


S = Solution()
print(S.solve("AACECAAAA"))
print(S.solve("AAAACECAA"))
print(S.solve("apple"))
print(S.solve("banana"))"""
# TC: O(n^2) Explanation: for n substrings, we might be trying to find whether they're palindrome and each time n time is consumed in doing this
# SC: O(1)


# Approach2: Improved TC at cost of SC. Refer to Day-16/KMPAlgoOrLPS(pi)Array.py to understand KMP because here we use LPS array.
# In above approach if what we're doing is finding the longest palindromic substring from the start of the given string. For achieving the same, instead what we can also do is - if we reverse the current string and append it at the end of given string and find the LCS on it, then the last index of LCS array should hold the count of longest palindromic length from starting of the given string that matched with ending just like what happened in Approach1. But here Time Complexity would be far less. Consider 'AACECAAAA' then approach1 will essentially stop after identifying the portion 'AACECAA' i.e. longest palindrome since the start which in this approach as mentioned above we do AACECAAAA + AAAACECAA=> AACECAAAAAAACECAA where now finding LCS will essentially make us compare the starting of given string with given string's ending as we iterate over that part.
# Thus we iterate over the combined string where implied is that half way through this, we'll start matching given string's start with the end and if matched the common count increments and stored at that index of LCS. Let's understand with one last example:
# for DAADBCECBA using                                DAADBCECBAABCECBDAAD (LCS shown only for part where first and second half are matched for the combined string i.e. givenString & its reverse is matched i.e. from index 0 and 9's match onwards)
# Approach1 Step1: D and A are compared and ct=1  Approach2: D & A are compared and no match so 0 is inserted at 9th index of LPS = [0,0,0,0,0,0,0,0,0]
#           Step2: D and B are compared and ct=2  Approach2: D & B are compared and no match so 0 is inserted at 10th index LPS = [0,0,0,0,0,0,0,0,0,0]
#           Step3: D and C compared and ct=3      Approach2: D & C are compared and no match so 0 is inserted LPS = [0,0,0,0,0,0,0,0,0,0,0]
#           Step4: D and E compared and ct=4      Approach2: D & E are compared and no match so 0 is inserted LPS = [0,0,0,0,0,0,0,0,0,0,0,0]
#           Step5: D and C compared and ct=5      Approach2: D & C are compared and no match so 0 is inserted LPS = [0,0,0,0,0,0,0,0,0,0,0,0,0]
#           Step6: D and B compared and ct=6      Approach2: D & B are compared and no match so 0 is inserted LPS = [0,0,0,0,0,0,0,0,0,0,0,0,0,0]
#           Step7: D D compared & match ct=6      Approach2: D & D are compared and is match so 1 is inserted LPS = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,1]
#           Step8: A A compared & match ct=6      Approach2: A & A are compared and is match so 2 is inserted LPS = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,2]
#           complete substring found so done      Approach2: A & A are compared and is match so 3 is inserted LPS = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,2,3]
#                                                 Approach2: D & D are compared and is match so 4 is inserted LPS = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,2,3,4]
# So we see the same comparisons are made throughout howeveer in Approach1 we had a count of not participating items which we return directly but for LCS how will we find it? Answer is by subtraction of LCS's last index value from len(givenstring) which here is 10-4=>6 which is same as Approach1's ct as we saw. Also although here in LCS first half was all 0s but in some case first halve's last index and such can be 1 or something and that'd be an inconsistency we'll be having as we enter the second half. So that's covered in below comment where we add '$'.
# To handle the edge case where given string only have repetition of 1 same character like 'aa' as we reverse and concate i.e.aaaa the LCS will give wrong answer [0,1,2,3]=> LCS[-1]=3 suggesting longest palindrome from the start in given string is of length 3, while given string itself is of length 2. To handle these cases we concate a special symbol like "$" in between givenstring and its reverse. This separates the given string from its reverse, in the combined string, and thus makes sure that while filling LPS, by the time we get started with filling the portion of repeated string there is no residual value from earlier. So for aa$aa we can see LCS=[0,1,0,1,2]=> LCS[-1]=2 which is accurate length.

class Solution:
    def solve(self, A):
        f = self.kmp(A + '$' + A[::-1])
        return len(A) - f[-1]

    def kmp(self, pattern):
        f = [0] * len(pattern)
        i = 1
        j = 0
        while i < len(f):
            if pattern[j] == pattern[i]:
                f[i] = j + 1
                i += 1
                j += 1
            elif j > 0:
                j = f[j - 1]
            else:
                i += 1
        return f

S=Solution()
print(S.solve("ABC"))
print(S.solve("AA"))
print(S.solve("AAACECAAAA"))
# TC: O(5n) Explanation: n time to reverse A when doing A[::-1], plus 2n time for creating a prefilled f array of length 2n, and 2n more time to iterate over thus created f array
# SC: O(2n) Explanation: f takes 2n space as A and reverse of A is both passed to create f