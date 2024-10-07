class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        s1 = sentence1.split()
        s2 = sentence2.split()
        start = 0
        end1 = len(s1)-1
        end2 = len(s2)-1
        if len(s1) > len(s2):
            return self.areSentencesSimilar(sentence2,sentence1)

        while start < len(s1) and s1[start] == s2[start]:
            start+=1
        while end1 >=0 and s1[end1] == s2[end2]:
            end1-=1
            end2-=1
        return end1<start
