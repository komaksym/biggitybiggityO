# Time:  O(n)

class Solution(object):
    def minDiffInBST(self, root):
        
        def dfs(node):
            if not node:
                return
            dfs(node.left)
            self.result = min(self.result, node.val-self.prev)
            self.prev = node.val
            dfs(node.right)

        self.prev = float('-inf')
        self.result = float('inf')
        dfs(root)
        return self.result


