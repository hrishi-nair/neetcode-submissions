class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}  # Keeps track of character frequencies in the current window
        max_length = 0
        max_freq = 0
        left = 0
        
        # 'right' pointer expands our window
        for right in range(len(s)):
            # Update the count for the incoming character
            count[s[right]] = 1 + count.get(s[right], 0)
            
            # Update the maximum frequency of any single character seen in the current window
            max_freq = max(max_freq, count[s[right]])
            
            # Window length is (right - left + 1)
            # If the number of characters to replace exceeds k, shrink the window from the left
            while (right - left + 1) - max_freq > k:
                count[s[left]] -= 1
                left += 1
                
            # Track the maximum valid window size found so far
            max_length = max(max_length, right - left + 1)
            
        return max_length