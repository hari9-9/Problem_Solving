class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []
        ans = 0
        for o in operations:
            if o == '+':
                if len(record)>=2:
                    score = record[-1] + record[-2]
                    ans+=score
                    record.append(score)
            elif o == 'D':
                if len(record):
                    score = record[-1]*2
                    ans+=score
                    record.append(score)
            elif o == 'C':
                if len(record):
                    score = record.pop()
                    ans-=score
            else:
                ans += int(o)
                record.append(int(o))
        return ans
