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

# Basics of linked list: It is an object, which has n items/nodes/object with each item pointing to it's consequtive other/others depending on singly/doubly or cirular linked list. In singly linked list, at the front, we'll have a head pointer pointing to the first node, and next of the last node in that linked list pointing to None.

# NOTE: Although in above examples we see the given input as a list, but in reality the input we're getting is a linked list; to prepare which we'll have to have to custom make it as Object. We would have to implement an insert method to push nodes one after the other in class ListNode and thus prepare head (name of input array in pre-given code of this problem). To get better understanding of this checkout the dir structure ../ProblemsOrLearnings_OutsideOfStriverList/LinkedListBasicOperations. Hence, here I have not considered putting down entire solution which couold be ran; but in leetcode, on this question's link, we can paste as much code in solution as given below and it could be ran.

# ---------------------------------------------------------------------------------------------------------------------------------------
# Approach1: Starting with a prev=None we start traversing the given linked list from begining, each time while creating a new node where currently traversed node's val will be new node's val and it's next pointing to prev, after which we'll update prev to this newly made node.
# Definition for singly-linked list.   #----------this is given in leetcode text editor
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        # print(head) #O/P:ListNode{val: 1, next: ListNode{val: 2, next: ListNode{val: 3, next: ListNode{val: 4, next: ListNode{val: 5, next: None}}}}}
        prev = None
        while (head is not None):
            new_node = ListNode(head.val, prev)
            prev = new_node
            head = head.next
        return prev  # At ending prev will be at begining and head will be pointing to None which will be the ending so we return prev here as whole/starting of LL

# TC: O(n) Explanation: To traverse over n items in while loop, it will take n time.
# SC: O(n) Explanation: We'd have stored n extra nodes in prev at the ending.


# Approach2: While going over the entire linked list we'll maintain 3 variables keeping track of current, previous and next node. With each iteration, next node will be marked first as current's next node, then current's next will be made point to it's previous. Now beacuse next is already stored we dont worry about not reaching current's next node by curr.next which is now pointing to prev node, bacuse next Node could be accessed with next variable. Further the prev node will become current and curr will become next node.
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr, nextNode = None, head, None
        while curr:
            nextNode = curr.next
            curr.next = prev
            prev = curr
            curr = nextNode
        return prev

S = Solution()
S.reverseList([1, 2, 3, 4, 5])
# TC: O(n) Explanation: while loop to go over a linked list of size n will be here taking n time.
# SC: O(1) Explanation: The assignment curr = head does not create a new copy of the linked list but simply referrs the head node's mem block to the curr variable. This is because mutable datatypes in python i.e. array,dict,set and objects are not passed by value but implicity passed by reference always in Python which is further explained in ../ProblemsOrLearnings_OutsideOfStriverList/'Shallow, Deep Copy and Assignment Operations' and ../ProblemsOrLearnings_OutsideOfStriverList/'Variable Scope in Functions and Recursions'. Hence curr, nextNode and prev will take O(1) space only. So it is safe to say that above algo work with O(1) Space Complexity.
