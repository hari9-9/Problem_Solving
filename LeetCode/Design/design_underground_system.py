class UndergroundSystem:

    def __init__(self):
        self.curr = {}
        self.station = defaultdict(list)


    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.curr[id] = (stationName,t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:

        if self.curr[id]:
            start , start_time = self.curr[id]
            self.station[(start,stationName)].append(t-start_time)

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        nums = self.station[(startStation , endStation)]
        return sum(nums)/len(nums)


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)
