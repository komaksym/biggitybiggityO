# Time:  ls: O(l + klogk), l is the path length, k is the number of entries in the last level directory
#        mkdir: O(l)
#        addContentToFile: O(l + c), c is the content size
#        readContentFromFile: O(l + c)

class TrieNode(object):

    def __init__(self):
        self.is_file = False
        self.children = {}
        self.content = ""

class FileSystem(object):

    def __init__(self):
        self.__root = TrieNode()


    def ls(self, path):
        curr = self.__getNode(path)

        if curr.is_file:
            return [self.__split(path, '/')[-1]]

        return sorted(curr.children.keys())


    def mkdir(self, path):
        curr = self.__putNode(path)
        curr.is_file = False


    def addContentToFile(self, filePath, content):
        curr = self.__putNode(filePath)
        curr.is_file = True
        curr.content += content


    def readContentFromFile(self, filePath):
        return self.__getNode(filePath).content


    def __getNode(self, path):
        curr = self.__root
        for s in self.__split(path, '/'):
            curr = curr.children[s]
        return curr


    def __putNode(self, path):
        curr = self.__root
        for s in self.__split(path, '/'):
            if s not in curr.children:
                curr.children[s] = TrieNode()
            curr = curr.children[s]
        return curr


    def __split(self, path, delim):
        if path == '/':
            return []
        return path.split('/')[1:]


