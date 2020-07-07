class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if rowIndex == 0:
            return [1]
        lastRow = self.getRow(rowIndex-1)
        res = [1]
        for i in range(len(lastRow)-1):
            res.append(lastRow[i]+lastRow[i+1])
        res.append(1)
        return res
        
