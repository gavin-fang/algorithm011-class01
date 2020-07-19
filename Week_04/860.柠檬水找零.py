#
# @lc app=leetcode.cn id=860 lang=python3
#
# [860] 柠檬水找零
#

# @lc code=start
class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        # 贪心算法思想，找零时先考虑10美元，再看5美元的
        if not bills:
            return False
        count5, count10 = 0, 0
        for bill in bills:
            if bill == 5: count5 += 1
            elif bill == 10:  count10, count5 = count10 + 1, count5 - 1
            elif count10: count10, count5 = count10 - 1, count5 - 1
            else: count5 -= 3
            # 每次来一个客户检查5美元是否够用
            if count5 < 0: return False
        return True
        
# @lc code=end

