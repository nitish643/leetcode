class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        n=len(nums)
        tsum=(n*(n+1))//2
        s=sum(nums)
        return tsum-s