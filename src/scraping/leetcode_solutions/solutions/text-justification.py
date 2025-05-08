# Time:  O(n)

class Solution(object):
    def fullJustify(self, words, maxWidth):
        
        def add            if i <                
               

        def connect(words, maxWidth, begin, end, length, is_last):
            s = [] 
            for i in range(n):
                s += words[begin + i],
                s += ' ' * add           
            line = "".join(s)
            if len(line) < maxWidth:
                line += ' ' * (maxWidth - len(line))
            return line

        res = []
        begin, length = 0, 0
        for i in range(len(words)):
            if length + len(words[i]) + (i - begin) > maxWidth:
                res += connect(words, maxWidth, begin, i, length, False),
                begin, length = i, 0
            length += len(words[i])

       
        res += connect(words, maxWidth, begin, len(words), length, True),
        return res


