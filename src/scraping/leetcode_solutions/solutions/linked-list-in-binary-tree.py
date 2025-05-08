# Time:  O(n + l)

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# kmp solution
class Solution(object):
    def isSubPath(self, head, root):
        def getPrefix(head):
            pattern, prefix = [head.val], [-1]
            j = -1
            node = head.__next__
            while node:
                while j+1 and pattern[j+1] != node.val:
                    j = prefix[j]
                if pattern[j+1] == node.val:
                    j += 1
                pattern.append(node.val)
                prefix.append(j)
                node = node.__next__
            return pattern, prefix
            
        def dfs(pattern, prefix, root, j):
            if not root:
                return False
            while j+1 and pattern[j+1] != root.val:
                j = prefix[j]
            if pattern[j+1] == root.val:
                j += 1
            if j+1 == len(pattern):
                return True
            return dfs(pattern, prefix, root.left, j) or \
                   dfs(pattern, prefix, root.right, j)
        
        if not head:
            return True
        pattern, prefix = getPrefix(head)
        return dfs(pattern, prefix, root, -1)
# dfs solution
class Solution2(object):
    def isSubPath(self, head, root):
        def dfs(head, root):
            if not head:
                return True
            if not root:
                return False
            return root.val == head.val and \
                   (dfs(head.__next__, root.left) or 
                    dfs(head.__next__, root.right))
    
        if not head:
            return True
        if not root:
            return False
        return dfs(head, root) or \
               self.isSubPath(head, root.left) or \
               self.isSubPath(head, root.right)
