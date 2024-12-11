#
# @lc app=leetcode.cn id=LCR 121 lang=python3
# @lcpr version=30204
#
# [LCR 121] 寻找目标值 - 二维数组
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def findTargetIn2DPlants(self, plants: List[List[int]], target: int) -> bool:
        i = len(plants) -1
        j = 0
        while i >= 0 and j <= len(plants[0]) -1:
            if target == plants[i][j]:
                return True
            elif target < plants[i][j]:
                i -= 1
            else:
                j += 1
        return False



        
# @lc code=end



#
# @lcpr case=start
# [[2,3,6,8],[4,5,8,9],[5,9,10,12]]\n8\n
# @lcpr case=end

# @lcpr case=start
# [[1,3,5],[2,5,7]]\n4\n
# @lcpr case=end

#

