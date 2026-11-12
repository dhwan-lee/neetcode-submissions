class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        hashmap = {}
        max_sequence = 0

        for i in range(len(s)):
            if s[i] in hashmap:
                l = max(l, hashmap[s[i]] + 1)
                
            hashmap[s[i]] = i
            max_sequence = max(max_sequence, i - l + 1)

        return max_sequence