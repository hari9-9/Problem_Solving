class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        hash = defaultdict(list)
        wordList.append(beginWord)
        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i]+"*"+word[i+1:]
                hash[pattern].append(word)

        visited = set()
        visited.add(beginWord)
        q = []
        q.append(beginWord)
        res = 1
        while q:
            for _ in range(len(q)):
                word = q.pop(0)
                if word == endWord:
                    return res
                for j in range(len(word)):
                    curr = word[:j]+"*"+word[j+1:]
                    for node in hash[curr]:
                        if node not in visited:
                            visited.add(node)
                            q.append(node)
            res+=1
        return 0


        
