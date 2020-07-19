#
# @lc app=leetcode.cn id=121 lang=python3
#
# [121] 买卖股票的最佳时机
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 遍历一次，依次记录最大利润和最低点
        # profit, minprice = 0, float('inf')
        # for price in prices:
        #     minprice = min(price, minprice)
        #     profit = max(profit, price - minprice)
        # return profit

        # 遍历一次，滑动窗口法
        profit = 0
        begin = 0
        for end in range(1, len(prices)):
            if prices[begin] >= prices[end]:
                begin = end
            cur_profit = prices[end] - prices[begin]
            profit = cur_profit if cur_profit > profit else profit
        return profit
# @lc code=end

