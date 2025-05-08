# Time:  O(1)

# string
class Solution(object):
    def convertDateToBinary(self, date):
        """
        :type date: str
        :rtype: str
        """
        return "-".join([bin(int(x))[2:] for x in date.split('-')])
