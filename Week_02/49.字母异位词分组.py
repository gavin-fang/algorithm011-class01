#
# @lc app=leetcode.cn id=49 lang=python3
#
# [49] 字母异位词分组
#

# @lc code=start
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # 用字典，key为有相同字符的元组(因为列表不能做key)，比下面方法快一点
        dict = {}
        for str in strs:
            str_0 = tuple(sorted(str))
            if str_0 in dict:
                dict[str_0].append(str)
            else:
                dict[str_0] = [str]
        return list(dict.values())

        # 用字典，key为字母计数的元组
        # dict = {}
        # for str in strs:
        #     count = [0] * 26
        #     for c in str:
        #         count[ord(c) - ord('a')] += 1
        #     count = tuple(count)
        #     if count in dict:
        #         dict[count].append(str)
        #     else:
        #         dict[count] = [str]
        # return list(dict.values())
# @lc code=end

