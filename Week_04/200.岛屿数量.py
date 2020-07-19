#
# @lc app=leetcode.cn id=200 lang=python3
#
# [200] 岛屿数量
#

# @lc code=start
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(i, j, grid):
            # 判断边界
            if i < 0 or i > len(grid) - 1 or j < 0 or j > len(grid[0]) - 1:
                return
            # 格子不是岛屿，直接返回
            if grid[i][j] != '1':
                return
            # 不用0是为了区分海洋和已遍历过的陆地格子
            grid[i][j] = '2'
            # 递归格子的上下左右格子
            dfs(i - 1, j, grid)
            dfs(i + 1, j, grid)
            dfs(i, j - 1, grid)
            dfs(i, j + 1, grid)
        
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    dfs(i, j, grid)
                    count += 1
        return count

# @lc code=end

