# @lcpr-before-debug-begin
from python3problem27 import *
from typing import *
# @lcpr-before-debug-end

#
# @lc app=leetcode.cn id=27 lang=python3
# @lcpr version=30204
#
# [27] 移除元素
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = j = 0

        while j < len(nums):
            if nums[j] != val:
                if i != j:
                    nums[j], nums[i] = nums[i], nums[j]
                i = i+1
            j = j+1
        return i



        
# @lc code=end



#
# @lcpr case=start
# [3,2,2,3]\n3\n
# @lcpr case=end

# @lcpr case=start
# [0,1,2,2,3,0,4,2]\n2\n
# @lcpr case=end

#

