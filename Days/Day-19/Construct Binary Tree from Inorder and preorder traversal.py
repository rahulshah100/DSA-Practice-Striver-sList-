# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/

# Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.

# Example 1:
# Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
# Output: [3,9,20,null,null,15,7]

# Example 2:
# Input: preorder = [-1], inorder = [-1]
# Output: [-1]

# Constraints:
# 1 <= preorder.length <= 3000
# inorder.length == preorder.length
# -3000 <= preorder[i], inorder[i] <= 3000
# preorder and inorder consist of unique values.
# Each value of inorder also appears in preorder.
# preorder is guaranteed to be the preorder traversal of the tree.
# inorder is guaranteed to be the inorder traversal of the tree.
# ----------------------------------------------------------------------------------------------------------------------------------------
# Approach1: Because preOrder is like root, leftNode, rightNode we can identify from preOrder array's first entry that what is value of rootNode but further we still need to make distinction in the rest of the array for how much further is the array length ascribed to leftNode tree and how much is rightNode. For this, we find the root node in inOrder array (here constraints assert only unique value so we cant confuse finding rootNode) and because inOrder is like left, root, right we can say to the left of identified node the length of the portion is part of rootNode's left tree. So to create a leftTree out of this identified leftTree part we put a recursive call with updated preOrder and inOrder arrays which is assigned back to `root.left`. This also makes us return root at the end so `root.left` is assigned accurate thing and not None. After this we put a recursive call for right tree and assign it to `root.right`. Discussing on updates in array params passed into the recursive calls against `root.left` and `root.right`, in root.left the preStart i.e. startIndex of preOrderArr is updated to preStart+1 and preEnd is updated to preStart+leftTreeLength whereas for inOrder array the inStart stays the same but inEnd is updated to inRoot (which is where we identified the root of preOrder inside inOrder) - 1. For rightTree call preStart is updated to preStart+leftTreeLength+1 while preEnd stays same; and inStart is changed to inRoot+1 while inEnd stays same. To assist us in locating inRoot we create a map of node val against the array index of inOrder where that value is found. Also. to identify when to stop recursion as we can see in recursive calls below preStart is always incremented with 1 at-least for both left and right calls while preEnd is not so at point of convergence preStart will become a value higher than preEnd and that's when we return.
from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inMap = {}
        for i in range(len(inorder)):
            val = inorder[i]
            inMap[val] = i
        return self.buildTreeHelper(preorder, 0, len(preorder) - 1, inorder, 0, len(inorder) - 1, inMap)

    def buildTreeHelper(self, preorder, preStart, preEnd, inorder, inStart, inEnd, inMap):
        if preStart > preEnd:
            return None
        root = TreeNode(preorder[preStart])
        inRoot = inMap[root.val]
        leftTreeLength = inRoot - inStart

        root.left = self.buildTreeHelper(preorder, preStart + 1, preStart + leftTreeLength, inorder, inStart, inRoot - 1, inMap)
        root.right = self.buildTreeHelper(preorder, preStart + leftTreeLength + 1, preEnd, inorder, inRoot + 1, inEnd, inMap)

        return root
# TC: O(2n) Explanation: n to create inMap and n to collectively create left and rightTrees
# SC: O(2n) Explanation: n for stack space and n for InMap