class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        numNums = len(nums)
        leftProd = [0] * numNums
        rightProd = [0] * numNums
        res = [0] * numNums

        prev = 1
        for i in range(numNums):
            prev *= nums[i] 
            leftProd[i] = prev

        prev = 1
        for i in range(numNums - 1, -1, -1):
            prev *= nums[i] 
            rightProd[i] = prev
        
        res[0] = rightProd[1]
        res[numNums - 1] = leftProd[numNums - 2]
        for i in range(1, numNums - 1):
            res[i] = leftProd[i - 1] * rightProd[i + 1]

        return res

        

            

       

        