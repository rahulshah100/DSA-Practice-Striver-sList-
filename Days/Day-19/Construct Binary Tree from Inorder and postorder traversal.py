# https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/

# Given two integer arrays inorder and postorder where inorder is the inorder traversal of a binary tree and postorder is the postorder traversal of the same tree, construct and return the binary tree.

# Example 1:
# Input: inorder = [9,3,15,20,7], postorder = [9,15,7,20,3]
# Output: [3,9,20,null,null,15,7]

# Example 2:
# Input: inorder = [-1], postorder = [-1]
# Output: [-1]

# Constraints:
# 1 <= inorder.length <= 3000
# postorder.length == inorder.length
# -3000 <= inorder[i], postorder[i] <= 3000
# inorder and postorder consist of unique values.
# Each value of postorder also appears in inorder.
# inorder is guaranteed to be the inorder traversal of the tree.
# postorder is guaranteed to be the postorder traversal of the tree.
# -----------------------------------------------------------------------------------------------------------------------------------------
# Approach1: Refer Day19/ConstructBinaryTreeFromInorderAndPreorderTraversal.py coz here we've used same code with 3 differences. 1)coz we've postOrder the root is postorder[postEnd] instead of preorder[preStart] 2)recursive call for leftTree is where params of postStart and postEnd are different from what we had for preStart and preEnd. For leftTree the postStart is as is i.e.postStart but postEnd becomes postStart + leftTreeLength - 1 which can be understood while dry-running an example. 3) For rightTree postStart becomes postStart+leftTreeLength while postEnd is made postEnd-1
from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        inMap = {}
        for i in range(len(inorder)):
            val = inorder[i]
            inMap[val] = i
        return self.buildTreeHelper(postorder, 0, len(postorder) - 1, inorder, 0, len(inorder) - 1, inMap)

    def buildTreeHelper(self, postorder, postStart, postEnd, inorder, inStart, inEnd, inMap):
        if postStart > postEnd:
            return None

        root = TreeNode(postorder[postEnd])
        inRoot = inMap[root.val]
        leftTreeLength = inRoot - inStart

        root.left = self.buildTreeHelper(postorder, postStart, postStart + leftTreeLength - 1, inorder, inStart, inRoot - 1, inMap)
        root.right = self.buildTreeHelper(postorder, postStart + leftTreeLength, postEnd - 1, inorder, inRoot + 1, inEnd, inMap)
        return root
# TC: O(2n)
# SC: O(2n)