# Time:  O(h)

# Definition for a Node.
class Node:
    def __init__(self, val):
        pass


class Solution(object):
    def flipBinaryTree(self, root, leaf):
        curr, parent = leaf, None
        while True:
            child = curr.parent
            curr.parent = parent
            if curr.left == parent:
                curr.left = None
            else:
                curr.right = None
            if curr == root:
                break
            if curr.left:
                curr.right = curr.left
            curr.left = child
            curr, parent = child, curr
        return leaf
