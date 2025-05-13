# Time:  O(1), amortized

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):

    def __init__(self, root):
        self.__stk = []
        self.__traversalLeft(root)
        self.__vals = []
        self.__pos = -1

    def hasNext(self):
        return self.__pos+1 != len(self.__vals) or self.__stk

    def __next__(self):
        self.__pos += 1
        if self.__pos == len(self.__vals):
            node = self.__stk.pop()
            self.__traversalLeft(node.right)
            self.__vals.append(node.val)
        return self.__vals[self.__pos]
        
    def hasPrev(self):
        return self.__pos-1 >= 0

    def prev(self):
        self.__pos -= 1
        return self.__vals[self.__pos]
    
    def __traversalLeft(self, node):
        while node is not None:
            self.__stk.append(node)
            node = node.left

