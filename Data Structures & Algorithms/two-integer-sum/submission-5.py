class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_hash = {}
        
        for i, num in enumerate(nums):
            diff = target - num
            if diff in nums_hash:
                return [nums_hash[diff], i]

            nums_hash[num] = i
            