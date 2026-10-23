class Solution:
    def encode(self, strs: List[str]) -> str:
        res = map(lambda word: f"({len(word)}){word}", strs)
        return "".join(res)

    def parseNumber(self, s: str, i: int) -> Tuple[int, int]:
        j = s.index(")", i)
        return int(s[i+1:j]), j + 1

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0

        while i < len(s):
            strLen, i = self.parseNumber(s, i)
            result.append(s[i : i + strLen])
            i += strLen

        return result