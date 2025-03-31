# @lcpr-before-debug-begin
from python3problem713 import *
from typing import *
# @lcpr-before-debug-end

#
# @lc app=leetcode.cn id=713 lang=python3
# @lcpr version=30204
#
# [713] 乘积小于 K 的子数组
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        n = len(nums)
        result = 0
        left=0
        right =0
        p = nums[left]
        for left, x in enumerate(nums):
            while right+1 < n and p * nums[right+1] < k:
                p = p * nums[right+1]
                right = right+1
            if p < k:
                result += (right-left+1)
            
            if right +1 < n and left == right:
                right = right +1
                p = p * nums[right]
            p = p / nums[left]

        return result
        
# @lc code=end



#
# @lcpr case=start
# [10,5,2,6]\n100\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3]\n0\n
# @lcpr case=end

#

