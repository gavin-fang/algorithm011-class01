#
# @lc app=leetcode.cn id=455 lang=python3
#
# [455] 分发饼干
#

# @lc code=start
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        # 贪心算法，先按升序排序，选择刚好满足小朋友胃口大小的饼干（饼干大于等于胃口）
        # count = 0  # count可以不用，直接返回i也可以
        i, j = 0, 0
        g.sort()
        s.sort()
        while i < len(g) and j < len(s):
            if s[j] >= g[i]:
                # count += 1
                i += 1
                j += 1
            else:
                j += 1
        # return count
        return i
        
# @lc code=end

