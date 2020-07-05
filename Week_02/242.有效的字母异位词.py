#
# @lc app=leetcode.cn id=242 lang=python3
#
# [242] 有效的字母异位词
#

# @lc code=start
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # 排序后看两字符串是否相等
        # return sorted(s) == sorted(t)
        
        # 字典
        # dict = {}
        # if len(s) != len(t):
        #     return False
        # for ch in s:
        #     dict[ch] = dict.get(ch, 0) + 1
        # for ch in t:
        #     dict[ch] = dict.get(ch, 0) - 1
        #     if dict[ch] < 0:
        #         return False
        # return True

        # 用一个数组存放a-z的出现次数
        arr = [0 for i in range(26)]
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            arr[ord(s[i]) - ord('a')] += 1
            arr[ord(t[i]) - ord('a')] -= 1
        for i in range(26):
            if arr[i] != 0:
                return False
        return True
# @lc code=end

