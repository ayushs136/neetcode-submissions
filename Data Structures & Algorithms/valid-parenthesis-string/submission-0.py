class Solution:
    def checkValidString(self, s: str) -> bool:
        min = 0
        max = 0
        for i in range(len(s)):
            ch = s[i]
            if ch == "(":
                max += 1
                min += 1
            elif ch == ")":
                max -= 1
                min -= 1
            else:
                min -= 1
                max += 1
            if min < 0:
                min = 0
            if max < 0:
                return False

        return min == 0
