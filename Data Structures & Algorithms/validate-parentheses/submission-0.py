class Solution:
    def isValid(self, s: str) -> bool:
        stack = list()

        closeToOpen = {")": "(", "]": "[", "}": "{"}

        for ch in s:
            if ch in closeToOpen:
                if stack and stack[-1] == closeToOpen[ch]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(ch)
        return True if not stack else False
