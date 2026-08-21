class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        def add(a, b):
            return a + b
        def mul(a, b):
            return a * b
        def sub(a, b):
            return a - b
        def div(a, b):
            return int(a / b)
        
        eval = {
            "+": add,
            "-": sub,
            "/": div,
            "*": mul
        }

        stack = []
        for token in tokens:
            if token in eval.keys():
                b = stack.pop()
                a = stack.pop()
                res = eval[token](a, b)
                stack.append(res)
            else:
                stack.append(int(token))
        
        return stack[0]