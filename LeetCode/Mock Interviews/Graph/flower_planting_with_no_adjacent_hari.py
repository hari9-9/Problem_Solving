class Solution:
    def gardenNoAdj(self, N: int, paths: List[List[int]]) -> List[int]:
        if len(paths)==0:
            return [1]*N
        #graph=[[-1 for x in range(N+1)] for y in range(N+1)]
        graph=[[] for y in range(N+1)]
        plants=[0 for x in range(N)]
        '''for i in range(len(paths)):
            graph[paths[i][0]][paths[i][1]]=1
            graph[paths[i][1]][paths[i][0]]=1'''
        for i in paths:
            graph[i[0]].append(i[1])
            graph[i[1]].append(i[0])
        print(graph)
        for i in range(1,len(plants)+1):
            avail=[1,2,3,4]
            p=graph[i]
            if(len(p)):
                for j in p:
                    if(plants[j-1] in avail):
                        avail.remove(plants[j-1])    
            plants[i-1]=avail[0]
            
        return plants
            
