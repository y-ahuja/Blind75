class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [1]*len(nums)
        pre = 1
        post = 1
        for i in range(len(nums)):
            ans[i] *= pre
            pre = pre*nums[i]
            ans[len(nums)-i-1] *= post
            post = post*nums[len(nums)-i-1]
        return ans
 