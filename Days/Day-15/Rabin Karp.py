# https://leetcode.com/problems/repeated-string-match/description/

# Given two strings a and b, return the minimum number of times you should repeat string a so that string b is a substring of it. If it is impossible for b to be a substring of a after repeating it, return -1.
# Notice: string "abc" repeated 0 times is "", repeated 1 time is "abc" and repeated 2 times is "abcabc".

# Example 1:
# Input: a = "abcd", b = "cdabcdab"
# Output: 3
# Explanation: We return 3 because by repeating a three times "abcdabcdabcd", b is a substring of it.

# Example 2:
# Input: a = "a", b = "aa"
# Output: 2

# Constraints:
# 1 <= a.length, b.length <= 10^4
# a and b consist of lowercase English letters.
# --------------------------------------------------------------------------------------------------------------------------------------
# Approach1: 'a' could be a parent string holding the substring b in one of the 4 sorts of cases. For eg: for all 4 cases consider a=abcd. Case 1) b=cdabcdab so this is where b is in a format of prefix + n*a + suffix, where n could be found by len(b)//len(a). So in this case to obtain the middle part i.e.n*a we'll need n a's and also for finding prefix and suffix we'll use 2 more a-items to be appended in 'a' this gives us total repeat counts of 'a' to be n+2 before it can possibly hold b as a substring. Similarly, for Case 2) b = abcdab that's where n*a + suffix gives the answer i.e. n + 1 is count. Case 3) b = cdabcd that's where prefix + n*a gives the answer i.e. n + 1 is count. Case 4) b = abcdabcd that's where n*a gives the answer, making the count to be n. So basically as we can see n*a and then n+1 or n+2 times when a has been extended upto, we should cover all possibilities for it to hold the substring 'b' and yet if it doesn't we return -1.
class Solution:
    def repeatedStringMatch(self, a, b):
        n = len(b) // len(a)
        n = max(n, 1) #In cases where a is 'aab' and b is 'aa', we'll get n=len(b)//len(a) as 0, and we need to make sure return n is returning 1 and not 0
        ct, temp = n, a
        while ct > 1:
            ct -= 1
            a += temp

        if b in a:
            return n

        a=a+temp
        if b in a:
            return n + 1

        a=a+temp
        if b in a:
            return n + 2
        return -1

S = Solution()
print(S.repeatedStringMatch("abcd", "cdabcdab"))
print(S.repeatedStringMatch("abc", "cabcabca"))
print(S.repeatedStringMatch("aa", "a"))
print(S.repeatedStringMatch("aaaaaaaaaaaaaaaaaaaaaab", "ba"))
# TC: O(n + 3*n*m) where len(a) is n and len(b) is m  Explanation: n TC for the while loop and then thrice we'll utilise n*m TC to check for `b in a`. Using b in a, 'b' string of length m is matched with every character in 'a' which gives the worst case n*m TC.
# SC: O(1)


# Approach2: Using KMP. Knuth Morris Pratt (KMP) is an optimised than brute force but not as optimal as Rabin Karp. Refer to Day-16/KMPAlgoOrLPS(pi)Array.py to understand KMP. Here we have just done two changes that in strStr `if j == m - 1:` we return True instead of the index where string was found and at the end of strStr we return False instead of -1 so that self.strStr will know whether in the if-condition it is True or False
class Solution:
    def repeatedStringMatch(self, a, b):
        n = len(b) // len(a)
        n = max(n, 1)
        ct, temp = n, a
        while ct > 1:
            ct -= 1
            a += temp

        if self.strStr(a, b):
            return n

        a = a + temp
        if self.strStr(a, b):
            return n + 1

        a = a + temp
        if self.strStr(a, b):
            return n + 2
        return -1

    def strStr(self, a: str, b: str) -> int:
        f = self.kmp(b)
        n, m = len(a), len(b)
        i = j = 0
        while i < n:
            if b[j] == a[i]:
                if j == m - 1:
                    return True
                i += 1
                j += 1
            elif j > 0:  # If
                j = f[j - 1]
            else:
                i += 1
        return False

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

S = Solution()
print(S.repeatedStringMatch("abcd", "cdabcdab"))
# TC: O(n+m)
# SC: O(m)


# Approach3: Rabin Karp -  we substitute the inbuilt `if substring in string` from approach1 with rabinKarp. Here the idea is that using unicode value of each character, hashing the value of substring i.e. summing up the unicodes using an equation in a way this sum is almost impossible to be replicated for any other combination of same or different characters. Once this is done we apply the same equation to first n items (n is length of subString) to givenStr and from there on check after every iteration whether the hash matches with that of subString's and in case it is not, we'll remove the first item of this hash, and we'll add next item from givenString. As soon as hash matches we return True. And if the givenString is exhausted we return False.
# Explanation-I (as below code claims): In rolling window portion where we remove the first item that became part of the current hash and add the next item from givenString into currentHash number, equation we've used is kind-of using the same as equation #--1 except here instead of mul * hash_givenString, we update hash_givenString to `hash_givenString - (self.cal(givenString[i - 1])*idx_mul)`. So this is where the part that is subtracted i.e. `self.cal(givenString[i - 1])` from `hash_givenString` still makes sense coz we're removing the i-1th item (where because i goes over the range of 1 to H-N+1, i-1 will mean we remove from givenString's 0th to H-Nth index items) but question is why are we multiplying the item to be removed with idl_mux i.e. `self.cal(givenString[i - 1]) * idl_mux`? The answer is - suppose we've mul=58 and unicodes of 1st, 2nd and 3rd items of givenStrings are 37, 42 and 16 respectively then the equation to calculate givenString hash initially will be: 58*0 + 37 and suppose it gives total as => 37; then 2nd equation will be 58*38 + 42 => 1098 and then 3rd equation will be 58*1098 + 16=> 21964. Now from this i.e. 21964, if we want to remove the 0th item i.e. 37 how can we? So if we reverse engineer the answer i.e. 21964 => 58*1098 + 16 => 58*(58*37 + 42) + 16 => 58*58*((58*0 + 37) + 42) + 16 from this we can see to remove 37 we need to remove 37*(58^2) i.e. givenString[0]*(mul^n-1). Now in Explanation-I if we see how in same iteration, as the new item gets added one more 58*()... equation is written, so now next for removing 42 we'll again have 3 instances 58's multiplied to it and to remove which we'll have to do givenString[1]*(mul^n-1). Thus we can see (mul^n-1) stays constant which we've made into idx_mul.
import sys

class Solution:
    def repeatedStringMatch(self, a, b):
        n = len(b) // len(a)
        n = max(n,1)  # In cases where a is 'aab' and b is 'aa' we'll get n=len(b)//len(a) as 0, and we need to make sure return n is returning 1 and not 0
        ct, temp = n, a
        while ct > 1:
            ct -= 1
            a += temp

        if self.rabinKarp(a, b):
            return n

        a = a + temp
        if self.rabinKarp(a, b):
            return n + 1

        a = a + temp
        if self.rabinKarp(a, b):
            return n + 2
        return -1

    def rabinKarp(self, givenString, subString):
        # Initiating variables
        N = len(subString)
        H = len(givenString)
        mul = ord('z') - ord('a')  #ord() gives unicode value and from a,b,...c these values are in increasing order  #As here the constraint states only smallercase alphabets are covered hence we only make our mul big enough to accomodate diversity for this much range, or in general we can choose it to be higher number in case we have more characters in our string to distinguish between or further choose smaller mul if we'd lesser characters to differentiate. Also here ord('z') - ord('a') is 25 which is odd although not a prime, we'll try taking it as a prime in case we take mul to be a rigged i.e. hard number like mul=71 to ensure lesser chances of hash to repeat between different combinations of chars.
        over = sys.maxsize  #depending on a 64 bit or 32 bit system the biggest number the system can store i.e. 2^64 or 2^31 is denoted here
        if N > H:
            return False

        # Calculating hash_subString, and first n item's hash for hash_givenString
        hash_subString = 0
        hash_givenString = 0
        for i in range(N):
            hash_subString = (mul * hash_subString + ord(subString[i])) % over        # %over to ensure number doesn't get super-super-big
            hash_givenString = (mul * hash_givenString + ord(givenString[i])) % over  #---1
        if hash_subString == hash_givenString:
            return True

        # Rolling window to remove items from 1 upto H-N+1, where in each iteration a new/next char starting from index N would be added in hash_givenString
        idx_mul = mul ** (N - 1)            #See - Explanation-I
        for i in range(1, H - N + 1):
            hash_givenString = (mul
                             * (hash_givenString - (ord(givenString[i - 1]) * idx_mul))
                             + ord(givenString[i + N - 1])
                             ) % over
            if hash_subString == hash_givenString:
                return True
        return False

S = Solution()
print(S.repeatedStringMatch("aa", "a"))
# TC: O(m) given length of subString is n and givenString is m  Explanation: If n is bigger than m we return -1 at the start, hence it's safe to assume m is bigger than n as we progress the algorithm. Further, for length n out of m we traverse in first for loop and the remaining ones we traverse in second for-loop. So in total we only traversed m items.
# SC: O(1)