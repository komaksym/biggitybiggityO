# Time:  O(n)

class Solution(object):
    def findMinMoves(self, machines):
        
        total = sum(machines)
        if total % len(machines): return -1

        result, target, curr = 0, total / len(machines), 0
        for n in machines:
            curr += n - target
            result = max(result, max(n - target, abs(curr)))
        return result

