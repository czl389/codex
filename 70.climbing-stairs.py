#
# @lc app=leetcode.cn id=70 lang=python3
# @lcpr version=30204
#
# [70] 爬楼梯
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    cache = {}
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        cached_value = self.cache.get(n)
        if cached_value:
            return cached_value
        else:
            result = self.climbStairs(n-1) + self.climbStairs(n-2)
            self.cache[n] = result
        return result
        
# @lc code=end



#
# @lcpr case=start
# 2\n
# @lcpr case=end

# @lcpr case=start
# 3\n
# @lcpr case=end

#

