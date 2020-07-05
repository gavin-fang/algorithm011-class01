#
# @lc app=leetcode.cn id=144 lang=python3
#
# [144] 二叉树的前序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        # 迭代
        res = []
        if not root:
            return res
        stack = [root]
        while stack:
            p = stack.pop()
            res.append(p.val)
            if p.right:
                stack.append(p.right)
            if p.left:
                stack.append(p.left)
        return res

        # 递归
        # res = []
        # def helper(root):
        #     if not root:
        #         return
        #     res.append(root.val)
        #     helper(root.left)
        #     helper(root.right)
        
        # helper(root)
        # return res
# @lc code=end

