class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_arr = []
        suffix_arr = []
        prev = 0
        res = []
    
        for i, num in enumerate(nums):
            if i == 0:
                prev = num
                prefix_arr.append(prev)
            else:
                prev *= num
                prefix_arr.append(prev)

        prev = 0
        for i in range(len(nums) - 1, -1, -1):
            if i == len(nums) - 1:
                prev = nums[i]
                suffix_arr.append(prev)
            else:
                prev *= nums[i]
                suffix_arr.append(prev)
        
        suffix_arr.reverse()

        for i in range(len(nums)):
            if i == 0:
                res.append(suffix_arr[1])
            elif i == len(nums) - 1:
                res.append(prefix_arr[i - 1])
            else:
                res.append(prefix_arr[i - 1] * suffix_arr[i + 1])

        
        return res
