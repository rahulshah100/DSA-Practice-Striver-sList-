# https://leetcode.com/problems/intersection-of-two-linked-lists/
# Find intersection point of Y LinkedList
# Given the heads of two singly linked - lists headA and headB, return the node at which the two lists intersect.If the two linked lists have no intersection at all, return null. For example, the following two linked lists begin to intersect at node c1: The test cases are generated such that there are no cycles anywhere in the entire linked structure. Note that the linked lists must retain their original structure after the function returns.

# Custom Judge:  The inputs to the judge are given as follows(your program is not given these inputs): intersectVal - The value of the node where the intersection occurs.This is 0 if there is no intersected node. listA - The first linked list. listB - The second linked list. skipA - The  number of nodes to skip ahead in listA(starting from the head) to get to the intersected node. skipB - The number of nodes to skip ahead in listB(starting from the head) to get to the intersected node. The judge will then create the linked structure based on these inputs and pass the two heads, headA and headB to your program.If you correctly return the intersected node, then your solution will be accepted.

# Example 1:
# Input: intersectVal = 8, listA = [4, 1, 8, 4, 5], listB = [5, 6, 1, 8, 4, 5], skipA = 2, skipB = 3
# Output: Intersected at '8'
# Explanation: The intersected node's value is 8 (note that this must not be 0 if the two lists intersect). From the head of A, it reads as [4, 1, 8, 4, 5].From the head of B, it reads as [5, 6, 1, 8, 4, 5].There are 2 nodes before the intersected node in A; There are 3 nodes before the intersected node in B. - Note that the intersected node's value is not 1 because the nodes with value 1 in A and B (2nd node in A and 3rd node in B) are different node references. In other words, they point to two different locations in memory, while the nodes with value 8 in A and B (3rd node in A and 4th node in B) point to the same location in memory.

# Example 2:
# Input: intersectVal = 2, listA = [1, 9, 1, 2, 4], listB = [3, 2, 4], skipA = 3, skipB = 1
# Output: Intersected at '2'
# Explanation: The intersected node's value is 2 (note that this must not be 0 if the two lists intersect). From the head of A, it reads as [1, 9, 1, 2, 4].From the head of B, it reads as [3, 2, 4].There are 3 nodes before the intersected node in A; There are 1 node before the intersected node in B.

# Example 3:
# Input: intersectVal = 0, listA = [2, 6, 4], listB = [1, 5], skipA = 3, skipB = 2
# Output: No intersection
# Explanation: From the head of A, it reads as [2, 6, 4].From the head of B, it reads as [1, 5].Since the two lists do not intersect, intersectVal must be 0, while skipA and skipB can be arbitrary values.
# Explanation: The   two lists do not intersect, so return null.

# Constraints:
# The number of nodes of listA is in the m. The number of nodes of listB is in the n.
# 1 <= m, n <= 3 * 10^4
# 1 <= Node.val <= 10^5
# 0 <= skipA < m
# 0 <= skipB < n
# intersectVal is 0 if listA and listB do not intersect.
# intersectVal == listA[skipA] == listB[skipB] if listA and listB intersect.
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Approach 1: For each node of linked list 2, traverse the entire linked list 1 and see if it matches with selected node of linked list 2.
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        headBB = headB
        while headBB:
            headAA = headA
            while headAA:
                if headAA == headBB:
                    return headAA
                headAA = headAA.next
            headBB = headBB.next
        return None
# TC:O(m*n) Explanation: For linkelist B with m items and linkedlist A with n. We'll run n items for m times, in worst case to match all nodes from list A with head Node of list B
# SC: O(1) Explanation: Only two new pointers used which are referencing and not taking any more space at all


# Approach 2: Using List hashmap. Iterate through any one linked list and store the nodes i.e. objects in the hashmap. Further, traverse over the remaining linked list and check for all of it's node, if they are found in hashmap. If so, return the node.
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        hashmap=[]
        while headA:
            hashmap.insert(0,headA)
            headA=headA.next
        print(hashmap)
        while headB:
            if headB in hashmap:
                return headB
            headB=headB.next
        return None
# TC: >O(n+m) Explanation: Traversing n nodes to store LL1 in the hashmap, and traversing m nodes to further check for LL2 if any of the nodes are present in the hashmap, will make us have n+m TC. Also the checking in hashmap i.e. 'in' wont likely work in constant space here, as the items stored in our list type hashmap are objects, and so hashing them might be complicated resulting in more than O(1) TC, which will add onto m+n Time and make resulting TC to be more than m+n.
# SC: O(n) Explanation: Given that we're storing linked list 1 in hashmap, we'll store n items in the given hashmap resulting in O(n) space complexity.


# Approach 3: Same as Approach2, just by using Dict hashmap. Using id of objects as identifying factor for common nodes
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        hashmap={}
        while headA:
            hashmap[id(headA)]=True
            headA=headA.next
        print(hashmap)
        while headB:
            if id(headB) in hashmap:
                return headB
            headB=headB.next
        return None #Not mentioning this is totally fine as by default as function exhaust None is only returned
# TC: O(n+m) Explanation: Here, keys are simple characters, unlike objects in Appraoch2. So hashing/finding the item in hashmap will happen in O(1) TC.
# SC: O(n)

# Approach 4: Considering the possibility of linked lists having different lengths, we'll firstly find their length and will subtract the difference. We'll make the longer linked list's head come forward by the difference. From here on, we'll move heads of both the linked lists simultanously while checking if they are pointing at the same location, in which case we return the head. If not, we return None.
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        headAA, headBB = headA, headB
        lenA, lenB = 0, 0
        while headAA or headBB:
            if headAA: #Once headAA becomes None if-condition wont be validated. 'if None' works similarly to 'if False' that what 'if' is checking into has become None and so there's nothing more to be unraveled
                lenA += 1
                headAA = headAA.next
            if headBB:
                lenB += 1
                headBB = headBB.next

        if lenA > lenB:
            while lenA > lenB:
                headA = headA.next
                lenA -= 1
        elif lenB > lenA:
            while lenB > lenA:
                headB = headB.next
                lenB -= 1

        while headA:
            if headA == headB:
                return headA
            headA = headA.next
            headB = headB.next
        return None
# TC: O(M)+O(M-N)+O(N)=>O(2M) Explanation: Assuming M is the size of bigger linked list, we'll traverse M items, and simultaneously find length of both the linked lists. We'll take M-N time to make the head of longer linked list shift forward by M-N nodes. Further we'll traverse the length M-(M-N) or N and traverse all items of both lists to see if they match.
# SC: O(1)


# Approach 5: Same as Approach 4 but better code implementation. So here, we will shift the heads of the two given linked lists, before they'll be at the same lengths in different linked lists than their original ones; from where on we'll further traverse their corresponding lists simultanously, and will either return None as both heads exhaust traversing all the nodes, or if before exhausting they match then we'll return the matching node. In brief, for 2 given linked lists we'll traverse them simultanously and when one of their's head points None but the other is not, we'll shift the head of the linked list pointing to null to the start of the other linked list. In general, as we traverse both lists simultaneoulsy, the shorter list will be exhausted first and so will be shifted to start of longer list. Once head1 of shorter list has shifted to start of longer, the longer list's head would still have some item's to exhaust, after which it'll be at starting of shorted linked list; in which case now they have equal elements in front of them. So from this iteration onwards, either they'll point to None i.e.reach the end together or will find a common item. In either case, as the heads match we return them.
class Solution: #Consider 5,6,7 and 2,1,11,6,7. list1 will be None when list2 is 6. Further list 1 proceeds as 2,1,11,6,7 whereas list2 is 7,None,5,6,7. See 6,7 comes as 4th and 5th sequence for both pointers.
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        headAA, headBB = headA, headB
        while headAA!=headBB:
            headAA = headB if headAA==None else headAA.next
            headBB = headA if headBB==None else headBB.next
        return headAA
# TC: O(2M) Assuming M is length of longer list or if lists are of equal lengths Explanation:we'll have time complexity computed in the same way as it was in approach4, and we will get total TC as 2M.
# SC: O(1)