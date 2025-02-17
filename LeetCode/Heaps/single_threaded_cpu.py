class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        heap = []
        time = 1
        indexed_tasks = [(t[0], t[1], i) for i, t in enumerate(tasks)]
        indexed_tasks.sort(key=lambda x: x[0])
        res= []
        i=0
        while i < len(indexed_tasks) or heap:
            if not heap and i<len(indexed_tasks) and indexed_tasks[i][0]>time:
                time = indexed_tasks[i][0]
            while i <len(indexed_tasks) and indexed_tasks[i][0] <= time:
                heapq.heappush(heap,(indexed_tasks[i][1],indexed_tasks[i][2]))
                i+=1

            if heap:
                t , index = heapq.heappop(heap)
                res.append(index)
                time+= t
        return res
