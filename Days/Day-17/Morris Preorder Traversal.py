# https://www.codingninjas.com/studio/problems/preorder-traversal_3838888?topList=striver-sde-sheet-problems&utm_source=striver&utm_medium=website

# Visit Day17/MorrisInorderTraversal because here there's just a one line change. So for InOrder we had to follow order of L,C,R i.e.left right and center, so from current we kept going Ls i.e.left till we reached the leftMost and then started storing the items on way back. Instead, as we have to store Cs here we'll store C as we're shifting the C to C.left. Hence, we shift the line `resArr.append(currNode.val)` from under the `Revert the changes made in the 'if' part to restore the original tree` to now `Make currNode as the right child of its inorder predecessor` at the spot, just before we do currNode = currNode.left.
from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        resArr = []

        currNode = root
        while currNode:
            if not currNode.left:
                resArr.append(currNode.val)
                currNode = currNode.right
            else:
                # Find the inorder predecessor
                predecessor = currNode.left
                while predecessor.right and predecessor.right != currNode:
                    predecessor = predecessor.right

                # Make currNode as the right child of its inorder predecessor
                if not predecessor.right:
                    predecessor.right = currNode
                    resArr.append(currNode.val)
                    currNode = currNode.left
                # Revert the changes made in the 'if' part to restore the original tree
                else:
                    predecessor.right = None
                    currNode = currNode.right
        return resArr

# Example taken as below
#       1
#      / \
#     2   3
#    / \
#   4   5
#        \
#         6
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.left.right.right = TreeNode(6)

result = Solution()
print(result.preorderTraversal(root)) #O/P: [1, 2, 4, 5, 6, 3]
# TC: O(n)
# SC: O(1)