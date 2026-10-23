class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indexDict = {}
        for index in range(len(nums)):
            if nums[index] in indexDict:
                return [indexDict[nums[index]], index]
            indexDict[nums[index]] = index

        i = 0
        j = len(nums) - 1
        
        sortedNums = sorted(nums)

        while i < j:
            currSum = sortedNums[i] + sortedNums[j]
            if currSum < target:
                i += 1
            elif currSum > target:
                j -= 1
            else:
                return sorted([indexDict[sortedNums[i]], indexDict[sortedNums[j]]])
        