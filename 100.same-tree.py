#
# @lc app=leetcode.cn id=100 lang=python3
# @lcpr version=30204
#
# [100] 相同的树
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None:
            if q is None:
                return True
            else:
                return False
        if q is None:
            return False

        return (p.val == q.val) and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right) 
        
# @lc code=end



#
# @lcpr case=start
# [1,2,3]\n[1,2,3]\n
# @lcpr case=end

# @lcpr case=start
# [1,2]\n[1,null,2]\n
# @lcpr case=end

# @lcpr case=start
# [1,2,1]\n[1,1,2]\n
# @lcpr case=end

#

