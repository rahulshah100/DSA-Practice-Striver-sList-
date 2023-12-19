# https://leetcode.com/problems/lru-cache/

# Design a data structure that follows the constraints of a Least Recently Used(LRU) cache.

# Implement the LRUCache class:
# LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
# int get(int key) Return the value of the key if the key exists, otherwise return -1.
# void put(int key, int value) Update the value of the key if the key exists.Otherwise, add the key - value pair to the cache.If the number of keys exceeds the capacity from this operation, evict the least recently used key.

# The functions get and put must each run in O(1) average time complexity.

# Example1:
# Input
# ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
# [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
# Output: [null, null, null, 1, null, -1, null, -1, 3, 4]

# Explanation
# LRUCache lRUCache = new LRUCache(2);
# lRUCache.put(1, 1); // cache is {1 = 1}
# lRUCache.put(2, 2); // cache is {1 = 1, 2 = 2}
# lRUCache.get(1); // return 1
# lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1 = 1, 3 = 3}
# lRUCache.get(2); // returns - 1 (not found)
# lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4 = 4, 3 = 3}
# lRUCache.get(1); // return -1(not found)
# lRUCache.get(3); // return 3
# lRUCache.get(4); // return 4

# Constraints:
# 1 <= capacity <= 3000
# 0 <= key <= 104
# 0 <= value <= 105
# At most 2 * 105 calls will be made to get and put.
# ---------------------------------------------------------------------------------------------------------------------------------------
# Approach1: Than stack/queue we here think of using Doubly linked list to store key, value in Nodes and alongside using a dictionary to store these nodes (i.e. their locations will be stored) as value across dictionary's keys; because in queue although FIFO order is by default maintained and thus removing the least recently used item which assuming is at bottom of queue, will be easy which implies for put() when capacity has been increased, and we have to remove LRU item, or when a key which is already there has been performed get() upon, and so we want the key, value pair to now be brought to top - in that case we can delete its prior occurrence in queue and simply insert it back on top of queue is all easy to achieve. And so it is (easy) in to perform put() where the key already exists, and we can delete its prior occurrence and insert back the new one on top of queue. In this we face only one issue/optimisation-opportunity that in queue for get() or put() to locate the key and then deleting it is something that takes O(n). This couldn't be helped by using a hashDict where although index at which the key is stored could be fetched but to reach that index we'll imminently have to keep doing .get() and thus popped items must be held in a temp_queue, where after popping the item we wanted to delete and not storing it in temp_queue all the earlier items now have to be re-transferred from temp_queue to our original queue. On the other hand using a Doubly LL i.e. we'll have pre-built head and tail as 2 nodes which will have a prev and next pointer pointing to None and tail in case of head and vice versa in case of tail, and new nodes with same pointers could keep being added in between; here using hashDict if we already have access to specific node then deleting is O(1) operation, coz we can just set node-to-be-deleted's previous node's next pointer to this node's next and this node's next node can have its previous set to this Node's previous. That is how deleting is achieved and to maintain the FIFO order, we make a point to store newly created Node's just after Head, thus the Node farthest from head i.e. the one pointed by tail's previous is Least recently used.
class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None


class LRUCache:
    def __init__(self, capacity: int):
        self.dict = {}
        self.capacity = capacity
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key in self.dict:
            value = self.removeKey(key)
            self.insertKey(key, value)
            return value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.dict:
            self.removeKey(key)
        elif len(self.dict) >= self.capacity:
            self.removeKey(self.tail.prev.key)
        self.insertKey(key, value)

    def removeKey(self, key):
        currNode = self.dict[key]
        currNode.prev.next = currNode.next
        currNode.next.prev = currNode.prev
        value = currNode.value
        del self.dict[key]
        return value

    def insertKey(self, key, value):
        newNode = Node(key, value)
        newNode.next = self.head.next
        newNode.prev = self.head
        self.head.next.prev = newNode
        self.head.next = newNode
        self.dict[key] = newNode

# TC: O(1) Explanation: In get() as well as put() there are no loops or other statements which will take proportional time as to any given capacity or anything for that matter, rather they run in constant time.
# SC: O(capacity) Explanation: As per given capactiy we can create as many Nodes and store as many items in self.dict i.e.O(2 * capacity) generalised as O(capacity)