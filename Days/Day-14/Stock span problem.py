# https://leetcode.com/problems/online-stock-span/

# Design an algorithm that collects daily price quotes for some stock and returns the span of that stock's price for the current day.
# The span of the stock's price in one day is the maximum number of consecutive days (starting from that day and going backward) for which the stock price was less than or equal to the price of that day.
# For example, if the prices of the stock in the last four days is [7,2,1,2] and the price of the stock today is 2, then the span of today is 4 because starting from today, the price of the stock was less than or equal 2 for 4 consecutive days.
# Also, if the prices of the stock in the last four days is [7,34,1,2] and the price of the stock today is 8, then the span of today is 3 because starting from today, the price of the stock was less than or equal 8 for 3 consecutive days.

# Implement the StockSpanner class:
# StockSpanner() Initializes the object of the class.
# int next(int price) Returns the span of the stock's price given that today's price is price.

# Example 1:
# Input
# ["StockSpanner", "next", "next", "next", "next", "next", "next", "next"]
# [[], [100], [80], [60], [70], [60], [75], [85]]
# Output
# [null, 1, 1, 1, 2, 1, 4, 6]

# Explanation
# StockSpanner stockSpanner = new StockSpanner();
# stockSpanner.next(100); // return 1
# stockSpanner.next(80);  // return 1
# stockSpanner.next(60);  // return 1
# stockSpanner.next(70);  // return 2
# stockSpanner.next(60);  // return 1
# stockSpanner.next(75);  // return 4, because the last 4 prices (including today's price of 75) were less than or equal to today's price.
# stockSpanner.next(85);  // return 6

# Constraints:
# 1 <= price <= 105
# At most 10^4 calls will be made to next.
# -------------------------------------------------------------------------------------------------------------------------------------------
# Approach1: In next() we'll reverse traverse the priceArr everytime and thus return count
class StockSpanner:
    def __init__(self):
        self.stack=[]

    def next(self, price: int) -> int:
        count=1
        for i in range(len(self.stack)-1,-1,-1):
            if self.stack[i]>price:
                break
            else:
                count+=1
        self.stack.append(price)
        return count
# TC: O(n^2) Explanation: For each next call n time is taken
# SC: O(n)


# Approach2: Using monotonous stack we'll store numbers as well as their stock span together as a tuple, in the next() as we receive them. While doing this if we find stack to be empty we'll store item and (it's span as) 1. If stack is not empty and last number is bigger than current number, we simply store current number with its span as 1. Conversely, for a non-empty stack if we find current number is greater or equal to last number, then last number's count is fetched and added with a one (for including current item) and we pop the last item; we continue doing so till either the new last is bigger than currItem or stack is empty and after which we store this item and the sum total of these counts. Here popping is important coz now at worst the whole stack of say n items would collectively be traversed only once, or we could have just kept stored in stack all the numbers and seeing count on the last one we'll go those many numbers back and then check that one's value but there unnecessary complexity for going those many numbers back will be utilised every corresponding time.
class StockSpanner:
    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        if not self.stack or self.stack[-1][0] > price:
            self.stack.append((price, 1))
            return 1
        ct = 1
        while self.stack and self.stack[-1][0] <= price:
            val, valCt = self.stack.pop()
            ct += valCt
        self.stack.append((price, ct))
        return ct

S = StockSpanner()
print(S.next(100), end=" ")
print(S.next(80), end=" ")
print(S.next(60), end=" ")
print(S.next(70), end=" ")
print(S.next(60), end=" ")
print(S.next(75), end=" ")
print(S.next(85), end=" ")
# TC: O(2n) Explanation: for n operations O(1) time is taken n times and in which at worst the whole stack collectively will be traversed for n times, so n+n is the TC
# SC: O(2n) Explanation: stack will at worst store n pairs each of which has 2 items