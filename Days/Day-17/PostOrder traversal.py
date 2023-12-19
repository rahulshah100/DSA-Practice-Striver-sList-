# https://leetcode.com/problems/binary-tree-postorder-traversal/

# Given the root of a binary tree, return the postorder traversal of its nodes' values.

# Example 1:
# Input: root = [1,null,2,3]
# Output: [3,2,1]
# Example 2:
# Input: root = []
# Output: []
# Example 3:
# Input: root = [1]
# Output: [1]

# Constraints:
# The number of the nodes in the tree is in the range [0, 100].
# -100 <= Node.val <= 100


# Follow up: Recursive solution is trivial, could you do it iteratively?
# -------------------------------------------------------------------------------------------------------------------------------------------
# Postorder has the order: left,right, currNode
# -------------------------------------------------------------------------------------------------------------------------------------------
# Approach1: Recursive - see Day17/InorderTraversal.py to understand this where only the order of execution of statements are different
# Definition for a binary tree node.
"""
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root) -> List[int]:
        currNode, resArr=root, []
        def helper(root):
            if not root:
                return
            helper(root.left)
            helper(root.right)
            resArr.append(root.val)
        helper(root)
        return resArr"""
# TC: O(n)
# SC: O(n)


# Approach2: Iterative - Using 2 stacks. Unlike inorder iterative traversal, this is more different because consider:
#          1
#         / \
#        2   3
#       / \
#      4   5
# For currentNode = 2 for inOrder we have external stack storing this item. Once stored currNode goes to left and becomes 4. After storing 4, currNode goes to left and becomes None. Once None, stack is popped and currNode goes to the popped item's right i.e. 4's right which again is None. Thus, as currNode becomes None again, we further pop stack, this time to obtain 2 and make currNode as 2's right which is 5 where currNode goes left and becomes None. Again as currNode is None stack pops and gives 5, and we make currNode go to 5's right which is None. As None again, we again pop stack and get 1 and make currNode 1's right... and so on. Thus, if we observe item from stack is accessed only once when its left is returned, we pop this item from stack and go to its right. While for postOrder not only do we need to access the item once to go to right but second time again after right to come back to currNode; this time to store it. Furthermore, after having accessed an item second time, now unlike first time we don't want to go to the right but currNode's parent. Thus accessing stack item twice and having to decipher the number of time we are accessing because both times different operation has to be performed makes postOrder tricky. So iterative implementation in attempt of trying to replicate the recursive one is such that we need to write it much differently here.
#  Iterative - 2 Stack method: We'll do this in kinda like preOrder fashion so to keep the hold on currentNode and later reverse thus generated resArr. So first, we append root into stack and then run a while loop un-till the stack gets empty. In this loop the stack is popped and popped item's value is stored in resArr. The same Popped item's left is further appended in the stack, and then popped's right is appended. This is keeping in mind next time as stack pops the right item gets stored first in resArr, and then the left which makes order in resArr as currNode, right, left which is perfectly reverse of how we want it to be for postOrder.
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

class Solution:
    def postorderTraversal(self, root):
        if root is None: #This had to be handled because stack1 will add None and classify as not empty to start below while loop where top.val will then give error
            return

        resArr, stack = [], []
        stack.append(root)
        while stack:
            top = stack.pop()
            resArr.append(top.val)

            if top.left:    # Push left child to stack if it exists
                stack.append(top.left)
            if top.right:   # Push right child to stack if it exists
                stack.append(top.right)
        return resArr[::-1]
# Example usage:
# Create a sample binary tree
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

result = Solution()
print(result.postorderTraversal(root))
# TC: O(2n) Explanation: To traverse we require n time and later to reverse resArr n more time
# SC: O(2n) Explanation: not just stack but here also an n space is counted towards resArr because it has to be reversed before returning. Hence, it cant be said to be used directly for storing answer.
