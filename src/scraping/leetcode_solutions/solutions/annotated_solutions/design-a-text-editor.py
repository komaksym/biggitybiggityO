# Time:  ctor:        O(1)
#        addText:     O(l)
#        deleteText:  O(k)
#        cursorLeft:  O(k)
#        cursorRight: O(k)

# design, stack
class TextEditor(object):

    def __init__(self):
        self.__LAST_COUNT = 10
        self.__left = []
        self.__right = []

    def addText(self, text):
        for x in text:
            self.__left.append(x)

    def deleteText(self, k):
        return self.__move(k, self.__left, None)

    def cursorLeft(self, k):
        self.__move(k, self.__left, self.__right)
        return self.__last_characters()

    def cursorRight(self, k):
        self.__move(k, self.__right, self.__left)
        return self.__last_characters()

    def __move(self, k, src, dst):
        cnt = min(k, len(src))
        for _ in range(cnt):
            if dst is not None:
                dst.append(src[-1])
            src.pop()
        return cnt

    def __last_characters(self):
        return "".join(self.__left[-self.__LAST_COUNT:])
