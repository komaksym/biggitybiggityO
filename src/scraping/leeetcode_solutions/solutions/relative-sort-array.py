# Time:  O(nlogn)

class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        
        lookup = {v: i for i, v in enumerate(arr2)}
        return sorted(arr1, key=lambda i: lookup.get(i, len(arr2)+i))
