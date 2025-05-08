# Time:  precompute: O(max_s^(1/5) * log(max_s))
#        runtime:    O(log(max_s))

import bisect 


# precompute, bitmasks, combinatorics, binary search
i, area = 1, 0
vol = [0]
class Solution(object):
    def maxSizedArray(self, s):
        
        global i, area
        while vol[-1] <= s:
            area += 2*((i-1)*i+sum((((i-1)>>(bit+1))*(1<<bit))*(1<<bit) for bit in range((i-1).bit_length()) if not (i-1)&(1<<bit)))-((i-1)|(i-1))
            vol.append(((0+(i-1))*i//2)*area)
            i += 1
        return bisect.bisect_right(vol, s)-1
