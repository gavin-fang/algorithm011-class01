#
# @lc app=leetcode.cn id=152 lang=python3
#
# [152] 乘积最大子数组
#

# @lc code=start
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        imax, imin = 1, 1
        res = -float('inf')
        for i in range(len(nums)):
            # 当前元素值为负数时，交换连续乘积的最大和最小值
            if nums[i] < 0:
                imax, imin = imin, imax
            # 更新当前连续乘积的最大和最小值
            imax = max(imax * nums[i], nums[i])
            imin = min(imin * nums[i], nums[i])
            res = max(res, imax)
        return res



# 维护当前最大值imax，imax = max(imax * nums[i], nums[i])
# 维护当前最小值imin，imin = min(imin * nums[i], nums[i])
# @lc code=end

