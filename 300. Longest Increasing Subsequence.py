# https://leetcode.com/problems/longest-increasing-subsequence/description/

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        mx = 0
        n = len(nums)
        dp = [-1 for _ in range(2501)]
        def solve(n):
            if dp[n] != -1:
                return dp[n]
            ans = 1
            for i in range(n):
                if nums[i] < nums[n]:
                    ans = max(ans, solve(i)+1)
            dp[n] = ans
            return dp[n]

        for i in range(n):
            mx = max(mx, solve(i))

        return mx