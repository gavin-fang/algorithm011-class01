#
# @lc app=leetcode.cn id=322 lang=python3
#
# [322] 零钱兑换
#

# @lc code=start
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        for i in range(1, amount + 1):
            for j in range(len(coins)):
                if i >= coins[j]:
                    dp[i] = min(dp[i], dp[i - coins[j]] + 1)
        return dp[amount] if dp[amount] != float('inf') else -1

# 1. subproblem
# 2. DP array, f(n) = min(f(n - coin), for coin in [coins]) + 1
# 3. DP方程， dp[n] = min(dp[n - k] for k in [coins]) + 1
        
# @lc code=end

