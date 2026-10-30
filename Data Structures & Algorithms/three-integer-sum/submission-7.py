class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        l = len(nums)
        res = []
        i = 0

        while i < l - 2:
            while i > 0 and i < l - 2 and nums[i] == nums[i - 1]:
                i += 1
            target = -nums[i]
            j = i + 1
            k = l - 1

            while j < k:
                curSum = nums[j] + nums[k]
                if curSum < target:
                    j += 1
                elif curSum > target:
                    k -= 1
                else:
                    res.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                while j < k and j > i + 1 and nums[j] == nums[j - 1]:
                    j += 1
                while j < k and k < l - 1 and nums[k] == nums[k + 1]:
                    k -= 1
            i += 1 
        return res
