# https://leetcode.com/problems/reverse-nodes-in-k-group/

# Reverse Nodes in k-Group
# Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list. k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is. You may not alter the values in the list's nodes, only nodes themselves may be changed.

# Example 1:
# Input: head = [1,2,3,4,5], k = 2
# Output: [2,1,4,3,5]

# Example 2:
# Input: head = [1,2,3,4,5], k = 3
# Output: [3,2,1,4,5]

# Constraints:
# The number of nodes in the list is n.
# 1 <= k <= n <= 5000
# 0 <= Node.val <= 1000
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Approach1: Starting from begining of given linked list, we'll check if k items are there and if so we'll reverse first pair of k items. Further, on remaining list after first k item, we'll make a recursive call and keep reversing all the k item pairs as found. If less than k items found, we'll return the given list as it is.
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        count, node = 0, head
        while node and count < k: #this will ensure, k nodes items are left in the linked list
            node = node.next
            count += 1
        if count < k: return head #if nodes are not enough to form one more k item's group, we return the list as it is.
        ''' # print('1- head', head) '''
        new_head, prev = self.reverse(head, count) #for a group of k items, we'll get them reversed here. new_head will start from after k items in given list, while prev will only have k items here, but in a reversed fashion.
        ''' print('2-', 'new_head', new_head, '\nprev', prev, '\nhead', head, '\n') '''
        head.next = self.reverseKGroup(new_head, k) #We'll further break down the remaining list after k items, by calling it on the same function again on new_head which has after k items, and we'll set the response as head.next; head.next is a part of pre; As list is reversed, head.next which was starting is now pointing to the None. While this starting of this item would be pointed by prev. So by changing head.next, we'll see changes in prev.
        ''' # print('3-', 'new_head', new_head, '\nprev', prev, '\nhead', head, '\n') '''
        return prev #if a k sized group is found in the called linkedlist then prev would be returned as final output or output to it's calling function at the 'head.next=self.reverseKGroup' command. How head.next was initially always pointing to None, it will now have it's sublist's prev set as it's next. Prev is returned because after reversal of linked list, last node would become the starting and it would be pointed by prev.

    def reverse(self, head, count):
        prev, cur, nxt = None, head, head
        while count > 0: #Till we exhaust k, we'll reverse those many items, in the given linked list.
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
            count -= 1
        return (cur, prev)
# An Example and it's print command outputs:
# Input: [1,2,3,4,5] 2
# Print: 1- head ListNode{val: 1, next: ListNode{val: 2, next: ListNode{val: 3, next: ListNode{val: 4, next: ListNode{val: 5, next: None}}}}}
# 2- new_head ListNode{val: 3, next: ListNode{val: 4, next: ListNode{val: 5, next: None}}}
# prev ListNode{val: 2, next: ListNode{val: 1, next: None}}
# head ListNode{val: 1, next: None}

# 1- head ListNode{val: 3, next: ListNode{val: 4, next: ListNode{val: 5, next: None}}}
# 2- new_head ListNode{val: 5, next: None}
# prev ListNode{val: 4, next: ListNode{val: 3, next: None}}
# head ListNode{val: 3, next: None}

# 3- new_head ListNode{val: 5, next: None}
# prev ListNode{val: 4, next: ListNode{val: 3, next: ListNode{val: 5, next: None}}}
# head ListNode{val: 3, next: ListNode{val: 5, next: None}}

# 3- new_head ListNode{val: 3, next: ListNode{val: 5, next: None}}
# prev ListNode{val: 2, next: ListNode{val: 1, next: ListNode{val: 4, next: ListNode{val: 3, next: ListNode{val: 5, next: None}}}}}
# head ListNode{val: 1, next: ListNode{val: 4, next: ListNode{val: 3, next: ListNode{val: 5, next: None}}}}
# TC: O(2n) Explanation: for counting k pairs for f times such that kf=n, where n is total nodes, we'll set counter i.e.'count += 1' by iterating over k pairs for f times, taking O(n) time. Further in reverse we'll reducing count from k to 0 for f times, we'll again take O(n) time.
# SC: O(n) Explanation: Stack Space required to call requried recursive function at the worst possible point for space complexity is n/k. Say, for 17 nodes given with k=5, first recursive call would be made on node 6th to 17th, 2nd on 11th to 17, 3rd on 16th to 17th, which can be shown by 17/5=3. We generalize n/k as n.


# Approach2: Count elements and till count doesn't becomes zero, for a pair of k elements we'll preform iterative reversal usimg a prev,curr and next pointers where curr will stay the same for one pair of k elements and so prev would be used alongside next to reverse directions of nodes pointed by next. As a reversal for a k item is completed, we'll decrease count by k and check if count are enough to reverse a one more k items group. If we have to reverse, then before this, now we'll change the curr to starting of this group and again keep it constant for that group.
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        curr = head
        count = 0
        while curr:
            count += 1
            curr = curr.next

        dummy = ListNode(0)
        dummy.next = head
        prev = curr = nex = dummy  # doing it like this so it could initially fit the first two lines in below while loop.
        while count >= k:
            curr = prev.next
            nex = curr.next
            for i in range(1, k):
                curr.next = nex.next
                nex.next = prev.next
                prev.next = nex
                nex = curr.next
            count -= k
            prev = curr
        return dummy.next
# TC: O(2n) Explanation: for counting k pairs for f times such that kf=n, where n is total nodes, we'll set counter i.e.'count += 1' by iterating over k pairs for f times, taking O(n) time. Further in reverse we'll reducing count from k to 0 for f times, we'll again take O(n) time.
# SC: O(1)