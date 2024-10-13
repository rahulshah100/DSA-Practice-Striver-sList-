# https://leetcode.com/problems/same-tree/

# Given the roots of two binary trees p and q, write a function to check if they are the same or not.
# Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

# Example 1:
# Input: p = [1,2,3], q = [1,2,3]
# Output: true

# Example 2:
# Input: p = [1,2], q = [1,null,2]
# Output: false

# Example 3:
# Input: p = [1,2,1], q = [1,1,2]
# Output: false

# Constraints:
# The number of nodes in both trees is in the range [0, 100].
# -104 <= Node.val <= 104
# --------------------------------------------------------------------------------------------------------------------------------------
# Approach1: Traverse the tree in inOrder fashion where first we check the base condition i.e. if we ran out on tree where coz so far everything must have matched for us to be able to reach beyond lastNode, hence we return True here. Further we check for currentNode that if their values are not same then no point in further traversal and we return None here. But we have an edge case here -  what if even to compare values, what if we don't have that node in one of the tree? So we first check 'if p and not q or q and not p' where we return False and in addition if either of two of them aren't False, we still wanna return False 'if p.val != q.val' so that's all made into one `if p and not q or q and not p or p.val != q.val: return False`. After this we traverse and go-to left and below it go-to right. Now say a child node returns False then how to bump it up the call stack? So as this child could be either of left or right child call, after these two lines we put if checks. But for that the recursive calls are assigned to l and r such variables so those return values are preserved. Further if l has returned True that means that path has been identical and we'll return True if r is True or will return False if r is False, so that's how we write it `if l: return r` and vice versa for `if r`.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q: return True

        if p and not q or q and not p or p.val != q.val: return False
        l = self.isSameTree(p.left, q.left)
        r = self.isSameTree(p.right, q.right)

        if l: return r
        if r: return l
# TC: O(n)
# SC: O(n)