class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {"(": ")", "{": "}", "[": "]"}
        stack = []
        for paren in s:
            if paren in pairs:
                stack.append(paren)
            elif stack and paren == pairs[stack[-1]]:
                stack.pop()
            else:
                return False
        if stack:
            return False
        return True
