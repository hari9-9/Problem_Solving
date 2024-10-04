class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        print(skill)
        i=0
        j=len(skill)-1
        chem=0
        sum = skill[i]+skill[j]
        while i<len(skill)/2:
            p1=skill[i]
            p2=skill[j]
            if p1+p2 == sum:
                chem+=(p1*p2)
                i+=1
                j-=1
            else:
                return -1
        return chem
