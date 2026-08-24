class Solution:
    def findLengthOfLCIS(self, nums):
        if not nums:
            return 0
        count = 1
        ans = 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                count += 1
            else:
                count = 1
            ans = max(ans, count)
        return ans