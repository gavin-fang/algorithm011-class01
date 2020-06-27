#
# @lc app=leetcode.cn id=70 lang=python3
#
# [70] 爬楼梯
#

# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        # 递归法，从后往前看f(n) = f(n-1) + f(n-2)，

        # 动态规划，常规
        '''
        if n == 1:
            return 1
        if n == 2:
            return 2
        dp = []
        dp.extend([1, 1, 2])
        for i in range(3, n+1):
            dp.append(dp[i-1] + dp[i-2])
        return dp[n]
        '''

        # 动态规划优化，用两个变量暂存前面计算的值
        if n == 1:
            return 1
        if n == 2:
            return 2
        a, b = 1, 2
        for i in range(n-2):
            temp = a + b
            a = b
            b = temp
        return b
# @lc code=end

