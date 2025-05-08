# Time:  ctor:    O(1)
#        birth:   O(1)
#        death:   O(1)
#        inherit: O(n)

import collections


class ThroneInheritance(object):

    def __init__(self, kingName):
        self.__king = kingName
        self.__family_tree = collections.defaultdict(list)
        self.__dead = set()
        

    def birth(self, parentName, childName):
        self.__family_tree[parentName].append(childName)


    def death(self, name):
        self.__dead.add(name)
        
    
    def getInheritanceOrder(self):
        result = []
        stk = [self.__king]
        while stk:  # preorder traversal
            node = stk.pop()
            if node not in self.__dead:
                result.append(node)
            if node not in self.__family_tree:
                continue
            for child in reversed(self.__family_tree[node]):
                stk.append(child)
        return result

