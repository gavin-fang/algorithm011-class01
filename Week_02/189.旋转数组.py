#
# @lc app=leetcode.cn id=189 lang=python3
#
# [189] 旋转数组
#

# @lc code=start
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 尾部pop，头部insert，时间长一些
        # for i in range(k):
        #     temp = nums.pop()
        #     nums.insert(0, temp)
    

        # 三次反转
        n = len(nums)
        k = k % n
        def swap(l, r):
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1
        swap(0, n - 1)
        swap(0, k - 1)
        swap(k, n -1)

    


# @lc code=end

