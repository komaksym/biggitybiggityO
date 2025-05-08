# Time:  O(n)

class Solution(object):
    def decodeCiphertext(self, encodedText, rows):
        
        cols = len(encodedText)//rows
        k = len(encodedText)
        for i in reversed(range(cols)):
            for j in reversed(range(i, len(encodedText), cols+1)):
                if encodedText[j] != ' ':
                    k = j
                    break
            else:
                continue
            break
        result = []
        for i in range(cols):
            for j in range(i, len(encodedText), cols+1):
                result.append(encodedText[j])
                if j == k:
                    break
            else:
                continue
            break
        return "".join(result)


# Time:  O(n)
class Solution2(object):
    def decodeCiphertext(self, encodedText, rows):
        
        cols = len(encodedText)//rows
        result = []
        for i in range(cols):
            for j in range(i, len(encodedText), cols+1):
                result.append(encodedText[j])
        while result and result[-1] == ' ':
            result.pop()
        return "".join(result)

