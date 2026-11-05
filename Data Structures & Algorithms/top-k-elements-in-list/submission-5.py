class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}

        for num in nums:
            if num in counts:
                counts[num] += 1
            else:
                counts[num] = 1

        # print(counts)
        res = sorted(counts, key=counts.get, reverse=True)
        # print(res[:k])
        return res[:k]
        
        
