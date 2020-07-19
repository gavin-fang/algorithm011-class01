#
# @lc app=leetcode.cn id=69 lang=python3
#
# [69] x 的平方根
#

# @lc code=start
class Solution:
    def mySqrt(self, x: int) -> int:
        # 二分查找法
        # l, r = 0, x
        # res = -1
        # while l <= r:
        #     mid = (l + r) // 2
        #     tmp = mid * mid
        #     if tmp <= x:
        #         res = mid
        #         l = mid + 1
        #     else: r = mid - 1
        # return res
        
        # 牛顿迭代法
        r = x
        while r*r > x:
            r = (r + x//r) // 2
        return r
# @lc code=end

