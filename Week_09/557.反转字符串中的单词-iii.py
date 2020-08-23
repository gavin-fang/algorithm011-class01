#
# @lc app=leetcode.cn id=557 lang=python3
#
# [557] 反转字符串中的单词 III
#

# @lc code=start
class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split()
        res= [''.join(reversed(item)) for item in s]
        return ' '.join(res)
        
# @lc code=end

