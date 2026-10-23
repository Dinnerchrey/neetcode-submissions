class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numToFreq = dict()
        for num in nums:
            numToFreq[num] = numToFreq.get(num, 0) + 1
        
        maxFreq = len(nums)

        freqBuckets = [[] for _ in range(maxFreq + 1)] 
        for num, freq in numToFreq.items():
            freqBuckets[freq].append(num)

        result = []
        count = 0
        i = maxFreq
        while (count != k):
            result.extend(freqBuckets[i])
            count += len(freqBuckets[i])
            i -= 1
        
        return result

