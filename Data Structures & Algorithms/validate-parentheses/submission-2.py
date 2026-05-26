class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        # Map CLOSING brackets to their corresponding OPENING brackets
        bkts = {
            ')': '(',
            '}': '{',
            ']': '['
        }
        
        for char in s:
            # If the character is a closing bracket
            if char in bkts:    
                # Pop the top element if stack isn't empty, otherwise use a dummy value
                top_element = stack.pop() if stack else '#'
                
                # Check if the opening bracket matches the required one
                if bkts[char] != top_element:
                    return False
            else:
                # If it's an opening bracket, push it onto the stack
                stack.append(char)
        
        # Instead of 'return True', ensure the stack is completely empty
        # (This catches cases like s = "(((", where brackets are never closed)
        return not stack