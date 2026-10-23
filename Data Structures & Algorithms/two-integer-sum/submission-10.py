class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indexDict = {} 

        for i in range(len(nums)):
            indexDict[nums[i]] = i
        
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement not in indexDict or indexDict[complement] == i:
                continue
            return [i, indexDict[complement]]