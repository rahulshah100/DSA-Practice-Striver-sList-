# https://leetcode.com/problems/merge-two-sorted-lists/
# Merge Two Sorted Lists:
# You are given the heads of two sorted linked lists list1 and list2. Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists. Return the head of the merged linked list.

# Example 1:
# Input: list1 = [1, 2, 4], list2 = [1, 3, 4]
# Output: [1, 1, 2, 3, 4, 4]

# Example 2:
# Input: list1 = [], list2 = []
# Output: []

# Example 3:
# Input: list1 = [], list2 = [0]
# Output: [0]

# Constraints: The number of nodes in both lists is in the range[0, 50].
# -100 <= Node.val <= 100
# Both list1 and list2 are sorted in non - decreasing order.
# ---------------------------------------------------------------------------------------------------------------------------------------------------------
# Approach1: We will go through all the items of both the given sorted linked lists and will keep on comparing and storing, in a different linked list, the smaller value amongst the both given arrays. We will start by creating a dummy Node, the next of which we'll return as our answer. We have to create a dummy so we can keep appending the nodes to it and form a linkedlist.
# Definition for singly-linked list.
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummyForHead = ListNode(0) #As in class ListNode, the second param is having None value as default, we can only pass one arguement here. 0 or any value here doesn't matter.
        temp = dummyForHead #So this is how we created two pointers pointing a same ListNode. We'll use dummyForHead as the Head Pointer and temp to keep adding new items in linkedlist we are creating
        while list1 != None and list2 != None:
            if list1.val < list2.val:
                temp.next = list1
                list1 = list1.next
            else:
                temp.next = list2
                list2 = list2.next
            temp = temp.next
        temp.next = list1 or list2  #If items are left in either linked lists, then we as such that linked list would be having values from there on, we'll take that whole set and directly append it to temp.next.
        return dummyForHead.next
# TC: O(n+m) Explanation: to go through n items of linked list 1 and to go through m items of linked list 2 we will in total take n+m time
# SC: O(n+m) Explanation: given that we are storing all items of both lists in a new list, we'll require extra n+m space to store all the items.

# Approach2: Improved space than approach1. If either of the linked lists are given None or Empty, we'll return the other. If both are None or empty, we'll return list2. We'll start with making list1 as our starting point and so will compare first elem of both given linked lists and if list2 is found to be having 0th index smaller than list1's, we'll swap list1 and list2. At this point list1 is pointed by the head. Further on we'll traverse all the items of list1 and list2. If the next of list1 is not none and it's value is less than list2's, we'll move to the further node in list1. If list1's next is None or smaller than list2's then we'll swap list1's next with list2 and will keep moving forward and checking for further elements.
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 or not list2:
            return list1 if not list2 else list2
        seek, target = (list1, list2) if list1.val < list2.val else (list2, list1)
        head = seek
        while seek and target:
            while seek.next and seek.next.val < target.val:
                seek = seek.next
            seek.next, target = target, seek.next
            seek = seek.next
        return head
# TC: O(m+n)
# SC: O(1)