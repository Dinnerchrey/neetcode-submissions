class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = dict()
        for num in nums:
            freqs[num] = 1 + freqs.get(num, 0)

        return list(map(lambda pair : pair[0], sorted(freqs.items(), key = lambda pair : pair[1], reverse = True)))[:k]
