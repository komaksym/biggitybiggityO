# Time:  O(nlogn)
# Space: O(n)

import collections


class Solution(object):
    def groupStrings(self, strings):
        groups = collections.defaultdict(list)
        for s in strings:  # Grouping.
            groups[self.hashStr(s)].append(s)

        result = []
        for key, val in groups.items():
            result.append(sorted(val))

        return result

    def hashStr(self, s):
        base = ord(s[0])
        hashcode = ""
        for i in range(len(s)):
            if ord(s[i]) - base >= 0:
                hashcode += chr(ord('a') + ord(s[i]) - base)
            else:
                hashcode += chr(ord('a') + ord(s[i]) - base + 26)
        return hashcode

