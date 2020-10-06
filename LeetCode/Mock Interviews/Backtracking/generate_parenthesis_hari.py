class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def solver(ans , curr , open , close , n):
            if(len(curr)==2*n):
                ans.append(curr)
                return
            else:
                if(open<n):
                    solver(ans , curr+'(' , open+1 , close , n)
                if(close<open):
                    solver(ans , curr+')' , open , close+1 ,n)
        
        ans=[]
        solver(ans,"",0,0,n)
        return ans
