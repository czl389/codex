#
# @lc app=leetcode.cn id=162 lang=python3
# @lcpr version=30204
#
# [162] 寻找峰值
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) -2
        # 红蓝染色法
        # 红色表示峰顶左边的元素
        # 蓝色表示峰顶右侧（包括峰顶）的元素
        #【left，right】 表示待染色区
        while left <= right:
            m = (left+right)//2
            if nums[m] < nums[m+1]:
                left = m + 1
            else:
                right = m -1
        return left
        
        
# @lc code=end



#
# @lcpr case=start
# [1,2,3,1]\n
# @lcpr case=end

# @lcpr case=start
# [1,2,1,3,5,6,4]\n
# @lcpr case=end

#

