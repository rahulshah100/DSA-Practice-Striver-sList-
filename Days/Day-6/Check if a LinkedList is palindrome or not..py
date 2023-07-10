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
# Approach 1: 2 Pointers Method=> As in singly linked list reverse front & back both traversal is not possible by default, so to keep comparing the front and back items we make the given linked list into an array and use a starting and ending pointers to compare items.
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

        l, u = 0, len(arr) - 1
        while l < u:
            if arr[l] != arr[u]:
                return False
            l += 1
            u -= 1
        return True
# TC: O(n) Explanation: n time to save n items in an array, and addition n/2 time to traverse the array using two pointers i & j. Total TC is n + n/2, so we can mention it as linear TC.
# SC: O(n) Explanation: to store n items in an array.

# Approach 2: We will use a fast and a slow pointer which will move by one and two nodes respectively, to find the middle node of given linked list. Starting from the head, as soon as fast->next or fast->next->next (in case of odd and in case of even number of nodes respectively) points to None, the slow pointer would be pointing at the middle node. From slow->next to the remaining part of linked list we will reverse it. Now, we will use a pointer from the starting of linked list and move slow to slow->next, so to further on compare node values pointed by both of these pointers. If till slow reaches None and items have matched, then we have a palindrom for a linked list.
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        fast = slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        curr = slow
        prev = None #If here we did prev = slow, then as both curr and prev will start pointing the same linked list, after #--1 the prev would still point to prev.next which due to #--1 will start pointing prev and list will become a cycle and hence undending.
        nextNode=None
        while curr:
            nextNode = curr.next
            curr.next = prev #--1
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