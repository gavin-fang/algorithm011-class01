#
# @lc app=leetcode.cn id=122 lang=python3
#
# [122] 买卖股票的最佳时机 II
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 贪心算法，简单的一次遍历，比较数组中连续数值间的差值情况，选择性加入利润
        # 包含了三种情况：升序；降序；一般情形，有峰有谷
        profit = 0
        for i in range(1, len(prices)):
            tmp = prices[i] - prices[i - 1]
            if tmp > 0: profit += tmp
        return profit

        
        
# @lc code=end

