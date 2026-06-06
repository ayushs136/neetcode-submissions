class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        def is_integer_string(val):
            # Strip leading minus sign if it exists, then check if remaining characters are digits
            return val.isdigit() or (val.startswith('-') and val[1:].isdigit())

        ans = 0

        stack = []

        for n in tokens:
            if is_integer_string(n):
                stack.append(int(n))
               
            else:
                val1 = 0
                val2 = 0
                if stack:
                    val1 = int(stack.pop())
                if stack:
                    val2 = int(stack.pop())

                if n == "+":
                    ans = val1 + val2
                elif n == "-":
                    ans = val2 - val1
                elif n == "*":
                    ans = val1 * val2
                elif n == "/" and val2 != 0:
                    ans = int(val2 / val1)
                stack.append(int(ans))

        return stack[-1]
