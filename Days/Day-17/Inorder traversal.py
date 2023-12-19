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
#  Inorder means the order is - leftChildVal, currentNodeVal, rightChildVal
# -------------------------------------------------------------------------------------------------------------------------------------------
# Approach1: Recursive solution - we'll create a resArr array to store our answer and return at the end.
# Consider below example
#          1
#         / \
#        2   3
#       / \
#      4   5
# To fill this resArr we'll create a subFunction where first thing is we go to the left node of current node, i.e. 2, by calling the same subFunction and this time passing it current node's left. This will take us to root's left and then its left i.e. 4 and so on up-till we're on last left node. Here we write base condition that when currentNode is encountered to be None we simply return from there. When this happens for first time we'll be returned to last left node i.e.4. This last left node can still have a right and if so we need to traverse there but to maintain the order of items (Left,Current,Right) as described in inOrder, we first append this currentNode's value itself in resArr. After this, now we call the same subFunction with root.right i.e. 4's right. Suppose this node doesn't have a right, and hence we encounter the base condition of None and get returned. then now what we need to do is go to the node above i.e.2 for which we don't write anything and thus simply None gets returned by default, and we get returned to parentNode i.e.2 for it's leftNode call. Now we will append currentNode's value i.e. 2 and go to its rightNode. Further this node's left i.e. 5's left would be checked which being None base condition returns it, and 5's value is then appended in resArr as currentNode after which we go to it's right which also returns None by base condition. After this we get returned to 5's parent Node for it's right subFunction call. By this time we have run out on the subFunction call for Node 2, and it gets returned to it's parentNode as the parentNode's left subFunction call i.e. 1's left has been thus returned. Now we know 1 is appended in resArr and after which 1's right is called. 3's left is checked and as base returns it, 3 is appended and further it's right which is None gets returned from base. Thus having run out on subFunction for 3, we return to the parentNode i.e.1 as it's right subFunction call and run out on the function's length.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        resArr = []

        def helper(root):
            if not root:
                return
            helper(root.left)
            resArr.append(root.val)
            helper(root.right)

        helper(root)
        return resArr
# TC: O(n) Explanation: In total if we see we're visiting each node in tree just for once and there is no repetition in this visiting trajectory. For paying each node a visit, basically they're one away from the other closest node, and so we can safely say because n items are stored we can traverse all in a total of n time. Although here we can argue that despite being one away from each other, appending the very first node is not happening till we traverse all the way to leftmost node which itself could take logn time in a perfect binary tree (as the one given in approach1's example) or n in worst case of an imperfect binary tree like this one:
#                                               1
#                                                \
#                                                 2
#                                                 /
#                                                3
# But that argument is resolved from the fact that even if so, this has to be done once and that time is compensated by how currentNode is then automatically stored like we don't have to traverse as left returns but roughly thus n time is taken could be said in total
# SC: O(n) Explanation: resArr is directly storing and returning the answer so its space is exempted. Space n is in worst case consumed for auxiliary/recursive stack storage


# Approach2: Iterative Approach - We'll follow same thing as approach1 with just one exception that here as recursive stack space won't be provided implicitly, we replicate that by an external stack. So we use a stack to store parentNodes and a resArr to store InOrder Items that will be returned at the end. So we start by assigning the root to a variable currNode. As we saw in Approach1 we first traverse all the way to left and each time the recursive call stores the call stack. Here to be able to come back as we do `while currNode: currNode=currNode.left` we append the currNode in stack too. Thus, we'll be at leftNode's left which will be None when we exit the while currNode. After this we pop the item from stack first store it into resArr and then make currNode as this popped item's right. Thus, we will now traverse the right and if it's empty the item's val would be stored and further its parent is accessed by popping stack top and we'll make current as this node's right. That's the whole algo, and we'll put this looping part into a while loop that goes on till currNode is not None or stack is not Empty, for obvious reasons.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        resArr, stack = [], []
        currNode = root
        while currNode or stack:
            while currNode:
                stack.append(currNode)
                currNode = currNode.left
            currNode = stack.pop()
            resArr.append(currNode.val)
            currNode = currNode.right
        return resArr
# TC: O(n)
# SC: O(n) Explanation: n to store all the items of binary tree in worst case in the stack
