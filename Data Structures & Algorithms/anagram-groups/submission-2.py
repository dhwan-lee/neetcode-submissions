class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        found = defaultdict(list)
        res = []
        for s in strs:
            temp = "".join(sorted(s))
            found[temp]
            found[temp].append(s)

        for ans in found.values():
            res.append(ans)

        return res
