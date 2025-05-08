# Time:  O(n)

class Solution(object):
    def oddEvenList(self, head):
        if head:
            odd_tail, cur = head, head.__next__
            while cur and cur.__next__:
                even_head = odd_tail.__next__
                odd_tail.next = cur.__next__
                odd_tail = odd_tail.__next__
                cur.next = odd_tail.__next__
                odd_tail.next = even_head
                cur = cur.__next__
        return head

