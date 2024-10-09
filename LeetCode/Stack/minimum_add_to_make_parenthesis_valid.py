class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        dq = deque()
        res = 0
        for i in list(s):
            if i == '(':
                dq.append('(')
            else:
                if dq:
                    dq.pop()
                else:
                    res+=1
        return res+len(dq)
