class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for c in tokens:    
            if c == '+':
                stack.append(int(stack.pop()) + int(stack.pop()))
            elif c == '-':
                a, b = int(stack.pop()), int(stack.pop())
                stack.append(b - a)
            elif c == '*':
                stack.append(int(stack.pop()) * int(stack.pop()))
            elif c == '/':
                a, b = int(stack.pop()), int(stack.pop())
                stack.append(int(float(b) / a))
            else:
                stack.append(c)
        return stack[0]