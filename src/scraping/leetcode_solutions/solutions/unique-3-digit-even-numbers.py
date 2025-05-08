# Time:  O(n)
# Space: O(1)

# freq table, combinatorics
class Solution(object):
    def totalNumbers(self, digits):
        """
        :type digits: List[int]
        :rtype: int
        """
        cnt = [0]*10
        for x in digits:
            cnt[x] += 1
        even = sum(cnt[i] != 0 for i in range(0, len(cnt), 2))
        odd = sum(cnt[i] != 0 for i in range(1, len(cnt), 2))
        result = 0
        for i in range(2, len(cnt), 2):
            if cnt[i] >= 3:
                result += 1  # eee
        result += even*(odd+even-1)*(odd+even-2)  # xye
        if cnt[0]:
            result -= 1*(even-1)*(odd+even-2)  # 0xe
        for i in range(len(cnt)):
            if cnt[i] < 2:
                continue
            if i == 0:
                result += (odd+even)-1  # x00
            elif i%2:
                result += even  # ooe
            else:
                result += 3*(even-1)-int(cnt[0] != 0)  # eeE, eEe, Eee excluding 0ee
                result += 2*odd  # eoe, oee
        return result
