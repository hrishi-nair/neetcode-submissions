class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1] * len(nums)
        total = 1
        for i in range(len(nums)):
            prefix[i] = total
            total *= nums[i]
        
        suffix = [1] * len(nums)
        total = 1
        for i in range(len(nums) - 1, -1 , -1 ):
            suffix[i] = total
            total *= nums[i]
        
        result = [1] * len(nums)
        for i in range(len(nums)):
            result[i] = (prefix[i] * suffix[ i ])
        return result

            