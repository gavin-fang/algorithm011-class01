#
# @lc app=leetcode.cn id=64 lang=python3
#
# [64] 最小路径和
#

# @lc code=start
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        m, n = len(grid), len(grid[0])
        for i in range(1, m):
            grid[i][0] += grid[i - 1][0]
        for j in range(1, n):
            grid[0][j] += grid[0][j - 1] 
        for i in range(1, m):
            for j in range(1, n):
                grid[i][j] += min(grid[i - 1][j], grid[i][j - 1])
        return grid[m - 1][n - 1]

# 1. subproblem, min_sum(i, j) = min(min_sum(i - 1, j), min_sum(i, j - 1)) + a[i, j]
# 2. dp array, dp[i][j]
# 3. dp equation, dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i, j]
# @lc code=end

