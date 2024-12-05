class Solution:
    def canChange(self, start: str, target: str) -> bool:
        start_q = []
        stop_q = []
        for i in range(len(start)):
            if start[i]!='_':
                start_q.append((start[i],i))
            if target[i]!='_':
                stop_q.append((target[i],i))
        if len(start_q) != len(stop_q):
            return False
        while len(start_q):
            start_c , start_i = start_q.pop(0)
            stop_c, stop_i = stop_q.pop(0)
            if start_c != stop_c or (start_c == 'L' and start_i <stop_i) or (start_c == 'R' and start_i > stop_i):
                return False
        return True
