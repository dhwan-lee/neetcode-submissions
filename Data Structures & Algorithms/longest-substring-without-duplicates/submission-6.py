class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        max_leng = 0
        left = 0

        for right, char in enumerate(s):
            if char in seen and seen[char] >= left:
                left = seen[char] + 1

            seen[char] = right
            max_leng = max(max_leng, right - left + 1)

        return max_leng
