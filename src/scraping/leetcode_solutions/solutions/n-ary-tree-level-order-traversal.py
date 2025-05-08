# Time:  O(n)

class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children


class Solution(object):
    def levelOrder(self, root):
        
        if not root:
            return []
        result, q = [], [root]
        while q:
            result.append([node.val for node in q])
            q = [child for node in q for child in node.children if child]
        return result

