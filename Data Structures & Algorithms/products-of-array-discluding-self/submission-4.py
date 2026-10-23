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
        memo = dict()

        prod = reduce(lambda x, y: x * y, nums)
        res = []

        for i in range(len(nums)):
            if nums[i] in memo:
                res.append(memo[nums[i]])
            elif nums[i] == 0:
                x = self.productExceptIndex(nums, i)
                memo[0] = x
                res.append(x)
            elif nums[i] == 1:
                memo[1] = prod
                res.append(prod)
            else:
                x = prod // nums[i]
                memo[nums[i]] = x
                res.append(x)

        return res

        