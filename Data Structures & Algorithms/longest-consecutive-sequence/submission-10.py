class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0

        for num in numSet:
            if num - 1 not in numSet:
                n = 1
                cur = num
                while cur + 1 in numSet:
                    n += 1 
                    cur += 1
                longest = max(longest, n) 
        return longest

