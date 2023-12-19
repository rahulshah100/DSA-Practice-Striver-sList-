# https://takeuforward.org/data-structure/preorder-inorder-postorder-traversals-in-one-traversal/

# Problem statement
# You have been given a Binary Tree of 'N' nodes, where the nodes have integer values. Your task is to return the In-Order, Pre-Order, and Post-Order traversals of the given binary tree.

# For example:
# For the given binary tree:
#        1
#       / \
#      3   4
#     / \   \
#    5   2   7
#         \
#          6
# The Inorder traversal will be [5, 3, 2, 1, 7, 4, 6].
# The Preorder traversal will be [1, 3, 5, 2, 4, 7, 6].
# The Postorder traversal will be [5, 2, 3, 7, 6, 4, 1].

# Sample Input 1 :
# 1 2 3 -1 -1 -1  6 -1 -1
# Sample Output 1 :
# 2 1 3 6
# 1 2 3 6
# 2 6 3 1
# Explanation of Sample Output 1 :
# The given binary tree is shown below:
# Inorder traversal of given tree = [2, 1, 3, 6]
# Preorder traversal of given tree = [1, 2, 3, 6]
# Postorder traversal of given tree = [2, 6, 3, 1]

# Sample Input 2 :
# 1 2 4 5 3 -1 -1 -1 -1 -1 -1
# Sample Output 2 :
# 5 2 3 1 4
# 1 2 5 3 4
# 5 3 2 4 1
# Explanation of Sample Output 2 :
# The given binary tree is shown below:
# Inorder traversal of given tree = [5, 2, 3, 1, 4]
# Preorder traversal of given tree = [1, 2, 5, 3, 4]
# Postorder traversal of given tree = [5, 3, 2, 4, 1]

# Constraints :
# 1 <= 'N' <= 10^5
# 0 <= 'data' <= 10^5

# where 'N' is the number of nodes and 'data' denotes the node value of the binary tree nodes.
# --------------------------------------------------------------------------------------------------------------------------------------------------------
# Approach1: Using a stack (because for all 3 traversals we go left, left, and left so the last inserted is first needed to be popped) we store a pair of (root, Order) where order can be 1,2, or 3 indicating whether preOrder, inOrder or postOrder array should append the root's value. Such order is there because preOrder inserts the current first then traverse to L and then R, while inOrder does L, C and R i.e. it traverses to left Most and then starts appending Cs whereas postOrder will traverse all the left and then all the right before starting to append items. To replicate this logic we store the (root, order-1) in stack as a pair and run a while loop till stack is empty. First thing we do in the loop is pop it and check if order obtained is 1, 2 or 3. For order-1 we'll append the node's val into preOrder and so that now on our way return, this item can become accessible for inOrder we restore the same node but with an incremented order. After this we traverse further left by storing in stack the poppedItem'sLeft and order-1 as the new pair. Thus, all the way to the bottom in below example which will be node-3 we'll reach, by the time storing all these items in preOrder. When at 3 after preOrder array stores its value, nothing extra is stored in stack as 3 doesn't have left or right Nodes and so at top then we'll have the same node and incremented order i.e. (3,2). Now is in which iteration as 2 is
#           1
#         /   \
#        2     5
#       / \   /  \
#      3  4   6  7
class BinaryTreeNode :
    def __init__(self, data) :
        self.data = data
        self.left = None
        self.right = None

def getTreeTraversal(root):
    stack = []
    preO,postO,inO = [],[],[]
    stack.append((root, 1))
    while stack:
        top=stack.pop()
        if top[1]==1:
            preO.append(top[0].data)
            stack.append((top[0], top[1]+1))
            if top[0].left:
                stack.append((top[0].left, 1))
        elif top[1]==2:
            inO.append(top[0].data)
            stack.append((top[0], top[1]+1))
            if top[0].right:
                stack.append((top[0].right, 1))
        else:
            postO.append(top[0].data)
    return inO, preO, postO
# TC: O(3n)
# SC: O(n)