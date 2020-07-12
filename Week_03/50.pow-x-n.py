#
# @lc app=leetcode.cn id=50 lang=python3
#
# [50] Pow(x, n)
#

# @lc code=start
class Solution:
    def myPow(self, x: float, n: int) -> float:
        # 分治法
        def compute(n):
            # recursion terminator
            if n == 0:
                return 1.0
            # prepare data
            # conquer subproblems
            y = compute(n // 2)
            # process and generate the final result
            return y * y if n % 2 == 0 else y * y * x
        return compute(n) if n >= 0 else 1.0/compute(-n)
# @lc code=end

