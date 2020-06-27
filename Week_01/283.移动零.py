#
# @lc app=leetcode.cn id=283 lang=python3
#
# [283] 移动零
#

# @lc code=start
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 两次遍历
        j = 0
        for i in range(len(nums)):
            if nums[i]:
                nums[j] = nums[i]
                j += 1
        for i in range(j, len(nums)):
            nums[i] = 0
        return nums

        # 双指针法，一次遍历
        # j = 0
        # for i in range(len(nums)):
        #     if nums[i]:
        #         if i > j:
        #             nums[j] = nums[i]
        #             nums[i] = 0
        #         j += 1
        # return nums

# @lc code=end

