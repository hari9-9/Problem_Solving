class Trie:
    def __init__(self):
        self.child = [None]*26
        self.end = -1

    def insert(self,word ,end):
        node = self
        for char in word:
            c_index = ord(char)-ord('a')
            if node.child[c_index] is None:
                node.child[c_index] = Trie()
            node = node.child[c_index]
        node.end = end


class Solution:
    directions = [(-1,0),(0,1),(1,0),(0,-1)]
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        rows = len(board)
        cols = len(board[0])
        def dfs(node,i,j):
            c_index = ord(board[i][j]) - ord('a')
            if node.child[c_index] is None:
                return
            node = node.child[c_index]
            if node.end >= 0:
                ans.append(words[node.end])
                node.end = -1
            temp = board[i][j]
            board[i][j] = "0"
            for dx,dy in Solution.directions:
                nx = dx+i
                ny = dy+j
                if 0<=nx<rows and 0<=ny<cols and board[nx][ny] !='0':
                    dfs(node,nx,ny)
            board[i][j] = temp

        root = Trie()
        ans = []
        for index, word in enumerate(words):
            root.insert(word,index)
        for i in range(rows):
            for j in range(cols):
                dfs(root,i,j)
        return ans


        
