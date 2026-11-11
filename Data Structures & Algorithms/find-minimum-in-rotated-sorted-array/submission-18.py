class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) -1 
        mid = (l + r) // 2
        min_output = nums[l]

        while (l <= r):
            # print(mid)
            if nums[l] <= nums[mid]:
                min_output = min(nums[l], min_output)
                l = mid + 1
            else:
                min_output = min(nums[mid], min_output)
                r = mid

            mid = (l + r) // 2

        return min_output

