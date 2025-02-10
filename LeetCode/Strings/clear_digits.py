class Solution:
    def clearDigits(self, s: str) -> str:
        s = list(s)
        index_of_char = None
        i=0
        while s and i != len(s):
            if s[i].isalpha():
                index_of_char = i
                i+=1
            else:
                s.pop(i)
                if index_of_char is not None:
                    s.pop(index_of_char)
                i=0
                index_of_char = None
        return "".join(s)
