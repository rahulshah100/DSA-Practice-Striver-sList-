# https://leetcode.com/problems/binary-tree-paths/description/

# Given the root of a binary tree, return all root-to-leaf paths in any order.
# A leaf is a node with no children.

# Example 1:
# Input: root = [1,2,3,null,5]
# Output: ["1->2->5","1->3"]

# Example 2:
# Input: root = [1]
# Output: ["1"]

# Constraints:
# The number of nodes in the tree is in the range [1, 100].
# -100 <= Node.val <= 100
# --------------------------------------------------------------------------------------------------------------------------------------
# Approach1: We can identify that recursive inorder traversal could be quite simply used here. Using an additional temp param that holds node values of traversed items, we join the temp items with "->" and append it as a string in resArr, when we detect we've hit an end/leafNode. So we append the current Node's val as a string in temp (as a string because only then for joining it later using join(), the string concate was working) before we dive deeper in the inOrder tree traversal. We pop this when we come out after both left and right returns, to set temp right. Now we'd think that base condition is where we detect the leaf and that's where we should append temp into resArr, but it is not accurate. So for a node with only right or say only left child, the other call of its will hit the base condition but not necessarily it means the tree is stopping there in that branch. So instead to detect the leaf node between the temp append and temp pop we check if current node has neither left nor right child and which being true we append joined() temp into resArr
from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        resArr = []

        def helper(root, temp):
            if not root:
                return

            temp.append(str(root.val))
            if not root.left and not root.right:
                resArr.append("->".join(temp))
            helper(root.left, temp)
            helper(root.right, temp)
            temp.pop()

        helper(root, [])
        return resArr


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.right = TreeNode(5)
#        1
#       / \
#      2   3
#       \
#        5

S = Solution()
print(S.binaryTreePaths(root))
# TC: O(n)
# SC: O(2n) Explanation: Recursive stack space and temp constitutes to n space each