#
# @lc app=leetcode.cn id=24 lang=python3
#
# [24] 两两交换链表中的节点
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        # 递归法
        '''
        if not head or not head.next:
            return head
        first, second = head, head.next
        first.next = self.swapPairs(second.next)
        second.next = first
        return second
        '''

        # 迭代法
        # 定义一个指向头结点的新结点
        '''
        dummy_node = ListNode(-1)
        dummy_node.next = head
        pre = dummy_node
        while head and head.next:
            first, second = head, head.next
            # 一次交换
            pre.next = second
            first.next = second.next
            second.next = first
            # 重置pre和head
            pre = first
            head = first.next
        return dummy_node.next
        '''

        
        pre_node = ListNode(-1)
        pre_node.next = head
        pre = pre_node
        while head and head.next:
            first, second = head, head.next
            # 交换
            pre.next = second
            first.next = second.next
            second.next = first
            # 更新pre和head
            pre = first
            head = first.next
        return pre_node.next



# @lc code=end

