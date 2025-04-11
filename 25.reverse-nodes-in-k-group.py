# @lcpr-before-debug-begin
from python3problem25 import *
from typing import *
# @lcpr-before-debug-end

#
# @lc app=leetcode.cn id=25 lang=python3
# @lcpr version=30204
#
# [25] K 个一组翻转链表
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
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # n 是翻转次数
        n =0
        probe = head
        while probe:
            i = 0
            for i in range(k):
                probe = probe.next
                if i == k-1:
                    n +=1
                if probe is None:
                    break
        print(n)

        dummy_node = ListNode(next=head)
        p0 = dummy_node
        prev = None
        current = head
        for _ in range(n):
            for i in range(k):
                next_node = current.next
                current.next = prev
                prev = current
                current = next_node
                i+=1
            newp0 = p0.next
            p0.next.next = current
            p0.next = prev
            p0 = newp0
        return dummy_node.next

        


        
# @lc code=end



#
# @lcpr case=start
# [1,2,3,4,5]\n2\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3,4,5]\n3\n
# @lcpr case=end

#

