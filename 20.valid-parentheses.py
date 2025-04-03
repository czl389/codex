#
# @lc app=leetcode.cn id=20 lang=python3
# @lcpr version=30204
#
# [20] 有效的括号
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        d = {
            "(": ")",
            "[": "]",
            "{": "}"
        }

        stack = []
        for x in s:
            if x in d.keys():
                stack.append(x)
            else:
                if len(stack) == 0:
                    return False
                if  d[stack.pop()] != x:
                    return False
        return False if len(stack) else True

        
# @lc code=end



#
# @lcpr case=start
# "()"\n
# @lcpr case=end

# @lcpr case=start
# "()[]{}"\n
# @lcpr case=end

# @lcpr case=start
# "(]"\n
# @lcpr case=end

# @lcpr case=start
# "([])"\n
# @lcpr case=end

#

