#
# @lc app=leetcode.cn id=20 lang=python3
#
# [20] 有效的括号
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        # 暴力解法，出现标准的()、[]、{}替换为''，超出时间限制
        # if len(s) % 2 != 0:
        #     return False
        # while len(s) > 0:
        #     s.replace('[]', '')
        #     s.replace('()', '')
        #     s.replace('{}', '')
        # return True if len(s) == 0 else False

        # 栈
        dict = {')':'(', ']':'[', '}':'{'}
        stack = []
        for c in s:
            if c in dict:
                temp = stack.pop() if stack else ''
                if dict[c] != temp:
                    return False
            else: stack.append(c)

        return not stack
# @lc code=end

