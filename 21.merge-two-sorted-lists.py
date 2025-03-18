#
# @lc app=leetcode.cn id=21 lang=python3
# @lcpr version=30204
#
# [21] 合并两个有序链表
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
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy_node = p0 = ListNode()
        p1 = list1
        p2 = list2
        while p1 or p2:
            if p1 is None:
                p0.next = p2
                break
            elif p2 is None:
                p0.next = p1
                break            
            if p1.val <= p2.val:
                p0.next = p1
                p1 = p1.next
            else:
                p0.next = p2
                p2 = p2.next
            p0 = p0.next

        return dummy_node.next
            


        
# @lc code=end



#
# @lcpr case=start
# [1,2,4]\n[1,3,4]\n
# @lcpr case=end

# @lcpr case=start
# []\n[]\n
# @lcpr case=end

# @lcpr case=start
# []\n[0]\n
# @lcpr case=end

#

