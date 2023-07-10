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
# Approach1: Create a dummyNode with any arbitary value as a placeholder, which would be pointed as head. Now in a while loop uptill either list1 or list2 becomes 0, we'll run comparison between both pointer's value and smaller one would become a new Node pointed by existing dummyNode. Accordingly we'll keep incrementing list1 or list2 as well as dummyNode to it's next node. Further, to handle cases where list1 became None while list2 didnt or vice versa, we'll run while loop on those individual pointers. At last, head.next would be returned
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1==None: #This does take care, also of the case where list1=[]. So [] is how input is shown but in reality this doesnt show an empty array but it is just a way to represent input, as we're given in question we're given linked lists so what list1=[] really means is there are no Node Objects list1 is pointing to, implying it is pointed to None. So empty arr==None=> false but empty LL/LLpointer==None=>True
            return list2
        elif list2==None:
            return list1

        head=dummyNode=ListNode(0)

        while list1 and list2:
            if list1.val<=list2.val:
                dummyNode.next=ListNode(list1.val)
                list1=list1.next
            else:
                dummyNode.next=ListNode(list2.val)
                list2=list2.next
            dummyNode=dummyNode.next

        while list1:
            dummyNode.next=ListNode(list1.val)
            list1=list1.next
            dummyNode=dummyNode.next

        while list2:
            dummyNode.next=ListNode(list2.val)
            list2=list2.next
            dummyNode=dummyNode.next

        return head.next
# TC: O(m+n)
# SC: O(m+n) Explanation: Those many extra newNodes are made


# Approach2: Like Approach1 we'll create a placeholder Node with arbitary value pointed by 2 pointers. Now, unlike approach1 instead of creating newNode at each iteration, one pointer amongst the two pointing to placeholder node would make the next of placeholder node point to smaller value amongst list1 and list2. Later to accordingly increment list1 or list2's alongside incrementing pointer pointing to placeholder to now it's next. This will go on till list1 or list2 is None. Later we'll check if list1 is not empty will just append the whole of the remaining list at once or vice versa with list2. Finally returning the next of the other pointer pointing to placeholder Node.
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        temp = dummyForHead = ListNode(0)
        while list1 and list2:
            if list1.val < list2.val:
                temp.next = list1
                list1 = list1.next
            else:
                temp.next = list2
                list2 = list2.next
            temp = temp.next

        if list1:
            temp.next = list1
        elif list2:
            temp.next=list2

        return dummyForHead.next
# TC: O(n+m) Explanation: to go through n items of linked list 1 and to go through m items of linked list 2 we will in total take n+m time
# SC: O(1) Explanation: only a constant space utilizing ListNode object for val 0 has been created


# Approach3: More efficient space handling than approach2, using an in-place algorithm. Idea: with aid of an extra pointer- prev, while iterating through lists we'll keep comparing between nodes of both lists and keep making sure list1's node val is always smaller than list2's; we'll use prev to wove/interlace both the lists into 1 by following the  movement of list1 pointer. So we'll use a while loop to increment list1 till it's over. In any iteration, if list1's val is found bigger than list2's we'll swap list1 and list2. With this flipping of list1, our prev pointer will help to conjoin the current list with updates values of list1.
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 == None:
            return list2
        elif list2 == None:
            return list1

        if list1.val <= list2.val:
            pass
        else:
            list1, list2 = list2, list1

        prev = head = list1
        list1 = list1.next

        while list1:
            if list1.val <= list2.val:
                prev.next = list1
                list1 = list1.next
                prev = prev.next
            else:
                list1, list2 = list2, list1
        prev.next = list2
        return head
# TC: O(m+n)
# SC: O(1)