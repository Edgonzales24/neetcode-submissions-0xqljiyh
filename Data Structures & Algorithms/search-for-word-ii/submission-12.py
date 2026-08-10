class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False
    
    def addWord(self, word):
        curr = self
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.endOfWord = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        ROWS, COLS = len(board), len(board[0])
        root = TrieNode()
        for w in words:
            root.addWord(w)
        
        path, res = set(), set()
        
        def dfs(r, c, node, word):
            if (not (0 <= r < ROWS and 0 <= c < COLS) or
                board[r][c] not in node.children or
                (r, c) in path):
                return
            
            path.add((r, c))
            node = node.children[board[r][c]]
            word += board[r][c]

            if node.endOfWord:
                res.add(word)
            
            dfs(r + 1, c, node, word)
            dfs(r - 1, c, node, word)
            dfs(r, c + 1, node, word)
            dfs(r, c - 1, node, word)
            path.remove((r, c))

        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, root, "")
        return list(res)
