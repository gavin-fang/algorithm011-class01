#
# @lc app=leetcode.cn id=53 lang=python3
#
# [53] 最大子序和
#

# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        dp = nums  # 也可以直接在nums数组上进行dp递推
        for i in range(1, n):
            # 最大子序和 = 当前元素自身最大 or 包含之前后最大
            dp[i] = max(dp[i - 1] + nums[i], nums[i])
        return max(dp)
        

# DP
# 1. 分治（找重复子问题） max_sum(i) = max(max_sum(i - 1), max_sum(i - 1) + a[i])
# 2. 状态数组定义 f[i]
# 3. dp方程  f[i] = max(f[i - 1], f[i - 1] + a[i])
# @lc code=end

