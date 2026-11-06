class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        posSpeeds = list(zip(position, speed))
        posSpeeds.sort(key = lambda x: x[0])
        count = 1
        
        curPos, curSpeed = posSpeeds.pop()
        curDistance = target - curPos
        longestTime = curDistance / curSpeed
        while posSpeeds:
            nextPos, nextSpeed = posSpeeds[-1][0], posSpeeds[-1][1]
            curDistance = target - curPos
            longestTime = max(longestTime, curDistance / curSpeed)
            nextPosByTarget = nextPos + nextSpeed * longestTime 

            if nextPosByTarget < target:
                count += 1
                
            curPos, curSpeed = posSpeeds.pop()
        return count

                

        
     

        