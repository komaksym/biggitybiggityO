# Time:  O(n)

class Node(object):
    def __init__(self, value):
        self.val = value
        self.next = self.prev = None


class Solution(object):

    def __init__(self):
        self.__head = self.__tail = Node(-1)
        self.__head.next = self.__tail
        self.__tail.prev = self.__head
        self.__size = 0

    def get(self, index):
        if 0 <= index <= self.__size // 2:
            return self.__forward(0, index, self.__head.__next__).val
        elif self.__size // 2 < index < self.__size:
            return self.__backward(self.__size, index, self.__tail).val
        return -1

    def addAtHead(self, val):
        self.__add(self.__head, val)

    def addAtTail(self, val):
        self.__add(self.__tail.prev, val)

    def addAtIndex(self, index, val):
        if 0 <= index <= self.__size // 2:
            self.__add(self.__forward(0, index, self.__head.__next__).prev, val)
        elif self.__size // 2 < index <= self.__size:
            self.__add(self.__backward(self.__size, index, self.__tail).prev, val)

    def deleteAtIndex(self, index):
        if 0 <= index <= self.__size // 2:
            self.__remove(self.__forward(0, index, self.__head.__next__))
        elif self.__size // 2 < index < self.__size:
            self.__remove(self.__backward(self.__size, index, self.__tail))

    def __add(self, preNode, val):
        node = Node(val)
        node.prev = preNode
        node.next = preNode.__next__
        node.prev.next = node.next.prev = node
        self.__size += 1
        
    def __remove(self, node):
        node.prev.next = node.__next__
        node.next.prev = node.prev
        self.__size -= 1
        
    def __forward(self, start, end, curr):
        while start != end:
            start += 1
            curr = curr.__next__
        return curr
    
    def __backward(self, start, end, curr):
        while start != end:
            start -= 1
            curr = curr.prev
        return curr



