class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops = {
            "+": (lambda x, y: x + y),
            "-": (lambda x, y: x - y),
            "*": (lambda x, y: x * y),
            "/": (lambda x, y: x / y),
        }
        stack = []

        for tok in tokens:
            if tok in ops:
                num2 = stack.pop()
                num1 = stack.pop()
                stack.append(int(ops[tok](num1, num2)))
            else:
                stack.append(int(tok))
        return stack[0]
