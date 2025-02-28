# @lcpr-before-debug-begin
from python3problem415 import *
from typing import *
# @lcpr-before-debug-end

#
# @lc app=leetcode.cn id=415 lang=python3
# @lcpr version=30204
#
# [415] 字符串相加
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        len_diff = len(num1) - len(num2)
        if len_diff > 0:
            num2 = "0" * len_diff + num2
        elif len_diff < 0:
            num1 = "0" * (-1 * len_diff) + num1
        result = ""
        digit_carry = 0
        for i in range(len(num1)-1, -1, -1):
            sum = int(num1[i]) + int(num2[i]) + digit_carry
            digit_sum = sum % 10
            digit_carry = sum // 10
            result = str(digit_sum) + result
            if i == 0 and digit_carry != 0:
                result = str(digit_carry) + result
        return result



        
# @lc code=end



#
# @lcpr case=start
# "11"\n"123"\n
# @lcpr case=end

# @lcpr case=start
# "456"\n"77"\n
# @lcpr case=end

# @lcpr case=start
# "0"\n"0"\n
# @lcpr case=end

# @lcpr case=start
# "9"\n"99"\n
# @lcpr case=end

#

