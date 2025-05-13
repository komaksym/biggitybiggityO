# Time:  O(logn) on average for each operation

# see proof in references:
# 1. https://kunigami.blog/2012/09/25/skip-lists-in-python/
# 2. https://opendatastructures.org/ods-cpp/4_4_Analysis_Solutions.html
# 3. https://brilliant.org/wiki/skip-lists/
import random


class SkipNode(object):
    def __init__(self, level=0, num=None):
        self.num = num
        self.nexts = [None]*level


class Solution(object):
    P_NUMERATOR, P_DENOMINATOR = 1, 2 
    MAX_LEVEL = 32 

    def __init__(self):
        self.__head = SkipNode()
        self.__len = 0

    def search(self, target):
        return True if self.__find(target, self.__find_prev_nodes(target)) else False
        
    def add(self, num):
        node = SkipNode(self.__random_level(), num)
        if len(self.__head.nexts) < len(node.nexts): 
            self.__head.nexts.extend([None]*(len(node.nexts)-len(self.__head.nexts)))
        prevs = self.__find_prev_nodes(num)
        for i in range(len(node.nexts)):
            node.nexts[i] = prevs[i].nexts[i]
            prevs[i].nexts[i] = node
        self.__len += 1

    def erase(self, num):
        prevs = self.__find_prev_nodes(num)
        curr = self.__find(num, prevs)
        if not curr:
            return False
        self.__len -= 1   
        for i in reversed(range(len(curr.nexts))):
            prevs[i].nexts[i] = curr.nexts[i]
            if not self.__head.nexts[i]:
                self.__head.nexts.pop()
        return True
    
    def __find(self, num, prevs):
        if prevs:
            candidate = prevs[0].nexts[0]
            if candidate and candidate.num == num:
                return candidate
        return None

    def __find_prev_nodes(self, num):
        prevs = [None]*len(self.__head.nexts)
        curr = self.__head
        for i in reversed(range(len(self.__head.nexts))):
            while curr.nexts[i] and curr.nexts[i].num < num:
                curr = curr.nexts[i]
            prevs[i] = curr
        return prevs

    def __random_level(self):
        level = 1
        while random.randint(1, Solution.P_DENOMINATOR) <= Solution.P_NUMERATOR and \
              level < Solution.MAX_LEVEL:
            level += 1
        return level

    def __len__(self):
        return self.__len
    
    def __str__(self):
        result = []
        for i in reversed(range(len(self.__head.nexts))):
            result.append([])
            curr = self.__head.nexts[i]
            while curr:
                result[-1].append(str(curr.num))
                curr = curr.nexts[i]
        return "\n".join(["->".join(x) for x in result])
