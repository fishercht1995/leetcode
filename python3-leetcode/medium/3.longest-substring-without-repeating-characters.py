#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)
        max_len = 0
        start = 0
        dic = {}
        for i in range(len(s)):
            if s[i] not in dic:
                dic[s[i]] = i
            else:
                if dic[s[i]] >= start:
                    start = dic[s[i]] + 1
                dic[s[i]] = i
            if i + 1 - start >= max_len:
                max_len = i + 1 - start 
        return max_len

# @lc code=end

