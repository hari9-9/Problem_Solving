class Solution:
    @staticmethod
    def solve(digits,ind,output,ans,mapping):
        if ind >= len(digits):
            ans.append("".join(output.copy()))
            return
        num = int(digits[ind])-0
        val = mapping[num]
        for v in val:
            output.append(v)
            Solution.solve(digits,ind+1,output,ans,mapping)
            output.pop()




    def letterCombinations(self, digits: str) -> List[str]:
        ans = []
        output = []
        if len(digits)==0:
            return []
        mapping = ["","","abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"]
        Solution.solve(digits,0,output,ans,mapping)
        return ans
