class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seen = {}
        for chars in s:
            if not chars in seen:
                seen[chars] = 1
            else:
                seen[chars] += 1
        
        for chars in t:
            if not chars in seen:
                return False
            else: 
                seen[chars] -= 1
                if seen[chars] < 0:
                    return False
        
        for char, count in seen.items():
            if count != 0:
                return False
        return True