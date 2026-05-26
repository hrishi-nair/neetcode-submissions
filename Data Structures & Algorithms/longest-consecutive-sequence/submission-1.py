class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        max_cnt = 0
        for i in range(len(nums)):
            count = 1
            start = nums[i]
            for j in range(i + 1, len(nums)):
                if nums[j] == start:
                    continue
                if nums[j] == start + 1:
                    count += 1
                    start = nums[j]
                else:
                    break
            if count > max_cnt:
                max_cnt = count
        return max_cnt
