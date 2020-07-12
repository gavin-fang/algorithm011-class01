#
# @lc app=leetcode.cn id=77 lang=python3
#
# [77] 组合
#

# @lc code=start
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def backtrack(first = 1, cur = []):
            # terminator
            if len(cur) == k:  
                res.append(cur[:])
            for i in range(first, n + 1):
                # 添加i到当前组合中
                cur.append(i)
                # drill down
                backtrack(i + 1, cur)
                # backtrack
                cur.pop()
        res = []
        backtrack()
        return res
# @lc code=end

