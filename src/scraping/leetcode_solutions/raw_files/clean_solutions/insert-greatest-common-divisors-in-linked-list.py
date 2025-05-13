# Time:  O(n)

# linked list
class Solution(object):
    def insertGreatestCommonDivisors(self, head):
        def gcd(a, b):
            while b:
                a, b = b, a%b
            return a

        curr = head
        while curr.__next__:
            curr.next = ListNode(gcd(curr.val, curr.next.val), curr.next)
            curr = curr.next.__next__
        return head
