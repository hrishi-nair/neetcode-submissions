class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1] * len(nums)
        total = 1
        for i in range(len(nums)):
            result[i] = total
            total *= nums[i]
        
        total = 1
        for i in range(len(nums) - 1, -1 , -1 ):
            result[i] = result[i] * total
            total *= nums[i]
        
        return result

            