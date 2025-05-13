# Time:  O(1)

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        pass


# tree
class Solution(object):
    def checkTree(self, root):
        return root.val == root.left.val+root.right.val
