class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""

        for s in strs:
            res += str(len(s)) + "#" + s

        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        j = 1
        while (i < len(s)):
            if s[j] != "#":
                j += 1
            else:
                size = int(s[i:j])
                j += 1
                res.append(s[j : j + size])
                i = j + size
                j = i
    
        return res
            
        
