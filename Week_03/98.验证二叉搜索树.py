#
# @lc app=leetcode.cn id=98 lang=python3
#
# [98] 验证二叉搜索树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        # 中序遍历元素递增的性质，用栈
        # stack = []
        # p = root
        # pre = -float("inf")
        # while p or stack:
        #     while p:
        #         stack.append(p)
        #         p = p.left
        #     temp = stack.pop()
        #     if temp.val <= pre:
        #         return False
        #     pre = temp.val
        #     p = temp.right
        # return True

        # 二叉搜索树的定义，设置递归比较的low和high值
        def helper(root, low, high):
            if not root:
                return True
            if low < root.val < high:
                return helper(root.left, low, root.val) and helper(root.right, root.val, high)
            else:
                return False
        return helper(root, float("-inf"), float("inf"))



# @lc code=end

