class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        res = []
        sp=0
        for i in range(len(s)):
            if sp <len(spaces) and i == spaces[sp]:
                res.append(" ")
                sp+=1
            if i < len(s):
                res.append(s[i])
        return "".join(res)
