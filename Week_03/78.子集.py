#
# @lc app=leetcode.cn id=78 lang=python3
#
# [78] 子集
#

# @lc code=start
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # 迭代
        # res = [[]]
        # for num in nums:
        #     res = res + [[num] + i for i in res]
        # return res

        # 回溯
        res = []
        n = len(nums)
        def helper(i, subset):
            res.append(subset)
            for j in range(i, n):
                helper(j + 1, subset + [nums[j]])
        helper(0, [])
        return res
# @lc code=end

