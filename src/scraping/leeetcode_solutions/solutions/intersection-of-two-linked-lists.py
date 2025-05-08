# Time:  O(m + n)

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
   
   
    def getIntersectionNode(self, headA, headB):
        curA, curB = headA, headB
        while curA != curB:
            curA = curA.__next__ if curA else headB
            curB = curB.__next__ if curB else headA
        return curA
