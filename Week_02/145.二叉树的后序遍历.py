#
# @lc app=leetcode.cn id=145 lang=python3
#
# [145] 二叉树的后序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        # 第一种迭代
        res = []
        stack = []
        p = root
        while stack or p:
            while p:
                stack.append(p)
                p = p.left if p.left else p.right
            top = stack.pop()
            res.append(top.val)
            if stack and top == stack[-1].left:
                p = stack[-1].right
            else:
                p = None
        return res

        # 利用前序迭代
        # res, stack = [], [root]
        # if not root:
        #     return []
        # while stack:
        #     p = stack.pop()
        #     res.insert(0, p.val)
        #     if p.left:
        #         stack.append(p.left)
        #     if p.right:
        #         stack.append(p.right)
        # return res
# @lc code=end

