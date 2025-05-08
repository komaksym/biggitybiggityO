# Time:  O(nlogn)

# sort
class Solution(object):
    def countOperationsToEmptyArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        idxs = list(range(len(nums)))
        idxs.sort(key=lambda x: nums[x])
        return len(idxs)+sum(len(idxs)-(i+1) for i in range(len(idxs)-1) if idxs[i] > idxs[i+1])


# Time:  O(nlogn)
# sort, bit, fenwick tree
class Solution2(object):
    def countOperationsToEmptyArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        class BIT(object): 
            def __init__(self, n):
                self.__bit = [0]*(n+1) 

            def add(self, i, val):
                i += 1 
                while i < len(self.__bit):
                    self.__bit[i] += val
                    i += (i & -i)

            def query(self, i):
                i += 1 
                ret = 0
                while i > 0:
                    ret += self.__bit[i]
                    i -= (i & -i)
                return ret
        
        bit = BIT(len(nums))
        idxs = list(range(len(nums)))
        idxs.sort(key=lambda x: nums[x])
        result = len(nums)
        prev = -1
        for i in idxs:
            if prev == -1:
                result += i
            elif prev < i:
                result += (i-prev)-(bit.query(i)-bit.query(prev-1))
            else:
                result += ((len(nums)-1)-bit.query(len(nums)-1))-((prev-i)-(bit.query(prev)-bit.query(i-1)))
            bit.add(i, 1)
            prev = i
        return result
