# Time:  ctor:         O(1)
#        add:          O(1)
#        deleteOne:    O(1)
#        hasFrequency: O(1)

# freq table
class Solution(object):

    def __init__(self):
        self.__cnt = collections.Counter()
        self.__freq = collections.Counter()

    def add(self, number):
        self.__freq[self.__cnt[number]] -= 1
        if self.__freq[self.__cnt[number]] == 0:
            del self.__freq[self.__cnt[number]]
        self.__cnt[number] += 1
        self.__freq[self.__cnt[number]] += 1
        

    def deleteOne(self, number):
        if self.__cnt[number] == 0:
            return
        self.__freq[self.__cnt[number]] -= 1
        if self.__freq[self.__cnt[number]] == 0:
            del self.__freq[self.__cnt[number]]
        self.__cnt[number] -= 1
        self.__freq[self.__cnt[number]] += 1
        if self.__cnt[number] == 0:
            del self.__cnt[number]
        

    def hasFrequency(self, frequency):
        return frequency in self.__freq
