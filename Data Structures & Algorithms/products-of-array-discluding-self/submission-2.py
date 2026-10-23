from functools import reduce

class Solution:
    def productExceptIndex(self, nums: List[int], index: int) -> int:
        result = 1
        for i in range(len(nums)):
            if i == index:
                continue
            result *= nums[i]
        return result
            
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = reduce(lambda x, y: x * y, nums)
        res = []
        for i in range(len(nums)):
            if nums[i] == 0:
                res.append(self.productExceptIndex(nums, i))
            elif nums[i] == 1:
                res.append(prod)
            else:
                res.append(prod // nums[i])
        return res

        