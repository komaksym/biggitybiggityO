# Time:  O(h)

class Solution(object):
    def inorderSuccessor(self, root, p):
        
       
        if p and p.right:
            p = p.right
            while p.left:
                p = p.left
            return p

       
        successor = None
        while root and root != p:
            if root.val > p.val:
                successor = root
                root = root.left
            else:
                root = root.right

        return successor

