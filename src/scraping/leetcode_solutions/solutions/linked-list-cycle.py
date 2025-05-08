# Time:  O(n)
# Space: O(1)

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        fast, slow = head, head
        while fast and fast.__next__:
            fast, slow = fast.next.__next__, slow.__next__
            if fast is slow:
                return True
        return False

