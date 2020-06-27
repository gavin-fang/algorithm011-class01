#
# @lc app=leetcode.cn id=11 lang=python3
#
# [11] 盛最多水的容器
#

# @lc code=start
class Solution:
    def maxArea(self, height: List[int]) -> int:
        # 双指针法，左右夹逼
        left, right = 0, len(height) - 1
        max_area = 0
        while left < right:
            if height[left] < height[right]:
                h = height[left]
                area = (right - left) * h
                max_area = max(max_area, area)
                left += 1
            else:
                h = height[right]
                area = (right - left) * h
                max_area = max(max_area, area)
                right -= 1
        return max_area
# @lc code=end

