# https://practice.geeksforgeeks.org/problems/flattening-a-linked-list/1

# Flattening a Linked List
# Given a Linked List of size N, where every node represents a sub - linked - list and contains two pointers: (i) a next pointer to the next node, (ii) a bottom pointer to a linked list where this node is head. Each of the sub - linked - list is in sorted order. Flatten the Link List such that all the nodes appear in a single level while maintaining the sorted order.
# Note: The flattened list will be printed using the bottom pointer instead of next pointer.For more clearity have a look at the printList() function in the driver code.

# Example 1:
# Input: 5 -> 10 -> 19 -> 28 | | | | 7 20 22 35 | | | 8 50 40 | | 30 45
# Output: 5-> 7-> 8 - > 10 -> 19-> 20-> 22-> 28-> 30-> 35-> 40-> 45-> 50.
# Explanation: The resultant linked lists has every node in a single level.
# (Note: | represents the bottom pointer.)

# Example 2:
# Input: 5 -> 10 -> 19 -> 28 | | 7 22 | | 8 50 | 30
# Output: 5->7->8->10->19->22->28->30->50
# Explanation: The resultant linked lists has every node in a single level.
# (Note: | represents the bottom pointer.)

# Your Task: You do not need to read input or print anything.Complete the function flatten() that takes the head of the linked list as input parameter and returns the head of flattened link list.

# Expected Time Complexity: O(N * M)
# Expected Auxiliary Space: O(1)

# Constraints:
# 0 <= N <= 50
# 1 <= Mi <= 20
# 1 <= Element of linked list <= 103
# -----------------------------------------------------------------------------------------------------------------------------------------------------------------
# Approach 1: We'll use recursion, where-in from the base case we trigger a condition to return the computation, and build from there. So we'll call recursion to get to last node of linked list. From there we'll compute the bottom of last two nodes i.e.their entire sublist and that will serve as a sorted list which will be further computed with the sublist/node prior to second last.
'''
class Node:
    def __init__(self, d):
        self.data=d
        self.next=None
        self.bottom=None

'''
def mergeTwoLists(list1, list2):
    temp = Node(0)  # This zero value node wont be returned, so could have taken any random thing too instead of zero
    start = temp
    while list1 and list2:
        if list1.data < list2.data:
            temp.bottom = list1  # as we're making this as a sublist we'll append not to it's next but the bottom
            temp = temp.bottom
            list1 = list1.next
        else:
            temp.bottom = list2
            temp = temp.bottom
            list2 = list2.bottom
    if list1:
        temp.bottom = list1
    elif list2:
        temp.bottom = list2
    return start.bottom


def flatten(root):
    if root.next == None or root == None:
        return root
    root.next = flatten(root.next)
    root = mergeTwoLists(root, root.next)
    return root
# TC: O(TotalOfAllNodesInListAndSubLists) Explanation: Ultimately, time is boiling down for being used in the comparison between all the nodes in all sublists across the given list.
# SC: O(size of longest sublist) Explanation: temp will take extra space in storing the maxNodesInAnySublist number of nodes.