#
# @lc app=leetcode.cn id=236 lang=python3
#
# [236] 二叉树的最近公共祖先
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # root为空返回None，p、q中有一个是root则返回root
        if not root:
            return None
        if p == root or q == root:
            return root
        # left、right存放递归之后的结果
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        # 一边为空则返回另一边的结果
        if not left:
            return right
        if not right:
            return left
        # p、q分别在两边则返回root
        if left and right:
            return root
        return None
        
# @lc code=end

