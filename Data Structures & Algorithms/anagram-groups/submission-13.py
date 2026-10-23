class Solution:
    def getFreqs(self, s: str) -> List[int]:
        freqs = [0] * 26
        for c in s:
            freqs[ord(c) - ord('a')] = freqs[ord(c) - ord('a')] + 1
        return tuple(freqs)
    
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list) 
        for s in strs:
            freqs = self.getFreqs(s)
            groups[freqs].append(s)
        return list(groups.values())


        