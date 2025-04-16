# @lcpr-before-debug-begin
from python3problem143 import *
from typing import *
# @lcpr-before-debug-end

#
# @lc app=leetcode.cn id=143 lang=python3
# @lcpr version=30204
#
# [143] 重排链表
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # find middle node
        def mid(head: Optional[ListNode]) -> Optional[ListNode]:
            slow = fast = head
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            return slow
        middle_node = mid(head)

        def reverse(head: Optional[ListNode]) -> Optional[ListNode]:
            prev = None
            current = head
            while current:
                next_node = current.next
                current.next = prev
                prev = current
                current = next_node
            return prev
        head2 = reverse(middle_node)

        current1 = head
        current2 = head2

        while current1 is not middle_node:
            next_node1 = current1.next
            next_node2 = current2.next

            current1.next = current2
            if next_node1 is middle_node:
                break
            current2.next = next_node1

            current1 = next_node1
            current2 = next_node2


# @lc code=end



#
# @lcpr case=start
# [1,2,3,4]\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3,4,5]\n
# @lcpr case=end

#

