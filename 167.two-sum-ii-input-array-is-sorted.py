#
# @lc app=leetcode.cn id=167 lang=python3
# @lcpr version=30204
#
# [167] 两数之和 II - 输入有序数组
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        idl = 0
        idr = len(numbers)-1
        while idl < idr:
            if numbers[idl] + numbers[idr] > target:
                idr-=1
            elif numbers[idl] + numbers[idr] < target:
                idl +=1
            else:
                return [idl+1, idr+1]
        return [0, 0]
        
# @lc code=end



#
# @lcpr case=start
# [2,7,11,15]\n9\n
# @lcpr case=end

# @lcpr case=start
# [2,3,4]\n6\n
# @lcpr case=end

# @lcpr case=start
# [-1,0]\n-1\n
# @lcpr case=end

#

