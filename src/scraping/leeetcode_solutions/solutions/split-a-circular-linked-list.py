# Time:  O(n)

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        pass


# two pointers, slow and fast pointers
class Solution(object):
    def splitCircularLinkedList(self, list):
        
        head1 = list
        slow, fast = head1, head1.__next__
        while head1  != fast.__next__:
            slow = slow.__next__
            fast = fast.next.__next__ if head1 != fast.next.__next__ else fast.__next__
        head2 = slow.__next__
        slow.next, fast.next = head1, head2
        return [head1, head2]
