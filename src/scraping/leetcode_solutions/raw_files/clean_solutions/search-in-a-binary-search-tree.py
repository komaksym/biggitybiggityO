# Time:  O(h)

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def searchBST(self, root, val):
        while root and val != root.val:
            if val < root.val:
                root = root.left
            else:
                root = root.right
        return root

