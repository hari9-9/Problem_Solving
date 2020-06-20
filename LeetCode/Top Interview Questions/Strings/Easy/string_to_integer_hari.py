class Solution:
    def myAtoi(self, str: str) -> int:
        str = str.strip()
        neg = False
        digits ={i for i in "0123456789"}
        result = 0
        if not str:
            return 0
        if(str[0] == '-' ):
            neg = True
        if (str[0] == '-' or str[0] == '+'):
            str=str[1:]
        for i in str:
            if i in digits:
                result = (result*10) +int(i)
            else:
                break
        if neg:
            result = -result
        result = max(min(result , 2**31-1),-2**31)
        return result
