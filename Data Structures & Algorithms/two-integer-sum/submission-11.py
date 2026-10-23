class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = dict()
        for j, num in enumerate(nums):
            comp = target - num
            if comp in seen:
                return [seen[comp], j] 
            seen[num] = j
        