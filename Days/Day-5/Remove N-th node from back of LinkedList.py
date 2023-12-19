# https://leetcode.com/problems/remove-nth-node-from-end-of-list/
# Remove Nth Node From End of List
# Given the head of a linked list, remove the nth node from the end of the list and return its head.

# Example 1:
# Input: head = [1, 2, 3, 4, 5], n = 2
# Output: [1, 2, 3, 5]

# Example 2:
# Input: head = [1], n = 1
# Output: []

# Example 3:
# Input: head = [1, 2], n = 1
# Output: [1]

# Constraints:
# The number of nodes in the list is sz.
# 1 <= sz <= 30
# 0 <= Node.val <= 100
# 1 <= n <= sz
# ---------------------------------------------------------------------------------------------------------------------------------------------------
# Approach1: To figure the number of node that has to be removed from front, we'll calculate total length of linked list and will subtract given n from it. Further in a loop, we'll traverse nodes in the given linked list until we're at the node which is right before the node to be removed. Once there, we'll bypass the node that is to be removed, by setting it's previous node's next as next.next.
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        traverseHead = head
        length = 0
        while traverseHead:
            length += 1
            traverseHead = traverseHead.next

        if length - n == 0:  # for test case like [1] and n=1 or [1,2] and n=2, where due to length-n==0 the below for loop wont run and the below line #--1 will directly skip iterating over the first item that might have to be removed.
            return head.next

        traverseHead = head
        for i in range(length - n - 1):
            head = head.next

        head.next = head.next.next #--1
        return traverseHead
# TC: O(2n) Explanation: while loop takes n time to compute legth by traversing n nodes. for loop can take n time additional, in worst case.
# SC: O(1)


# Approach2: Averting the if condition used in Approach1 by creating an Extra Node, and avoiding count method by using 3 pointers. We'll create an extra node, at which dummy, slow and fast pointers will initially be pointing. fast's next would be pointed at the head and further in a for loop, we'll traverse fast as fast.next uptill nth item. Once fast is at nth item, now we'll start moving slow parallely with fast, uptill fast.next is not detected to be None, at which point we'll set slow's next as it's next.next
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        fast=slow=dummy=ListNode(0)
        fast.next=slow.next=head
        for i in range(n):
            fast=fast.next
        while fast.next:
            slow=slow.next
            fast=fast.next
        slow.next=slow.next.next #--2
        return dummy.next
# TC:O(n) Explanation:fast will at max traverse for one length of given array before fast.next becomes Null, and that's when we're returning the answer.
# SC: O(1) Explanation: Dummy Node is taking 1 constant space, apart from which nothing else occupies any space.


# Approach 3: Trading off the use of dummy node from Appraoch2 with an extra if block to handle edge cases. So like Approach 1, we'll seperately take care of edge cases where the very first item of list has to be deleted.
class Solution:
    def removeNthFromEnd(self, head, n):
        fast = slow = head
        for _ in range(n):
            fast = fast.next
        if fast==None: #Eg: in [1,2] to remove 1, n will be 2. So above for loop will run for 0,1. Given that fast=head =>fast=1 and so for loop iterations makes fast as 2 and then None. Triggering this block.
            return head.next
        while fast.next:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return head
# TC:O(n)
# SC: O(1)