# Time:  O(1)

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class BSTIterator(object):
    def __init__(self, root):
        self.__stk = []
        self.__traversalLeft(root)

    def hasNext(self):
        return self.__stk

    def __next__(self):
        node = self.__stk.pop()
        self.__traversalLeft(node.right)
        return node.val
    
    def __traversalLeft(self, node):
        while node is not None:
            self.__stk.append(node)
            node = node.left

