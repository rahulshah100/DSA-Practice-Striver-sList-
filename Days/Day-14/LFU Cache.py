# https://leetcode.com/problems/lfu-cache/

# Design and implement a data structure for a Least Frequently Used (LFU) cache.

# Implement the LFUCache class:
# LFUCache(int capacity) Initializes the object with the capacity of the data structure.
# int get(int key) Gets the value of the key if the key exists in the cache.Otherwise, returns - 1.
# void put(int key, int value) Update the value of the key if present, or inserts the key if not already present.When the cache reaches its capacity, it should invalidate and remove the least frequently used key before inserting a new item.For this problem, when there is a tie(i.e., two or more keys with the same frequency), the least recently used key would be invalidated. To determine the least frequently used key, a use counter is maintained for each key in the cache.The key with the smallest use counter is the least frequently used key.

# When a key is first inserted into the cache, its use counter is set to 1(due to the put operation).The use counter for a key in the cache is incremented either a get or put operation is called on it.

# The functions get and put must each run in O(1) average time complexity.

# Example1:
# Input
# ["LFUCache", "put", "put", "get", "put", "get", "get", "put", "get", "get", "get"]
# [[2], [1, 1], [2, 2], [1], [3, 3], [2], [3], [4, 4], [1], [3], [4]]
# Output
# [null, null, null, 1, null, -1, 3, null, -1, 3, 4]

# Explanation
# // cnt(x) = the use counter for key x
# // cache = [] will show the last used order for tiebreakers(leftmost element is most recent) LFUCache
# lfu = new LFUCache(2);
# lfu.put(1, 1);  // cache = [1, _], cnt(1) = 1
# lfu.put(2, 2);  // cache = [2, 1], cnt(2) = 1, cnt(1) = 1
# lfu.get(1);     // return 1
#                 // cache = [1, 2], cnt(2) = 1, cnt(1) = 2
# lfu.put(3, 3);  // 2 is the LFU key because cnt(2) = 1 is the smallest, invalidate 2.
#                 // cache = [3, 1], cnt(3) = 1, cnt(1) = 2
# lfu.get(2);     // return -1(not found)
# lfu.get(3);     // return 3
#                 // cache = [3, 1], cnt(3) = 2, cnt(1) = 2
# lfu.put(4, 4);  // Both 1 and 3 have the same cnt, but 1 is LRU, invalidate 1.
#                 // cache = [4, 3], cnt(4) = 1, cnt(3) = 2
# lfu.get(1);     // return -1(not found)
# lfu.get(3);     // return 3
#                 // cache = [3, 4], cnt(4) = 1, cnt(3) = 3
# lfu.get(4);     // return 4
#                 // cache = [4, 3], cnt(4) = 2, cnt(3) = 3

# Constraints:
# 1 <= capacity <= 104
# 0 <= key <= 105
# 0 <= value <= 109
# At most 2 * 105 calls will be made to get and put.
# ---------------------------------------------------------------------------------------------------------------------------------------
# Approach1: Essentially from LRU Cache.py here we'll try creating one more hashMap i.e. freq_list_map which is storing frequency as keys and against which we'll have a doubly Linked list which will have all the Nodes whose keys would have a frequency identical to this dictionary's current key. An in these doubly LL, that we have across frequencies in freq_list_map they'll follow an LRU order of insertion and deletion. We'll always keep track of the minimum frequency min_freq with a separate variable and when we have to delete item least frequently used, then we'll delete the last Node from freq_list_map's DLL stored across min_freq. So that for a given node it'll be easier for us to keep track of a node's frequency, Node class is provided with a count attribute.
class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.cnt = 1
        self.prev = None
        self.next = None


class List:
    def __init__(self):
        self.size = 0
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def add_front(self, node):
        temp = self.head.next
        node.next = temp
        node.prev = self.head
        temp.prev = node
        self.head.next = node
        self.size += 1

    def remove_node(self, del_node):
        del_prev = del_node.prev
        del_next = del_node.next
        del_prev.next = del_next
        del_next.prev = del_prev
        self.size -= 1


class LFUCache:
    def __init__(self, capacity):
        self.key_node = {}
        self.freq_list_map = {}
        self.max_size_cache = capacity
        self.min_freq = 0
        self.curr_size = 0 #count of total nodes i.e. all the nodes through all the frequencies

    def update_freq_list_map(self, node):
        del self.key_node[node.key]
        self.freq_list_map[node.cnt].remove_node(node)

        if node.cnt == self.min_freq and self.freq_list_map[node.cnt].size == 0:
            self.min_freq += 1

        if node.cnt + 1 in self.freq_list_map:
            next_higher_freq_list = self.freq_list_map[node.cnt + 1]
        else:
            next_higher_freq_list = List()
        node.cnt += 1
        next_higher_freq_list.add_front(node)

        self.freq_list_map[node.cnt] = next_higher_freq_list
        self.key_node[node.key] = node

    def get(self, key):
        if key in self.key_node:
            node = self.key_node[key]
            value = node.value
            self.update_freq_list_map(node)
            return value
        return -1

    def put(self, key, value):
        if self.max_size_cache == 0: #Where cache capacity is Zero
            return

        if key in self.key_node:
            node = self.key_node[key]
            node.value = value
            self.update_freq_list_map(node)
        else:
            if self.curr_size == self.max_size_cache:
                list_to_remove_from = self.freq_list_map[self.min_freq]
                del self.key_node[list_to_remove_from.tail.prev.key]
                list_to_remove_from.remove_node(list_to_remove_from.tail.prev)
                self.curr_size -= 1

            self.curr_size += 1
            self.min_freq = 1

            if self.min_freq in self.freq_list_map:
                new_list = self.freq_list_map[self.min_freq]
            else:
                new_list = List()
            new_node = Node(key, value)
            new_list.add_front(new_node)
            self.key_node[key] = new_node
            self.freq_list_map[self.min_freq] = new_list
# TC: O(1) Explanation: We are not using any loops or anything, it's all one time executable bunch of code for both get() and put().
# SC: O(3n) Explanation: For one item, it's entry in key_node, freq_list_temp and as a Node occupies 3 times the space