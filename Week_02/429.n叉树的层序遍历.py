#
# @lc app=leetcode.cn id=429 lang=python3
#
# [429] N叉树的层序遍历
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        # 迭代法1
        res, stack = [], [root]
        while any(stack):
            res.append([node.val for node in stack])
            stack = [child for node in stack for child in node.children if child]
        return res
        
        # 迭代法2
        # res = []
        # stack = [root]
        # if not root:
        #     return []
        # while stack:
        #     temp = []
        #     new_stack = []
        #     for node in stack:
        #         temp.append(node.val)
        #         for child in node.children:
        #             new_stack.append(child)
        #     stack = new_stack
        #     res.append(temp)
        # return res
        
# @lc code=end

