class Solution:
    def compress(self, chars: List[str]) -> int:
        ins = 0
        i=0
        while i < len(chars):
            gl=1
            while i+1 < len(chars) and chars[i]==chars[i+1]:
                gl+=1
                i+=1
            chars[ins] = chars[i]
            ins += 1
            if gl > 1:
                for digit in str(gl):
                    chars[ins] = digit
                    ins += 1
            i+=1
        return ins
