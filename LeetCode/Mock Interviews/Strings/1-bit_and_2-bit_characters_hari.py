class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        flag=True
        i=0
        while i <len(bits):
            if(bits[i]==1):
                if(i+1)<len(bits):
                    flag=False
                    i+=2
            else:
                flag=True
                i+=1
                
        return flag
