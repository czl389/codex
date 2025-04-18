# @lcpr-before-debug-begin
from python3problem83 import *
from typing import *
# @lcpr-before-debug-end

#
# @lc app=leetcode.cn id=83 lang=python3
# @lcpr version=30204
#
# [83] 删除排序链表中的重复元素
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
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        back = head
        while back:
            front = back.next
            while front and front.val == back.val:
                front = front.next
            back.next = front
            back = front
        return head

# @lc code=end



#
# @lcpr case=start
# [1,1,2]\n
# @lcpr case=end

# @lcpr case=start
# [1,1,2,3,3]\n
# @lcpr case=end

#

