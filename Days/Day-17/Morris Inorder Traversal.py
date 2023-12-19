# https://leetcode.com/problems/binary-tree-inorder-traversal/

# Given the root of a binary tree, return the inorder traversal of its nodes' values.

# Example 1:
# Input: root = [1,null,2,3]
# Output: [1,3,2]
# Example 2:
# Input: root = []
# Output: []
# Example 3:
# Input: root = [1]
# Output: [1]

# Constraints:
# The number of nodes in the tree is in the range [0, 100].
# -100 <= Node.val <= 100

# Follow up: Recursive solution is trivial, could you do it iteratively?
# -------------------------------------------------------------------------------------------------------------------------------------------
# Approach1: Unlike recursive or iterative inOrder methods as discussed in Day17/InOrderTraversal.py which takes O(n) space and O(n) time complexity the Morris Traversal doesn't take any extra space and its time complexity stays O(n). In Morris Inorder Traversal we traverse from root to left most node with the intuition that for inOrder L,C,R i.e. left Center Right is arrangement and hence we do inevitably have to reach the leftMost before starting to store node values for answer. While undergoing this traversal to the leftMost the issue we faced earlier was the loss of access to go back to parent's once we're at child node. The solution to that problem we found in iterative method earlier was by using external stack and in recursive was by recursive stack space. Here the issue is resolved by branching of leaf nodes with its inOrder Predecessor, while we are first traversing to leftMost Node. Like C is inOrder predecessor in L,C,R. So the idea is that, consider below example, and we can say 7 will come just before 3 in the answer and 6 will come just before 1 and 12 comes before 4 (answer is: 12,4,6,1,7,3,5) so what we can think is if rightMost Node in every branch can point its right pointer to its branchTopNode's rightNode then from leftMost item we can go like 12,4,6,1,7,3,5 by following all the right pointers.
#             3
#         /      \
#        1        5
#       / \
#      4   7
#     / \
#    12  6
# To do this we'll first assign root as currNode and see if it does have a left and if it doesn't we store the currentItem's val in resArr and move to its rightNode. This is because as go right in L,C,R as.we can see we can never go to L or C and that they're left behind or stored first already, hence we store this and go. Suppose now we found a left going branch in it, and it looks like above example. So further what we'll do is we keep current as it is i.e. at 3 and use a new variable predecessor which will be 1 (mind we checked the currNode has a left and only that's how we assign predecessor). From here till we can find predecessor's right we go right by making predecessor = predecessor.right. Once this loop is over we have predecessor at 7 and current at 3. We point predecessor's right to currNode. Mind you this is that part of algo where before storing items, we are still going to leftMost Node in this tree i.e. 12. So further we shift current to current's left i.e. 1. This was one iteration under a huge while loop. Further the algo again checks if current i.e. 1 has a left and which being true predecessor is assigned to it i.e. 4. Now predecessor shift to all the way right i.e. 6 and 6's right will be pointed to current i.e. 1. Current is once again shifted to current's left i.e. 4. In next iteration we check current has a left and make it the predecessor i.e. 12. We go right all the way and end up at 12 itself and point its right to current i.e. 4. Current is shifted to current's left and is made into 12. It's not having left current's value is stored in resArr and currNode goes to currNode.right. This is where traversal to leftMost is over, and we now traverse back storing items in order L,C,R. Now we're at 4 again, and it does have a left i.e. 12 which can be made predecessor so how do we understand if this has been traced already and that when it is discovered we store the current i.e. 4 in answer and go to its right? Answer is earlier where were making predecessor go all the way right here it'll become an infinite loop, and so we'll add an additional condition there to check if predecessor.right == currNode which when violates we break the loop. After breaking loop we simply check if loop was broke because predecessor.right is None and if not we know the second case has happened. This second is what we were discussing and when that happens predecessor's right is pointed to None again and current is added to answer and current is made current.right.

# Definition for a binary tree node.
from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
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
                    currNode = currNode.left
                # Revert the changes made in the 'if' part to restore the original tree
                else:
                    predecessor.right = None
                    resArr.append(currNode.val)
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
print(result.inorderTraversal(root)) #O/P: [4, 2, 5, 6, 1, 3]
# TC: O(n) #Explanation: For complete left traversal almost n time will be taken depending on how well-balanced binary tree is, or the time=number of nodes onto left. Further these nodes are traversed via there rightPointer where we might once more loop to left to discover the infinite looping condition and to recover from it, as we progress from LeftMost to Center again. Thus roughly 2n time for whole algo but generalised as n.
# SC: O(1)