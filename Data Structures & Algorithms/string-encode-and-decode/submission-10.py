class Solution:
    def encode(self, strs: List[str]) -> str:
        return "".join(map(lambda s: f"({len(s)})" + s, strs))

    def parse_num(self, s: str, i: int) -> Tuple[int, int]:
        j = s.index(")", i)
        return int(s[i+1:j]), j+1

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        t_len = len(s)

        while i < t_len:
            w_len, i = self.parse_num(s, i)
            res.append(s[i : i + w_len])
            i += w_len

        return res
