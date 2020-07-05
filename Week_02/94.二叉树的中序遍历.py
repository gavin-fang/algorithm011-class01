#
# @lc app=leetcode.cn id=94 lang=python3
#
# [94] 二叉树的中序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        # 递归
        # res = []
        # def helper(root):
        #     if not root:
        #         return
        #     if root.left:
        #         helper(root.left)
        #     res.append(root.val)
        #     if root.right:
        #         helper(root.right)
        # helper(root)
        # return res

        # 用stack，迭代
        res = []
        stack = []
        p = root
        while p or stack:
            while p:
                stack.append(p)
                p = p.left
            top = stack.pop()
            res.append(top.val)
            p = top.right
        return res
# @lc code=end

