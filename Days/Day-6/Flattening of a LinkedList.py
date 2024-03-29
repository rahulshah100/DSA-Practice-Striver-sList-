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
# Approach 1: We'll use recursion, where-in initially we'll run recursion to keep going to next node, up-till we are on last node. Having returned from last node's call we'll merge the sublist of last two nodes in sorted way and that will be returned as a one sorted list which will be further merged with the sublist/node prior to second last and so on...
'''
class Node:
    def __init__(self, d):
        self.data=d
        self.next=None
        self.bottom=None

'''
def flatten(root):
    if root:
        sortedArr = flatten(root.next)
        tempList = dummy = Node(0)
        while root or sortedArr:                                      #--0
            if not sortedArr or root and root.data <= sortedArr.data: #If this was just root.data <= sortedArr.data and at #--0 we'd "while root and sortedArr" then we'd need to have #--1 and #--2
                tempList.bottom = root
                root = root.bottom
            else:
                tempList.bottom = sortedArr
                sortedArr = sortedArr.bottom
            tempList = tempList.bottom

        # while root:                   #--1
        #     tempList.bottom=root
        #     root=root.bottom
        #     tempList=tempList.bottom

        # while sortedArr:          #--2
        #     tempList.bottom=sortedArr
        #     sortedArr=sortedArr.bottom
        #     tempList=tempList.bottom
        root = dummy.bottom
    return root
# TC: O(N*N*M) where N is the no. of nodes in the main linked list and M is the no of nodes in a single sub-linked list Explanation: there will be N recursive calls i.e. as many calls as number of nodes in-line of node.next sequence are there, which will take N time. Once recursion is done and we're backtracking, for second last recursive call where last 2 node's sub-lists are merged we'll have M+M elems to compare and merge. For third last call these 2M elems from last recursive call + M elem from the current sublist will be merged. So 2M+3M+4M...+NM will be time used additionally => M(1+2+..+N) => M(N((N+1)/2)) => MNN. Thus Total time is N (for building tree) + NNM for execution, generalized as NNM.
# SC: O(N) where N is the no of nodes in the main linked list Explanation: Ignoring recursive stack space, all we're using is temp and sortedArr as a node, a pointer. No real/extra space is used apart from creating an extra Node(0) which doesnt keep adding up on each recursive call and hence is constant. If we count recursive stack: n calls hence n recursive stack space