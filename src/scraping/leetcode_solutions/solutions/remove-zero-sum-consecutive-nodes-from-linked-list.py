# Time:  O(n)

import collections


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def removeZeroSumSublists(self, head):
        curr = dummy = ListNode(0)
        dummy.next = head
        prefix = 0
        lookup = collections.OrderedDict()
        while curr:
            prefix += curr.val
            node = lookup.get(prefix, curr)
            while prefix in lookup:
                lookup.popitem()
            lookup[prefix] = node
            node.next = curr.__next__
            curr = curr.__next__
        return dummy.__next__
