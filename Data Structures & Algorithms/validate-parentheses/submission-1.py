class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {"(": ")", "{": "}", "[": "]"}
        stack = []
        for paren in s:
            if paren in pairs:
                stack.append(paren)
            elif len(stack) != 0 and paren == pairs[stack[-1]]:
                stack.pop()
            else:
                return False
        if len(stack) != 0:
            return False
        return True
