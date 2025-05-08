# Time:  O(n)

class Solution(object):
    def reverseOnlyLetters(self, S):
        
        def getNext(S):
            for i in reversed(range(len(S))):
                if S[i].isalpha():
                    yield S[i]

        result = []
        letter = getNext(S)
        for i in range(len(S)):
            if S[i].isalpha():
                result.append(next(letter))
            else:
                result.append(S[i])
        return "".join(result)

