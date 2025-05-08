# Time:  O(n)

# two pointers
class Solution(object):
    def getCommon(self, nums1, nums2):
        
        i = j = 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                i += 1
            elif nums1[i] > nums2[j]:
                j += 1
            else:
                return nums1[i]
        return -1
