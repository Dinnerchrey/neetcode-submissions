class Solution:
    def getFreqs(self, s: str) -> List[int]:
        freqs = [0] * 26
        for c in s:
            freqs[ord(c) - ord('a')] = freqs[ord(c) - ord('a')] + 1
        return tuple(freqs)
    
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups: Dict[Tuple[int], List[str]] = {}
        for s in strs:
            freqs = self.getFreqs(s)
            if freqs in groups:
                groups[freqs].append(s)
            else:
                groups[freqs] = [s]
        return list(groups.values())


        