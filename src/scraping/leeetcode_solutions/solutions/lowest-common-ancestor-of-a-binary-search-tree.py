# Time:  O(n)

class Solution(object):
   
   
   
   
    def lowestCommonAncestor(self, root, p, q):
        s, b = sorted([p.val, q.val])
        while not s <= root.val <= b:
           
            root = root.left if s <= root.val else root.right
       
        return root

