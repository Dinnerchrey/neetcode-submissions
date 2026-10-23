class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numToFreqs = dict()
        for num in nums:
            numToFreqs[num] = 1 + numToFreqs.get(num, 0)
        
        n = len(nums)

        freqToNums = [[] for _ in range(n + 1)]

        for num, freq in numToFreqs.items():
            freqToNums[freq].append(num)

        result = []
        resultCount = 0

        for i in range(n, -1, -1):
            if len(freqToNums[i]) > 0:
                result += freqToNums[i]
            if len(result) == k:
                return result
