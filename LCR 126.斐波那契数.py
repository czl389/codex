#
# @lc app=leetcode.cn id=LCR 126 lang=python3
# @lcpr version=30204
#
# [LCR 126] 斐波那契数
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def __init__(self):
        self.cache = {}
    def fib(self, n: int) -> int:
        cached_value = self.cache.get(n)
        if cached_value is not None:
            return cached_value
        if n == 0:
            return 0
        if n == 1:
            return 1
        cached_value = self.fib(n - 1) + self.fib(n-2)
        self.cache[n] = cached_value
        return cached_value % 1000000007
# @lc code=end



#
# @lcpr case=start
# 2\n
# @lcpr case=end

# @lcpr case=start
# 3\n
# @lcpr case=end

# @lcpr case=start
# 4\n
# @lcpr case=end

#

