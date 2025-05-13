# Time:  O(n)

# tree
class Solution(object):
    def createBinaryTree(self, descriptions):
        nodes = {}
        children = set()
        for p, c, l in descriptions:
            parent = nodes.setdefault(p, TreeNode(p))
            child = nodes.setdefault(c, TreeNode(c))
            if l:
                parent.left = child
            else:
                parent.right = child
            children.add(c)
        return nodes[next(p for p in nodes.keys() if p not in children)]
