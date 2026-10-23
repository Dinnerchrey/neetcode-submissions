class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        sFreqs = dict()
        tFreqs = dict()

        for i in range(len(s)):
            sFreqs[s[i]] = 1 + sFreqs.get(s[i], 0)
            tFreqs[t[i]] = 1 + tFreqs.get(t[i], 0)
        
        return sFreqs == tFreqs 
        