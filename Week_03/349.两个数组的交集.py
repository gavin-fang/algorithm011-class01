#
# @lc app=leetcode.cn id=349 lang=python3
#
# [349] 两个数组的交集
#

# @lc code=start
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # Python内置操作
        # return set(nums1) & set(nums2)

        # 哈希表
        # res = []
        # dict = {}
        # for num in nums1:
        #     dict[num] = dict.get(num, 0) + 1
        # for num in nums2:
        #     if num in dict:
        #         res.append(num)
        # return set(res)

        # 排序加双指针
        nums1.sort()
        nums2.sort()
        


        



# @lc code=end

