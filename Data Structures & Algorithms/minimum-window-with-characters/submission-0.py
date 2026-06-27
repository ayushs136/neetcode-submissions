class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if t == "":
            return ""

        countT, window = defaultdict(int), defaultdict(int)
        for c in t:
            countT[c] += 1

        have, need = 0, len(countT)

        left = 0
        res, resLen = [-1, -1], float("inf")

        for right in range(len(s)):
            c = s[right]
            window[c] += 1

            if c in countT and window[c] == countT[c]:
                have += 1


            while have == need:
                if (right - left + 1) < resLen:
                    resLen = right - left + 1
                    res = [left, right]

                window[s[left]] -= 1
                if s[left] in countT and window[s[left]] < countT[s[left]]:
                    have -= 1
                left += 1

        left, right = res

        return s[left : right + 1] if resLen != float("inf") else ""
