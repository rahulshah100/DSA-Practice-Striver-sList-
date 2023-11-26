# https://leetcode.com/problems/implement-stack-using-queues/

# Implement a last - in -first - out(LIFO) stack using only two queues.The implemented stack should support all the functions of a normal stack(push, top, pop, and empty).

# Implement the MyStack class:
# void push(int x) Pushes element x to the top of the stack.
# int pop() Removes the element on the top of the stack anreturns it.
# int top() Returns the element on the top of the stack.
# boolean empty() Returns true if the stack iempty, false otherwise. Notes:

# You must use only standard operations of a queue, which means that only push to back, peek / pop from front, size and is empty operations are valid.
# Depending on your language, the queue may not be supported natively.You may simulate a queue using a list or deque(double - ended queue) as long as you use only a queue 's standard operations.

# Example1:
# Input
# ["MyStack", "push", "push", "top", "pop", "empty"]
# [[], [1], [2], [], [], []]
# Output
# [null, null, null, 2, 2, false]
# Explanation
# MyStack
# myStack = new
# MyStack();
# myStack.push(1);
# myStack.push(2);
# myStack.top(); // return 2
# myStack.pop(); // return 2
# myStack.empty(); // return False

# Constraints:
# 1 <= x <= 9
# At most 100 calls will be made to push, pop, top, and empty.
# All the calls to pop and top are valid.

# Follow - up: Can you implement the stack using only one queue?
# -------------------------------------------------------------------------------------------------------------------
# Approach1: Using 2 Queues, if we can reverse the whole queue, then deleting its first item would be same as deleting the last item of original order of items; which is what stack does. Thus, once items are in reversed order in queue, pop() is taken care of and so is top(), where we'll only return queue.queue[0] now; whereas to implement empty() is also simple. All we have to do is take care of inserting new items in reversed fashion in push(). For this we initialize 2 already built queues out of which 1 is actual and second is a temp one used to aid in reversing items in original queue. We know adding item by default goes to top, but we want it reversed hence out of 2 queues, we put this item in a queue which is empty. Now the other queue that is holding all previously reversed items will shift them onto the first queue; for this shifting we to delete these items from the other queue and make it empty for next round where we can put a new item again in an empty queue. But if we noticed it wasn't the other queue and instead the first one, so we swap them both.
from queue import Queue

class MyStack:

    def __init__(self):
        self.queue = Queue()
        self.Q2 = Queue()

    def push(self, x: int) -> None:
        self.Q2.put(x)
        for i in range(self.queue.qsize()):
            self.Q2.put(self.queue.get())
        self.queue, self.Q2 = self.Q2, self.queue

    def pop(self) -> int: #As constraints state only valide operation for this call, we dont put a check condition but directly return
        return self.queue.get()

    def top(self) -> int: #As constraints state only valide operation for this call, we dont put a check condition but directly return
        return self.queue.queue[0]

    def empty(self) -> bool:
        return self.queue.qsize()==0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
# TC: O(2n) Explanation: push() uses 2n TC each time as push() executes, given that it shifts all items from queue to Q2 and then swaps them each of which consumes n time
# SC: O(n) Explanation: although 2 queues used 2nd queue is always empty after swapping and hence we'll always almost use n space


# Approach2: Better Time Complexity - instead of using a different array to reverse the item, we push new item on top first and then in the same queue all the items below the newly added one are reversed in a fashion that from 0th index to top-1, items are inserted over the newly added item. Eg: consider push() is made in order 1,4,6,2 then at first we'll only have 1; then 4 is inserted and we've 1,4 but below 4, we'll shift the items i.e. 1 to over the newly added item i.e. 4 and we'll have 4,1. Now we add 6 and we have 4,1,6 and we reverse items below 6 to get 6,4,1 and at last we add 2 to get 6,4,1,2 and reverse items below 2 to get 2,6,4,1 and thus we can see we've reversed all the items in queue.
from queue import Queue

class MyStack:

    def __init__(self):
        self.queue= Queue()

    def push(self, x: int) -> None:
        self.queue.put(x)
        for i in range(self.queue.qsize()-2,-1,-1):
            self.queue.put(self.queue.get())

    def pop(self) -> int:
        return self.queue.get()

    def top(self) -> int:
        return self.queue.queue[0]

    def empty(self) -> bool:
        return self.queue.qsize()==0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
# TC: O(n) Explanation: push() takes n TC each time as push() executes, given that we're only shifting all the item once from bottom to top
# SC: O(n) Explanation: only one queue is used which takes n space