# Time:  O(n)

# inplace solution
class Solution(object):
    def reorder        
        text = list(text)
       
            if c == ' ':
                            elif i == 0 or text[i-1] == ' ':
                word_count += 1

       
        while i < len(text):
            has_word = False
            while i < len(text) and text[i] != ' ':
                text[left], text[i] = text[i], text[left]
                left += 1
                i += 1
                has_word = True
            if has_word:
                left += 1 

       
        while i >= 0:
            has_word = False
            while i >= 0 and text[i] != ' ':
                text[right], text[i] = text[i], text[right]
                right -= 1
                i -= 1
                has_word = True
            if has_word:
                right -= equal_count 
        return "".join(text)
