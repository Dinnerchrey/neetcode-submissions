class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        i = 0
        j = n - 1

        total = 0
        max_i = height[i]
        max_j = height[j]

        while i < j:
            if height[i] < height[j]:
                i += 1
                max_i = max(max_i, height[i])
                total += max_i - height[i] 
            else:
                j -= 1
                max_j = max(max_j, height[j])
                total += max_j - height[j] 

        return total
