class Solution:

    def smooth(self , img,i,j,res):
        dirs = [[0,1], [1,0], [-1,0], [0,-1],[-1,-1],[-1,+1],[+1,-1],[1,1]]
        avg = [img[i][j]]
        for dx , dy in dirs:
            x = i+dx
            y = j+dy
            if 0<=x<len(img) and 0<=y<len(img[0]):
                avg.append(img[x][y])
        res[i][j] = math.floor(sum(avg) / len(avg))



    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        res = copy.deepcopy(img)
        for i in range(len(img)):
            for j in range(len(img[0])):
                self.smooth(img,i,j,res)
        return res
        
