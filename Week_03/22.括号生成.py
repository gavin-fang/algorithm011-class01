#
# @lc app=leetcode.cn id=22 lang=python3
#
# [22] 括号生成
#

# @lc code=start
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # 递归法，left、right记录已经用掉的左右括号个数
        res = []
        s = ""
        def generate(left, right, s):
            # terminator
            if left == n and right == n:
                res.append(s)
                return
            # process current logic
            # drill down
            if left < n: generate(left + 1, right, s + "(")        
            if left > right and right < n: generate(left, right + 1, s + ")")
        generate(0, 0, s)
        return res
# @lc code=end

