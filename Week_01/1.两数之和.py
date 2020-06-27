#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 哈希表
        dict = {}
        for i, num in enumerate(nums):
            if target - num in dict:
                return [dict[target - num], i]
            dict[num] = i
        return []
        
# @lc code=end

