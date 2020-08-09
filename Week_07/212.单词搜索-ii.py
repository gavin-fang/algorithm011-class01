#
# @lc app=leetcode.cn id=212 lang=python3
#
# [212] 单词搜索 II
#

# @lc code=start
import collections
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
end_of_word = '#'
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        if not words: return []
        if not board or not board[0]: return []
        self.result = set()

        # 构建trie前缀树
        root = collections.defaultdict()
        for word in words:
            node = root
            for ch in word:
                node = node.setdefault(ch, collections.defaultdict())
            node[end_of_word] = end_of_word
        
        # 遍历board
        self.m, self.n = len(board), len(board[0])
        for i in range(self.m):
            for j in range(self.n):
                if board[i][j] in root:
                    self._dfs(board, i, j, "", root)
        return list(self.result)

    def _dfs(self, board, i, j, cur_word, cur_dict):
        cur_word += board[i][j]
        cur_dict = cur_dict[board[i][j]]
        # terminator
        if end_of_word in cur_dict:
            self.result.add(cur_word)
        # 保证不重复使用
        tmp, board[i][j] = board[i][j], '@'
        # drill down
        for k in range(4):
            x, y = dx[k] + i, dy[k] + j
            if 0 <= x < self.m and 0 <= y < self.n and board[x][y] != '@' and board[x][y] in cur_dict:
                self._dfs(board, x, y, cur_word, cur_dict)
        # reverse state
        board[i][j] = tmp
# @lc code=end

