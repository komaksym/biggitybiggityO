# Time:  O(n^2)

import collections


class Solution(object):
    def numTilePossibilities(self, tiles):
        """
        :type tiles: str
        :rtype: int
        """
        fact = [0.0]*(len(tiles)+1)
        fact[0] = 1.0
        for i in range(1, len(tiles)+1):
            fact[i] = fact[i-1]*i
        count = collections.Counter(tiles)

        
        coeff = [0.0]*(len(tiles)+1)
        coeff[0] = 1.0
        for i in count.values():
            new_coeff = [0.0]*(len(tiles)+1)
            for j in range(len(coeff)):
                for k in range(i+1):
                    if k+j >= len(new_coeff):
                        break
                    new_coeff[j+k] += coeff[j]*1.0/fact[k]
            coeff = new_coeff

        result = 0
        for i in range(1, len(coeff)):
            result += int(round(coeff[i]*fact[i]))
        return result


# Time:  O(r), r is the value of result
class Solution2(object):
    def numTilePossibilities(self, tiles):
        """
        :type tiles: str
        :rtype: int
        """
        def backtracking(counter):
            total = 0
            for k, v in counter.items():
                if not v:
                    continue
                counter[k] -= 1
                total += 1+backtracking(counter)
                counter[k] += 1
            return total

        return backtracking(collections.Counter(tiles))
