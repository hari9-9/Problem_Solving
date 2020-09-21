class Solution:
    def largestTimeFromDigits(self, arr: List[int]) -> str:
        max_time=-1
        for h1,h2,m1,m2 in itertools.permutations(arr):
            h=h1*10+h2
            m=m1*10+m2
            if h<24 and m<60:
                max_time = max(max_time , h*60+m)
        if max_time == -1:
            return ""
        else:
            return "{:02d}:{:02d}".format(max_time // 60, max_time % 60)    
        
