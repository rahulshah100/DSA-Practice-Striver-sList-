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


# Approach2: Approach1 but more presentable:
"""class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        temp=dummy=ListNode(0)
        while list1 or list2:
            if not list2 or (list1 and list1.val<=list2.val):
                temp.next=ListNode(list1.val)
                list1=list1.next
            else:
                temp.next=ListNode(list2.val)
                list2=list2.next
            temp=temp.next
        return dummy.next"""
# Time and Space complexities same as above


# Approach3: Improvement in approach1 (could be done similarly with approach2) dont use new nodes for all the nodes of LL1 and LL2 but instead just create a starting Node pointed by dummy and temp such two variables, and it's next will directly point on to LL1 or LL2. Respectively the corresponding pointer will be increased.Like and so would the temp. Same process repeats and as we run out of loop, we then join rest of whichever amongst LL1 and LL2 is left.
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


# Approach4: More efficient space handling than approach2, by even avoiding creation of one extra dummy/head node. Along with given heads of two different LL we'll use 2 extra variable here: one for keeping note of new head of the combined LL and second to help us combine. So we'll iterate through arrays making sure that list 1 is having smaller value than list 2. If so we'll simply traverse list 1 to it's next node. If turns out LL 1 is greater, we swap List1 with List at that point and here's where 2nd extra pointer we created comes handy. Second pointer will keep following list1 in every step hence here after swap secondExtraPointer is at the point in former list1 till where it was shorted in ascending order. Now with list1 swapped we make secondExtraPointer's next as list1 just like we had it keep following. Now list1 is bound to run out on first than list2 and as that happens we just change temp's next to list 2
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list2: #this block is necessary to avoid errors starting at #--1
            return list1
        if not list1:
            return list2

        if list1.val > list2.val: #--1
            list1, list2 = list2, list1

        temp = newHead = list1

        while list1.next:
            if list1.next.val > list2.val:
                list1, list2 = list2, list1.next
            else:
                list1 = list1.next
            temp.next = list1
            temp = temp.next

        temp.next = list2

        return newHead
# TC: O(m+n)
# SC: O(1)