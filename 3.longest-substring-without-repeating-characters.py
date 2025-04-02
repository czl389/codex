#
# @lc app=leetcode.cn id=3 lang=python3
# @lcpr version=30204
#
# [3] 无重复字符的最长子串
#

from collections import defaultdict

# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0
        n = len(s)
        result = 0

        count = defaultdict(int)

        for right, x in enumerate(s):
            count[x] += 1
            while count[x] > 1:
                count[s[left]] -=1
                left = left+1
   
            result = max(result, right-left+1)

        return result
        
# @lc code=end



#
# @lcpr case=start
# "abcabcbb"\n
# @lcpr case=end

# @lcpr case=start
# "bbbbb"\n
# @lcpr case=end

# @lcpr case=start
# "pwwkew"\n
# @lcpr case=end

#

