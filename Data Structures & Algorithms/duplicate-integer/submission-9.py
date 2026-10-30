class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if len(nums) == 0:
            return False

        counts = {}
        for num in nums:
            if num in counts:
                counts[num] += 1
                return True
            else:
                counts[num] = 1

        
        return False
