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
            elif nums[r] > nums[mid]:
                min_output = min(nums[mid], min_output)
                r = mid
            # elif nums[l] > nums[mid]:
            #     min_output = min(nums[mid], min_output)
                
            # elif nums[r] < nums[mid]:
            #     min_output = min(nums[r], min_output)
            else:
                return min_output

            mid = (l + r) // 2

        return min_output

