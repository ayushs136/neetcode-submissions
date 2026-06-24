class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        n = len(s)

        left = max_len = 0
        char_map = defaultdict(int)

        for right in range(n):
            char_map[s[right]] += 1

            length = right - left + 1
            max_val = max(char_map.values())

            if length - max_val <= k:
                max_len = max(max_len, length)
            else:
                char_map[s[left]] -= 1
                left += 1

        return max_len
