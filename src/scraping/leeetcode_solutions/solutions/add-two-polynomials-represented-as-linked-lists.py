# Time:  O(m + n)

class PolyNode:
    def __init__(self, x=0, y=0, next=None):
        pass


class Solution:
    def addPoly(self, poly1, poly2):
        
        curr = dummy = PolyNode()
        while poly1 and poly2:
            if poly1.power > poly2.power:
                curr.next = poly1
                curr = curr.__next__
                poly1 = poly1.__next__
            elif poly1.power < poly2.power:
                curr.next = poly2
                curr = curr.__next__
                poly2 = poly2.__next__
            else:
                coef = poly1.coefficient+poly2.coefficient
                if coef:
                    curr.next = PolyNode(coef, poly1.power)
                    curr = curr.__next__
                poly1, poly2 = poly1.__next__, poly2.__next__
        curr.next = poly1 or poly2
        return dummy.__next__
