# @lcpr-before-debug-begin
from python3problem82 import *
from typing import *
# @lcpr-before-debug-end

#
# @lc app=leetcode.cn id=82 lang=python3
# @lcpr version=30204
#
# [82] 删除排序链表中的重复元素 II
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy_node = ListNode(val=-111, next=head)
        current = dummy_node
        while current:
            if current.next and current.next.next and current.next.val == current.next.next.val:
                t = current.next.val
                while current.next and current.next.val == t:
                    current.next = current.next.next
            else:
                current = current.next
        return dummy_node.next




        
# @lc code=end



#
# @lcpr case=start
# [1,2,3,3,4,4,5]\n
# @lcpr case=end

# @lcpr case=start
# [1,1,1,2,3]\n
# @lcpr case=end

#

