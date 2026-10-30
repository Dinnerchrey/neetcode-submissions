class Solution:
    def trap(self, height: List[int]) -> int:
        l = len(height)
        ls = [0 for _ in range(l)] 
        rs = [0 for _ in range(l)] 

        for i in range(1,l):
            ls[i] = max(ls[i - 1], height[i - 1])

        for i in range(l - 2, -1, -1):
            rs[i] = max(rs[i + 1], height[i + 1])
        
        total = 0
        for i in range(1, l - 1):
            depth = min(ls[i],rs[i])
            total += max(0, depth - height[i])
        return total


        

        