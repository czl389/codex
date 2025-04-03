#
# @lc app=leetcode.cn id=35 lang=python3
# @lcpr version=30204
#
# [35] 搜索插入位置
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # 红蓝染色法
        # 红色小于target
        # 蓝色大于等于target
        #【left， right】是待染色区
        left = 0
        right = len(nums)-1
        while left <= right:
            m = (left+right)//2
            if nums[m] < target:
                left = m +1
            else:
                right = m -1
        return left
        
# @lc code=end



#
# @lcpr case=start
# [1,3,5,6]\n5\n
# @lcpr case=end

# @lcpr case=start
# [1,3,5,6]\n2\n
# @lcpr case=end

# @lcpr case=start
# [1,3,5,6]\n7\n
# @lcpr case=end

#

