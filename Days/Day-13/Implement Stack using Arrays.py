# https://www.codingninjas.com/studio/problems/stack-implementation-using-array_3210209?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf

# Problem Statement
# Stack is a data structure that follows the LIFO (Last in First out) principle. Design and implement a stack to implement the following functions:
# 1. Push(num): Push the given number in the stack if the stack is not full.
# 2. Pop: Remove and print the top element from the stack if present, else print -1.
# 3. Top: Print the top element of the stack if present, else print -1.
# 4. isEmpty: Print 1 if the stack is empty, else print 0.
# 5. isFull: Print 1 if the stack is full, else print 0.
# You have been given ‘m’ operations which you need to perform in the stack. Your task is to implement all the functions of the stack.

# Example:
# We perform the following operations on an empty stack which has capacity 2:
# When operation 1 1 is performed, we insert 1 in the stack.
# When operation 1 2  is performed, we insert 2 in the stack.
# When operation 2 is performed, we remove the top element from the stack and print 2.
# When operation 3 is performed, we print the top element of the stack, i.e., 3.
# When operation 4 is performed, we print 0 because the stack is not empty.#
# When operation 5 is performed, we print 0 because the stack is size 1, which is not equal to its capacity.

# Detailed Explanation
# Sample Input 1:
# 2 6
# 1 1
# 1 2
# 2
# 3
# 4
# 5
# Sample Output 1:
# 2
# 1
# 0
# 0
# Explanation For Sample Output 1:
# We perform the following operations on an empty stack which has capacity 2:
# When operation 1 1 is performed, we insert 1 in the stack.
# When operation 1 2  is performed, we insert 2 in the stack.
# When operation 2 is performed, we remove the top element from the stack and print 2.
# When operation 3 is performed, we print the top element of the stack, i.e., 1.
# When operation 4 is performed, we print 0 because the stack is not empty.
# When operation 5 is performed, we print 0 because the stack is size 1, which is not equal to its capacity.

# Sample Input 2:
# 5 5
# 1 2
# 2
# 2
# 1 1
# 3
# Sample Output 2:
# 2
# -1
# 1
# Explanation For Sample Output 2:
# We perform the following operations on an empty stack which has a capacity of 5:
# When operation 1 2 is performed, we insert 2 in the stack.
# When operation 2 is performed, we remove the top element from the stack and print 2.
# When operation 2 is performed, as the stack is empty, we print -1.
# When operation 1 1 is performed, we insert 1 in the stack.
# When operation 3 is performed, we print the top element of the stack, i.e., 1.

# Constraints:
# 1 <= 'n', 'm' <= 10^3
# Time Limit: 1 sec
# -------------------------------------------------------------------------------------------------------------------------------------------
# A Bit Info about Stack: as their english names suggest Heap is like a triangular heap i.e. a binary tree which expands towards bottom; while stack is one item on top of other formation where the last item which is at the top is deleted i.e.LIFO order is followed for removal; while something we'll soon see if Que is like stack where it is single file but this is where first entered will leave the first i.e.FIFO order is followed.

# In python list is almost identical to stack and so we dont have any in-built stack implementation
# -------------------------------------------------------------------------------------------------------------------------------------------
class Stack:
    def __init__(self, n: int):
        self.capacity = n
        self.stack = []

    def Push(self, num):
        if len(self.stack) < self.capacity:
            self.stack.append(num)

    def Pop(self):
        if len(self.stack) > 0:
            return self.stack.pop()
        return -1

    def Top(self):
        if len(self.stack) > 0:
            return self.stack[-1]
        return -1

    def isEmpty(self):
        return len(self.stack) == 0

    def isFull(self):
        return len(self.stack) == self.capacity
# TC: O(1) Each stack operation takes O(1) time
# SC: O(n) is space stack will take to store n items