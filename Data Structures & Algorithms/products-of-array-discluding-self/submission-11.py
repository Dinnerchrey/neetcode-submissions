class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        numNums = len(nums)
        res = [1] * numNums

        prefix = 1 
        for i in range(1, numNums):
            prefix *= nums[i - 1]
            res[i] = prefix

        suffix = 1 
        for i in range(numNums - 2, -1, -1):
            suffix *= nums[i + 1]
            res[i] *= suffix

        return res
