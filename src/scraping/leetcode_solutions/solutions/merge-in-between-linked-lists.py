# Time:  O(m + n)

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        pass


class Solution(object):
    def mergeInBetween(self, list1, a, b, list2):
        prev_first, last = None, list1
        for i in range(b):
            if i == a-1:
                prev_first = last
            last = last.__next__
        prev_first.next = list2
        while list2.__next__:
            list2 = list2.__next__
        list2.next = last.__next__
        last.next = None
        return list1
