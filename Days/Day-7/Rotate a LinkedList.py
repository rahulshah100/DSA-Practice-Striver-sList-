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
        if head == None or head.next == None:
            return head

        end = head
        while k:
            head = end # as end points to head after each reversal, the head must be shifted to the new starting of linked list.
            while end.next:
                secondlast = end #Also remember variable scope is it's function and not the loop. Hence secondlast could be accessed at #--1
                end = end.next
            end.next = head
            secondlast.next = None #--1
            k -= 1
        return end
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
        if head==None or head.next==None or k==0:
            return head
        temp, count=head, 0
        while temp:
            count+=1
            temp=temp.next
        temp.next=head #Last item points to head
        k=k%count      #reducing k to k%n
        lastNode=0
        while lastNode<count-k-1:
            head=head.next
            lastNode+=1
        temp=head.next #registering the starting of reversed list
        head.next=None #pointing n-kth item to None
        return temp
# TC: O(n) Explanation: n Time for counting total length of given linked list. Later, we'll just traverse for once to go till n-kth item. Hence in total n+n-k time is taken which is generalised as n.
# SC: O(1)