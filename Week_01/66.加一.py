#
# @lc app=leetcode.cn id=66 lang=python3
#
# [66] 加一
#

# @lc code=start
class Solution:
    def plusOne(self, digits):
        for i in range(len(digits) - 1, -1, -1):
            digits[i] += 1
            if digits[i] < 10:
                return digits
            digits[i] = 0
        digits.insert(0, 1)
        return digits
          
            
# @lc code=end

