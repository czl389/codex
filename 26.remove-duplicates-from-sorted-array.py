# @lcpr-before-debug-begin
from python3problem26 import *
from typing import *
# @lcpr-before-debug-end

#
# @lc app=leetcode.cn id=26 lang=python3
# @lcpr version=30204
#
# [26] 删除有序数组中的重复项
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        j = 1
        while j < len(nums):
            if nums[j] != nums[i]:
                i = i+1
                if i != j:
                    nums[j], nums[i] = nums[i], nums[j]
            j = j+1
        return i+1
        
# @lc code=end



#
# @lcpr case=start
# [1,1,2]\n
# @lcpr case=end

# @lcpr case=start
# [0,0,1,1,1,2,2,3,3,4]\n
# @lcpr case=end

#
