class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        numNums = len(nums)
        leftProd = [1] * numNums
        rightProd = [1] * numNums
        res = [0] * numNums

        for i in range(1, numNums):
            leftProd[i] = leftProd[i - 1] * nums[i - 1]

        for i in range(numNums - 2, -1, -1):
            rightProd[i] = rightProd[i + 1] * nums[i + 1]

        for i in range(numNums):
            res[i] = leftProd[i] * rightProd[i]

        return res
