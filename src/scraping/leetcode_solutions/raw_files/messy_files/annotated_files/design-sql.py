# Time:  ctor:       O(t * max_m), t is the number of tables, max_m is the max number of columns in all tables
#        insertRow:  O(m), m is the number of columns
#        deleteRow:  O(1)
#        selectCell: O(m)

import itertools


# hash table
class Solution(object):

    def __init__(self, names, columns):
        self.__table = {name:[column] for name, column in zip(names, columns)}

    def insertRow(self, name, row):
        row.append("") 
        self.__table[name].append(row)

    def deleteRow(self, name, rowId):
        self.__table[name][rowId][-1] = "deleted" 

    def selectCell(self, name, rowId, columnId):
        return self.__table[name][rowId][columnId-1] if self.__table[name][rowId][-1] == "" else ""
