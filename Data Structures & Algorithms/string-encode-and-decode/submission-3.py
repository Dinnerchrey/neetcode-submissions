class Solution:

    def encode(self, strs: List[str]) -> str:
        res = map(lambda word: f"({len(word)}){word}", strs)
        return "".join(res)

    def parse_word(self, s: str) -> Tuple[str, str]:
        end_prefix = s.index(")")
        word_len = int(s[1:end_prefix])
        return (s[end_prefix + 1 : end_prefix + word_len + 1], s[end_prefix + word_len + 1 :])

    def decode(self, s: str) -> List[str]:
        res = []
        while (s != ""):
            word, remaining = self.parse_word(s)
            res.append(word)
            s = remaining
        return res


