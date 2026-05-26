from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        triplets = []
        n = len(nums)
        
        for i in range(n - 2):
            # Skip duplicate values for the anchor element 'i'
            if i > 0 and nums[i] == nums[i - 1]:
                continue
                
            target = -nums[i]
            j = i + 1
            k = n - 1
            
            while j < k:
                current_sum = nums[j] + nums[k]
                
                if current_sum == target:
                    # 1. Append the VALUES, not the indices
                    triplets.append([nums[i], nums[j], nums[k]])
                    
                    # 2. Move pointers inward after a match
                    j += 1
                    k -= 1
                    
                    # 3. Skip duplicate values for 'j' and 'k' to avoid duplicate triplets
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1
                        
                elif current_sum < target:
                    j += 1  # Need a larger sum
                else:
                    k -= 1  # Need a smaller sum
                    
        return triplets