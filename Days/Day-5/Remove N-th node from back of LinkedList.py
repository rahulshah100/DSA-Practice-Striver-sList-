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

        traverseHead = head
        start = traverseHead
        for i in range(length - n - 1):
            print("Ok")
            head = head.next
        if length - n - 1 < 0:  # for test case like [1] and n=1 or [1,2] and n=2, where due to length-n-1<0, the above for loop wont run and the below line #--1 will directly skip iterating over the first item that might have to be removed.
            return head.next
        head.next = head.next.next #--1
        print(traverseHead)
        return traverseHead
# TC: O(2n) Explanation: while loop takes n time to compute legth by traversing n nodes. for loop can take n time additional, in worst case.
# SC: O(1)


# Approach2: We'll create a dummy node, at which slow and fast pointers will initially be pointing. Futher, for given n i.e. number of elem to be deleted from behind, we'll set fast's next as the given linked list's value and will traverse fast in given linked list uptill nth item. Once fast is at nth item, now we'll start moving slow parallely with fast, uptill fast.next is detected to be None, in which case we'll set next as next.next.
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy=ListNode(0) #This value:0 wont matter as we'll directly return dummy.Next as O/P
        fast, slow= dummy, dummy #Both points to dummy Node
        fast.next=head #the dummyNode's next for fast and slow gets set to head
        slow.next=head
        print(0,slow,'\n',fast,'\n',dummy,'\n\n')
        for i in range(0,n):
            fast=fast.next
        print(1,slow,'\n',fast,'\n',dummy,'\n','\n')
        while fast.next:
            slow=slow.next
            fast=fast.next
            print(2,slow,'\n',fast,'\n',dummy,'\n\n')
        slow.next=slow.next.next #--2
        return dummy.next #As slow and fast pointers are way ahead in linked list traversal, if we return them with fast mostly we'll get None as output while with slow, the elems later than what had to deleted is what will be outputted. However, as fast and slow are assigned to dummy, they're all three pointing at the same mem location and hence at #--2 when we made a change with slow, that change was inscribed in mem location pointed by all three variables i.e.dummy, fast, slow. However as dummy is not moved, if we output it we'll get the whole list from starting with the appropriate elems removed.
# TC:O(n) Explanation:fast will at max traverse for one length of given array before fast.next becomes Null, and that's when we're returning the answer.
# SC: O(1) Explanation: Dummy Node is taking 1 constant space, apart from which nothing else occupies any space.


# Approach 3: Trading off the use of dummy node from Appraoch2  with an extra if block to handle edge cases. So like Approach 1, we'll seperately take care of edge cases where the very first item of list has to be deleted.
class Solution:
    def removeNthFromEnd(self, head, n):
        fast = slow = head
        for _ in range(n):
            fast = fast.next
        if not fast: #for edge cases
            return head.next
        while fast.next:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return head
# TC:O(n) Explanation:fast will at max traverse for one length of given array before fast.next becomes Null, and that's when we're returning the answer.
# SC: O(1)