class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        left = 0
        max_sub = 0
        
        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
                
            seen.add(s[right])
            max_sub = max(max_sub, right - left + 1)
            
        return max_sub