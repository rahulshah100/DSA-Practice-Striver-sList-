# https://leetcode.com/problems/maximum-width-of-binary-tree/

# Given the root of a binary tree, return the maximum width of the given tree.
# The maximum width of a tree is the maximum width among all levels.
# The width of one level is defined as the length between the end-nodes (the leftmost and rightmost non-null nodes), where the null nodes between the end-nodes that would be present in a complete binary tree extending down to that level are also counted into the length calculation.
# It is guaranteed that the answer will in the range of a 32-bit signed integer.

# Example 1:
# Input: root = [1,3,2,5,3,null,9]
# Output: 4
# Explanation: The maximum width exists in the third level with length 4 (5,3,null,9).

# Example 2:
# Input: root = [1,3,2,5,null,null,9,6,null,7]
# Output: 7
# Explanation: The maximum width exists in the fourth level with length 7 (6,null,null,null,null,null,7).

# Example 3:
# Input: root = [1,3,2,5]
# Output: 2
# Explanation: The maximum width exists in the second level with length 2 (3,2).

# Constraints:
# The number of nodes in the tree is in the range [1, 3000].
# -100 <= Node.val <= 100
# ----------------------------------------------------------------------------------------------------------------------
# Approach1: Supremely tricky is how in this question width is considered. So to make sure we understand the term width here consider these examples:
#     1
#    / \
#   3   2
#  / \   \
# 5   3   9
# Here width for level 1 is 1, level 2 is 2, level 3's is - between 2 non-null nodes max distance - so 5 and 9 have 5,3,None,9 that's why width of 4. Max width is 4

#     1
#    / \
#   3   2
#  / \
# 5   3
# Width of level 3 is 2 because 5,3, are non-null nodes. Max width is 2

#         1
#       /  \
#      3    2
#     / \  /
#    5  6 7
#   /   \
#  1    2
# Width of level 3 is 3 because farthest non-null nodes are 5 and 7 and 5,6,7 forms width of 3. On leve 4 width is 2 for the range would be 1,2. Max width here is 3 and not 2 i.e. not necessarily last level always has max width

#        1
#       / \
#      3   2
#     /     \
#    5       4
#   /          \
#  7            6
# Width at last level is between 7,6 where we have 7,none, none,none ,none,none, none,6 so width is 8. Width here for level 3 is 5, None, None, 4 i.e.width of 4.
# Now with algo, here we can see level order is the way to go for traversal because on same level we have to find something. So while traversing in the level order we can sequentially number the items where at the end of each level we can do subtraction of first node number of that level from last node number of the same level which gives us width of that level and by keeping a comparison of all such widths we can find the maxWidth of tree. To handle the case like below where there is a gap in level between the farthest non-null nodes like 5,None,None,9 then we could see sequential numbering won't work because 1 is numbered 1, 3 is 2, 2 is 3, 5 is 4 and 9 is 5; so for level3 (5-4)+1=>2 as length where the Nones in between weren't taken into account. So instead we use a hack of numbering but not in sequential order but in-keeping with formulas of left child as 2n+1 and right child as 2n+2 where n is parent node's number. With this the below 5 will be numbered as 2*2 + 1=> 5, and 9 will be numbered 2*3 + 2=> 8, and the difference (8-5 + 1)=> 4 is accurate width. For this implementation in queue we'll store node and number. We'll start a while loop after inserting (root, 0) in queue, for up-till queue is emptied. In queue, so we get to operate on a level at one time what we'll do is register the size of queue and run a for-loop for those many iterations and in each iteration we pop the bottom and append child nodes with their appropriate numbers into the queue. Before this for-loop we'll just keep the number of bottom most item stored as leftMostNodePosition and in for-loop we'll keep updating the currentNode position with number of node popped, so that at the end of for-loop the rightNode correctly updates to hold number of rightMostNode of that level. We then take difference of leftMostNodePosition and currentNode and thus get the width. Constant comparisons of such widths gives us maxWidth of tree.
#     1
#    / \
#   3   2
#  /     \
# 5       9
from queue import Queue
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxWidth, queue = 0, Queue()

        queue.put((root, 0))
        while len(queue.queue):
            queueSize = queue.qsize()
            leftMostNodePosition = queue.queue[0][1]

            for i in range(queueSize):
                node, currNodePosition = queue.get()
                if node.left:
                    queue.put((node.left, 2 * currNodePosition))
                if node.right:
                    queue.put((node.right, 2 * currNodePosition + 1))

            maxWidth = max(maxWidth, currNodePosition - leftMostNodePosition + 1)
        return maxWidth


# Example usage:
root1 = TreeNode(1)
root1.left = TreeNode(3)
root1.right = TreeNode(2)
root1.left.left = TreeNode(5)
root1.left.right = TreeNode(3)
root1.right.right = TreeNode(9)

s = Solution()
print(s.widthOfBinaryTree(root1))  # Output: 4
# TC: O(n) Explanation: for traversing n nodes simply n time is taken at worst here
# SC: O(n) Explanation: for queue space