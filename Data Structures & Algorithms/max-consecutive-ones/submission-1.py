class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_ones = 0
        curr = 0
        for i in nums:
            if i == 1:
                curr += 1
                if curr > max_ones:
                    max_ones = curr
            else:
                curr = 0
                if curr > max_ones:
                    max_ones = curr

        return max_ones