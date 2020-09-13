class Solution:    
    def letterCombinations(self, digits: str) -> List[str]:
        def combo(result,digits,curr,ind,mapping):
            if(ind==len(digits)):
                result.append(curr)
                return
            possibilties=mapping[int(digits[ind])]
            for p in possibilties:
                combo(result,digits,curr+p,ind+1,mapping)
        if(len(digits)==0):
            return[]
        result=[]
        mapping=[
            '0',
            '1',
            'abc',
            'def',
            'ghi',
            'jkl',
            'mno',
            'pqrs',
            'tuv',
            'wxyz',
        ]
        combo(result,digits,"",0,mapping)
        return result
