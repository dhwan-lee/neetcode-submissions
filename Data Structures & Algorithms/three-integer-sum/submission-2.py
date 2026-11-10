class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        sorted_nums = sorted(nums)
        res = []

        for i, value in enumerate(sorted_nums):
            if value > 0:
                return res
            
            if i > 0 and value == sorted_nums[i - 1]:
                continue

            l, r = i + 1, len(sorted_nums) - 1

            while l < r:
                total = value + sorted_nums[l] + sorted_nums[r]

                if total == 0:
                    res.append([value, sorted_nums[l], sorted_nums[r]])
                    l += 1
                    r -= 1
                    while sorted_nums[l] == sorted_nums[l - 1] and l < r:
                        l += 1

                elif total > 0:
                    r -= 1
                elif total < 0:
                    l += 1
            
        
        return res

                