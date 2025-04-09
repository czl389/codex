# @lcpr-before-debug-begin
from python3problem33 import *
from typing import *
# @lcpr-before-debug-end

#
# @lc app=leetcode.cn id=33 lang=python3
# @lcpr version=30204
#
# [33] 搜索旋转排序数组
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def minIndex(nums: List[int]) -> int:
            n = len(nums)
            # 红色表示最小值左侧
            # 蓝色表示最小值及其右侧
            # 【left, right】是待检测区
            left = 0
            right = n-1
            while left <= right:
                m = (left+right)//2
                if nums[m] <= nums[-1]:
                    right = m -1
                else:
                    left = m +1
            return left
        min_index = minIndex(nums)

        left = 0
        right = min_index-1
        if target <= nums[-1]:
            left = min_index
            right = len(nums)-1
        while left <= right:
            m = (left+right) //2
            if target > nums[m]:
                left = m + 1
            else:
                right = m - 1
        if left < len(nums) and nums[left] == target:
            return left
        return -1


        
# @lc code=end



#
# @lcpr case=start
# [4,5,6,7,0,1,2]\n0\n
# @lcpr case=end

# @lcpr case=start
# [4,5,6,7,0,1,2]\n3\n
# @lcpr case=end

# @lcpr case=start
# [3,1]\n3\n
# @lcpr case=end

#

