# https://leetcode.com/problems/palindrome-linked-list/

# Palindrome Linked List: Given the head of a singly linked list, return true if it is a palindrome or false otherwise.

# Example 1:
# Input: head = [1, 2, 2, 1]
# Output: true

# Example 2:
# Input: head = [1, 2]
# Output: false

# Constraints:
# The number of nodes in the list is in the range[1, 105]. 
# 0 <= Node.val <= 9
# ----------------------------------------------------------------------------------------------------------------------------------
# Approach 1: 2 Pointers Method=> As in singly linked list front & back both traversal is not possible by default, so to keep comparing the front and back items we make the given linked list into an array and use a starting and ending pointers to compare items.
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        arr = []
        while head:
            arr.append(head.val)
            head = head.next

        for i in range(len(arr)):
            if arr[i] != arr[len(arr) - i - 1]:
                return False

        return True
# TC: O(n) Explanation: n time to save n items in an array, and addition n/2 time to traverse the array using two pointers i & j. Total TC is n + n/2, so we can mention it as linear TC.
# SC: O(n) Explanation: to store n items in an array.

# Approach 2: Using turtle hayer method i.e. fast and slow pointer, we'll get slow pointer to either middle node or n//2+1th node in case of odd or even number of nodes respectively. Now say in [1,2,3,2,1] slow is at 3; starting from slow we'll reverse the rest of the list so we'll have 1->2->3<--------             #Side example for even nums: [17, 23, 23, 17]       17->23->23<---------
#      None<------|        |                                                                          |         |
#                          |<--2<--1                                                                  -->None   17
# This reversal is done using 3 pointer method curr,next and prev. So at the end of reversal we'll have prev at last being right most 1, which goes to 2 and then 3 and then None. Such is the flow of head starting from left most 1. Taking benefit of this, we run a while loop where we compare head and prev's values. If they don't match before prev becomes None in while-loop we return False or else True.
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        fast = slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        curr = slow
        prev = None
        nextNode=None
        while curr:
            nextNode = curr.next
            curr.next = prev
            prev = curr
            curr = nextNode

        while prev:
            if head.val != prev.val:
                return False
            head = head.next
            prev = prev.next
        return True
# TC: O(1.5n) Explanation: n/2 time till slow will be at the middle. n/2 time to reverse the later half of linked list, from after where slow is pointing. n/2 time more, for comparing item's pointed by slow till slow traverses and becomes none.
# SC: O(1)