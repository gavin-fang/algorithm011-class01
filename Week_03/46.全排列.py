#
# @lc app=leetcode.cn id=46 lang=python3
#
# [46] 全排列
#

# @lc code=start
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # 回溯法
        n = len(nums)
        res = []
        def backtrack(pre):
            # terminator
            if pre == n:
                res.append(nums[:]) # nums[:]创建一个nums的副本，对原来的nums没有影响
            for i in range(pre, n):
                nums[pre], nums[i] = nums[i], nums[pre]
                backtrack(pre + 1)
                nums[pre], nums[i] = nums[i], nums[pre]
        backtrack(0)
        return res
# @lc code=end

