class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = [0] * n
        stack = [0]

        for i in range(1, n):
            if temperatures[i] > temperatures[i-1]:
                while stack and temperatures[stack[-1]] < temperatures[i]:
                    j = stack.pop()
                    res[j] = i - j
            stack.append(i)
        return res

