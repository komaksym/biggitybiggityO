# Time:  O(n)

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def lcaDeepestLeaves(self, root):
        
        def lcaDeepestLeavesHelper(root):
            if not root:
                return 0, None
            d1, lca1 = lcaDeepestLeavesHelper(root.left)
            d2, lca2 = lcaDeepestLeavesHelper(root.right)
            if d1 > d2:
                return d1+1, lca1
            if d1 < d2:
                return d2+1, lca2
            return d1+1, root

        return lcaDeepestLeavesHelper(root)[1]
