#
# @lc app=leetcode.cn id=110 lang=python3
# @lcpr version=30204
#
# [110] 平衡二叉树
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
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def height(root: Optional[TreeNode]) -> int:
            if root is None:
                return 0
            hl = height(root.left)
            hr = height(root.right)
            if hl == -1 or hr == -1:
                return -1
            if abs(hl - hr) > 1:
                return -1
            return max(hl, hr) +1
        return height(root) != -1
        
# @lc code=end



#
# @lcpr case=start
# [3,9,20,null,null,15,7]\n
# @lcpr case=end

# @lcpr case=start
# [1,2,2,3,3,null,null,4,4]\n
# @lcpr case=end

# @lcpr case=start
# []\n
# @lcpr case=end

#

