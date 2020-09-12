class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        count=0
        currx=points[0][0]
        curry=points[0][1]
        for i in range(1,len(points)):
            dx=currx-points[i][0]
            dy=curry-points[i][1]
            count+= max(abs(dx),abs(dy))
            currx=points[i][0]
            curry=points[i][1]
        return count
