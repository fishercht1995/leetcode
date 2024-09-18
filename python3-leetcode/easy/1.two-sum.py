#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        helper_dict = {}
        for i in range(len(nums)):
            if target - nums[i] in helper_dict:
                return [helper_dict[target - nums[i]], i]
            else:
                helper_dict[nums[i]] = i
        return None
# @lc code=end

