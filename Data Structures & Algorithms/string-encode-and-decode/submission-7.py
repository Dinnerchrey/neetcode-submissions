class Solution:
    def encode(self, strs: List[str]) -> str:
        res = map(lambda word: f"({len(word)}){word}", strs)
        return "".join(res)

    # Returns a pair of parsed value and index after the ending bracket
    def parseNumber(self, s: str, i: int) -> Tuple[int]:
        intString = ""
        j = i + 1
        while s[j] != ")":
            intString += s[j]
            j += 1
        return (int(intString), j + 1)

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0

        while i < len(s):
            strLen, i = self.parseNumber(s, i)
            result.append(s[i : i + strLen])
            i += strLen

        return result