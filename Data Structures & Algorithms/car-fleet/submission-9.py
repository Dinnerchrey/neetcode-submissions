class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        posSpeeds = [(p,s) for p, s in zip(position, speed)] 
        posSpeeds.sort(reverse=True, key = lambda x: x[0])
        
        stack = []
        for pos, spd in posSpeeds:
            timeTo = (target - pos) / spd
            if not stack or timeTo > stack[-1]:
                stack.append(timeTo)
        return len(stack)






