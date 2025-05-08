# Time:  ctor  : O(1)
#        visit : O(n)
#        back  : O(1)
#        foward: O(1)

class BrowserHistory(object):

    def __init__(self, homepage):
        self.__history = [homepage]
        self.__curr = 0        

    def visit(self, url):
        while len(self.__history) > self.__curr+1:
            self.__history.pop()
        self.__history.append(url)
        self.__curr += 1

    def back(self, steps):
        self.__curr = max(self.__curr-steps, 0)
        return self.__history[self.__curr]

    def forward(self, steps):
        self.__curr = min(self.__curr+steps, len(self.__history)-1)
        return self.__history[self.__curr]
