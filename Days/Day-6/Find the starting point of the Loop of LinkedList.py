# https://leetcode.com/problems/linked-list-cycle-ii/

# Linked List Cycle II
# Given the head of a linked list, return the node where the cycle begins.If there is no cycle, return null. There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer.Internally, pos is used to denote the index of the node that tail's next pointer is connected to (0-indexed). It is -1 if there is no cycle. Note that pos is not passed as a parameter. Do not modify the linked list.

# Example 1:
# Input: head = [3, 2, 0, -4], pos = 1
# Output: tail connects to node index 1
# Explanation: There is a cycle in the linked list, where tail connects to the second node.

# Example 2:
# Input: head = [1, 2], pos = 0
# Output: tail connects to node index 0
# Explanation: There is a cycle in the linked list, where tail connects to the first node.

# Example 3:
# Input: head = [1], pos = -1
# Output: no cycle Explanation: There is no cycle in the linked list.

# Constraints:
# The number of the nodes in the list is in the range[0, 104].
# -10^5 <= Node.val <= 10^5
# pos is -1 or a valid index in the linked - list.
# --------------------------------------------------------------------------------------------------------------------------------------------------------------
# Approach1: Using a hashmap. Traverse the linked list while checking for every node if the node's id is present in hashmap. If so, return the head, if not then store the node's id. If whole traversal through LL completes i.e. LL pointer points to None, then we return designated value showing no cycle present
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        hash={}
        while head:
            if id(head) in hash:
                return head
            hash[id(head)]=head
            head=head.next
        return None
# TC: O(n) Explanation: due to storage of id in hashmap the 'not in' operation will only take O(1), as keys are simpler.
# SC: O(n) Explanation: to store n id's as keys and n nodes as values, 2n space would be taken, which is generalized as O(n);

# Approach2: Turtle Hayer Method: Taking a fast and a slow pointer which moves two and one node respectively; as they meet, we'll shift the fast pointer back to the starting of linked list and now move it one node at a time until it meets slow pointer again. This time the colliding point we have is the starting point of our loop, for given linked list. On contrary, if fast becomes None, then that'd mean no cycle is there and we will return None. To see proof/intution of this logic check out:https://www.youtube.com/watch?v=QfbOhn0WZ88&list=PLgUwDviBIf0p4ozDR_kJJkONnb1wdx2Ma&index=37&ab_channel=takeUforward
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast = slow = head
        while fast and fast.next: #--1
            fast=fast.next.next
            slow=slow.next
            if fast==slow:
                fast=head
                while fast!=slow:
                    fast=fast.next
                    slow=slow.next
                return fast
        return None
# TC: O(n) Explanation: Two pointers might take couple of turns in a loop before meeting but still that would be expressed in linear time complexity, making it O(N).
# SC: O(1)


# Approach2: Just a Different way of writing
"""
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                break
        if not fast or not fast.next:  #At this point we dont know how we got out of above while block 1). if fast became == slow and thus break was triggered or 2).fast/fast.next became null and while block got terminated, in which case coz we reached None we know given LL does not have a Cycle and would want to return None. Hence to check if it is 2) we use this if block here.
            return None

        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next

        return slow
"""