# https://leetcode.com/problems/implement-queue-using-stacks/

# Implement a first in first out(FIFO) queue using only two stacks.The implemented queue should support all the functions of a normal queue(push, peek, pop, and empty).

# Implement the MyQueue class:
# void push(int x) Pushes element x to the back of the queue.
# int pop() Removes the element from the front of the queue and returns it.
# int peek() Returns the element at the front of the queue.
# boolean empty() Returns true if the queue is empty, false otherwise.

# Notes:
# You must use only standard operations of a stack, which means only push to top, peek / pop from top, size, and is empty operations are valid.
# Depending on your language, the stack may not be supported natively.You may simulate a stack using a list or deque(double - ended queue) as long as you use only a stack 's standard operations.

# Example 1:
# Input
# ["MyQueue", "push", "push", "peek", "pop", "empty"]
# [[], [1], [2], [], [], []]
# Output
# [null, null, null, 1, 1, false]
# Explanation
# MyQueue myQueue = new MyQueue();
# myQueue.push(1); // queue is: [1]
# myQueue.push(2); // queue is: [1, 2](leftmost is front of the queue)
# myQueue.peek(); // return 1
# myQueue.pop(); // return 1, queue is [2]
# myQueue.empty(); // return false

# Constraints:
# 1 <= x <= 9
# At most 100 calls will be made to push, pop, peek, and empty.
# All the calls to pop and peek are valid.

# Follow - up: Can you implement the queue such that each operation is amortized O(1) time complexity? In other words, performing n operations will take overall O(n) time even if one of those operations may take longer.
# ------------------------------------------------------------------------------------------------------------------------------
# Approach1: In ImplementStackUsingQueus - Approach1 what we did in the push that is using 2 Queues could be done here too, just with an exception that with popping in queues we get elements from index 0th towards the higher ones, while here with popping stacks we'll get items from last index to 0th one. Because of this property we need to seperate transferring and popping of items from a stack to the other.
class MyQueue:

    def __init__(self):
        self.stack=[]
        self.stack2=[]

    def push(self, x: int) -> None:
        self.stack2.append(x)
        for i in range(len(self.stack)):
            self.stack2.append(self.stack[i])
        for i in range(len(self.stack)):
            self.stack.pop()
        self.stack,self.stack2=self.stack2,self.stack

    def pop(self) -> int: #As constraints state only valide operation for this call, we dont put a check condition but directly return
        return self.stack.pop()

    def peek(self) -> int: #As constraints state only valide operation for this call, we dont put a check condition but directly return
        return self.stack[-1]

    def empty(self) -> bool:
        return len(self.stack)==0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
# TC: O(3n) Explanation: As all pop() and peek() are valid (as given in constraints) it is safe to assume push is called equal or more times than we call pop() and peek() collectively. In such cases we generalize push()'s time across all input cases - this is called amortized TC. Amortized is different than average case TC (how we say worst case or average case or best case time complexity) because of reason that average case TC considers the expected time taken by an algorithm over all possible inputs while amortized focuses on the average cost of a sequence of operations on the algo for possibly every single input, rather than the average cost over all possible inputs). Here as push is called more we generalize the TC using that which is n for  appending in stack2, n for popping from stack and n for swapping stack, and stack2
# SC: O(2n) SC: In push(), before popping from stack, both the stacks are holding n elements each


# Approach2: Better Space and Time Complexity - Rather than having to run pop() separately in a for-loop, we do an improvement here. Consider stack to be holding some items already in a reversed order somehow - now for each push() we'll first shift all stack items to stack2 by popping them; thus we'll have all items reversed in stack2. Now we'll append the new item on top in stack2 and transfer them all back to stack, by popping. Thus stack will get them reversed again and items will be in the wanted order.
"""def push(self, x: int) -> None:      #Only this function changes and so it's the only one copied here rather than whole class
    for i in range(len(self.stack)):
        self.stack2.append(self.stack.pop())
    self.stack2.append(x)
    for i in range(len(self.stack2)):
        self.stack.append(self.stack2.pop())"""
# TC: O(2n) Explanation: popping from stack for n times and then popping from stack2 for n times takes 2n in total
# SC: O(n)  Explanation: At no point both stacks are holding all items simultaneously but they are always in either one of the stack, thus we'll only hold n space


# Approach3: Better Amortized Time Complexity - As we notice push is called most times, we think of taking away some of its load and distributing it instead to the function that's called lesser times so the longer piece of code won't be frequently ran. For this we identify push() is not returning, and it doesn't matter anything how we arrange items in it, as far as pop(), and peek() returns right answers and empty() could check if there are items. Here is where intuition occurs that if we simply keep inserting elements in order they appear in push and only in pop or peek if we reverse them, we'll have better amortized TC, given that pop and peek are not only lesser called but also that they have O(1) TC, so now most functions will have more like O(n) frequency than anyone having much more, and it's a better generalization of TC. To make this viable, we still use 2 stacks and in push we insert items in stack2 which are popped and thus reversed in stack1, but in this attempt stack2 becomes empty and so that for next push we have all the items maintained, in push() we first transfer/pop all items from stack1 into stack2 before appending the new item. Also, this is good as it empties stack1 which would be further used in next pop which otherwise would have appended items on top of existing ones in it. Also, this means as we're maintaining 2 stacks either could be filled when empty() is checked and so there we do summation of length of both these arrays and check it it's 0.
class MyQueue:

    def __init__(self):
        self.stack = []
        self.stack2 = []

    def push(self, x: int) -> None:
        for i in range(len(self.stack)):
            self.stack2.append(self.stack.pop())
        self.stack2.append(x)

    def pop(self) -> int:
        for i in range(len(self.stack2)):
            self.stack.append(self.stack2.pop())
        return self.stack.pop()

    def peek(self) -> int:
        for i in range(len(self.stack2)):
            self.stack.append(self.stack2.pop())
        return self.stack[-1]

    def empty(self) -> bool:
        return len(self.stack) + len(self.stack2) == 0

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
# TC: O(n) Explanation: Amortized TC is now n as push or most of the operations are only taking n time
# SC: O(n) Explanation: Due transfer of items between 2 stacks with only popping unlike simple for-loop appending from one stack to other, here we'll have any given item at any item only in either of the stacks and thus collectiveyl both stacks will always ever use n space