class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        l = len(nums)
        res = []

        for i in range(l - 2):
            if i > 0 and nums[i - 1] == nums[i]:
                continue
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
        return res
