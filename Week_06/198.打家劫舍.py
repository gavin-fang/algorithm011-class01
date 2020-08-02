#
# @lc app=leetcode.cn id=198 lang=python3
#
# [198] 打家劫舍
#

# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        dp = [[0 for _ in range(2)] for _ in range(len(nums))]
        dp[0][0], dp[0][1] = 0, nums[0]
        res = 0
        for i in range(1, len(nums)):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1])
            dp[i][1] = dp[i - 1][0] + nums[i]
            res = max(dp[i][0], dp[i][1])
        return res

# subproblem, a[i], i = 0..n-1, 返回a[n - 1]
# 加一个维度，a[i][0]:不偷，a[i][1]:偷
# 状态数组, dp[i][0或1]
# dp方程, dp[i][0] = max(dp[i - 1][0], dp[i - 1][1])
#        dp[i][1] = dp[i - 1][0] + a[i]
# @lc code=end

