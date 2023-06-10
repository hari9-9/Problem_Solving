class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count =0
        if n == 0 :
            return True
        for i in range(len(flowerbed)):
            if flowerbed[i] == 0:
                left = i==0 or flowerbed[i-1] == 0
                right = i==len(flowerbed)-1 or flowerbed[i+1]==0
                if right and left:
                    flowerbed[i] = 1
                    count += 1
                    if count == n:
                        return True
        return False