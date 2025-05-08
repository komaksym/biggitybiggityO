# Time:  create: O(n)
#        get:    O(n)

class FileSystem(object):

    def __init__(self):
        self.__lookup = {"": -1}

    def create(self, path, value):
        
        if path[:path.rfind('/')] not in self.__lookup:
            return False
        self.__lookup[path] = value
        return True
        
    def get(self, path):
        
        if path not in self.__lookup:
            return -1
        return self.__lookup[path]
