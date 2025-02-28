# @lcpr-before-debug-begin
from python3problem15 import *
from typing import *
# @lcpr-before-debug-end

#
# @lc app=leetcode.cn id=15 lang=python3
# @lcpr version=30204
#
# [15] 三数之和
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []

        for i in range(len(nums)-2):
            j = i+1
            k = len(nums)-1

            if nums[i] +nums[i+1] + nums[i+2] > 0:
                break
            if nums[-3] + nums[-2] + nums[-1] <0:
                break

            if i >0 and nums[i] == nums[i-1]:
                continue
            if nums[i] + nums[-1] + nums[-2] <0:
                continue

            while j < k:
                if nums[j] + nums[k] < -1 * nums[i]:
                    j+=1
                elif nums[j] + nums[k] > -1 * nums[i]:
                    k-=1
                else:
                    ans.append([nums[i], nums[j], nums[k]])
                    j+=1
                    while j<k and nums[j] == nums[j-1]:
                        j+=1

                    k-=1
                    while j<k and nums[k] == nums[k+1]:
                        k-=1
        return ans

# @lc code=end



#
# @lcpr case=start
# [-1,0,1,2,-1,-4]\n
# @lcpr case=end

# @lcpr case=start
# [0,1,1]\n
# @lcpr case=end

# @lcpr case=start
# [0,0,0]\n
# @lcpr case=end

#

