# https://leetcode.com/problems/reverse-nodes-in-k-group/

# Reverse Nodes in k-Group
# Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list. k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is. You may not alter the values in the list's nodes, only nodes themselves may be changed.

# Example 1:
# Input: head = [1,2,3,4,5], k = 2
# Output: [2,1,4,3,5]

# Example 2:
# Input: head = [1,2,3,4,5], k = 3
# Output: [3,2,1,4,5]

# Constraints:
# The number of nodes in the list is n.
# 1 <= k <= n <= 5000
# 0 <= Node.val <= 1000
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Approach1: For given linked list, we'll first check if k items are there and if so we'll reverse first pair of k items. Further the last elem of this reversed list would have it's next as a recursive function call to this same function this time with it's head passed at n-kth elem. If less than k items are found anytime then we'll return the given list as it is.
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        ct = k
        temp = head
        while ct and temp:
            ct -= 1
            temp = temp.next

        if not ct:  # This means ct became 0 and we are changing it to 1 i.e. we had k items for this iteration call
            curr = temp = head
            prev = None
            ct = k
            while ct:
                ct -= 1
                nextNode = curr.next
                curr.next = prev
                prev = curr
                curr = nextNode
            temp.next = self.reverseKGroup(curr, k)
            return prev  # Prev will be at the head, as linked list is reversed and curr would be at k+1th position from start of LL
        return head  # Only for when in last iteration if we have less than k items and if not ct condition is not worked out as ct is remaining and not 0, we dont wanna reverse items and return as is

# TC: O(2n) Explanation: n time collectively for counting k pairs throughout all function call. Further, for reversal we'll take a total O(n) time again. So total 2n work is done. Now although recursion is there but if we break down tree forming it's just that in n levels, collectively a 2n work/TC is done/utilised which has been counted already.
# SC: O(n) Total n/k calls would be made. Hence n/k Stack Space would be required which could be generalize as n.