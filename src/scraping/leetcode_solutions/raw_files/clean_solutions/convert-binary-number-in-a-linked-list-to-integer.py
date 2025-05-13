# Time:  O(n)

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def getDecimalValue(self, head):
        result = 0
        while head: 
            result = result*2 + head.val 
            head = head.__next__ 
        return result
