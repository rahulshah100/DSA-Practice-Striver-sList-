# https://leetcode.com/problems/add-two-numbers/
# Add Two Numbers
# You are given two non - empty linked lists representing two non - negative integers.The digits are stored in reverse order, and each of their nodes contains a single digit.Add the two numbers and return the sum as a linked list.  You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Example 1:
# Input: l1 = [2, 4, 3], l2 = [5, 6, 4]
# Output: [7, 0, 8]
# Explanation: 342 + 465 = 807.

# Example 2:
# Input: l1 = [0], l2 = [0]
# Output: [0]

# Example 3:
# Input: l1 = [9, 9, 9, 9, 9, 9, 9], l2 = [9, 9, 9, 9]
# Output: [8, 9, 9, 9, 0, 0, 0, 1]

# Constraints:
# The number of nodes in each linked list is in the range[1, 100].
# 0 <= Node.val <= 9
# It is guaranteed that the list represents a number that does not have leading zeros.
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Approach1: To add two numbers, say: 342 and 9765, what we do is starting from behind we add 5 and 2 and put 7 at the back of the sumed number, then add 4 and 6 and get 10, from which we put 0 and one is carried so summed is 07. 3 is further added to 7 along with the one from carry, so it sums it up to 11, from which  one is carried and 1 is placed in summed, making it: 107. Further 1 from carry and 9 is added, so summed becomes: 10107. Here as linked list are already reversed, we can start from first node and keep adding node values alongside keeping a carry as needed, and do summation in normal procedure.
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        summed=dummy=ListNode(0)
        carry = 0
        while l1 or l2 or carry:
            sum=carry

            if l1:
                sum+=l1.val
                l1=l1.next
            if l2:
                sum+=l2.val
                l2=l2.next

            carry=sum//10
            sum%=10

            summed.next=ListNode(sum)
            summed=summed.next
        return dummy.next
# TC: O(max(m,n)) where m and n are length of LL1 and LL2 respectively Explanation: To sum up all the integers from both given linked list, we'll have to iterate for as many times as is the length of number/LL.
# SC: O(max(m,n)) where m and n are length of LL1 and LL2 respectively Explanation: If longer list is 10 integers, to store a new number holding summation of two given list, we'll have to store around 10 or 11 nodes only.