# Time:  O(n)

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def middleNode(self, head):
        
        slow, fast = head, head
        while fast and fast.__next__:
            slow, fast = slow.__next__, fast.next.__next__
        return slow

