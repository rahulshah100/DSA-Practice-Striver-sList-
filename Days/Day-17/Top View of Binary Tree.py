# https://practice.geeksforgeeks.org/problems/top-view-of-binary-tree/1

# Given below is a binary tree. The task is to print the top view of binary tree. Top view of a binary tree is the set of nodes visible when the tree is viewed from the top. For the given below tree
#        1
#     /     \
#    2       3
#   /  \    /   \
# 4    5  6      7
# Top view will be: 4 2 1 3 7
# Note: Return nodes from leftmost node to rightmost node. Also if 2 nodes are outside the shadow of the tree and are at same position then consider the left ones only(i.e. leftmost).
# For ex - 1 2 3 N 4 5 N 6 N 7 N 8 N 9 N N N N N will give 8 2 1 3 as answer. Here 8 and 9 are on the same position but 9 will get shadowed.

# Example 1:
# Input:
#       1
#    /    \
#   2      3
# Output: 2 1 3

# Example 2:
# Input:
#        10
#     /      \
#   20        30
#  /   \    /    \
# 40   60  90    100
# Output: 40 20 10 30 100
# Your Task:
# Since this is a function problem. You don't have to take input. Just complete the function topView() that takes root node as parameter and returns a list of nodes visible from the top view from left to right.

# Expected Time Complexity: O(NlogN)
# Expected Auxiliary Space: O(N).

# Constraints:
# 1 ≤ N ≤ 105
# 1 ≤ Node Data ≤ 105
# ------------------------------------------------------------------------------------------------------------------------------------------
# Approach1: Visit Day17/BottomViewOfBinaryTree.py because here we just add one line to it where before adding an axis->nodeVal to mapDataStructure we check if an entry for that axis doesn't already exist because if so, the top items is already added and we don't want it overwritten.
from queue import Queue
import math

class Solution:
    def topView(self,root):
        resArr = []
        Q, mapDict = Queue(), {}

        Q.put((root, 0))
        while len(Q.queue):
            currNode, axis = Q.get()
            if axis not in mapDict:
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
# TC: O(n)
# SC: O(n)