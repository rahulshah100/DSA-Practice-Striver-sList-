# https://leetcode.com/problems/balanced-binary-tree/

# Given a binary tree, determine if it is height-balanced (A height-balanced binary tree is a binary tree in which the depth of the two subtrees of every node never differs by more than one)

# Example 1:
# Input: root = [3,9,20,null,null,15,7]
# Output: true

# Example 2:
# Input: root = [1,2,2,3,3,null,null,4,4]
# Output: false

# Example 3:
# Input: root = []
# Output: true

# Constraints:
# The number of nodes in the tree is in the range [0, 5000].
# -104 <= Node.val <= 104
# -------------------------------------------------------------------------------------------------------------------------------------------
# Approach1: Visit Day18/HeightOfABinaryTree.py first to understand how height of tree is found. Here using the heights of left and right child trees we find the modulus/absolute difference and if greater than 1 we return False. To further build upon the logic, we can agree on using an inOrder traversal for visiting each node of the tree where for each node we compute its left and right child height. As we reach to the point None is root node so far we didn't return False hence the tree has been found balanced, and so we return True here. Plus before reaching to this point where we run out on tree and encounter None say if right side has been found balanced yet left-side hasn't so right call must be returning True while left would be returning False to carry this conviction forward the way we attempt inOrder is by doing an 'and' between the left and right call and returning the result to parent calls.
# Definition for a binary tree node.
"""class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        lh = self.maxDepth(root.left)
        rh = self.maxDepth(root.right)

        if abs(lh - rh) > 1:
            return False

        return self.isBalanced(root.left) and self.isBalanced(root.right)

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        l = self.maxDepth(root.left)
        r = self.maxDepth(root.right)
        return 1 + (max(l, r))"""
# TC: O(n^2) Explanation: InOrder takes n time for traversing the tree and in it for computing height n time is taken per iteration.
# SC: O(n^2) Explanation: At worst inOrder holds n stack space and on top computing height might take n more stack space.


# Approach2: Bottom up for all nodes we'll find if difference in left, right children is greater than 1 using inOrder traversal. So we start with traversing through all the way from left nodes first, leading ourselves to leftmost Node in the tree, where we encounter base condition of no root. Here we return 0 indicating height for this None node. Once left child call is over right child call will be executed and say there is no right child for the leftMost Node, so 0 is returned there too. Now to find if this much portion that is for leftMost node if tree is balanced we computer absolute difference of left and right call values and here they're 0-0 and so not greater than 1. Further we want to return this much height which as we saw for calculating tree height in Day18/HeightOfABinaryTree.py is returned using 1+max(left,right). So further for this parent's right too as this gets returned as its left and it goes to its right where say no right node is there we find difference 1-0 still not greater than 1. But for its parent i.e.leftMost's parent's parent as this returns as the left call with value 2 and say there is no right node here then difference is 2-0 which is greater than 1. At this point we return -1. So its parent will now get -1 returned in its leftCall and to send it above in chain of recursive call thus right after `left_height = dfs_height(root.left)` we check if left call returns -1 and if so we return that too thus sending it to parents left where again it is sent above. Same could happen with right_height so we put return -1 even after there if right_height==-1. For converting thus returned 0 or and -1 and anything else too, into True/False as question requires, we do
# Approach2: Bottom up for all nodes we'll find if difference in left, right children is greater than 1 using inOrder traversal. So we start with traversing through all the way from left nodes first, leading ourselves to leftmost Node in the tree, where we encounter base condition of no root. Here we return 0 indicating height for this None node. Once left child call is over right child call will be executed and say there is no right child for the leftMost Node, so 0 is returned there too. Now to find if this much portion that is for leftMost node if tree is balanced we computer absolute difference of left and right call values and here they're 0-0 and so not greater than 1. Further we want to return this much height which as we saw for calculating tree height in Day18/HeightOfABinaryTree.py is returned using 1+max(left,right). So further for this parent's right too as this gets returned as its left and it goes to its right where say no right node is there we find difference 1-0 still not greater than 1. But for its parent i.e.leftMost's parent's parent as this returns as the left call with value 2 and say there is no right node here then difference is 2-0 which is greater than 1. At this point we return -1. So its parent will now get -1 returned in its leftCall and to send it above in chain of recursive call thus right after `left_height = dfs_height(root.left)` we check if left call returns -1 and if so we return that too thus sending it to parents left where again it is sent above. Same could happen with right_height so we put return -1 even after there if right_height==-1. For converting thus returned 0 or and -1 and anything else too, into True/False as question requires, we do
# Approach2: Bottom up for all nodes we'll find if difference in left, right children is greater than 1 using inOrder traversal. So we start with traversing through all the way from left nodes first, leading ourselves to leftmost Node in the tree, where we encounter base condition of no root. Here we return 0 indicating height for this None node. Once left child call is over right child call will be executed and say there is no right child for the leftMost Node, so 0 is returned there too. Now to find if this much portion that is for leftMost node if tree is balanced we computer absolute difference of left and right call values and here they're 0-0 and so not greater than 1. Further we want to return this much height which as we saw for calculating tree height in Day18/HeightOfABinaryTree.py is returned using 1+max(left,right). So further for this parent's right too as this gets returned as its left and it goes to its right where say no right node is there we find difference 1-0 still not greater than 1. But for its parent i.e.leftMost's parent's parent as this returns as the left call with value 2 and say there is no right node here then difference is 2-0 which is greater than 1. At this point we return -1. So its parent will now get -1 returned in its leftCall and to send it above in chain of recursive call thus right after `left_height = dfs_height(root.left)` we check if left call returns -1 and if so we return that too thus sending it to parents left where again it is sent above. Same could happen with right_height so we put return -1 even after there if right_height==-1. For converting thus returned 0 or and -1 and anything else too, into True/False as question requires, we do `return dfs_height(root) != -1
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs_height(root):
            if not root:
                return 0

            left_height = dfs_height(root.left)
            if left_height == -1:
                return -1

            right_height = dfs_height(root.right)
            if right_height == -1:
                return -1

            if abs(left_height - right_height) > 1:
                return -1

            return max(left_height, right_height) + 1

        return dfs_height(root) != -1
# TC: O(n)
# SC: O(n)