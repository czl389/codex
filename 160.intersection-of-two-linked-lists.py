# @lcpr-before-debug-begin
from python3problem160 import *
from typing import *
# @lcpr-before-debug-end

#
# @lc app=leetcode.cn id=160 lang=python3
# @lcpr version=30204
#
# [160] 相交链表
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
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        pA = headA
        pB = headB

        round_pA = 1
        round_pB = 1
        while pA is not None and pB is not None:
            if pA == pB:
                return pA
            pA = pA.next
            if pA is None and round_pA == 1:
                pA = headB
                round_pA = 2
            
            pB = pB.next
            if pB is None and round_pB == 1:
                pB = headA
                round_pB = 2
        return None
        
# @lc code=end



#
# @lcpr case=start
# 8\n[4,1,8,4,5]\n[5,6,1,8,4,5]\n2\n3\n
# @lcpr case=end

# @lcpr case=start
# 2\n[1,9,1,2,4]\n[3,2,4]\n3\n1\n
# @lcpr case=end

# @lcpr case=start
# 0\n[2,6,4]\n[1,5]\n3\n2\n
# @lcpr case=end

#

