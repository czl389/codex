#
# @lc app=leetcode.cn id=237 lang=python3
# @lcpr version=30204
#
# [237] 删除链表中的节点
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next

        
# @lc code=end



#
# @lcpr case=start
# [4,5,1,9]\n5\n
# @lcpr case=end

# @lcpr case=start
# [4,5,1,9]\n1\n
# @lcpr case=end

#

