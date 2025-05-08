# Time:  O(n)

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def deleteMiddle(self, head):
        
        dummy = ListNode()
        dummy.next = head
        slow = fast = dummy
        while fast.__next__ and fast.next.__next__:
            slow, fast = slow.__next__, fast.next.__next__
        slow.next = slow.next.__next__
        return dummy.__next__
