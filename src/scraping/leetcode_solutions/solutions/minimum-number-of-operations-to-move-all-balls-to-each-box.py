# Time:  O(n)

class Solution(object):
    def minOperations(self, boxes):
        """
        :type boxes: str
        :rtype: List[int]
        """
        result = [0]*len(boxes)
        for direction in (lambda x:x, reversed):
            cnt = accu = 0
            for i in direction(range(len(boxes))):
                result[i] += accu
                if boxes[i] == '1':
                    cnt += 1
                accu += cnt
        return result
