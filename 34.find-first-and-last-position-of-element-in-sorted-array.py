# @lcpr-before-debug-begin
from python3problem34 import *
from typing import *
# @lcpr-before-debug-end

#
# @lc app=leetcode.cn id=34 lang=python3
# @lcpr version=30204
#
# [34] 在排序数组中查找元素的第一个和最后一个位置
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:

    def lowerBound(self, nums, target, left, right):
        # left,right 指向询问的左右边界
        # left 左边是红色，表示小于target的值
        # right 右边是蓝色，表示大于等于target的值
        if left > right:
            return left
        m = (left + right) // 2
        if nums[m] >= target:
            return self.lowerBound(nums, target, left, m-1)
        else:
            return self.lowerBound(nums, target, m+1, right)

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0:
            return [-1, -1]
        start = self.lowerBound(nums, target, 0, len(nums)-1)
        if start >= len(nums) or nums[start] != target:
            return [-1, -1]
        end = self.lowerBound(nums, target+1, start, len(nums)-1) -1
        return [start, end]


# @lc code=end



#
# @lcpr case=start
# [5,7,7,8,8,10]\n8\n
# @lcpr case=end

# @lcpr case=start
# [5,7,7,8,8,10]\n6\n
# @lcpr case=end

# @lcpr case=start
# []\n0\n
# @lcpr case=end

# @lcpr case=start
# [2,2]\n3\n
# @lcpr case=end

#

