class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        valid = {
            '[': ']',
            '{': '}',
            '(': ')'
        }
        
        for char in s:
            if char in valid:  # Opening bracket
                stack.append(char)
            else:  # Closing bracket
                # If stack is empty or top of the stack doesn't match
                if not stack or valid[stack.pop()] != char:
                    return False
        
        # If the stack is empty, all brackets are matched
        return len(stack) == 0
