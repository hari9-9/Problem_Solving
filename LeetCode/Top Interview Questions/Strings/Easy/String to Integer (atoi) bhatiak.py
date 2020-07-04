class Solution:
    def myAtoi(self, str: str) -> int:
        
        nos = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')
        
        if str in ('', ' ', None):
            return 0
        
        str = str.strip()
        no = str.split(" ")[0]
        
        if no in ('', ' ', None):
            return 0
        
        flag=0
        if no[0] in ('-', '+'):
            if no[0] == '-':
                flag=1
                no=no[1:]
            elif no[0] == '+':
                flag=0
                no=no[1:]
                
        if no in ('', ' ', None):
            return 0
        
        if(no[0] not in nos):
            return 0
        
        for i in range(len(no)):
            if no[i] not in nos:
                no=no[:i]
                break
                
        if no in ('', ' ', None):
            return 0
        
        no = int(no)
        if(flag==1): no=-no
        
        if no < -2**31:
            return -2**31
        elif no > 2**31-1:
            return 2**31-1
        return no
