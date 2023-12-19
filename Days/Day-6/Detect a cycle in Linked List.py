# https://leetcode.com/problems/linked-list-cycle/

# Linked List Cycle
# Given head, the head of a linked list, determine if the linked list has a cycle in it. There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter. Return true if there is a cycle in the linked list.Otherwise, return false.

# Example1:
# Input: head = [3, 2, 0, -4], pos = 1
# Output: true
# Explanation: There is a cycle in the linked list, where the tail connects to the 1 st node(0 - indexed).

# Example2:
# Input: head = [1, 2], pos = 0
# Output: true
# Explanation: There is a cycle in the linked list, where the tail connects to the 0 th node.

# Example3:
# Input: head = [1], pos = -1
# Output: false
# Explanation: There is no cycle in the linked list.

# Constraints: The number of the nodes in the list is in the range[0, 104]. -105 <= Node.val <= 105 pos is -1 or a valid index in the linked - list.
# -------------------------------------------------------------------------------------------------------------------------------------------------
# Approach1: Using a dict hashmap to store the node's address while traversing the LL. If we encounter a node which is not in hashmap we'll add it, and if it is then it got repeated and so we'll return the node. If whole traversal of LL completes, we'll return False
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        hashmap={}
        while head:
            if id(head) in hashmap:
                return True
            hashmap[id(head)]=head
            head=head.next
        return False
# TC: O(n) Explanation: As we're using the address of nodes which are simple integers as keys, the hashing/the 'in' operator wont take more than O(1), in which case, only n time is taken to traverse the n nodes.
# SC: O(n) Explanation: Using a dict to store n key-value pairs.

# Approach2: Tortoise Hare method. Using two pointers: fast and slow, we'll traverse the given linked list till fast or slow becomes None. Moving fast pointers by 2 Nodes and slow by 1 Node, if fast and slow matches, it means there is a cycle in given linked list and we'll return True. If fast or slow becomes none, then that means we are not having a loop in the given linked list and so we'll return False.
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast = slow = head
        while fast and fast.next: #Ensuring fast and fast.next is not be None is necessary. As fast.next is known here to be something, then after that something even if there is None then it is fine as at #--1 fast.next.next will be None and not that fast.next will be none coz then it'sll be None.next. Further in next iteration we have to ensure we stop which is why we put fast too here.
            fast = fast.next.next #--1
            slow = slow.next
            if slow == fast:
                return True
        return False
# TC: O(n) Explanation: Even if fast and slow takes couple of turns over the given linked list before matching, we will still have time complexity in Linear terms which can be shown as O(n).
# SC: O(1)