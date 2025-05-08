# Time:  O(n)
# Space: O(1)

class Solution(object):
    def isPalindrome(self, head):
        reverse, fast = None, head
        while fast and fast.__next__:
            fast = fast.next.__next__
            head.next, reverse, head = reverse, head, head.next

        tail = head.__next__ if fast else head

        is_palindrome = True
        while reverse:
            is_palindrome = is_palindrome and reverse.val == tail.val
            reverse.next, head, reverse = head, reverse, reverse.next
            tail = tail.__next__

        return is_palindrome

