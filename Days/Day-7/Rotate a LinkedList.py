# https://leetcode.com/problems/rotate-list/description/

# Rotate List
# Given the head of a linked list, rotate the list to the right by k places.

# Example 1:
# Input: head = [1, 2, 3, 4, 5], k = 2
# Output: [4, 5, 1, 2, 3]

# Example 2:
# Input: head = [0, 1, 2], k = 4
# Output: [2, 0, 1]

# Constraints:
# The number of nodes in the list is in the range[0, 500].
# -100 <= Node.val <= 100
# 0 <= k <= 2 * 10^9
# --------------------------------------------------------------------------------------------------------------------------------
# Approach1: for the given LL, for k times we'll repeat the process where in: everytime we'll traverse till the second last node and will point it to None, alongside making the last node point to the head.
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next:  # In case array is empty or has only 1 elem, return as is
            return head

        nextNode = head
        while k:
            k -= 1
            curr = nextNode
            while curr.next:
                prev = curr
                curr = curr.next
            prev.next = None
            curr.next = nextNode
            nextNode = curr
        return nextNode
# TC: O(kn) Explanation: for making a reversal, every time we'll stretch through entire list length i.e. n. So to make k reversals in n sized list TC will be O(kn)
# SC: O(1)

# Approach2: For a given linked list, if more reversals i.e. k, than the number of nodes are to be performed, then the result could be reduced to having k less than n. For example given the size of a linked list is 3 and we have to do 7 times the reversal of last item to front, the result would be the same as doing 1 reversal; as after three reversals the list would become how it was originally. So we save Time complexity by reducing k to k%n, if k>n. Now say if we have a 5 node linked list and have 3 reversals then basically uptill the second i.e. n-kth item, the items would stay as it is but from there it'll point to None and the last node in the list would start pointing to the head.
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # Handling Exception
        if not head or not head.next:
            return head

        # Counting total Nodes
        ct, temp = 0, head
        while temp:
            ct += 1
            temp = temp.next

        # Modify given k
        k %= ct
        if k == 0:  # This is important where no reversal has to be done or say, coz say head=[1,2] and k=0 then after below for-loop, curr'd be at 2. Further when curr=nextNode, curr becomes None and later `while curr.next` gives error, as None has no next property
            return head

        # Get to point which is to be last Node
        curr = head
        for i in range(ct - k - 1):
            prev = curr
            curr = curr.next

        # Point the next of to be Last Node to None
        nextNode = curr.next
        curr.next = None
        curr = nextNode

        # In the rest of portion after to be last node, go to very Last Node and make it point to starting of LL
        while curr.next:
            curr = curr.next
        curr.next = head

        return nextNode
# TC: O(2n) Explanation: n Time for counting total length of given linked list. Later, we'll just traverse to go till n-kth item, and after that we go to last node after n-kth and thus we collectively traversed n nodes again. Hence in total n+n time is taken which is generalised as n.
# SC: O(1)