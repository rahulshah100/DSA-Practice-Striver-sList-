# https://leetcode.com/problems/maximum-depth-of-binary-tree/

# Given the root of a binary tree, return its maximum depth.
# A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

# Example 1:
# Input: root = [3,9,20,null,null,15,7]
# Output: 3

# Example 2:
# Input: root = [1,null,2]
# Output: 2

# Constraints:
# The number of nodes in the tree is in the range [0, 104].
# -100 <= Node.val <= 100
# ----------------------------------------------------------------------------------------------------------------------------------------
# Approach1: As defined by constraints, when we have 0 nodes in binary tree we return length as 0. If not we traverse the left Node and after that traverse right Node; as they return we compare both the calls i.e. left and right child calls and max of them in addition of one for currentNode we return.
# Definition for a binary tree node.
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        l=self.maxDepth(root.left)
        r=self.maxDepth(root.right)
        return 1+(max(l, r))

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.right.right = TreeNode(5)

S = Solution()
print(S.maxDepth(root))
# TC: O(1)
# SC: O(n) Explanation: Stack space
