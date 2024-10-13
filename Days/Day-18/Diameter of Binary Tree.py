# https://leetcode.com/problems/diameter-of-binary-tree/

# Given the root of a binary tree, return the length of the diameter of the tree. The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root. The length of a path between two nodes is represented by the number of edges between them.

# Example 1:
# Input: root = [1,2,3,4,5]
# Output: 3
# Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].

# Example 2:
# Input: root = [1,2]
# Output: 1

# Constraints:
# The number of nodes in the tree is in the range [1, 104].
# -100 <= Node.val <= 100
# ------------------------------------------------------------------------------------------------------------------------------------------
# Approach1: Visit Day18/HeightOfABinaryTree.py first to understand how height of tree is found. Here what we'll do is as we traverse the given tree in inOrder fashion for each node we'll compute the height for its left child and right child. For computing diameter these two heights are added. Thus having found diameter we keep track of maxDiameter by using a maxWidth variable which keeps on comparing the widths as we find them.
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.maxWidth = 0

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        lh = self.maxDepth(root.left)
        rh = self.maxDepth(root.right)
        self.maxWidth = max(lh + rh, self.maxWidth)

        self.diameterOfBinaryTree(root.left)
        self.diameterOfBinaryTree(root.right)
        return self.maxWidth

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        l=self.maxDepth(root.left)
        r=self.maxDepth(root.right)
        return 1+(max(l, r))

#        1
#       / \
#      2   3
#     / \
#    4   5
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

S = Solution()
print(S.diameterOfBinaryTree(root))
# TC: O(n^2) Explanation: InOrder takes n time for traversing the tree and in it for computing height n time is taken per iteration.
# SC: O(2n) Explanation: At worst inOrder holds n stack space and on top computing height might take n more stack space.


# Approach2: Improved space and time complexity in approach1 - We see that in code of calculating height of a binary tree we're already performing inOrder traversal so there itself before returning, if this way for every node we compare and obtain the maxWidth then that will reduce time complexity coz now we only iterate over the tree once.
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.maxWidth = 0

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def helperfunc(root):
            if not root: return 0

            lh = helperfunc(root.left)
            rh = helperfunc(root.right)

            self.maxWidth = max(lh + rh, self.maxWidth)
            return 1 + max(lh, rh)

        helperfunc(root)
        return self.maxWidth

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

S = Solution()
print(S.diameterOfBinaryTree(root))
# TC: O(n)
# SC: O(n)