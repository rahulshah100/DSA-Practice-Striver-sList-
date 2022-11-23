# https://leetcode.com/problems/reverse-linked-list/

# Reverse a Linked List
# Given the head of a singly linked list, reverse the list, and return the reversed list.

# Example 1:
# Input: head = [1,2,3,4,5]
# Output: [5,4,3,2,1]

# Example 2:
# Input: head = [1,2]
# Output: [2,1]

# Example 3:
# Input: head = []
# Output: []

# Constraints:
# The number of nodes in the list is the range [0, 5000].
# -5000 <= Node.val <= 5000
# ------------------------------------------------------------------------------------------------------------------------

# NOTE: Although in above examples we see the given input:head as a list, but in reality the input we're getting is a linked list, to prepare which we'll have to have to custom make them as Objects. We would have to implement an insert method to push nodes one after the other in class ListNode and thus prepare an input to pass it as head. To get better understanding of this checkout ProblemsOrLearnings_OutsideOfStriverList/LinkedListBasicOperations. Hence, here I have not considered putting down entire solution which couold be ran; but in leetcode, on this question's link, we can paste this code in solution and would have to run it.

# Basics of linked list: It is an object, which has n items/nodes/object with each item pointing to it's consequtive other/others depending on singly/doubly or cirular linked list. In singly linked list, at the front, we'll have a head pointer pointing to the first node, and next of the last node in that linked list pointing to None.

# ------------------------------------------------------------------------------------------------------------------------
# Approach1: We will go through the given linked list and will keep creating new nodes with their previous ones being passed as the next.
# Definition for singly-linked list.   #----------this is given in leetcode text editor
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        # print(head) #O/P:ListNode{val: 1, next: ListNode{val: 2, next: ListNode{val: 3, next: ListNode{val: 4, next: ListNode{val: 5, next: None}}}}}
        prev = None
        while(head is not None):
            new_node = ListNode(head.val, prev)
            prev = new_node
            head = head.next
        return prev #At ending prev will be at begining and head will be pointing to None which will be the ending
# TC: O(n) Explanation: To traverse over n items in while loop, it will take n time.
# SC: O(n) Explanation: We'd have stored n extra nodes in prev at the ending.


# Approach2: Will go over all the items of given linked list and will swap their next nodes with a node before next node.
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr, prev, temp = head, None, None
        while curr:
            # This swapping is running nice, and is passing
            # temp=curr.next
            # curr.next=prev
            # prev=curr
            # curr=temp

            # This swapping is scrappy, and is not passing, but why??
            temp = prev
            prev = curr
            curr = curr.next
            print(curr)
            curr.next = temp
        return prev
S=Solution()
S.reverseList([1,2,3,4,5])
# TC: O(n) Explanation: while loop to go over a linked list of size n will be here taking n time.
# SC: O(1) Explanation: curr is being assigned to head and in python, assignment wont create a new copy but will make the variable assigned start pointing/referring to the variable it is being assigned to. Hence curr will take O(1) space only. Apart from that no other non-constant space occupancy is happening. So it is safe to say, above algo work with O(1) Space Complexity.