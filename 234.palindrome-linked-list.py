#
# @lc app=leetcode.cn id=234 lang=python3
# @lcpr version=30204
#
# [234] 回文链表
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
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        def middleNode(head: Optional[ListNode]) -> Optional[ListNode]:
            fast = slow = head
            while fast is not None and fast.next is not None:
                slow = slow.next
                fast = fast.next.next
            return slow
        m = middleNode(head)

        def reverseLink(head: Optional[ListNode]) ->  Optional[ListNode]:
            prev =None
            current = head
            while current:
                next_node = current.next
                current.next = prev
                prev = current
                current = next_node
            return prev
        head2 = reverseLink(m)
        left = head
        right = head2
        while left and right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        return True



        
# @lc code=end



#
# @lcpr case=start
# [1,2,2,1]\n
# @lcpr case=end

# @lcpr case=start
# [1,2]\n
# @lcpr case=end

#

