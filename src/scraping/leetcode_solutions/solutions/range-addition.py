# Time:  O(k + n)

class Solution(object):
    def getModifiedArray(self, length, updates):
        
        result = [0] * length
        for update in updates:
            result[update[0]] += update[2]
            if update[1]+1 < length:
                result[update[1]+1] -= update[2]

        for i in range(1, length):
            result[i] += result[i-1]

        return result

