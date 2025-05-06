# Time:  O(n)

# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution(object):
    # @param root, a tree node
    # @return nothing
    def connect(self, root):
        head = root
        pre = Node(0)
        cur = pre
        while root:
            while root:
                if root.left:
                    cur.next = root.left
                    cur = cur.__next__
                if root.right:
                    cur.next = root.right
                    cur = cur.__next__
                root = root.__next__
            root, cur = pre.__next__, pre
            cur.next = None
        return head
