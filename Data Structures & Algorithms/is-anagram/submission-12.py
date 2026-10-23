class Solution:
    def getFreqs(self, s: str) -> Dict[str, int]:
        res = {}
        for c in s:
            res[c] = res.get(c, 0) + 1
        return res

    def isAnagram(self, s: str, t: str) -> bool:
        return self.getFreqs(s) == self.getFreqs(t)
        