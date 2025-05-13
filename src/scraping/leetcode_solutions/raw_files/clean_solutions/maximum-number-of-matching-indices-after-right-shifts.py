# Time:  O(n^2)

# brute force
class Solution(object):
    def maximumMatchingIndices(self, nums1, nums2):
        return max(sum(nums2[j] == nums1[(i+j)%len(nums1)] for j in range(len(nums2))) for i in range(len(nums1)))
