# https://leetcode.com/problems/middle-of-the-linked-list/
# Middle of the Linked List:
# Given the head of a singly linked list, return the middle node of the linked list. If there are two middle nodes, return the second middle node.

# Example 1:
# Input: head = [1, 2, 3, 4, 5]
# Output: [3, 4, 5]
# Explanation: The middle node of the list is node 3.

# Example 2:
# Input: head = [1, 2, 3, 4, 5, 6]
# Output: [4, 5, 6]
# Explanation: Since the list has two middle nodes with values 3 and 4, we return the second one.

# Constraints: The number of nodes in the list is in the range[1, 100].
# 1 <= Node.val <= 100
# --------------------------------------------------------------------------------------------------------------------------------------------
# Approach1: We'll count the length of linked list from which we will calculate it's middle index. We'll then run a for loop to reach to the middle index. Till that iteration, the linked list which has been traversed that further, we'll return that linked list.
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr, ct = head, 0
        while curr:
            curr = curr.next
            ct += 1
        curr = head
        for i in range(ct // 2):
            curr = curr.next
        return curr
# TC: O(n + n//2) Explanation: n time to find the length + n//2 time to reach the mid from where we return output and exit the function.
# SC: O(1) Explanation: curr=head is a pass by reference and not pass by copy, because of head being an object i.e. mutable datatype. Hence curr wont incur a new space allocation but will refer/point at head's mem location itself.

# Approach 2: Tortoise Hayer method. We will use two: one fast and one slow pointer. Both starting from begining of linked list, slow will move one node at a time, while fast moves 2 nodes. As fast points to node whose next is None or the node itself is None, where our slow pointer is, it would be our middle index.
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head
        while fast and fast.next: #Not just head=None or [1] the while condition is optimal but also for [1,2] where at #--1 fast.next.next becomes None and next iteration of while loop wont run making this condition perfectly viable
            slow=slow.next
            fast=fast.next.next #--1
        return slow
#TC: O(n/2) Explanation: due to the fast pointer moving 2 nodes per iteration, in n/2 iterations, the loop should go through all n nodes. Hence n/2 is TC
#SC: O(1). Explanation: slow and fast are both just poiting/referring to head's mem location. So O(1) total space is used here.
