#
# @lc app=leetcode.cn id=221 lang=python3
#
# [221] 最大正方形
#

# @lc code=start
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        m, n = len(matrix), len(matrix[0])
        max_size = 0
        dp = matrix
        for i in range(m):
            for j in range(n):
                matrix[i][j] = int(matrix[i][j])
        for i in range(m):
            for j in range(n):
                if dp[i][j] == 1:
                    if i == 0 or j == 0:
                        dp[i][j] == 1
                    else:
                        dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1
                max_size = max(dp[i][j], max_size)
        return max_size * max_size

# 1. subproblem
#     sq_size(i, j) = min(sq_size(i-1, j-1), sq_size(i, j-1), sq_size(i-1, j)) + 1 if a[i][j] == 1
# 2. dp array, dp[i][j] (状态记录正方形最大边长，最终结果只要将其算平方即可)
# 3. dp equation, 
#     if a[i][j] == 1, dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1
# @lc code=end

