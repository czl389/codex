# @lcpr-before-debug-begin
from python3problem42 import *
from typing import *
# @lcpr-before-debug-end

#
# @lc app=leetcode.cn id=42 lang=python3
# @lcpr version=30204
#
# [42] 接雨水
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def trap(self, height: List[int]) -> int:
        prefix = [0] *len(height)
        suffix = [0] *len(height)
        for i in range(len(height)):
            if i == 0:
                prefix[i] = height[i]
            else:
                prefix[i] = max(prefix[i-1], height[i])
        
        for i in range(len(height)-1, -1, -1):
            if i == len(height)-1:
                suffix[i] = height[i]
            else:
                suffix[i] = max(suffix[i+1], height[i])
        
        result = 0
        for i in range(len(height)):
            result = result + min(prefix[i], suffix[i]) - height[i]
        return result




        
# @lc code=end



#
# @lcpr case=start
# [0,1,0,2,1,0,1,3,2,1,2,1]\n
# @lcpr case=end

# @lcpr case=start
# [4,2,0,3,2,5]\n
# @lcpr case=end

#

