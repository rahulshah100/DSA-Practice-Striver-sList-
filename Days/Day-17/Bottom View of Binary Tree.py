# https://practice.geeksforgeeks.org/problems/bottom-view-of-binary-tree/1

# Given a binary tree, print the bottom view from left to right.
# A node is included in bottom view if it can be seen when we look at the tree from bottom.
#                       20
#                     /    \
#                   8       22
#                 /   \        \
#               5      3       25
#                     /   \
#                   10    14
# For the above tree, the bottom view is 5 10 3 14 25.
# If there are multiple bottom-most nodes for a horizontal distance from root, then print the later one in level traversal. For example, in the below diagram, 3 and 4 are both the bottommost nodes at horizontal distance 0, we need to print 4.
#                       20
#                     /    \
#                   8       22
#                 /   \     /   \
#               5      3 4     25
#                      /    \
#                  10       14
# For the above tree the output should be 5 10 4 14 25.

# Note: The Input/Output format and Example given are used for the system's internal purpose, and should be used by a user for Expected Output only. As it is a function problem, hence a user should not read any input from the stdin/console. The task is to complete the function specified, and not to write the full code.

# Example 1:
# Input:
#        1
#      /   \
#     3     2
# Output: 3 1 2
# Explanation:
# First case represents a tree with 3 nodes
# and 2 edges where root is 1, left child of
# 1 is 3 and right child of 1 is 2.
# Thus nodes of the binary tree will be
# printed as such 3 1 2.

# Example 2:
# Input:
#          10
#        /    \
#       20    30
#      /  \
#     40   60
# Output: 40 20 60 30
# Your Task:
# This is a functional problem, you don't need to care about input, just complete the function bottomView() which takes the root node of the tree as input and returns an array containing the bottom view of the given tree.

# Expected Time Complexity: O(N*logN).
# Expected Auxiliary Space: O(N).

# Constraints:
# 1 <= Number of nodes <= 105
# 1 <= Data of a node <= 105
# -------------------------------------------------------------------------------------------------------------------------------------------
# Note: For when I don't read the whole question there is a clarification made there which I need to make myself aware about. In case of overlapping nodes the preference is given to the rightMost Node and the one close to bottom like here 60 overlaps 10 and we ditch 10
#          10
#        /    \
#       20    30
#      /  \
#     40   60
# And below here we ditch 3 and write 4 instead so bottom view is 5,10,4,14,25
#                       20
#                     /    \
#                   8       22
#                 /   \    /   \
#               5      3  4   25
#                      /   \
#                  10       14
# -------------------------------------------------------------------------------------------------------------------------------------------
# Approach1: Using a Queue and a Map Data structure we implement idea of vertical axis on the given Binary Tree. The way we use vertical axis is for below example we'll have an imaginary vertical axis passing from each node. Line 0 passing from 20,3,4; -1 passing from 8,10; -2 passing from 5; 1 from 22 and 14 and line 2 passing from 25.
#                       20
#                     /    \
#                   8       22
#                 /   \    /  \
#               5      3  4   25
#                      /   \
#                  10       14
# So we'll store in a Queue (because we want first stored things out first) the pair of (node, axis) and start the level order traversal i.e. start from node-20 to then go to 8 and after it to 22 and after that 5 and then 3, after which we go to 4 and 25 and then to 10 and 14. Reason for this traversal is so that left first then right and then bottom nodes come later and hence when they do they end up overwriting the left Nodes or right nodes of same axis in our MapDataStructure as we'll see, which is the priority we wanted to maintain. The way we'll start is (20,0) is stored in Queue and un-till Queue is emptied we run a loop. Here we pop the queue (for queue it is called get operation) and we'll assign the popped item value against its axis value in the map. We made axis as key so that for same axis later as other value on the right or at the bottom is encountered they can overwrite this one with their common criteria being the axis they share. Once this much is done we want to further the traversal and so in queue we append the popped item's left with the axis as axis-1 and after it we append the popped item's right and its axis as axis+1. So in next iteration the left of queue is popped, and we append its left and right and so on.. After the whole loop our map will hold the bottom most items for all axis, but they're not in order like it could be 5,14,10,25. So here we'll run a loop through mapDataStructure and from key comparisons we determine the value of MinAxis and MaxAxis values. Further, for this range i.e. MinAxis and MaxAxis (both included) we run a loop where the values against those keys are stored in resArr. resArr is returned at the last.
from queue import Queue
import math

class Solution:
    def bottomView(self, root):
        resArr = []
        Q, mapDict = Queue(), {}

        Q.put((root, 0))
        while len(Q.queue):
            currNode, axis = Q.get()
            mapDict[axis] = currNode.data

            if currNode.left:
                Q.put((currNode.left, axis - 1))

            if currNode.right:
                Q.put((currNode.right, axis + 1))

        minAxis, maxAxis = math.inf, -math.inf
        for key in mapDict:
            if key < minAxis: minAxis = key
            if key > maxAxis: maxAxis = key

        for axis in range(minAxis, maxAxis + 1):
            if axis in mapDict:
                resArr.append(mapDict[axis])

        return resArr
# TC: O(3n) Explanation: While and both for takes n time each
# SC: O(n) Explanation: map takes 2n at worst then q takes n at worst. So generalising it n is SC.