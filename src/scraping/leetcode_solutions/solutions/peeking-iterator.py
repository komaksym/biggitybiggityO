# Time:  O(1) per peek(), next(), hasNext()

class PeekingIterator(object):
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.iterator = iterator
        self.val_ = None
        self.has_next_ = iterator.hasNext()
        self.has_peeked_ = False


    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        if not self.has_peeked_:
            self.has_peeked_ = True
            self.val_ = next(self.iterator)
        return self.val_

    def __next__(self):
        """
        :rtype: int
        """
        self.val_ = self.peek()
        self.has_peeked_ = False
        self.has_next_ = self.iterator.hasNext()
        return self.val_

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.has_next_



