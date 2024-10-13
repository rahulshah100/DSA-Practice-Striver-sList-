# https://www.codingninjas.com/studio/problems/boundary-traversal-of-binary-tree_790725?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf

# Problem statement
# You are given a binary tree with 'n' nodes. The boundary nodes of this binary tree include the nodes from the left and right boundaries, as well as the leaf nodes. Each node is considered once.

# Figure out the boundary nodes of this binary tree in an anti-clockwise direction starting from the root node.
# Example:
# Input: Consider the binary tree A as shown in the figure:
# Binary Tree
# Output: [10, 5, 3, 7, 18, 25, 20]

# Sample Input 1:
# 10 5 20 3 8 18 25 -1 -1 7 -1 -1 -1 -1 -1 -1 -1
# Sample Output 1:
# 10 5 3 7 18 25 20
# Explanation of Sample Input 1:
# The nodes on the left boundary are [10, 5, 3]
# The nodes on the right boundary are [10, 20, 25]
# The leaf nodes are [3, 7, 18, 25].
# Please note that nodes 3 and 25 appear in two places but are considered once.

# Sample Input 2:
# 100 50 150 25 75 140 200 -1 30 70 80 -1 -1 -1 -1 -1 35 -1 -1 -1 -1 -1 -1
# Sample Output 2:
# 100 50 25 30 35 70 80 140 200 150

# Constraints:
# 1 <= n <= 10000
# Where 'n' is the total number of nodes in the binary tree.
# ---------------------------------------------------------------------------------------------------------------------------------------
# Approach1: We observe that boundary can be broken into 3 components - lefMostNodes,leafNodes,rightMostNodesButReverseOrder for all 3 of which components we make separate functions. lefMostNodes are counted by leftBoundary() where we check at the start if node is not leaf by checking it's not the case that it neither has any child, and if so violated it is leafNode at which point we must have traversed the whole leftNodeWall and we return. If not we append current Node in resArr and check if there is a further leftNode which if so we traverse onto and if not we check if there is a rightNode? which would be leftMost in that case and that's why we consider traversing there in the case root.left is not there but root.right is. After this for leafNode  in a separate function we perform inOrder where using the same condition to identify leaf node `if not root.left and not root.right` we store leaf nodes in resArr, when encountered with them. After that for rightMostNodesButReverseOrder it is almost similar to leftMostNodes where we store items in a tempArr first and then pop them and store in resArr, in which way they have been reversed while storing. resArr is returned at the end
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def leftBoundary(root, resArr):
    if not root.left and not root.right:
        return

    resArr.append(root.data)
    if root.left:
        leftBoundary(root.left, resArr)
    else:
        leftBoundary(root.right, resArr)


def leafNodes(root, resArr):
    if not root:
        return

    if not root.left and not root.right:
        resArr.append(root.data)

    leafNodes(root.left, resArr)
    leafNodes(root.right, resArr)


def rightBoundary(root, temp):
    if not root or (not root.left and not root.right): #Here at #--1 the function is directly passed the root.right which could be None which when checked for root.left or root.right can give error. This is not the case for #--2 where root is passed and not root.left, also for this root at #--3 as is visible it's been checked that it's not None so in leftBoundary we've not included this check
        return

    temp.append(root.data)
    if root.right:
        rightBoundary(root.right, temp)
    else:
        rightBoundary(root.left, temp)


def traverseBoundary(root):
    if not root: return       #--3
    resArr, temp = [], []
    leftBoundary(root, resArr) #--2
    leafNodes(root, resArr)
    rightBoundary(root.right, temp) #--1
    while len(temp):
        top = temp.pop()
        resArr.append(top)
    return resArr

#    1
#   / \
#  2   3
# / \   \
# 4   5  7
root = BinaryTreeNode(1)
root.left = BinaryTreeNode(2)
root.right = BinaryTreeNode(3)
root.left.left = BinaryTreeNode(4)
root.left.right = BinaryTreeNode(5)
root.right.right = BinaryTreeNode(7)
print(traverseBoundary(root))

# TC: O(n)
# SC: O(n)