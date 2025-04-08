#
# @lc app=leetcode.cn id=153 lang=python3
# @lcpr version=30204
#
# [153] 寻找旋转排序数组中的最小值
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def findMin(self, nums: List[int]) -> int:
        # 红蓝染色法
        #红色表示最小值的左侧
        #蓝色表示最小值以及右侧
        #在【left, right】中检测元素
        n = len(nums)
        left = 0
        right = n-2
        while left <= right:
            m = (left+right)//2
            if nums[m] < nums[n-1]:
                right = m -1
            else:
                left = m +1
        return nums[left]
        
# @lc code=end



#
# @lcpr case=start
# [3,4,5,1,2]\n
# @lcpr case=end

# @lcpr case=start
# [4,5,6,7,0,1,2]\n
# @lcpr case=end

# @lcpr case=start
# [11,13,15,17]\n
# @lcpr case=end

#

