class Solution:
    def minimumSteps(self, s: str) -> int:
        s=list(s)
        c_z = 0
        for i in s:
            if i == '0':
                c_z+=1

        curr_to_fill =0
        swaps = 0
        for i in range(len(s)):
            ele = s[i]
            if c_z == 0:
                break
            if ele == '0':
                if curr_to_fill == i:
                    curr_to_fill +=1
                    c_z-=1
                    continue
                else:
                    swaps += i-curr_to_fill
                    curr_to_fill+=1
                    c_z-=1
        return swaps



# one pass Solution

class Solution:
    def minimumSteps(self, s: str) -> int:
        s = list(s)
        swaps = 0
        write = 0
        for i in range(len(s)):
            if s[i] == '0':
                swaps += i-write
                write+=1
        return swaps
