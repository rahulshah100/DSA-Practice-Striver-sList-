# https://www.codingninjas.com/studio/problems/implement-queue-using-arrays_8390825?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf

# Queue is a linear data structure that follows the idea of First In First Out. That means insertion and retrieval operations happen at opposite ends.
# Implement a simple queue using arrays.
# You are given 'query' queries which are either of the 2 types:
# 1 'e': Enqueue (add) element ‘e’ at the end of the queue.
# 2: Dequeue (retrieve) the element from the front of the queue. If the queue is empty, return -1.

# Example:
# Input: Queries:
#              [ 1 2,
#                1 7,
#                2,
#                1 13,
#                2,
#                2,
#                2 ]
# Output:
#          [ 2,
#            7,
#            13,
#            -1 ]
# Explanation: After each operation, our queue is equal to the following:
# 1 2: {2}
# 1 7: {2, 7}
# 2: {7} and 2 is printed
# 1 13: {7, 13}
# 2: {13} and 7 is printed
# 2: {} and 13 is printed
# 2: {} and -1 is printed since the queue is empty.

# Detailed explanation ( Input/output format, Notes, Images )
# Sample Input 1:
# 7
# 1 2
# 1 7
# 2
# 1 13
# 2
# 2
# 2
# Sample Output 1:
# 2 7 13 -1

# Explanation Of Sample Input 1 :
# After each operation, our queue is equal to the following:
# 1 2: {2}
# 1 7: {2, 7}
# 2: {7} and 2 is printed
# 1 13: {7, 13}
# 2: {13} and 7 is printed
# 2: {} and 13 is printed
# 2: {} and -1 is printed since the queue is empty.

# Sample Input 2 :
# 4
# 2
# 2
# 1 2
# 1 4
# Sample Output 2 :
# -1 -1

# Explanation Of Sample Input 2 :
# After each operation, our queue is equal to the following:
# 2: {} and -1 is printed since the queue is empty.
# 2: {} and -1 is printed since the queue is empty.
# 1 2: {2}
# 1 4: {2, 4}

# Expected time complexity :
# Both the enqueue() and dequeue() functions should solve in constant time, that is O(1) time complexity.

# Constraints:
# 1 <= ‘query’ <= 10^5
# 1 <= ‘e’ <= 10^6
# -------------------------------------------------------------------------------------------------------------------------------------------
# Solution - For the given problem, according to the given infrastructure: Mainly with queues we'll have an array of fixed size; where a front and rear pointer will be used to pop and insert a new item respectively. In doing so, when an item's popped that index is emptied and moved forward to the next filled item, thus at one point front will be increased to last point in array and say in between rear kept on adding new items, where to add them? Answer is the starting indexes that have been poped and emptied, but how to access them? For this we'll always increment rear even beyond size of array and always refer to it as rear%len(arr) which will find it's appropriate location within bounds of array indexes. Similarly, for front we'll continuously increment it, and we'll refer to it as front%len(arr) instead of front.
class Queue:
    def __init__(self):
        self.front = 0
        self.rear = 0
        self.arr = [0] * 100001

    #  Enqueue (add) element 'e' at the end of the queue.
    def enqueue(self, e: int) -> None:
        if self.arr[self.rear % len(self.arr)] == 0:  # Checking the index is empty
            self.arr[self.rear % len(self.arr)] = e
            self.rear += 1

    #  Dequeue (retrieve) the element from the front of the queue.
    def dequeue(self) -> int:
        if self.front % len(self.arr) != self.rear % len(self.arr):
            currFirst = self.arr[self.front % len(self.arr)]
            self.arr[self.front % len(self.arr)] = 0  # Emptying this index
            self.front += 1
            return currFirst
        return -1

# TC: O(1) Explanation: for a Queue operation TC is O(1) in either of enque or deque's case
# SC: O(n) Explanation: for storing a Queue of length n
# ------------------------------------------------------------------------------------------------------------------------------------------
# Couple of extra function implementations in Queue
    def printAllTheElems(self):
        for i in range(self.front%len(self.arr), self.rear%len(self.arr) + 1):
            print(self.arr[i])

    def countQueueSize(self):
        ct=0
        for i in range(self.front%len(self.arr), self.rear%len(self.arr) + 1):
            ct+=1
        return ct

    def isEmpty(self):
        return (self.rear % len(self.arr)) == (self.front % len(self.arr)) and self.arr[self.rear % len(self.arr)] == 0
# ------------------------------------------------------------------------------------------------------------------------------------------
# Python has an in-built queue library which has PriorityQueues, LifoQueue and some other Data Structures from which we import Queue
from queue import Queue

myQueue = Queue()

# Insert/Enqueue
myQueue.put(1)
myQueue.put('12')
myQueue.put(9)

# Pop/Dequeue
print('Popped Item', myQueue.get()) #Popped Item 1

print('Is Queue empty?:', myQueue.empty()) #Is Queue empty?: False
print("Size of Queue", myQueue.qsize()) #Size of Queue 2

# Print the top
print("Top of Queue",myQueue.queue[0]) #Top of Queue 12

# Print all items
print("\nAll items in Queue:")      #All items in Queue:
for i in range(myQueue.qsize()):    #12
    print(myQueue.queue[i])         #9