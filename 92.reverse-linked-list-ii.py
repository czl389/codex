# @lcpr-before-debug-begin
from python3problem92 import *
from typing import *
# @lcpr-before-debug-end

#
# @lc app=leetcode.cn id=92 lang=python3
# @lcpr version=30204
#
# [92] 反转链表 II
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
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == right:
            return head
        dummy_node = ListNode(val=0, next=head)
        current = dummy_node
        previous = None
        i = 0
        p0 = None
        while current:
            if i == left -1:
                p0 = current
            if left <= i <= right:
                next_node = current.next
                current.next = previous
                previous = current
                current = next_node
            else:
                previous = current
                current = current.next
            i+=1
            if i > right:
                if p0.next is not None:
                    p0.next.next = current
                p0.next = previous
                break
        return dummy_node.next
        




        
# @lc code=end



#
# @lcpr case=start
# [1,2,3,4,5]\n2\n4\n
# @lcpr case=end

# @lcpr case=start
# [5]\n1\n1\n
# @lcpr case=end

# @lcpr case=start
# [3,5]\n1\n2\n
# @lcpr case=end

#

