# Time:  O(n)


class Solution(object):
    def wordPattern(self, pattern, str):
        if len(pattern) != self.wordCount(str):
            return False

        w2p, p2w = {}, {}
        for p, w in zip(pattern, self.wordGenerator(str)):
            if w not in w2p and p not in p2w:
                w2p[w] = p
                p2w[p] = w
            elif w not in w2p or w2p[w] != p:
                return False
        return True

    def wordCount(self, str):
        cnt = 1 if str else 0
        for c in str:
            if c == ' ':
                cnt += 1
        return cnt

    def wordGenerator(self, str):
        w = ""
        for c in str:
            if c == ' ':
                yield w
                w = ""
            else:
                w += c
        yield w


# Time:  O(n)
class Solution2(object):
    def wordPattern(self, pattern, str):
        words = str.split() 
        if len(pattern) != len(words):
            return False

        w2p, p2w = {}, {}
        for p, w in zip(pattern, words):
            if w not in w2p and p not in p2w:
                w2p[w] = p
                p2w[p] = w
            elif w not in w2p or w2p[w] != p:
                return False
        return True

