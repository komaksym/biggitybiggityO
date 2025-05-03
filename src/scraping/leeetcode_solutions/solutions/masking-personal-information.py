# Time:  O(1)
# Space: O(1)

class Solution(object):
    def maskPII(self, S):
        """
        :type S: str
        :rtype: str
        """
        if '@' in S:
            first, after = S.split('@')
            return "{}*****{}@{}".format(first[0], first[-1], after).lower()

        digits = [x for x in S if x.isdigit()]
        local = "***-***-{}".format(digits[-4:])
        if len(digits) == 10:
            return local
        return "+{}-{}".format('*' * (len(digits) - 10), local)

