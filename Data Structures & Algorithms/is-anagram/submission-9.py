class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        sFreqs = dict()
        tFreqs = dict()

        i = 0
        for i in range(len(s)):
            sFreqs[s[i]] = 1 + sFreqs.get(s[i], 0)
            tFreqs[t[i]] = 1 + tFreqs.get(t[i], 0)
        
        for letter, freq in sFreqs.items():
            if letter not in tFreqs or tFreqs[letter] != freq:
                return False
        return True
        