class Solution:

    def encode(self, strs: List[str]) -> str:
        res = map(lambda word: f"({len(word)}){word}", strs)
        return "".join(res)
    
    def parse_prefix(self, start: int, s: str) -> Tuple(int, int):
        end_prefix = start
        while s[end_prefix] != ")":
            end_prefix += 1
        word_len = int(s[start + 1 : end_prefix])
        return (word_len, end_prefix + 1)

    def parse_word(self, start: int, length: int, s: str) -> Tuple[str, int]:
        word_end = start + length
        return (s[start : word_end], word_end)

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i != len(s):
            word_len, i = self.parse_prefix(i, s)
            word, i = self.parse_word(i, word_len, s)
            res.append(word)
        return res
