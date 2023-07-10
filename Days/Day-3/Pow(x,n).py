# https://leetcode.com/problems/powx-n/

# Implement pow(x, n), which calculates x raised to the power n(i.e., x^n).

# Example1: Input: x = 2.00000, n = 10 Output: 1024.00000

# Example2: Input: x = 2.10000, n = 3 Output: 9.26100

# Example3:Input: x = 2.00000, n = -2 Output: 0.25000 Explanation: 2 ^ - 2 = 1 / 2^2 = 1 / 4 = 0.25

# Constraints:
# -100.0 < x < 100.0
# -2^31 <= n <= 2^31 - 1
# -10^4 <= x^n <= 10^4
# -------------------------------------------------------------------------------------------------------------------------------------------
# Approach1: My Original
"""class Solution:
    def myPow(self, x: float, n: int) -> float:
        total = 1
        negative = False
        if n < 0:
            negative = True
        for i in range(abs(n)):
            total = total * x
        if negative == True:
            return 1 / total
        else:
            return total


S = Solution()
print(S.myPow(2, 2))
"""
# Time Complexity:O(n) given n is the power.
# Space Complexity:O(1)


# Approach2: Same as Approach1 with more decent representation using recursion:
"""
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0: return 1
        if n > 0: return x * self.myPow(x, n - 1)
        if n < 0: return 1 / (x * self.myPow(x, -n -1))
"""


# TC and SC same as approach 1


# Approach3: Better Time complexity. An even power equation for npowerm could be written as (n*n)power(m/2). Eg: 6^8 => (6*6)^4. Odd Power equation npowerm can be written as n*(npower(m-1)) Eg: 6^7=>6*(6^6). If we have 6^7 we could see its flow as: 6^7=>6*(6^6)=>6*((6*6)^3)=>6*(36*((36)^2))=>216*((36*36)^1)=>216*1296 as we encounter n=1, we'll stop going further in recursion.
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        elif n > 0 and n % 2 == 0:  # NOTE: Here x*x*self.myPow(x, n // 2) cant work coz `2^8=>2*2*(2^4)=>2^(1+1+4)=>2^6!=2^8` but `2^8=(2*2)^4=>(2^2)^4=>2(2*4)=>2^8`
            return self.myPow(x * x, n // 2)
        elif n > 0 and n % 2 != 0:
            return x * self.myPow(x * x, (n - 1) // 2)
        elif n < 0 and n % 2 == 0:
            return 1 / self.myPow(x * x, -n // 2)
        elif n < 0 and n % 2 != 0:
            return 1 / (x * self.myPow(x * x, (-n - 1) // 2))


S = Solution()
print(S.pow(2, 3))
# Time Complexity: O(logn). As we can see each time the n is getting halved as we find n to be even, hence that could be represented by logn. For the times n is odd we are doing x*(x*x) and divide that whole term's power by 2 after subtracting 1 from it. So in that case also, just like the even one, the power gets halved. For this pattern we know logn time is required.
# Space Complexity: O(1).
