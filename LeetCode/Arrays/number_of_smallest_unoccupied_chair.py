class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        target = times[targetFriend]
        times.sort()
        n = len(times)
        chair = [0]*n
        for time in times:
            for i in range(n):
                if chair[i] <= time[0]:
                    chair[i] = time[1]
                    if time == target:
                        return i
                    break
        return 0
