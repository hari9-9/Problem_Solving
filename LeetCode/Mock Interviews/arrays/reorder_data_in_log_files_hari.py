class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        dig=[]
        al=[]
        for log in logs:
            if (log.split()[1]).isdigit():
                dig.append(log)
            else:
                al.append(log.split())
        #print(al)
        al.sort(key = lambda x:x[0])
        al.sort(key= lambda x:x[1:])
        for i in range(len(al)):
            al[i]=(' '.join(al[i]))
        return al+dig
