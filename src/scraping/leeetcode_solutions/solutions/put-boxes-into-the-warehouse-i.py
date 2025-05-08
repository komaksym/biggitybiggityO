# Time:  O(nlogn)

class Solution(object):
    def maxBoxesInWarehouse(self, boxes, warehouse):
        
        boxes.sort(reverse=True)
        result = 0
        for h in boxes:
            if h > warehouse[result]:
                continue
            result += 1
            if result == len(warehouse):
                break
        return result


# Time:  O(nlogn + m)
class Solution2(object):
    def maxBoxesInWarehouse(self, boxes, warehouse):
        
        boxes.sort()
        for i in range(1, len(warehouse)):
            warehouse[i] = min(warehouse[i], warehouse[i-1])
        result, curr = 0, 0
        for h in reversed(warehouse):
            if boxes[curr] > h:
                continue
            result += 1
            curr += 1
            if curr == len(boxes):
                break
        return result
