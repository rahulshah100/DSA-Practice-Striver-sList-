# https://leetcode.com/problems/min-stack/

# Design a stack that supports push, pop, top, and retrieving the minimum  element in constant time.

#  Implement the MinStack class:
# MinStack() initializes the stack object.
# void push(int val) pushes the element val onto the stack.
# void pop() removes the element on the top of the stack.
# int top() gets the top element of the stack.
# int getMin() retrieves the minimum element in the stack.
# You must implement a solution with O(1) time complexity for each function.

# Example1:
# Input: ["MinStack", "push", "push", "push", "getMin", "pop", "top", "getMin"] [[], [-2], [0], [-3], [], [], [], []]
# Output: [null, null, null, null, -3, null, 0, -2]

# Explanation
# MinStack minStack = new MinStack();
# minStack.push(-2);
# minStack.push(0);
# minStack.push(-3);
# minStack.getMin(); // return -3
# minStack.pop();
# minStack.top(); // return 0
# minStack.getMin(); // return -2

# Constraints:
# -231 <= val <= 231 - 1
# Methods pop, top and getMin operations will always be called on non-empty stacks.
# At most 3 * 104 calls will be made to push, pop, top, and getMin.
# -----------------------------------------------------------------------------------------------------------------------------------------
# Approach1: Brute Force - Only for getMin we're thinking of having to do something, for the other operations it's quite simple. So we do other operations simply and only in getMin we copy the current stack, sort it and return the bottom element
"""class MinStack:
    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

    def pop(self) -> None:
        if self.stack:
            self.stack.pop()

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]

    def getMin(self) -> int:
        temp=self.stack[:]
        temp.sort()
        return temp[0]
"""
# TC: O(nlogn) Explanation: Worst TC is where we sort the temp array in getMin
# SC: O(2n) Explanation: Considering the worst SC it'd be for running getMin where we replicate the given items


# Approach2: We'll use a minItem variable to keep track of minItem at every push. But as items could be popped, we'd need to fetch last minItem to return then and for which we need to have access to progressive minItem values for all the push operations. For this instead of only storing value in stack, we'll store a list of value and minItem at that point.
class MinStack:
    def __init__(self):
        self.stack = []
        self.minItem = None

    def push(self, val: int) -> None:
        if not self.stack:
            self.minItem = val
        else:
            self.minItem = min(val, self.stack[-1][-1]) #Here it is important to update minItem like this and not like self.minItem = min(val, self.minItem) because in the latter once we pop() minItem is not changed and so say in case like stack = [[7, 7],[2,2]] and minItem = 2, and we pop() then stack becomes [[7,7]] and minItem=2 and now if we get push(3,3) then as minitem is still 2 we'll compare min(2,3) instead of (7,3).
        self.stack.append([val, self.minItem])

    def pop(self) -> None:
        if self.stack:
            self.stack.pop()

    def top(self) -> int:
        if self.stack:
            return self.stack[-1][0]

    def getMin(self) -> int:
        if self.stack:
            return self.stack[-1][-1]

M=MinStack()
print(M.push(0), end=" ")
print(M.push(1), end=" ")
print(M.push(0), end=" ")
print(M.getMin(), end=" ")
print(M.pop(), end=" ")
print(M.getMin(), end=" ")
# TC: O(1)
# SC: O(2N) Explanation: As we're storing pairs, to store n items, we'll take 2n space


# Approach3: If we look at approach2, SC is 2n instead of n only because we'd to keep storing minItem besides every value, in the stack. Instead, if we maintained minItem only as a one variable to hold currenMin rather than storing all the progressive version/changes, we face only one issue that is as we pop items then based on availability of items, we need minItem to be rolled back to its earlier value that had become unaccessible. For this we use a formula (2 * val - min) which is used to store an item found smaller than existing minItem. So while pushing in stack, as we encounter an item/val smaller than current minItem we'll update minItem to it, but before that we push in stack not the val but 2 * val - min. So this is now our reference (that minItem is greater than val) to understand that from this point and backward we had a different minItem. But for this what's the proof that thus stored val which is 2*val - min is always going to be smaller than val? Proof of if it is that if min was equal to val then 2*val - min => 2*val - val => val but as min is bigger than val whenever hence 2*val - min will be smaller than val. So after encoding values and knowing how to identify the encoded value and changed min (i.e. when val is smaller than minItem), we have a question that how to retrieve original value and previousMin. For that original val could be right away said to be equal to minVal but before that the prevMin can be retrieved back using the formula 2*currMinItem - modifiedVal; where because modifiedVal is fetched from 2*actualVal - prevMin, the formula becomes 2*currMinItem - (2*actualVal - prevMin) where we know currMinItem is same as actualVal and so we can say formula is 2*currMinItem - (2*currMinItem - prevMin) => prevMin
import math

class MinStack:
    def __init__(self):
        self.stack = []
        self.minItem = math.inf

    def push(self, val: int) -> None:
        if not self.stack or val > self.minItem :
            self.stack.append(val)
        else:
            self.stack.append((2 * val) - self.minItem)
        self.minItem = min(self.minItem, val)

    def pop(self) -> None:
        if self.stack and self.minItem > self.stack[-1]:
            self.minItem= (2*self.minItem) - self.stack[-1]
        if self.stack:
            self.stack.pop()
        if not self.stack:
            self.minItem = math.inf

    def top(self) -> int:
        if self.stack and self.minItem > self.stack[-1]:
            return self.minItem
        elif self.stack:
            return self.stack[-1]

    def getMin(self) -> int:
        if self.stack:
            return self.minItem
# TC:O(1)
# SC:O(1)