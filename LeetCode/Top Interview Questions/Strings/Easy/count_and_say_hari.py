class Solution:
    def countAndSay(self, n: int) -> str:
        if n==1:
            return "1"
        if n==2:
            return "11"
        
        prev = "11"
        for i in range(3,n+1):
            prev+="!"
            temp = ""
            count = 1
            for j in range(1,(len(prev))):
                if(prev[j] != prev[j-1]):
                    temp += str(count)
                    temp += prev[j-1]
                    count=1
                    
                else:
                    count+=1
            
            prev=temp
            
        return prev
            
