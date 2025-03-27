# @lcpr-before-debug-begin
from python3problem209 import *
from typing import *
# @lcpr-before-debug-end

#
# @lc app=leetcode.cn id=209 lang=python3
# @lcpr version=30204
#
# [209] 长度最小的子数组
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        length = len(nums)
        l = r = 0
        tmp = nums[l]
        result = length+1
        while l < length and r < length:
            if tmp >= target:
                result = min(result, r-l+1)

                if l == len(nums)-1:
                    break
                tmp = tmp - nums[l]
                l = l+1
                if l > r:
                    if r == len(nums)-1:
                        break
                    r = r+1
                    tmp = tmp + nums[r]
            else:
                if r == len(nums)-1:
                    break
                r = r+1
                tmp = tmp + nums[r]
        if result == len(nums)+1:
            result = 0
        return result
        
# @lc code=end



#
# @lcpr case=start
# 7\n[2,3,1,2,4,3]\n
# @lcpr case=end

# @lcpr case=start
# 4\n[1,4,4]\n
# @lcpr case=end

# @lcpr case=start
# 11\n[1,1,1,1,1,1,1,1]\n
# @lcpr case=end

#

